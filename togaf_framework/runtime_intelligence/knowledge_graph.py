"""
Architecture Knowledge Graph

Stores and reasons over architecture knowledge using graph structure.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum


class NodeType(Enum):
    """Knowledge node types"""
    CONCEPT = "concept"
    PATTERN = "pattern"
    DECISION = "decision"
    PRINCIPLE = "principle"
    REQUIREMENT = "requirement"
    BEST_PRACTICE = "best_practice"


class RelationshipType(Enum):
    """Knowledge relationship types"""
    DEPENDS_ON = "depends_on"
    SUPPORTS = "supports"
    CONFLICTS_WITH = "conflicts_with"
    IMPLEMENTS = "implements"
    DERIVED_FROM = "derived_from"


@dataclass
class KnowledgeNode:
    """Node in knowledge graph"""
    
    node_id: str
    node_type: NodeType
    name: str
    description: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Relationship:
    """Relationship between nodes"""
    
    relationship_id: str
    source_id: str
    target_id: str
    relationship_type: RelationshipType
    properties: Dict[str, Any] = field(default_factory=dict)


class ArchitectureKnowledgeGraph:
    """Knowledge graph for architecture knowledge"""
    
    def __init__(self):
        self.nodes: Dict[str, KnowledgeNode] = {}
        self.relationships: Dict[str, Relationship] = {}
    
    def add_node(self, node: KnowledgeNode):
        """Add node to graph"""
        self.nodes[node.node_id] = node
    
    def add_relationship(self, relationship: Relationship):
        """Add relationship to graph"""
        self.relationships[relationship.relationship_id] = relationship
    
    def query(self, node_type: NodeType = None) -> List[KnowledgeNode]:
        """Query nodes by type"""
        if node_type:
            return [n for n in self.nodes.values() if n.node_type == node_type]
        return list(self.nodes.values())
