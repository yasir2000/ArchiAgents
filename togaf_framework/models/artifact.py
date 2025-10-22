"""
Architecture Artifact Model

Represents TOGAF architecture artifacts (catalogs, matrices, diagrams).
"""

from typing import Optional, Dict, Any, List
from ..core.base import TOGAFComponent
from ..core.enums import ArtifactType

# Re-export for convenience
__all__ = ['ArchitectureArtifact', 'ArtifactType']


class ArchitectureArtifact(TOGAFComponent):
    """
    Represents a TOGAF architecture artifact.
    
    Artifacts are outputs of the architecture process including catalogs,
    matrices, and diagrams that document the architecture.
    """
    
    def __init__(
        self,
        name: str,
        artifact_type: str,  # catalog, matrix, diagram
        phase: str,
        description: Optional[str] = None,
        content: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        super().__init__(name, description, metadata=metadata)
        self.artifact_type = artifact_type
        self.phase = phase
        self.content = content or {}
        self.references: List[str] = []
        self.format: str = "json"  # json, yaml, xml, diagram
        
    def add_reference(self, reference_id: str) -> None:
        """Add a reference to another artifact"""
        if reference_id not in self.references:
            self.references.append(reference_id)
            
    def validate(self) -> bool:
        """Validate the artifact"""
        return bool(self.name and self.artifact_type and self.phase)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        base_dict = super().to_dict()
        base_dict.update({
            'artifact_type': self.artifact_type,
            'phase': self.phase,
            'format': self.format,
            'references_count': len(self.references),
        })
        return base_dict
