"""
LangGraph Workflow Orchestration for TOGAF ADM

This module provides state machine-based workflow orchestration for TOGAF phases
using LangGraph. Each phase is modeled as a graph with nodes representing tasks
and edges representing transitions.

Features:
- State-based workflow management
- Conditional branching based on validation
- Parallel task execution
- Error handling and recovery
- Progress tracking
"""

from typing import Dict, List, Any, Optional, TypedDict, Annotated
from enum import Enum
import operator
from datetime import datetime

from ..ai_agents.agent_base import (
    TOGAFAgent, AgentTask, AgentRole, AgentCapability,
    TaskPriority, TaskStatus
)


# LangGraph will be optional - check if available
try:
    from langgraph.graph import StateGraph, END
    from langgraph.checkpoint.memory import MemorySaver
    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False
    # Define placeholder classes for type hints
    class StateGraph:
        pass
    END = "END"


class WorkflowState(TypedDict):
    """State for TOGAF workflow graph"""
    phase: str
    current_step: str
    completed_steps: Annotated[List[str], operator.add]
    artifacts: Dict[str, Any]
    recommendations: Annotated[List[str], operator.add]
    errors: Annotated[List[str], operator.add]
    validation_passed: bool
    agent_outputs: Dict[str, Any]
    iteration: int


class PhaseStep(Enum):
    """Standard steps in TOGAF phase workflows"""
    # Common steps
    INITIALIZE = "initialize"
    GATHER_INPUTS = "gather_inputs"
    ANALYZE = "analyze"
    DESIGN = "design"
    VALIDATE = "validate"
    REVIEW = "review"
    GENERATE_DELIVERABLES = "generate_deliverables"
    COMPLETE = "complete"
    
    # Phase A specific
    DEFINE_VISION = "define_vision"
    IDENTIFY_STAKEHOLDERS = "identify_stakeholders"
    ESTABLISH_PRINCIPLES = "establish_principles"
    CAPTURE_REQUIREMENTS = "capture_requirements"
    
    # Phase B specific
    MODEL_CAPABILITIES = "model_capabilities"
    MAP_PROCESSES = "map_processes"
    ANALYZE_VALUE_STREAMS = "analyze_value_streams"
    PERFORM_GAP_ANALYSIS = "perform_gap_analysis"
    
    # Phase C specific
    DESIGN_APPLICATIONS = "design_applications"
    DESIGN_DATA = "design_data"
    DEFINE_INTEGRATIONS = "define_integrations"
    
    # Phase D specific
    DESIGN_INFRASTRUCTURE = "design_infrastructure"
    DEFINE_SECURITY = "define_security"
    ESTABLISH_STANDARDS = "establish_standards"
    
    # Phase E specific
    ANALYZE_ALTERNATIVES = "analyze_alternatives"
    CALCULATE_ROI = "calculate_roi"
    DEVELOP_BUSINESS_CASE = "develop_business_case"
    
    # Phase F specific
    CREATE_ROADMAP = "create_roadmap"
    PLAN_MIGRATIONS = "plan_migrations"
    ASSESS_RISKS = "assess_risks"
    
    # Phase G specific
    ESTABLISH_GOVERNANCE = "establish_governance"
    MONITOR_COMPLIANCE = "monitor_compliance"
    MANAGE_CONTRACTS = "manage_contracts"
    
    # Phase H specific
    PROCESS_CHANGES = "process_changes"
    MONITOR_ARCHITECTURE = "monitor_architecture"
    CAPTURE_LESSONS = "capture_lessons"


class PhaseWorkflowGraph:
    """
    LangGraph-based workflow orchestrator for TOGAF phases.
    
    Creates a state machine that:
    - Orchestrates agent tasks
    - Manages workflow state
    - Handles conditional logic
    - Tracks progress
    - Manages errors and retries
    """
    
    def __init__(self, phase_name: str, agents: List[TOGAFAgent]):
        self.phase_name = phase_name
        self.agents = {agent.role: agent for agent in agents}
        self.workflow_graph = None
        self.checkpointer = None
        
        if LANGGRAPH_AVAILABLE:
            self.checkpointer = MemorySaver()
            self._build_graph()
    
    def _build_graph(self) -> None:
        """Build the workflow graph (to be overridden by phase-specific graphs)"""
        raise NotImplementedError("Subclasses must implement _build_graph")
    
    def create_initial_state(self) -> WorkflowState:
        """Create initial workflow state"""
        return {
            "phase": self.phase_name,
            "current_step": PhaseStep.INITIALIZE.value,
            "completed_steps": [],
            "artifacts": {},
            "recommendations": [],
            "errors": [],
            "validation_passed": False,
            "agent_outputs": {},
            "iteration": 0
        }
    
    def execute_workflow(
        self,
        initial_context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute the workflow graph.
        
        Args:
            initial_context: Initial context for the workflow
        
        Returns:
            Final state after workflow completion
        """
        if not LANGGRAPH_AVAILABLE:
            raise RuntimeError(
                "LangGraph not available. Install with: pip install langgraph"
            )
        
        state = self.create_initial_state()
        if initial_context:
            state["artifacts"].update(initial_context)
        
        # Run the graph
        final_state = self.workflow_graph.invoke(
            state,
            config={"configurable": {"thread_id": f"{self.phase_name}_{datetime.now().isoformat()}"}}
        )
        
        return final_state
    
    def _execute_agent_task(
        self,
        state: WorkflowState,
        task_name: str,
        agent_role: AgentRole,
        capabilities: List[AgentCapability],
        context: Optional[Dict[str, Any]] = None
    ) -> WorkflowState:
        """
        Execute a task using a specific agent.
        
        This is a helper method for graph nodes that delegate work to agents.
        """
        agent = self.agents.get(agent_role)
        if not agent:
            state["errors"].append(f"No agent found for role {agent_role.value}")
            return state
        
        # Create task
        task = AgentTask(
            task_id=f"{state['phase']}_{task_name}_{state['iteration']}",
            name=task_name,
            description=f"Execute {task_name} for {state['phase']}",
            agent_role=agent_role,
            priority=TaskPriority.HIGH,
            required_capabilities=capabilities,
            context=context or state.get("artifacts", {})
        )
        
        try:
            # Assign and execute task
            agent.assign_task(task)
            result = agent.execute_task(task)
            agent.complete_task(result)
            
            # Update state
            state["agent_outputs"][task_name] = result
            state["completed_steps"].append(task_name)
            
            # Collect recommendations
            if task.recommendations:
                state["recommendations"].extend(task.recommendations)
            
        except Exception as e:
            error_msg = f"Task {task_name} failed: {str(e)}"
            state["errors"].append(error_msg)
            agent.fail_task(error_msg)
        
        return state


class PhaseAWorkflowGraph(PhaseWorkflowGraph):
    """
    LangGraph workflow for TOGAF Phase A: Architecture Vision
    
    Workflow:
    1. Define vision
    2. Identify stakeholders (parallel)
    3. Establish principles (parallel)
    4. Capture requirements
    5. Validate
    6. Generate deliverables
    """
    
    def __init__(self, agents: List[TOGAFAgent]):
        super().__init__("Phase A: Architecture Vision", agents)
    
    def _build_graph(self) -> None:
        """Build Phase A workflow graph"""
        graph = StateGraph(WorkflowState)
        
        # Define nodes
        graph.add_node("define_vision", self._define_vision)
        graph.add_node("identify_stakeholders", self._identify_stakeholders)
        graph.add_node("establish_principles", self._establish_principles)
        graph.add_node("capture_requirements", self._capture_requirements)
        graph.add_node("validate", self._validate)
        graph.add_node("generate_deliverables", self._generate_deliverables)
        
        # Define edges
        graph.set_entry_point("define_vision")
        graph.add_edge("define_vision", "identify_stakeholders")
        graph.add_edge("identify_stakeholders", "establish_principles")
        graph.add_edge("establish_principles", "capture_requirements")
        graph.add_edge("capture_requirements", "validate")
        
        # Conditional edge based on validation
        graph.add_conditional_edges(
            "validate",
            self._check_validation,
            {
                "generate_deliverables": "generate_deliverables",
                "capture_requirements": "capture_requirements"  # Retry if validation fails
            }
        )
        
        graph.add_edge("generate_deliverables", END)
        
        self.workflow_graph = graph.compile(checkpointer=self.checkpointer)
    
    def _define_vision(self, state: WorkflowState) -> WorkflowState:
        """Define architecture vision"""
        return self._execute_agent_task(
            state,
            "define_vision",
            AgentRole.VISION_ANALYST,
            [AgentCapability.ANALYZE_REQUIREMENTS, AgentCapability.RECOMMEND_PRINCIPLES]
        )
    
    def _identify_stakeholders(self, state: WorkflowState) -> WorkflowState:
        """Identify and analyze stakeholders"""
        return self._execute_agent_task(
            state,
            "identify_stakeholders",
            AgentRole.STAKEHOLDER_ANALYST,
            [AgentCapability.ANALYZE_STAKEHOLDERS, AgentCapability.COMMUNICATE_STAKEHOLDERS]
        )
    
    def _establish_principles(self, state: WorkflowState) -> WorkflowState:
        """Establish architecture principles"""
        return self._execute_agent_task(
            state,
            "establish_principles",
            AgentRole.VISION_ANALYST,
            [AgentCapability.RECOMMEND_PRINCIPLES]
        )
    
    def _capture_requirements(self, state: WorkflowState) -> WorkflowState:
        """Capture architecture requirements"""
        return self._execute_agent_task(
            state,
            "capture_requirements",
            AgentRole.REQUIREMENTS_ENGINEER,
            [AgentCapability.ANALYZE_REQUIREMENTS]
        )
    
    def _validate(self, state: WorkflowState) -> WorkflowState:
        """Validate Phase A outputs"""
        return self._execute_agent_task(
            state,
            "validate",
            AgentRole.QUALITY_REVIEWER,
            [AgentCapability.VALIDATE_QUALITY, AgentCapability.VALIDATE_COMPLIANCE]
        )
    
    def _generate_deliverables(self, state: WorkflowState) -> WorkflowState:
        """Generate Phase A deliverables"""
        state["completed_steps"].append("generate_deliverables")
        state["current_step"] = "completed"
        return state
    
    def _check_validation(self, state: WorkflowState) -> str:
        """Check if validation passed"""
        # Simple validation: check if we have required outputs
        required_outputs = ["define_vision", "identify_stakeholders", "establish_principles", "capture_requirements"]
        validation_passed = all(output in state["agent_outputs"] for output in required_outputs)
        
        state["validation_passed"] = validation_passed
        state["iteration"] += 1
        
        # Prevent infinite loops
        if state["iteration"] > 3:
            return "generate_deliverables"
        
        return "generate_deliverables" if validation_passed else "capture_requirements"


# Additional phase workflow graphs would follow similar patterns
# For brevity, showing the structure for Phase B


class PhaseBWorkflowGraph(PhaseWorkflowGraph):
    """
    LangGraph workflow for TOGAF Phase B: Business Architecture
    
    Workflow:
    1. Model business capabilities
    2. Map business processes
    3. Analyze value streams
    4. Perform gap analysis
    5. Validate
    6. Generate deliverables
    """
    
    def __init__(self, agents: List[TOGAFAgent]):
        super().__init__("Phase B: Business Architecture", agents)
    
    def _build_graph(self) -> None:
        """Build Phase B workflow graph"""
        graph = StateGraph(WorkflowState)
        
        # Define nodes
        graph.add_node("model_capabilities", self._model_capabilities)
        graph.add_node("map_processes", self._map_processes)
        graph.add_node("analyze_value_streams", self._analyze_value_streams)
        graph.add_node("perform_gap_analysis", self._perform_gap_analysis)
        graph.add_node("validate", self._validate)
        graph.add_node("generate_deliverables", self._generate_deliverables)
        
        # Define edges
        graph.set_entry_point("model_capabilities")
        graph.add_edge("model_capabilities", "map_processes")
        graph.add_edge("map_processes", "analyze_value_streams")
        graph.add_edge("analyze_value_streams", "perform_gap_analysis")
        graph.add_edge("perform_gap_analysis", "validate")
        
        # Conditional validation
        graph.add_conditional_edges(
            "validate",
            self._check_validation,
            {
                "generate_deliverables": "generate_deliverables",
                "model_capabilities": "model_capabilities"
            }
        )
        
        graph.add_edge("generate_deliverables", END)
        
        self.workflow_graph = graph.compile(checkpointer=self.checkpointer)
    
    def _model_capabilities(self, state: WorkflowState) -> WorkflowState:
        """Model business capabilities"""
        return self._execute_agent_task(
            state,
            "model_capabilities",
            AgentRole.BUSINESS_ARCHITECT,
            [AgentCapability.DESIGN_ARCHITECTURE, AgentCapability.ANALYZE_GAPS]
        )
    
    def _map_processes(self, state: WorkflowState) -> WorkflowState:
        """Map business processes"""
        return self._execute_agent_task(
            state,
            "map_processes",
            AgentRole.BUSINESS_ARCHITECT,
            [AgentCapability.DESIGN_ARCHITECTURE]
        )
    
    def _analyze_value_streams(self, state: WorkflowState) -> WorkflowState:
        """Analyze value streams"""
        return self._execute_agent_task(
            state,
            "analyze_value_streams",
            AgentRole.BUSINESS_ARCHITECT,
            [AgentCapability.ANALYZE_DEPENDENCIES]
        )
    
    def _perform_gap_analysis(self, state: WorkflowState) -> WorkflowState:
        """Perform gap analysis"""
        return self._execute_agent_task(
            state,
            "perform_gap_analysis",
            AgentRole.BUSINESS_ARCHITECT,
            [AgentCapability.ANALYZE_GAPS]
        )
    
    def _validate(self, state: WorkflowState) -> WorkflowState:
        """Validate Phase B outputs"""
        return self._execute_agent_task(
            state,
            "validate",
            AgentRole.QUALITY_REVIEWER,
            [AgentCapability.VALIDATE_QUALITY]
        )
    
    def _generate_deliverables(self, state: WorkflowState) -> WorkflowState:
        """Generate Phase B deliverables"""
        state["completed_steps"].append("generate_deliverables")
        state["current_step"] = "completed"
        return state
    
    def _check_validation(self, state: WorkflowState) -> str:
        """Check if validation passed"""
        required_outputs = ["model_capabilities", "map_processes", "analyze_value_streams", "perform_gap_analysis"]
        validation_passed = all(output in state["agent_outputs"] for output in required_outputs)
        
        state["validation_passed"] = validation_passed
        state["iteration"] += 1
        
        if state["iteration"] > 3:
            return "generate_deliverables"
        
        return "generate_deliverables" if validation_passed else "model_capabilities"


def create_phase_workflow(
    phase_name: str,
    agents: List[TOGAFAgent]
) -> Optional[PhaseWorkflowGraph]:
    """
    Factory function to create appropriate workflow graph for a TOGAF phase.
    
    Args:
        phase_name: Name of the TOGAF phase (e.g., "Phase A", "Phase B")
        agents: List of agents to use in the workflow
    
    Returns:
        PhaseWorkflowGraph instance or None if phase not supported
    """
    workflows = {
        "Phase A": PhaseAWorkflowGraph,
        "Phase B": PhaseBWorkflowGraph,
        # Additional phases would be added here
    }
    
    workflow_class = workflows.get(phase_name)
    if workflow_class:
        return workflow_class(agents)
    
    return None
