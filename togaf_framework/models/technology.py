"""
Technology Component Model

Represents technology infrastructure components.
"""

from typing import Optional, Dict, Any, List
from ..core.base import ArchitectureElement
from ..core.enums import ArchiMateLayerType, CloudProvider


class TechnologyComponent(ArchitectureElement):
    """
    Represents a technology component.
    
    A technology component represents an encapsulation of technology infrastructure
    or platform functionality.
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        component_type: str = "server",  # server, network, storage, database, etc.
        cloud_provider: Optional[CloudProvider] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            name,
            description,
            layer=ArchiMateLayerType.TECHNOLOGY.value,
            metadata=metadata
        )
        self.component_type = component_type
        self.cloud_provider = cloud_provider
        self.specifications: Dict[str, Any] = {}
        self.dependencies: List[str] = []
        self.capacity: Optional[Dict[str, Any]] = None
        self.redundancy_level: str = "none"  # none, basic, high, fault_tolerant
        
    def set_specification(self, key: str, value: Any) -> None:
        """Set a technical specification"""
        self.specifications[key] = value
        
    def add_dependency(self, component_id: str) -> None:
        """Add a dependency on another component"""
        if component_id not in self.dependencies:
            self.dependencies.append(component_id)
            
    def set_capacity(self, capacity_info: Dict[str, Any]) -> None:
        """Set capacity information"""
        self.capacity = capacity_info
        
    def set_redundancy_level(self, level: str) -> None:
        """Set redundancy level"""
        if level in ['none', 'basic', 'high', 'fault_tolerant']:
            self.redundancy_level = level
            
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'component_type': self.component_type,
            'cloud_provider': self.cloud_provider.value if self.cloud_provider else None,
            'specifications': self.specifications,
            'dependencies_count': len(self.dependencies),
            'capacity': self.capacity,
            'redundancy_level': self.redundancy_level,
        })
        return base_dict
