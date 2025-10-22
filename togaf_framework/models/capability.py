"""
Business Capability Model

Represents business capabilities in the architecture.
"""

from typing import Optional, Dict, Any, List
from ..core.base import ArchitectureElement
from ..core.enums import ArchiMateLayerType


class BusinessCapability(ArchitectureElement):
    """
    Represents a business capability.
    
    A capability is an ability that an organization, person, or system possesses.
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        level: int = 1,
        parent_capability: Optional['BusinessCapability'] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            name,
            description,
            layer=ArchiMateLayerType.STRATEGY.value,
            metadata=metadata
        )
        self.level = level
        self.parent_capability = parent_capability
        self.sub_capabilities: List['BusinessCapability'] = []
        self.maturity_level: str = "initial"  # initial, defined, managed, optimized
        self.strategic_importance: str = "medium"  # low, medium, high, critical
        
    def add_sub_capability(self, capability: 'BusinessCapability') -> None:
        """Add a sub-capability"""
        capability.parent_capability = self
        capability.level = self.level + 1
        self.sub_capabilities.append(capability)
        
    def set_maturity_level(self, level: str) -> None:
        """Set capability maturity level"""
        if level in ['initial', 'defined', 'managed', 'optimized']:
            self.maturity_level = level
            
    def set_strategic_importance(self, importance: str) -> None:
        """Set strategic importance"""
        if importance in ['low', 'medium', 'high', 'critical']:
            self.strategic_importance = importance
            
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'level': self.level,
            'parent_capability': self.parent_capability.name if self.parent_capability else None,
            'sub_capabilities_count': len(self.sub_capabilities),
            'maturity_level': self.maturity_level,
            'strategic_importance': self.strategic_importance,
        })
        return base_dict
