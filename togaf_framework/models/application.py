"""
Application Component Model

Represents application components in the architecture.
"""

from typing import Optional, Dict, Any, List
from ..core.base import ArchitectureElement
from ..core.enums import ArchiMateLayerType


class Application(ArchitectureElement):
    """
    Represents an application component.
    
    An application component represents an encapsulation of application functionality
    aligned to implementation structure.
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        application_type: str = "custom",  # custom, cots, saas
        technology_stack: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            name,
            description,
            layer=ArchiMateLayerType.APPLICATION.value,
            metadata=metadata
        )
        self.application_type = application_type
        self.technology_stack = technology_stack or []
        self.interfaces: List[str] = []
        self.data_objects: List[str] = []
        self.users_count: Optional[int] = None
        self.lifecycle_status: str = "development"  # development, production, maintenance, sunset
        
    def add_interface(self, interface: str) -> None:
        """Add an application interface"""
        if interface not in self.interfaces:
            self.interfaces.append(interface)
            
    def add_data_object(self, data_object: str) -> None:
        """Add a data object"""
        if data_object not in self.data_objects:
            self.data_objects.append(data_object)
            
    def add_technology(self, technology: str) -> None:
        """Add a technology to the stack"""
        if technology not in self.technology_stack:
            self.technology_stack.append(technology)
            
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'application_type': self.application_type,
            'technology_stack': self.technology_stack,
            'interfaces_count': len(self.interfaces),
            'data_objects_count': len(self.data_objects),
            'users_count': self.users_count,
            'lifecycle_status': self.lifecycle_status,
        })
        return base_dict
