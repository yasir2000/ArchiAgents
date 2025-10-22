"""
CrewAI Team Integration for TOGAF Framework

This module provides specialized AI agent teams using CrewAI for collaborative
architecture work. Teams work together on complex TOGAF tasks that require
multiple perspectives and expertise.

Features:
- Specialized architecture agent crews
- Collaborative task execution
- Inter-agent communication
- Role-based responsibilities
- Automated workflow orchestration
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

from ..ai_agents.agent_base import (
    TOGAFAgent, AgentTask, AgentRole, AgentCapability,
    AgentTeam, TaskPriority, TaskStatus
)


# CrewAI will be optional - check if available
try:
    from crewai import Agent, Task, Crew, Process
    from crewai.tools import tool
    CREWAI_AVAILABLE = True
except ImportError:
    CREWAI_AVAILABLE = False
    # Define placeholder classes
    class Agent:
        pass
    class Task:
        pass
    class Crew:
        pass
    class Process:
        pass


@dataclass
class CrewConfiguration:
    """Configuration for a CrewAI team"""
    crew_name: str
    description: str
    process_type: str = "sequential"  # or "hierarchical"
    verbose: bool = True
    memory: bool = True
    max_iter: int = 15


class TOGAFArchitectureCrew:
    """
    Base class for TOGAF architecture crews using CrewAI.
    
    A crew is a team of specialized agents that collaborate on architecture tasks.
    """
    
    def __init__(
        self,
        config: CrewConfiguration,
        llm_provider: Optional[str] = None
    ):
        self.config = config
        self.llm_provider = llm_provider or "gpt-4"
        self.crew = None
        self.agents = []
        self.tasks = []
        
        if not CREWAI_AVAILABLE:
            raise RuntimeError(
                "CrewAI not available. Install with: pip install crewai"
            )
    
    def create_agent(
        self,
        role: str,
        goal: str,
        backstory: str,
        capabilities: List[str],
        verbose: bool = True,
        allow_delegation: bool = True
    ) -> Agent:
        """Create a CrewAI agent"""
        agent = Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            verbose=verbose,
            allow_delegation=allow_delegation,
            llm=self.llm_provider
        )
        self.agents.append(agent)
        return agent
    
    def create_task(
        self,
        description: str,
        agent: Agent,
        expected_output: str,
        context: Optional[List[Task]] = None
    ) -> Task:
        """Create a CrewAI task"""
        task = Task(
            description=description,
            agent=agent,
            expected_output=expected_output,
            context=context or []
        )
        self.tasks.append(task)
        return task
    
    def build_crew(self) -> Crew:
        """Build the crew from agents and tasks (to be overridden)"""
        raise NotImplementedError("Subclasses must implement build_crew")
    
    def execute(self, inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute the crew's tasks"""
        if not self.crew:
            self.crew = self.build_crew()
        
        result = self.crew.kickoff(inputs=inputs or {})
        
        return {
            "crew_name": self.config.crew_name,
            "result": result,
            "timestamp": datetime.now().isoformat()
        }


class PhaseAVisionCrew(TOGAFArchitectureCrew):
    """
    Specialized crew for TOGAF Phase A: Architecture Vision
    
    Team composition:
    - Vision Strategist: Defines strategic direction
    - Stakeholder Analyst: Identifies and analyzes stakeholders
    - Principles Architect: Establishes architecture principles
    - Requirements Engineer: Captures and validates requirements
    """
    
    def __init__(self, llm_provider: Optional[str] = None):
        config = CrewConfiguration(
            crew_name="Phase A Vision Crew",
            description="Collaborative team for creating architecture vision",
            process_type="sequential",
            verbose=True
        )
        super().__init__(config, llm_provider)
        self._setup_agents()
    
    def _setup_agents(self) -> None:
        """Setup specialized agents for Phase A"""
        
        # Vision Strategist
        self.vision_strategist = self.create_agent(
            role="Architecture Vision Strategist",
            goal="Define clear and compelling architecture vision that aligns with business strategy",
            backstory="""You are a senior enterprise architect with 15+ years of experience
            in defining architecture visions for Fortune 500 companies. You excel at translating
            business strategy into architectural direction and creating compelling visions that
            inspire stakeholders.""",
            capabilities=["strategic_thinking", "business_alignment", "vision_creation"]
        )
        
        # Stakeholder Analyst
        self.stakeholder_analyst = self.create_agent(
            role="Stakeholder Relationship Analyst",
            goal="Identify all key stakeholders and understand their concerns and requirements",
            backstory="""You are an expert in stakeholder management with deep understanding
            of organizational dynamics. You excel at identifying hidden stakeholders, understanding
            political landscapes, and translating stakeholder concerns into actionable requirements.""",
            capabilities=["stakeholder_analysis", "requirements_elicitation", "communication"]
        )
        
        # Principles Architect
        self.principles_architect = self.create_agent(
            role="Architecture Principles Expert",
            goal="Establish robust architecture principles that guide decision-making",
            backstory="""You are a thought leader in architecture governance with expertise
            in establishing principles that balance innovation with pragmatism. You create
            principles that are clear, actionable, and aligned with industry best practices.""",
            capabilities=["principle_definition", "governance", "best_practices"]
        )
        
        # Requirements Engineer
        self.requirements_engineer = self.create_agent(
            role="Requirements Engineering Specialist",
            goal="Capture, validate, and prioritize architecture requirements",
            backstory="""You are a meticulous requirements engineer with expertise in
            both functional and non-functional requirements. You excel at ensuring requirements
            are specific, measurable, achievable, relevant, and time-bound (SMART).""",
            capabilities=["requirements_engineering", "validation", "prioritization"]
        )
    
    def build_crew(self) -> Crew:
        """Build Phase A crew with tasks"""
        
        # Task 1: Define Vision
        vision_task = self.create_task(
            description="""Analyze the business context and strategic goals to create
            a compelling architecture vision. The vision should:
            1. Align with business strategy
            2. Address key business drivers
            3. Be inspirational yet achievable
            4. Provide clear direction for architecture work
            
            Output a vision statement with supporting rationale.""",
            agent=self.vision_strategist,
            expected_output="A clear vision statement (2-3 paragraphs) with business alignment rationale"
        )
        
        # Task 2: Analyze Stakeholders
        stakeholder_task = self.create_task(
            description="""Identify and analyze all key stakeholders for the architecture initiative.
            For each stakeholder:
            1. Define their role and influence level
            2. Identify their key concerns
            3. Determine their requirements
            4. Assess potential conflicts or alignments
            
            Create a comprehensive stakeholder map.""",
            agent=self.stakeholder_analyst,
            expected_output="Stakeholder analysis with 5-10 key stakeholders, their concerns, and influence levels",
            context=[vision_task]
        )
        
        # Task 3: Establish Principles
        principles_task = self.create_task(
            description="""Based on the vision and stakeholder needs, establish 5-7 core
            architecture principles. For each principle:
            1. Provide a clear name and statement
            2. Explain the rationale
            3. List implications for implementation
            4. Ensure alignment with industry best practices
            
            Principles should cover business, data, application, and technology layers.""",
            agent=self.principles_architect,
            expected_output="5-7 architecture principles with statements, rationale, and implications",
            context=[vision_task, stakeholder_task]
        )
        
        # Task 4: Capture Requirements
        requirements_task = self.create_task(
            description="""Synthesize stakeholder concerns and vision direction into
            specific architecture requirements. Requirements should:
            1. Be specific and measurable
            2. Cover functional and non-functional aspects
            3. Be prioritized (Critical, High, Medium, Low)
            4. Include acceptance criteria
            5. Identify dependencies and constraints
            
            Validate requirements against SMART criteria.""",
            agent=self.requirements_engineer,
            expected_output="10-15 prioritized requirements with acceptance criteria",
            context=[vision_task, stakeholder_task, principles_task]
        )
        
        # Build crew
        self.crew = Crew(
            agents=[
                self.vision_strategist,
                self.stakeholder_analyst,
                self.principles_architect,
                self.requirements_engineer
            ],
            tasks=[
                vision_task,
                stakeholder_task,
                principles_task,
                requirements_task
            ],
            process=Process.sequential,
            verbose=self.config.verbose,
            memory=self.config.memory
        )
        
        return self.crew


class BusinessArchitectureCrew(TOGAFArchitectureCrew):
    """
    Specialized crew for TOGAF Phase B: Business Architecture
    
    Team composition:
    - Capability Modeler: Maps business capabilities
    - Process Architect: Designs business processes
    - Value Stream Analyst: Analyzes value streams
    - Gap Analyst: Performs gap analysis
    """
    
    def __init__(self, llm_provider: Optional[str] = None):
        config = CrewConfiguration(
            crew_name="Phase B Business Architecture Crew",
            description="Collaborative team for business architecture design",
            process_type="sequential"
        )
        super().__init__(config, llm_provider)
        self._setup_agents()
    
    def _setup_agents(self) -> None:
        """Setup specialized agents for Phase B"""
        
        self.capability_modeler = self.create_agent(
            role="Business Capability Modeling Expert",
            goal="Create comprehensive business capability models that represent organizational abilities",
            backstory="""You are an expert in business capability modeling with experience
            across multiple industries. You understand how to decompose business functions
            into capabilities and map them to value delivery.""",
            capabilities=["capability_modeling", "decomposition", "business_analysis"]
        )
        
        self.process_architect = self.create_agent(
            role="Business Process Architect",
            goal="Design efficient and effective business processes",
            backstory="""You are a certified business process management professional
            with expertise in process mapping, optimization, and automation. You excel
            at identifying inefficiencies and designing streamlined processes.""",
            capabilities=["process_modeling", "bpmn", "optimization"]
        )
        
        self.value_stream_analyst = self.create_agent(
            role="Value Stream Analysis Specialist",
            goal="Analyze and optimize value streams for maximum customer value",
            backstory="""You are a lean thinking expert with deep understanding of
            value stream mapping and analysis. You identify waste, bottlenecks, and
            opportunities for value creation.""",
            capabilities=["value_stream_mapping", "lean_thinking", "flow_analysis"]
        )
        
        self.gap_analyst = self.create_agent(
            role="Architecture Gap Analysis Expert",
            goal="Identify gaps between current and target business architecture",
            backstory="""You are skilled at comparing as-is and to-be states to identify
            gaps, redundancies, and transformation opportunities. You provide clear roadmaps
            for closing capability gaps.""",
            capabilities=["gap_analysis", "transformation_planning", "impact_assessment"]
        )
    
    def build_crew(self) -> Crew:
        """Build Phase B crew with tasks"""
        
        # Task 1: Model Capabilities
        capability_task = self.create_task(
            description="""Create a comprehensive business capability model:
            1. Identify 15-20 core business capabilities
            2. Organize into logical capability domains
            3. Define maturity levels for each capability
            4. Map capabilities to business outcomes
            5. Identify capability dependencies""",
            agent=self.capability_modeler,
            expected_output="Business capability model with 15-20 capabilities organized by domain"
        )
        
        # Task 2: Map Processes
        process_task = self.create_task(
            description="""Design key business processes:
            1. Identify 8-10 critical business processes
            2. Map process flows with activities and decision points
            3. Identify process owners and stakeholders
            4. Define process inputs, outputs, and metrics
            5. Highlight automation opportunities""",
            agent=self.process_architect,
            expected_output="8-10 business process models with flows and metrics",
            context=[capability_task]
        )
        
        # Task 3: Analyze Value Streams
        value_stream_task = self.create_task(
            description="""Analyze end-to-end value streams:
            1. Map 3-5 key value streams
            2. Identify value-adding and non-value-adding activities
            3. Calculate cycle times and identify bottlenecks
            4. Recommend improvements for flow optimization""",
            agent=self.value_stream_analyst,
            expected_output="3-5 value stream maps with optimization recommendations",
            context=[capability_task, process_task]
        )
        
        # Task 4: Perform Gap Analysis
        gap_task = self.create_task(
            description="""Conduct comprehensive gap analysis:
            1. Compare current vs. target capabilities
            2. Identify capability gaps and redundancies
            3. Assess impact and priority of each gap
            4. Recommend initiatives to close gaps
            5. Estimate effort and timeline""",
            agent=self.gap_analyst,
            expected_output="Gap analysis report with prioritized initiatives",
            context=[capability_task, process_task, value_stream_task]
        )
        
        self.crew = Crew(
            agents=[
                self.capability_modeler,
                self.process_architect,
                self.value_stream_analyst,
                self.gap_analyst
            ],
            tasks=[
                capability_task,
                process_task,
                value_stream_task,
                gap_task
            ],
            process=Process.sequential,
            verbose=self.config.verbose
        )
        
        return self.crew


class TechnologyArchitectureCrew(TOGAFArchitectureCrew):
    """
    Specialized crew for TOGAF Phase D: Technology Architecture
    
    Team composition:
    - Cloud Architect: Designs cloud infrastructure
    - Security Architect: Defines security controls
    - Integration Architect: Plans integration patterns
    - DevOps Engineer: Establishes CI/CD and automation
    """
    
    def __init__(self, llm_provider: Optional[str] = None):
        config = CrewConfiguration(
            crew_name="Phase D Technology Architecture Crew",
            description="Collaborative team for technology architecture design",
            process_type="hierarchical"  # Hierarchical for technical coordination
        )
        super().__init__(config, llm_provider)
        self._setup_agents()
    
    def _setup_agents(self) -> None:
        """Setup specialized agents for Phase D"""
        
        self.cloud_architect = self.create_agent(
            role="Cloud Solutions Architect",
            goal="Design scalable, resilient cloud infrastructure",
            backstory="""You are a certified cloud architect with expertise in AWS, Azure,
            and GCP. You design cloud-native solutions that optimize for performance,
            cost, and reliability.""",
            capabilities=["cloud_design", "scalability", "cost_optimization"],
            allow_delegation=True  # Can delegate to others
        )
        
        self.security_architect = self.create_agent(
            role="Security Architecture Expert",
            goal="Establish comprehensive security controls and compliance",
            backstory="""You are a cybersecurity expert with certifications in CISSP,
            CISM, and cloud security. You design zero-trust architectures and ensure
            compliance with industry standards.""",
            capabilities=["security_design", "compliance", "risk_management"],
            allow_delegation=False
        )
        
        self.integration_architect = self.create_agent(
            role="Integration Architecture Specialist",
            goal="Design robust integration patterns and APIs",
            backstory="""You are an integration expert skilled in API design, message
            queuing, event-driven architecture, and service mesh patterns. You ensure
            seamless connectivity across systems.""",
            capabilities=["api_design", "event_driven", "microservices"],
            allow_delegation=False
        )
        
        self.devops_engineer = self.create_agent(
            role="DevOps & Automation Engineer",
            goal="Establish CI/CD pipelines and infrastructure automation",
            backstory="""You are a DevOps practitioner with expertise in GitOps,
            infrastructure as code, and continuous delivery. You automate everything
            to enable rapid, reliable deployments.""",
            capabilities=["cicd", "iac", "automation"],
            allow_delegation=False
        )
    
    def build_crew(self) -> Crew:
        """Build Phase D crew with tasks"""
        
        cloud_task = self.create_task(
            description="""Design cloud infrastructure architecture:
            1. Select appropriate cloud services (compute, storage, networking)
            2. Design for high availability and disaster recovery
            3. Plan multi-region deployment strategy
            4. Optimize for cost and performance
            5. Define infrastructure scaling strategy""",
            agent=self.cloud_architect,
            expected_output="Cloud infrastructure design with service selection and DR strategy"
        )
        
        security_task = self.create_task(
            description="""Establish security architecture:
            1. Design zero-trust network architecture
            2. Define identity and access management (IAM)
            3. Plan encryption strategy (at-rest and in-transit)
            4. Establish security monitoring and SIEM
            5. Ensure compliance (SOC2, ISO27001, GDPR)""",
            agent=self.security_architect,
            expected_output="Security architecture with controls and compliance mapping",
            context=[cloud_task]
        )
        
        integration_task = self.create_task(
            description="""Design integration architecture:
            1. Define API strategy (REST, GraphQL, gRPC)
            2. Design event-driven architecture patterns
            3. Plan service mesh implementation
            4. Establish API gateway and management
            5. Define integration standards and protocols""",
            agent=self.integration_architect,
            expected_output="Integration architecture with API strategy and patterns",
            context=[cloud_task]
        )
        
        devops_task = self.create_task(
            description="""Establish DevOps and automation:
            1. Design CI/CD pipeline architecture
            2. Define infrastructure as code strategy
            3. Plan monitoring and observability
            4. Establish GitOps workflows
            5. Define deployment strategies (blue/green, canary)""",
            agent=self.devops_engineer,
            expected_output="DevOps architecture with CI/CD and IaC strategies",
            context=[cloud_task, security_task, integration_task]
        )
        
        self.crew = Crew(
            agents=[
                self.cloud_architect,
                self.security_architect,
                self.integration_architect,
                self.devops_engineer
            ],
            tasks=[
                cloud_task,
                security_task,
                integration_task,
                devops_task
            ],
            process=Process.hierarchical,
            manager_llm=self.llm_provider,
            verbose=self.config.verbose
        )
        
        return self.crew


def create_phase_crew(
    phase_name: str,
    llm_provider: Optional[str] = None
) -> Optional[TOGAFArchitectureCrew]:
    """
    Factory function to create appropriate crew for a TOGAF phase.
    
    Args:
        phase_name: Name of the TOGAF phase
        llm_provider: LLM model to use (default: gpt-4)
    
    Returns:
        TOGAFArchitectureCrew instance or None if phase not supported
    """
    crews = {
        "Phase A": PhaseAVisionCrew,
        "Phase B": BusinessArchitectureCrew,
        "Phase D": TechnologyArchitectureCrew,
        # Additional phases would be added here
    }
    
    crew_class = crews.get(phase_name)
    if crew_class:
        return crew_class(llm_provider)
    
    return None
