"""
Architecture Principle Model

Represents architecture principles that guide decisions.
"""

from typing import Optional, Dict, Any, List
from ..core.base import TOGAFComponent


class ArchitecturePrinciple(TOGAFComponent):
    """
    Represents an architecture principle.
    
    Principles are general rules and guidelines that inform and support
    the way an organization fulfills its mission.
    """
    
    def __init__(
        self,
        name: str,
        statement: str,
        rationale: str,
        implications: List[str],
        description: Optional[str] = None,
        category: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, metadata=metadata)
        self.statement = statement
        self.rationale = rationale
        self.implications = implications or []
        self.category = category  # e.g., business, data, application, technology
        self.priority: str = "medium"  # low, medium, high, critical
        
    def add_implication(self, implication: str) -> None:
        """Add an implication of applying this principle"""
        if implication not in self.implications:
            self.implications.append(implication)
            
    def set_priority(self, priority: str) -> None:
        """Set principle priority"""
        if priority in ['low', 'medium', 'high', 'critical']:
            self.priority = priority
            
    def validate(self) -> bool:
        """Validate the principle"""
        return bool(self.name and self.statement and self.rationale)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'statement': self.statement,
            'rationale': self.rationale,
            'implications': self.implications,
            'category': self.category,
            'priority': self.priority,
        })
        return base_dict
