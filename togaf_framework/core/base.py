"""
Base Classes for TOGAF Framework

This module contains the foundational base classes used throughout the framework.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Dict, Any, List
from uuid import uuid4


class TOGAFComponent(ABC):
    """
    Abstract base class for all TOGAF components.
    
    Provides common functionality for identification, metadata, and lifecycle management.
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        owner: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.id = str(uuid4())
        self.name = name
        self.description = description or ""
        self.owner = owner
        self.metadata = metadata or {}
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.version = "1.0.0"
        
    def update_metadata(self, key: str, value: Any) -> None:
        """Update metadata"""
        self.metadata[key] = value
        self.updated_at = datetime.now()
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner': self.owner,
            'metadata': self.metadata,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'version': self.version,
        }
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate the component"""
        pass
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id='{self.id}', name='{self.name}')"


class ArchitectureElement(TOGAFComponent):
    """
    Base class for architecture elements.
    
    Extends TOGAFComponent with architecture-specific attributes.
    """
    
    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        owner: Optional[str] = None,
        layer: Optional[str] = None,
        status: str = "draft",
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, owner, metadata)
        self.layer = layer
        self.status = status
        self.relationships: List['ArchitectureRelationship'] = []
        self.properties: Dict[str, Any] = {}
        
    def add_relationship(self, relationship: 'ArchitectureRelationship') -> None:
        """Add a relationship to another element"""
        self.relationships.append(relationship)
        
    def get_relationships(self, relationship_type: Optional[str] = None) -> List['ArchitectureRelationship']:
        """Get relationships, optionally filtered by type"""
        if relationship_type:
            return [r for r in self.relationships if r.type == relationship_type]
        return self.relationships
    
    def set_property(self, key: str, value: Any) -> None:
        """Set a property"""
        self.properties[key] = value
        self.updated_at = datetime.now()
        
    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a property"""
        return self.properties.get(key, default)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'layer': self.layer,
            'status': self.status,
            'properties': self.properties,
            'relationships_count': len(self.relationships),
        })
        return base_dict
    
    def validate(self) -> bool:
        """Validate the architecture element"""
        if not self.name:
            return False
        if not self.layer:
            return False
        return True


class ArchitectureRelationship(TOGAFComponent):
    """
    Represents a relationship between architecture elements.
    """
    
    def __init__(
        self,
        name: str,
        source: ArchitectureElement,
        target: ArchitectureElement,
        relationship_type: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, metadata=metadata)
        self.source = source
        self.target = target
        self.type = relationship_type
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'source_id': self.source.id,
            'source_name': self.source.name,
            'target_id': self.target.id,
            'target_name': self.target.name,
            'type': self.type,
        })
        return base_dict
    
    def validate(self) -> bool:
        """Validate the relationship"""
        return self.source is not None and self.target is not None and bool(self.type)
    
    def __repr__(self) -> str:
        return f"Relationship('{self.source.name}' --{self.type}--> '{self.target.name}')"


class Deliverable(TOGAFComponent):
    """
    Base class for TOGAF deliverables.
    """
    
    def __init__(
        self,
        name: str,
        phase: str,
        description: Optional[str] = None,
        owner: Optional[str] = None,
        content: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, owner, metadata)
        self.phase = phase
        self.content = content or {}
        self.approval_status = "draft"
        self.approvers: List[str] = []
        
    def approve(self, approver: str) -> None:
        """Approve the deliverable"""
        if approver not in self.approvers:
            self.approvers.append(approver)
        if len(self.approvers) >= self.get_required_approvals():
            self.approval_status = "approved"
        self.updated_at = datetime.now()
        
    def get_required_approvals(self) -> int:
        """Get required number of approvals"""
        return self.metadata.get('required_approvals', 1)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'phase': self.phase,
            'approval_status': self.approval_status,
            'approvers': self.approvers,
            'content_keys': list(self.content.keys()),
        })
        return base_dict
    
    def validate(self) -> bool:
        """Validate the deliverable"""
        return bool(self.name and self.phase)
