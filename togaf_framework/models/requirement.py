"""
Requirement Model

Represents architecture requirements.
"""

from typing import Optional, Dict, Any, List
from ..core.base import TOGAFComponent
from ..core.enums import PriorityLevel


class Requirement(TOGAFComponent):
    """
    Represents an architecture requirement.
    
    Requirements define what the architecture must achieve or support.
    """
    
    def __init__(
        self,
        name: str,
        description: str,
        requirement_type: str,  # functional, non-functional, constraint
        source: Optional[str] = None,
        priority: PriorityLevel = PriorityLevel.MEDIUM,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, metadata=metadata)
        self.requirement_type = requirement_type
        self.source = source
        self.priority = priority
        self.status: str = "draft"  # draft, approved, implemented, verified
        self.acceptance_criteria: List[str] = []
        self.related_requirements: List[str] = []
        self.rationale: Optional[str] = None
        
    def add_acceptance_criterion(self, criterion: str) -> None:
        """Add an acceptance criterion"""
        if criterion not in self.acceptance_criteria:
            self.acceptance_criteria.append(criterion)
            
    def add_related_requirement(self, requirement_id: str) -> None:
        """Add a related requirement"""
        if requirement_id not in self.related_requirements:
            self.related_requirements.append(requirement_id)
            
    def set_status(self, status: str) -> None:
        """Set requirement status"""
        if status in ['draft', 'approved', 'implemented', 'verified']:
            self.status = status
            
    def set_rationale(self, rationale: str) -> None:
        """Set requirement rationale"""
        self.rationale = rationale
        
    def validate(self) -> bool:
        """Validate the requirement"""
        return bool(self.name and self.description and self.requirement_type)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'requirement_type': self.requirement_type,
            'source': self.source,
            'priority': self.priority.value,
            'status': self.status,
            'acceptance_criteria': self.acceptance_criteria,
            'related_requirements': self.related_requirements,
            'rationale': self.rationale,
        })
        return base_dict
