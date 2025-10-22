"""
TOGAF AI Agent Base Classes

Provides foundational classes for AI agents that work with TOGAF framework.
These agents can analyze, recommend, automate, and collaborate on architecture tasks.
"""

from typing import Dict, List, Optional, Any, Callable
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import json


class AgentRole(Enum):
    """Roles that AI agents can play in TOGAF processes"""
    # Phase-specific roles
    VISION_ANALYST = "vision_analyst"
    BUSINESS_ARCHITECT = "business_architect"
    DATA_ARCHITECT = "data_architect"
    APPLICATION_ARCHITECT = "application_architect"
    TECHNOLOGY_ARCHITECT = "technology_architect"
    SOLUTION_ARCHITECT = "solution_architect"
    MIGRATION_PLANNER = "migration_planner"
    GOVERNANCE_OFFICER = "governance_officer"
    CHANGE_MANAGER = "change_manager"
    
    # Cross-cutting roles
    STAKEHOLDER_ANALYST = "stakeholder_analyst"
    REQUIREMENTS_ENGINEER = "requirements_engineer"
    COMPLIANCE_CHECKER = "compliance_checker"
    RISK_ASSESSOR = "risk_assessor"
    COST_ANALYST = "cost_analyst"
    INTEGRATION_SPECIALIST = "integration_specialist"
    SECURITY_ARCHITECT = "security_architect"
    
    # Collaborative roles
    TEAM_COORDINATOR = "team_coordinator"
    DECISION_FACILITATOR = "decision_facilitator"
    KNOWLEDGE_CURATOR = "knowledge_curator"
    QUALITY_REVIEWER = "quality_reviewer"


class AgentCapability(Enum):
    """Capabilities that agents can possess"""
    # Analysis capabilities
    ANALYZE_REQUIREMENTS = "analyze_requirements"
    ANALYZE_STAKEHOLDERS = "analyze_stakeholders"
    ANALYZE_GAPS = "analyze_gaps"
    ANALYZE_RISKS = "analyze_risks"
    ANALYZE_COSTS = "analyze_costs"
    ANALYZE_DEPENDENCIES = "analyze_dependencies"
    
    # Design capabilities
    DESIGN_ARCHITECTURE = "design_architecture"
    DESIGN_SOLUTIONS = "design_solutions"
    DESIGN_INTEGRATIONS = "design_integrations"
    DESIGN_MIGRATIONS = "design_migrations"
    
    # Validation capabilities
    VALIDATE_COMPLIANCE = "validate_compliance"
    VALIDATE_STANDARDS = "validate_standards"
    VALIDATE_QUALITY = "validate_quality"
    VALIDATE_SECURITY = "validate_security"
    
    # Recommendation capabilities
    RECOMMEND_PRINCIPLES = "recommend_principles"
    RECOMMEND_PATTERNS = "recommend_patterns"
    RECOMMEND_TECHNOLOGIES = "recommend_technologies"
    RECOMMEND_IMPROVEMENTS = "recommend_improvements"
    
    # Collaboration capabilities
    COORDINATE_TEAMS = "coordinate_teams"
    FACILITATE_DECISIONS = "facilitate_decisions"
    MANAGE_KNOWLEDGE = "manage_knowledge"
    COMMUNICATE_STAKEHOLDERS = "communicate_stakeholders"


class TaskPriority(Enum):
    """Priority levels for agent tasks"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class TaskStatus(Enum):
    """Status of agent tasks"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"
    CANCELLED = "cancelled"


@dataclass
class AgentTask:
    """Represents a task assigned to an AI agent"""
    task_id: str
    name: str
    description: str
    agent_role: AgentRole
    priority: TaskPriority
    required_capabilities: List[AgentCapability]
    
    # Task metadata
    created_at: datetime = field(default_factory=datetime.now)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    status: TaskStatus = TaskStatus.PENDING
    
    # Task context
    context: Dict[str, Any] = field(default_factory=dict)
    dependencies: List[str] = field(default_factory=list)
    
    # Results
    result: Optional[Dict[str, Any]] = None
    errors: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    
    def start(self) -> None:
        """Mark task as started"""
        self.status = TaskStatus.IN_PROGRESS
        self.started_at = datetime.now()
    
    def complete(self, result: Dict[str, Any]) -> None:
        """Mark task as completed with results"""
        self.status = TaskStatus.COMPLETED
        self.completed_at = datetime.now()
        self.result = result
    
    def fail(self, error: str) -> None:
        """Mark task as failed"""
        self.status = TaskStatus.FAILED
        self.completed_at = datetime.now()
        self.errors.append(error)
    
    def add_recommendation(self, recommendation: str) -> None:
        """Add a recommendation from the task"""
        self.recommendations.append(recommendation)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary"""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "agent_role": self.agent_role.value,
            "priority": self.priority.value,
            "status": self.status.value,
            "required_capabilities": [c.value for c in self.required_capabilities],
            "created_at": self.created_at.isoformat(),
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "context": self.context,
            "dependencies": self.dependencies,
            "result": self.result,
            "errors": self.errors,
            "recommendations": self.recommendations
        }


@dataclass
class AgentMemory:
    """Memory system for AI agents to store context and learnings"""
    short_term: Dict[str, Any] = field(default_factory=dict)
    long_term: List[Dict[str, Any]] = field(default_factory=list)
    episodic: List[Dict[str, Any]] = field(default_factory=list)
    
    def remember_short_term(self, key: str, value: Any) -> None:
        """Store information in short-term memory"""
        self.short_term[key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }
    
    def remember_long_term(self, memory: Dict[str, Any]) -> None:
        """Store information in long-term memory"""
        memory["timestamp"] = datetime.now().isoformat()
        self.long_term.append(memory)
    
    def remember_episode(self, episode: Dict[str, Any]) -> None:
        """Store an episodic memory (experience)"""
        episode["timestamp"] = datetime.now().isoformat()
        self.episodic.append(episode)
    
    def recall_short_term(self, key: str) -> Optional[Any]:
        """Recall from short-term memory"""
        mem = self.short_term.get(key)
        return mem["value"] if mem else None
    
    def search_long_term(self, query: str) -> List[Dict[str, Any]]:
        """Search long-term memory (simple keyword search)"""
        query_lower = query.lower()
        return [
            mem for mem in self.long_term
            if any(query_lower in str(v).lower() for v in mem.values())
        ]
    
    def clear_short_term(self) -> None:
        """Clear short-term memory"""
        self.short_term.clear()


class TOGAFAgent:
    """
    Base class for AI agents that work with TOGAF framework.
    
    Agents can:
    - Execute tasks autonomously
    - Collaborate with other agents
    - Analyze architecture artifacts
    - Make recommendations
    - Learn from experiences
    """
    
    def __init__(
        self,
        name: str,
        role: AgentRole,
        capabilities: List[AgentCapability],
        description: Optional[str] = None
    ):
        self.name = name
        self.role = role
        self.capabilities = capabilities
        self.description = description or f"{role.value} agent"
        
        # Agent state
        self.memory = AgentMemory()
        self.current_task: Optional[AgentTask] = None
        self.task_history: List[AgentTask] = []
        self.collaborators: List['TOGAFAgent'] = []
        
        # Performance metrics
        self.tasks_completed = 0
        self.tasks_failed = 0
        self.total_execution_time = 0.0
    
    def can_perform(self, task: AgentTask) -> bool:
        """Check if agent can perform a task"""
        # Check if agent has required capabilities
        return all(cap in self.capabilities for cap in task.required_capabilities)
    
    def assign_task(self, task: AgentTask) -> None:
        """Assign a task to this agent"""
        if not self.can_perform(task):
            raise ValueError(
                f"Agent {self.name} cannot perform task {task.name}. "
                f"Missing capabilities: {set(task.required_capabilities) - set(self.capabilities)}"
            )
        
        self.current_task = task
        task.start()
    
    def execute_task(self, task: AgentTask) -> Dict[str, Any]:
        """
        Execute a task (to be overridden by specialized agents).
        
        This is the main method where AI logic would be implemented.
        Subclasses should override this to provide specific functionality.
        """
        raise NotImplementedError(
            f"Agent {self.name} must implement execute_task method"
        )
    
    def complete_task(self, result: Dict[str, Any]) -> None:
        """Complete the current task"""
        if self.current_task:
            self.current_task.complete(result)
            self.task_history.append(self.current_task)
            self.tasks_completed += 1
            
            # Learn from experience
            self.memory.remember_episode({
                "task": self.current_task.to_dict(),
                "result": result,
                "success": True
            })
            
            self.current_task = None
    
    def fail_task(self, error: str) -> None:
        """Fail the current task"""
        if self.current_task:
            self.current_task.fail(error)
            self.task_history.append(self.current_task)
            self.tasks_failed += 1
            
            # Learn from failure
            self.memory.remember_episode({
                "task": self.current_task.to_dict(),
                "error": error,
                "success": False
            })
            
            self.current_task = None
    
    def collaborate_with(self, agent: 'TOGAFAgent') -> None:
        """Establish collaboration with another agent"""
        if agent not in self.collaborators:
            self.collaborators.append(agent)
    
    def get_recommendations(self) -> List[str]:
        """Get recommendations from completed tasks"""
        recommendations = []
        for task in self.task_history:
            recommendations.extend(task.recommendations)
        return recommendations
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get agent performance metrics"""
        total_tasks = self.tasks_completed + self.tasks_failed
        success_rate = (self.tasks_completed / total_tasks * 100) if total_tasks > 0 else 0
        
        return {
            "agent_name": self.name,
            "role": self.role.value,
            "tasks_completed": self.tasks_completed,
            "tasks_failed": self.tasks_failed,
            "total_tasks": total_tasks,
            "success_rate": success_rate,
            "average_execution_time": (
                self.total_execution_time / total_tasks if total_tasks > 0 else 0
            ),
            "collaborators": [c.name for c in self.collaborators]
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert agent to dictionary"""
        return {
            "name": self.name,
            "role": self.role.value,
            "capabilities": [c.value for c in self.capabilities],
            "description": self.description,
            "performance": self.get_performance_metrics(),
            "current_task": self.current_task.to_dict() if self.current_task else None
        }
    
    def __repr__(self) -> str:
        return f"TOGAFAgent(name='{self.name}', role={self.role.value}, capabilities={len(self.capabilities)})"


@dataclass
class AgentTeam:
    """Represents a collaborative team of AI agents"""
    team_id: str
    name: str
    description: str
    agents: List[TOGAFAgent] = field(default_factory=list)
    team_lead: Optional[TOGAFAgent] = None
    
    def add_agent(self, agent: TOGAFAgent) -> None:
        """Add an agent to the team"""
        if agent not in self.agents:
            self.agents.append(agent)
            
            # Establish collaboration between all team members
            for team_agent in self.agents:
                if team_agent != agent:
                    agent.collaborate_with(team_agent)
                    team_agent.collaborate_with(agent)
    
    def set_lead(self, agent: TOGAFAgent) -> None:
        """Set team lead"""
        if agent in self.agents:
            self.team_lead = agent
        else:
            raise ValueError(f"Agent {agent.name} is not in team {self.name}")
    
    def get_team_capabilities(self) -> List[AgentCapability]:
        """Get all capabilities available in the team"""
        capabilities = set()
        for agent in self.agents:
            capabilities.update(agent.capabilities)
        return list(capabilities)
    
    def assign_task_to_team(self, task: AgentTask) -> TOGAFAgent:
        """
        Assign a task to the most suitable team member.
        Returns the agent that will handle the task.
        """
        # Find agents that can perform the task
        capable_agents = [agent for agent in self.agents if agent.can_perform(task)]
        
        if not capable_agents:
            raise ValueError(
                f"No agent in team {self.name} can perform task {task.name}"
            )
        
        # Prefer team lead if capable
        if self.team_lead and self.team_lead in capable_agents:
            selected_agent = self.team_lead
        else:
            # Select agent with best success rate
            selected_agent = max(
                capable_agents,
                key=lambda a: (
                    a.tasks_completed / max(a.tasks_completed + a.tasks_failed, 1)
                )
            )
        
        selected_agent.assign_task(task)
        return selected_agent
    
    def get_team_performance(self) -> Dict[str, Any]:
        """Get team performance metrics"""
        total_completed = sum(a.tasks_completed for a in self.agents)
        total_failed = sum(a.tasks_failed for a in self.agents)
        total_tasks = total_completed + total_failed
        
        return {
            "team_id": self.team_id,
            "team_name": self.name,
            "team_size": len(self.agents),
            "team_lead": self.team_lead.name if self.team_lead else None,
            "total_capabilities": len(self.get_team_capabilities()),
            "tasks_completed": total_completed,
            "tasks_failed": total_failed,
            "success_rate": (total_completed / total_tasks * 100) if total_tasks > 0 else 0,
            "agent_performance": [a.get_performance_metrics() for a in self.agents]
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert team to dictionary"""
        return {
            "team_id": self.team_id,
            "name": self.name,
            "description": self.description,
            "team_lead": self.team_lead.name if self.team_lead else None,
            "agents": [a.to_dict() for a in self.agents],
            "performance": self.get_team_performance()
        }
