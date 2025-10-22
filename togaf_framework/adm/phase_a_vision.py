"""
Phase A: Architecture Vision

This phase defines the scope and approach for the architecture initiative,
identifies stakeholders, creates the Architecture Vision, and obtains approval.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from .adm_phase import ADMPhase
from ..core.enums import ADMPhaseType
from ..core.base import Deliverable
from ..models.stakeholder import Stakeholder
from ..models.principle import ArchitecturePrinciple
from ..models.requirement import Requirement


class PhaseAArchitectureVision(ADMPhase):
    """
    Phase A: Architecture Vision
    
    Objectives:
    - Develop a high-level aspirational vision of the capabilities and business value
    - Obtain approval for a Statement of Architecture Work
    - Define the scope and constraints
    - Identify stakeholders and their concerns
    """
    
    phase_type = ADMPhaseType.PHASE_A
    
    def __init__(self, name: str = "Architecture Vision", **kwargs):
        super().__init__(name, **kwargs)
        self.vision_statement: Optional[str] = None
        self.business_goals: List[str] = []
        self.architecture_principles: List[ArchitecturePrinciple] = []
        self.key_stakeholders: List[Stakeholder] = []
        self.requirements: List[Requirement] = []
        self.constraints: List[str] = []
        self.assumptions: List[str] = []
        
    def _initialize_phase(self) -> None:
        """Initialize Phase A specific objectives and activities"""
        # Objectives
        self.add_objective("Develop high-level aspirational vision")
        self.add_objective("Obtain approval for Statement of Architecture Work")
        self.add_objective("Define scope, constraints and expectations")
        self.add_objective("Identify stakeholders and their concerns")
        self.add_objective("Create Architecture Vision document")
        self.add_objective("Secure stakeholder buy-in and approval")
        
        # Activities
        self.add_activity(
            "Establish Architecture Project",
            "Define project scope, approach, and governance",
            duration_days=5
        )
        self.add_activity(
            "Identify Stakeholders and Concerns",
            "Identify key stakeholders, their positions, and concerns",
            duration_days=10
        )
        self.add_activity(
            "Confirm Business Goals and Drivers",
            "Document business goals, drivers, and strategic context",
            duration_days=7
        )
        self.add_activity(
            "Assess Architecture Maturity",
            "Evaluate current architecture capability maturity",
            duration_days=5
        )
        self.add_activity(
            "Define Scope and Constraints",
            "Define boundaries, constraints, and assumptions",
            duration_days=7
        )
        self.add_activity(
            "Establish Architecture Principles",
            "Define or confirm architecture principles and guidelines",
            duration_days=5
        )
        self.add_activity(
            "Develop Architecture Vision",
            "Create high-level architecture vision and value proposition",
            duration_days=10
        )
        self.add_activity(
            "Define Target Architecture Value",
            "Quantify expected business value and KPIs",
            duration_days=5
        )
        self.add_activity(
            "Create Statement of Architecture Work",
            "Document scope, deliverables, timeline, and resources",
            duration_days=7
        )
        self.add_activity(
            "Secure Stakeholder Approval",
            "Present vision and obtain approval to proceed",
            duration_days=5
        )
        
    def set_vision_statement(self, vision: str) -> None:
        """Set the architecture vision statement"""
        self.vision_statement = vision
        self.updated_at = datetime.now()
        
    def add_business_goal(self, goal: str) -> None:
        """Add a business goal"""
        if goal not in self.business_goals:
            self.business_goals.append(goal)
            
    def add_principle(self, principle: ArchitecturePrinciple) -> None:
        """Add an architecture principle"""
        self.architecture_principles.append(principle)
        
    def add_key_stakeholder(self, stakeholder: Stakeholder) -> None:
        """Add a key stakeholder"""
        self.key_stakeholders.append(stakeholder)
        self.add_stakeholder(stakeholder.name)
        
    def add_requirement(self, requirement: Requirement) -> None:
        """Add a high-level requirement"""
        self.requirements.append(requirement)
        
    def add_constraint(self, constraint: str) -> None:
        """Add a constraint"""
        if constraint not in self.constraints:
            self.constraints.append(constraint)
            
    def add_assumption(self, assumption: str) -> None:
        """Add an assumption"""
        if assumption not in self.assumptions:
            self.assumptions.append(assumption)
            
    def execute(self) -> Dict[str, Any]:
        """Execute Phase A"""
        self.start_phase()
        
        results = {
            'phase': 'Architecture Vision',
            'vision_statement': self.vision_statement,
            'business_goals': self.business_goals,
            'principles_count': len(self.architecture_principles),
            'stakeholders_count': len(self.key_stakeholders),
            'requirements_count': len(self.requirements),
            'constraints': self.constraints,
            'assumptions': self.assumptions,
        }
        
        # Create key deliverables
        self._create_deliverables()
        
        return results
    
    def _create_deliverables(self) -> None:
        """Create Phase A deliverables"""
        # Architecture Vision Document
        vision_doc = Deliverable(
            name="Architecture Vision Document",
            phase="Phase A",
            description="High-level architecture vision and value proposition",
            content={
                'vision_statement': self.vision_statement,
                'business_goals': self.business_goals,
                'target_architecture': 'High-level description',
            }
        )
        self.add_output(vision_doc)
        
        # Statement of Architecture Work
        soaw = Deliverable(
            name="Statement of Architecture Work",
            phase="Phase A",
            description="Defines scope, approach, and governance for architecture work",
            content={
                'scope': 'Architecture scope definition',
                'constraints': self.constraints,
                'assumptions': self.assumptions,
            }
        )
        self.add_output(soaw)
        
        # Stakeholder Map
        stakeholder_map = Deliverable(
            name="Stakeholder Map",
            phase="Phase A",
            description="Identification and analysis of stakeholders",
            content={
                'stakeholders': [s.to_dict() for s in self.key_stakeholders],
            }
        )
        self.add_output(stakeholder_map)
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'vision_statement': self.vision_statement,
            'business_goals': self.business_goals,
            'principles_count': len(self.architecture_principles),
            'stakeholders_count': len(self.key_stakeholders),
            'requirements_count': len(self.requirements),
            'constraints_count': len(self.constraints),
            'assumptions_count': len(self.assumptions),
        })
        return base_dict
