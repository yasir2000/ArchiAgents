"""
Stakeholder Model

Represents stakeholders in the enterprise architecture.
"""

from typing import Optional, Dict, Any, List
from ..core.base import TOGAFComponent
from ..core.enums import StakeholderType


class Stakeholder(TOGAFComponent):
    """
    Represents a stakeholder in the enterprise architecture.
    
    Stakeholders are individuals, teams, or organizations with interests
    or concerns in the architecture.
    """
    
    def __init__(
        self,
        name: str,
        stakeholder_type: StakeholderType,
        role: Optional[str] = None,
        organization: Optional[str] = None,
        description: Optional[str] = None,
        contact_email: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, metadata=metadata)
        self.stakeholder_type = stakeholder_type
        self.role = role
        self.organization = organization
        self.contact_email = contact_email
        self.concerns: List[str] = []
        self.influence_level: str = "medium"  # low, medium, high
        self.interest_level: str = "medium"   # low, medium, high
        
    def add_concern(self, concern: str) -> None:
        """Add a stakeholder concern"""
        if concern not in self.concerns:
            self.concerns.append(concern)
            
    def set_influence_level(self, level: str) -> None:
        """Set influence level (low, medium, high)"""
        if level in ['low', 'medium', 'high']:
            self.influence_level = level
            
    def set_interest_level(self, level: str) -> None:
        """Set interest level (low, medium, high)"""
        if level in ['low', 'medium', 'high']:
            self.interest_level = level
            
    def validate(self) -> bool:
        """Validate the stakeholder"""
        return bool(self.name and self.stakeholder_type)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'stakeholder_type': self.stakeholder_type.value,
            'role': self.role,
            'organization': self.organization,
            'contact_email': self.contact_email,
            'concerns': self.concerns,
            'influence_level': self.influence_level,
            'interest_level': self.interest_level,
        })
        return base_dict
    
    def get_stakeholder_power(self) -> str:
        """Calculate stakeholder power based on influence and interest"""
        if self.influence_level == 'high' and self.interest_level == 'high':
            return 'key_player'
        elif self.influence_level == 'high' and self.interest_level in ['low', 'medium']:
            return 'keep_satisfied'
        elif self.influence_level in ['low', 'medium'] and self.interest_level == 'high':
            return 'keep_informed'
        else:
            return 'monitor'
