"""
TOGAF AI Agent Orchestrator

Master orchestrator that coordinates AI agents using both LangGraph workflows
and CrewAI teams to automate TOGAF ADM processes.

This orchestrator:
- Manages agent teams for each TOGAF phase
- Coordinates workflow execution using LangGraph
- Delegates complex tasks to CrewAI teams
- Supports multiple LLM providers (OpenAI, Anthropic, Google, Ollama, etc.)
- Tracks progress and performance
- Generates intelligent recommendations
- Learns from execution patterns
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import json
from pathlib import Path

from ..adm.togaf_orchestrator import TOGAFADMOrchestrator
from ..ai_agents.agent_base import (
    TOGAFAgent, AgentTeam, AgentRole, AgentCapability,
    AgentTask, TaskPriority
)
from ..ai_agents.llm_providers import (
    LLMProviderManager, LLMProvider, LLMConfig,
    get_recommended_models, get_provider_info
)
from ..ai_agents.langgraph_workflows import (
    PhaseWorkflowGraph, PhaseAWorkflowGraph, PhaseBWorkflowGraph,
    LANGGRAPH_AVAILABLE
)
from ..ai_agents.crewai_teams import (
    TOGAFArchitectureCrew, PhaseAVisionCrew, BusinessArchitectureCrew,
    TechnologyArchitectureCrew, CREWAI_AVAILABLE
)


class AIAgentOrchestrator:
    """
    Master orchestrator for AI-powered TOGAF architecture development.
    
    Combines:
    - TOGAF ADM orchestration
    - LangGraph workflow automation
    - CrewAI collaborative teams
    - Intelligent decision making
    - Continuous learning
    """
    
    def __init__(
        self,
        enterprise_name: str,
        project_name: str,
        scope: str,
        llm_provider: Optional[str] = None,
        llm_config: Optional[Dict[str, Any]] = None,
        enable_langgraph: bool = True,
        enable_crewai: bool = True
    ):
        """
        Initialize AI Agent Orchestrator
        
        Args:
            enterprise_name: Name of the enterprise
            project_name: Name of the architecture project
            scope: Scope of the architecture work
            llm_provider: LLM model/provider to use. Supports:
                - OpenAI: "gpt-4", "gpt-3.5-turbo"
                - Azure: "azure/gpt-4"
                - Anthropic: "claude-3-opus-20240229", "claude-3-sonnet-20240229"
                - Google: "gemini-pro", "gemini-1.5-pro"
                - Ollama (local): "llama3.1", "mistral", "mixtral", "phi-2"
                - Hugging Face: "org/model-name"
                Default: "gpt-4"
            llm_config: Additional LLM configuration (api_key, temperature, etc.)
            enable_langgraph: Enable LangGraph workflows
            enable_crewai: Enable CrewAI teams
        """
        # Initialize base TOGAF orchestrator
        self.togaf_orchestrator = TOGAFADMOrchestrator(
            enterprise_name=enterprise_name,
            project_name=project_name,
            architecture_scope=scope
        )
        
        # LLM configuration
        self.llm_model_name = llm_provider or "gpt-4"
        self.llm_config = llm_config or {}
        self.llm_provider_type = LLMProviderManager.auto_detect_provider(self.llm_model_name)
        
        # Create LLM instance
        self.llm = None
        try:
            self.llm = LLMProviderManager.create_llm(
                model_name=self.llm_model_name,
                **self.llm_config
            )
        except Exception as e:
            print(f"⚠️  Could not initialize LLM: {e}")
            print(f"   AI features will be limited without LLM")
        
        self.enable_langgraph = enable_langgraph and LANGGRAPH_AVAILABLE
        self.enable_crewai = enable_crewai and CREWAI_AVAILABLE
        
        # AI components
        self.agent_teams: Dict[str, AgentTeam] = {}
        self.workflow_graphs: Dict[str, PhaseWorkflowGraph] = {}
        self.crewai_teams: Dict[str, TOGAFArchitectureCrew] = {}
        
        # Execution tracking
        self.ai_execution_history: List[Dict[str, Any]] = []
        self.ai_recommendations: List[str] = []
        self.ai_learnings: List[Dict[str, Any]] = []
        
        # Initialize AI capabilities
        self._initialize_ai_system()
    
    def _initialize_ai_system(self) -> None:
        """Initialize AI agent system"""
        print("\n🤖 Initializing AI Multi-Agent System...")
        
        # Check capabilities
        capabilities = []
        if self.enable_langgraph:
            capabilities.append("LangGraph workflows")
        if self.enable_crewai:
            capabilities.append("CrewAI teams")
        
        if not capabilities:
            print("⚠️  AI agents disabled - Install langgraph and/or crewai")
            print("   pip install langgraph crewai")
            return
        
        print(f"✅ AI capabilities enabled: {', '.join(capabilities)}")
        
        # Initialize agent teams for each phase
        self._setup_agent_teams()
        
        # Initialize workflows if LangGraph available
        if self.enable_langgraph:
            self._setup_langgraph_workflows()
        
        # Initialize CrewAI teams if available
        if self.enable_crewai:
            self._setup_crewai_teams()
    
    def _setup_agent_teams(self) -> None:
        """Setup AI agent teams for TOGAF phases"""
        
        # Phase A Vision Team
        phase_a_team = AgentTeam(
            team_id="phase_a_vision",
            name="Architecture Vision Team",
            description="AI agents for creating architecture vision"
        )
        
        # Create Phase A agents
        vision_analyst = self._create_vision_analyst()
        stakeholder_analyst = self._create_stakeholder_analyst()
        principles_architect = self._create_principles_architect()
        requirements_engineer = self._create_requirements_engineer()
        quality_reviewer = self._create_quality_reviewer()
        
        phase_a_team.add_agent(vision_analyst)
        phase_a_team.add_agent(stakeholder_analyst)
        phase_a_team.add_agent(principles_architect)
        phase_a_team.add_agent(requirements_engineer)
        phase_a_team.add_agent(quality_reviewer)
        phase_a_team.set_lead(vision_analyst)
        
        self.agent_teams["Phase A"] = phase_a_team
        
        # Phase B Business Team
        phase_b_team = AgentTeam(
            team_id="phase_b_business",
            name="Business Architecture Team",
            description="AI agents for business architecture design"
        )
        
        business_architect = self._create_business_architect()
        phase_b_team.add_agent(business_architect)
        phase_b_team.add_agent(quality_reviewer)
        phase_b_team.set_lead(business_architect)
        
        self.agent_teams["Phase B"] = phase_b_team
        
        print(f"✅ Created {len(self.agent_teams)} agent teams")
    
    def _create_vision_analyst(self) -> TOGAFAgent:
        """Create Vision Analyst agent"""
        return TOGAFAgent(
            name="Vision Analyst",
            role=AgentRole.VISION_ANALYST,
            capabilities=[
                AgentCapability.ANALYZE_REQUIREMENTS,
                AgentCapability.RECOMMEND_PRINCIPLES,
                AgentCapability.DESIGN_ARCHITECTURE
            ],
            description="AI agent specialized in creating architecture visions"
        )
    
    def _create_stakeholder_analyst(self) -> TOGAFAgent:
        """Create Stakeholder Analyst agent"""
        return TOGAFAgent(
            name="Stakeholder Analyst",
            role=AgentRole.STAKEHOLDER_ANALYST,
            capabilities=[
                AgentCapability.ANALYZE_STAKEHOLDERS,
                AgentCapability.COMMUNICATE_STAKEHOLDERS,
                AgentCapability.ANALYZE_REQUIREMENTS
            ],
            description="AI agent specialized in stakeholder analysis"
        )
    
    def _create_principles_architect(self) -> TOGAFAgent:
        """Create Principles Architect agent"""
        return TOGAFAgent(
            name="Principles Architect",
            role=AgentRole.VISION_ANALYST,
            capabilities=[
                AgentCapability.RECOMMEND_PRINCIPLES,
                AgentCapability.VALIDATE_STANDARDS
            ],
            description="AI agent specialized in architecture principles"
        )
    
    def _create_requirements_engineer(self) -> TOGAFAgent:
        """Create Requirements Engineer agent"""
        return TOGAFAgent(
            name="Requirements Engineer",
            role=AgentRole.REQUIREMENTS_ENGINEER,
            capabilities=[
                AgentCapability.ANALYZE_REQUIREMENTS,
                AgentCapability.VALIDATE_QUALITY,
                AgentCapability.ANALYZE_DEPENDENCIES
            ],
            description="AI agent specialized in requirements engineering"
        )
    
    def _create_quality_reviewer(self) -> TOGAFAgent:
        """Create Quality Reviewer agent"""
        return TOGAFAgent(
            name="Quality Reviewer",
            role=AgentRole.QUALITY_REVIEWER,
            capabilities=[
                AgentCapability.VALIDATE_QUALITY,
                AgentCapability.VALIDATE_COMPLIANCE,
                AgentCapability.VALIDATE_STANDARDS,
                AgentCapability.VALIDATE_SECURITY
            ],
            description="AI agent specialized in quality assurance"
        )
    
    def _create_business_architect(self) -> TOGAFAgent:
        """Create Business Architect agent"""
        return TOGAFAgent(
            name="Business Architect",
            role=AgentRole.BUSINESS_ARCHITECT,
            capabilities=[
                AgentCapability.DESIGN_ARCHITECTURE,
                AgentCapability.ANALYZE_GAPS,
                AgentCapability.ANALYZE_DEPENDENCIES
            ],
            description="AI agent specialized in business architecture"
        )
    
    def _setup_langgraph_workflows(self) -> None:
        """Setup LangGraph workflow graphs"""
        try:
            # Get agents for each phase
            phase_a_agents = list(self.agent_teams.get("Phase A", AgentTeam("", "", "")).agents)
            phase_b_agents = list(self.agent_teams.get("Phase B", AgentTeam("", "", "")).agents)
            
            # Create workflow graphs
            if phase_a_agents:
                self.workflow_graphs["Phase A"] = PhaseAWorkflowGraph(phase_a_agents)
            
            if phase_b_agents:
                self.workflow_graphs["Phase B"] = PhaseBWorkflowGraph(phase_b_agents)
            
            print(f"✅ Created {len(self.workflow_graphs)} LangGraph workflows")
        except Exception as e:
            print(f"⚠️  LangGraph setup warning: {str(e)}")
    
    def _setup_crewai_teams(self) -> None:
        """Setup CrewAI teams"""
        try:
            self.crewai_teams["Phase A"] = PhaseAVisionCrew(self.llm_provider)
            self.crewai_teams["Phase B"] = BusinessArchitectureCrew(self.llm_provider)
            self.crewai_teams["Phase D"] = TechnologyArchitectureCrew(self.llm_provider)
            
            print(f"✅ Created {len(self.crewai_teams)} CrewAI teams")
        except Exception as e:
            print(f"⚠️  CrewAI setup warning: {str(e)}")
    
    def execute_phase_with_ai(
        self,
        phase_name: str,
        use_langgraph: bool = True,
        use_crewai: bool = False,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute a TOGAF phase with AI automation.
        
        Args:
            phase_name: Name of the phase (e.g., "Phase A", "Phase B")
            use_langgraph: Use LangGraph workflow orchestration
            use_crewai: Use CrewAI collaborative teams
            context: Additional context for execution
        
        Returns:
            Results including AI insights and recommendations
        """
        print(f"\n🤖 Executing {phase_name} with AI automation...")
        
        start_time = datetime.now()
        results = {
            "phase": phase_name,
            "execution_mode": [],
            "ai_outputs": {},
            "recommendations": [],
            "timestamp": start_time.isoformat()
        }
        
        # LangGraph workflow execution
        if use_langgraph and self.enable_langgraph and phase_name in self.workflow_graphs:
            print(f"  ⚙️  Running LangGraph workflow...")
            try:
                workflow = self.workflow_graphs[phase_name]
                workflow_result = workflow.execute_workflow(context)
                results["ai_outputs"]["langgraph"] = workflow_result
                results["execution_mode"].append("LangGraph")
                results["recommendations"].extend(workflow_result.get("recommendations", []))
            except Exception as e:
                results["ai_outputs"]["langgraph_error"] = str(e)
                print(f"  ⚠️  LangGraph execution failed: {str(e)}")
        
        # CrewAI team execution
        if use_crewai and self.enable_crewai and phase_name in self.crewai_teams:
            print(f"  👥 Running CrewAI team collaboration...")
            try:
                crew = self.crewai_teams[phase_name]
                crew_result = crew.execute(inputs=context or {})
                results["ai_outputs"]["crewai"] = crew_result
                results["execution_mode"].append("CrewAI")
            except Exception as e:
                results["ai_outputs"]["crewai_error"] = str(e)
                print(f"  ⚠️  CrewAI execution failed: {str(e)}")
        
        # Calculate duration
        duration = (datetime.now() - start_time).total_seconds()
        results["duration_seconds"] = duration
        
        # Store execution
        self.ai_execution_history.append(results)
        
        print(f"✅ {phase_name} AI execution completed in {duration:.2f}s")
        return results
    
    def get_ai_recommendations(self) -> List[str]:
        """Get all AI-generated recommendations"""
        recommendations = []
        for execution in self.ai_execution_history:
            recommendations.extend(execution.get("recommendations", []))
        return recommendations
    
    def get_ai_performance_metrics(self) -> Dict[str, Any]:
        """Get AI system performance metrics"""
        total_executions = len(self.ai_execution_history)
        total_duration = sum(e.get("duration_seconds", 0) for e in self.ai_execution_history)
        
        langgraph_executions = sum(
            1 for e in self.ai_execution_history 
            if "LangGraph" in e.get("execution_mode", [])
        )
        crewai_executions = sum(
            1 for e in self.ai_execution_history 
            if "CrewAI" in e.get("execution_mode", [])
        )
        
        # Agent team performance
        team_metrics = {}
        for phase_name, team in self.agent_teams.items():
            team_metrics[phase_name] = team.get_team_performance()
        
        return {
            "total_ai_executions": total_executions,
            "total_duration_seconds": total_duration,
            "average_duration": total_duration / total_executions if total_executions > 0 else 0,
            "langgraph_executions": langgraph_executions,
            "crewai_executions": crewai_executions,
            "total_recommendations": len(self.get_ai_recommendations()),
            "agent_teams": team_metrics,
            "capabilities": {
                "langgraph_enabled": self.enable_langgraph,
                "crewai_enabled": self.enable_crewai
            }
        }
    
    def save_ai_execution_log(self, filepath: str) -> None:
        """Save AI execution history to file"""
        log_data = {
            "enterprise": self.togaf_orchestrator.enterprise_name,
            "project": self.togaf_orchestrator.project_name,
            "ai_executions": self.ai_execution_history,
            "recommendations": self.get_ai_recommendations(),
            "performance_metrics": self.get_ai_performance_metrics(),
            "timestamp": datetime.now().isoformat()
        }
        
        with open(filepath, 'w') as f:
            json.dump(log_data, f, indent=2, default=str)
        
        print(f"✅ AI execution log saved: {filepath}")
    
    def generate_ai_insights_report(self) -> Dict[str, Any]:
        """Generate comprehensive AI insights report"""
        metrics = self.get_ai_performance_metrics()
        recommendations = self.get_ai_recommendations()
        
        return {
            "executive_summary": {
                "total_ai_executions": metrics["total_ai_executions"],
                "ai_efficiency_gain": f"{metrics['average_duration']:.2f}s average",
                "recommendations_generated": len(recommendations),
                "automation_coverage": {
                    "langgraph_workflows": metrics["langgraph_executions"],
                    "crewai_collaborations": metrics["crewai_executions"]
                }
            },
            "ai_recommendations": recommendations,
            "agent_performance": metrics["agent_teams"],
            "execution_history": self.ai_execution_history,
            "capabilities": {
                "workflow_orchestration": self.enable_langgraph,
                "collaborative_agents": self.enable_crewai,
                "llm_provider": self.llm_model_name,
                "llm_provider_type": self.llm_provider_type.value
            }
        }
    
    # LLM Provider Management Methods
    
    def get_llm_info(self) -> Dict[str, Any]:
        """Get information about current LLM provider"""
        return {
            "model": self.llm_model_name,
            "provider": self.llm_provider_type.value,
            "configured": self.llm is not None,
            "config": self.llm_config
        }
    
    def switch_llm_provider(
        self,
        model_name: str,
        **config
    ) -> bool:
        """
        Switch to a different LLM provider
        
        Args:
            model_name: New model name (e.g., "llama3.1", "claude-3-opus")
            **config: Additional configuration
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Create new LLM instance
            new_llm = LLMProviderManager.create_llm(
                model_name=model_name,
                **config
            )
            
            # Update configuration
            self.llm = new_llm
            self.llm_model_name = model_name
            self.llm_config = config
            self.llm_provider_type = LLMProviderManager.auto_detect_provider(model_name)
            
            print(f"✅ Switched to {model_name} ({self.llm_provider_type.value})")
            return True
            
        except Exception as e:
            print(f"❌ Failed to switch provider: {e}")
            return False
    
    @staticmethod
    def list_available_providers() -> List[str]:
        """List all available LLM providers"""
        return LLMProviderManager.get_available_providers()
    
    @staticmethod
    def get_recommended_models_by_use_case() -> Dict[str, List[str]]:
        """Get recommended models by use case"""
        return get_recommended_models()
    
    @staticmethod
    def get_all_provider_info() -> Dict[str, Dict[str, Any]]:
        """Get information about all providers"""
        return get_provider_info()
    
    @staticmethod
    def print_provider_guide():
        """Print helpful guide for LLM providers"""
        print("\n" + "=" * 80)
        print("LLM PROVIDER GUIDE")
        print("=" * 80)
        
        info = get_provider_info()
        for provider_id, details in info.items():
            print(f"\n📦 {details['name']}")
            print(f"   Models: {', '.join(details['models'][:3])}")
            print(f"   Install: {details['requires']}")
            if details.get('setup'):
                print(f"   Setup: {details['setup']}")
            print(f"   API Key: {details['api_key']}")
            print(f"   Pricing: {details['pricing']}")
        
        print("\n" + "=" * 80)
        print("RECOMMENDED MODELS BY USE CASE")
        print("=" * 80)
        
        recommendations = get_recommended_models()
        for use_case, models in recommendations.items():
            print(f"\n🎯 {use_case.replace('_', ' ').title()}:")
            for model in models:
                print(f"   • {model}")
        
        print("\n" + "=" * 80)
    
    def __repr__(self) -> str:
        return (
            f"AIAgentOrchestrator("
            f"enterprise='{self.togaf_orchestrator.enterprise_name}', "
            f"llm='{self.llm_model_name}', "
            f"langgraph={self.enable_langgraph}, "
            f"crewai={self.enable_crewai}, "
            f"teams={len(self.agent_teams)})"
        )
