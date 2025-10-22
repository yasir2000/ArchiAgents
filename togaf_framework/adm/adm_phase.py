"""
ADM Phase Base Class

This module defines the abstract base class for all TOGAF ADM phases.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime

from ..core.base import TOGAFComponent, Deliverable
from ..core.enums import ADMPhaseType, ArchitectureStatus
from ..core.exceptions import ValidationException


class ADMPhase(TOGAFComponent):
    """
    Abstract base class for TOGAF ADM phases.
    
    Each phase represents a step in the Architecture Development Method cycle,
    with specific objectives, activities, inputs, outputs, and governance checkpoints.
    """
    
    phase_type: ADMPhaseType = None
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        owner: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, owner, metadata)
        self.objectives: List[str] = []
        self.activities: List[Dict[str, Any]] = []
        self.inputs: List[Deliverable] = []
        self.outputs: List[Deliverable] = []
        self.stakeholders: List[str] = []
        self.status = ArchitectureStatus.DRAFT
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        self.completion_percentage: float = 0.0
        
        # Initialize phase-specific objectives and activities
        self._initialize_phase()
        
    @abstractmethod
    def _initialize_phase(self) -> None:
        """Initialize phase-specific objectives and activities"""
        pass
    
    @abstractmethod
    def execute(self) -> Dict[str, Any]:
        """Execute the phase and return results"""
        pass
    
    def add_objective(self, objective: str) -> None:
        """Add an objective to the phase"""
        if objective not in self.objectives:
            self.objectives.append(objective)
            
    def add_activity(
        self,
        name: str,
        description: str,
        responsible: Optional[str] = None,
        duration_days: Optional[int] = None
    ) -> None:
        """Add an activity to the phase"""
        activity = {
            'name': name,
            'description': description,
            'responsible': responsible,
            'duration_days': duration_days,
            'status': 'not_started',
            'completion_date': None,
        }
        self.activities.append(activity)
        
    def add_input(self, deliverable: Deliverable) -> None:
        """Add an input deliverable"""
        self.inputs.append(deliverable)
        
    def add_output(self, deliverable: Deliverable) -> None:
        """Add an output deliverable"""
        self.outputs.append(deliverable)
        
    def add_stakeholder(self, stakeholder: str) -> None:
        """Add a stakeholder"""
        if stakeholder not in self.stakeholders:
            self.stakeholders.append(stakeholder)
            
    def start_phase(self) -> None:
        """Mark phase as started"""
        self.status = ArchitectureStatus.UNDER_REVIEW
        self.start_date = datetime.now()
        
    def complete_phase(self) -> None:
        """Mark phase as completed"""
        self.status = ArchitectureStatus.APPROVED
        self.end_date = datetime.now()
        self.completion_percentage = 100.0
        
    def update_progress(self, percentage: float) -> None:
        """Update completion percentage"""
        if 0 <= percentage <= 100:
            self.completion_percentage = percentage
            self.updated_at = datetime.now()
        else:
            raise ValidationException("Progress percentage must be between 0 and 100")
            
    def get_activity_status(self, activity_name: str) -> Optional[str]:
        """Get status of a specific activity"""
        for activity in self.activities:
            if activity['name'] == activity_name:
                return activity['status']
        return None
    
    def complete_activity(self, activity_name: str) -> None:
        """Mark an activity as completed"""
        for activity in self.activities:
            if activity['name'] == activity_name:
                activity['status'] = 'completed'
                activity['completion_date'] = datetime.now()
                self._calculate_progress()
                break
                
    def _calculate_progress(self) -> None:
        """Calculate overall phase progress based on completed activities"""
        if not self.activities:
            return
        completed = sum(1 for a in self.activities if a['status'] == 'completed')
        self.completion_percentage = (completed / len(self.activities)) * 100
        
    def validate(self) -> bool:
        """Validate the phase"""
        if not self.name:
            raise ValidationException("Phase name is required")
        if not self.objectives:
            raise ValidationException(f"Phase {self.name} must have objectives")
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'phase_type': self.phase_type.value if self.phase_type else None,
            'objectives': self.objectives,
            'activities_count': len(self.activities),
            'inputs_count': len(self.inputs),
            'outputs_count': len(self.outputs),
            'stakeholders': self.stakeholders,
            'status': self.status.value if hasattr(self.status, 'value') else self.status,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'completion_percentage': self.completion_percentage,
        })
        return base_dict
    
    def get_deliverables_summary(self) -> Dict[str, Any]:
        """Get summary of deliverables"""
        return {
            'inputs': [d.to_dict() for d in self.inputs],
            'outputs': [d.to_dict() for d in self.outputs],
        }
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', status='{self.status}', progress={self.completion_percentage}%)"
