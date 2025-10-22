"""
Runtime Intelligence Layer for TOGAF & ArchiMate

Provides autonomous AI-driven decision-making across TOGAF phases
and ArchiMate modeling layers through intelligent agents.

Key Components:
- Runtime Decision Engine: Core AI decision-making logic
- ArchiMate Model Intelligence: Model analysis and manipulation
- TOGAF Phase Advisors: Phase-specific recommendations
- Autonomous Agent Controller: Multi-agent coordination
- Knowledge Graph: Architecture knowledge management
- Learning System: Continuous improvement
"""

from .decision_engine import (
    RuntimeDecisionEngine, DecisionContext, DecisionResult,
    DecisionOption, DecisionType, DecisionPriority, DecisionConfidence
)
from .archimate_intelligence import (
    ArchiMateModelAnalyzer, ArchiMateLayer, ModelInsight,
    ArchiMateElement, ArchiMateRelationship,
    ElementType, RelationshipType
)
from .togaf_advisor import TOGAFPhaseAdvisor, PhaseRecommendation, TOGAFPhase
from .autonomous_controller import AutonomousArchitectureController
from .knowledge_graph import (
    ArchitectureKnowledgeGraph, KnowledgeNode, Relationship,
    NodeType, RelationshipType as KnowledgeRelationshipType
)
from .learning_system import ArchitectureLearningSystem, LearningFeedback

__all__ = [
    # Core Engine
    "RuntimeDecisionEngine",
    "DecisionContext",
    "DecisionResult",
    "DecisionOption",
    "DecisionType",
    "DecisionPriority",
    "DecisionConfidence",
    
    # ArchiMate Intelligence
    "ArchiMateModelAnalyzer",
    "ArchiMateLayer",
    "ModelInsight",
    "ArchiMateElement",
    "ArchiMateRelationship",
    "ElementType",
    "RelationshipType",
    
    # TOGAF Advisor
    "TOGAFPhaseAdvisor",
    "PhaseRecommendation",
    "TOGAFPhase",
    
    # Autonomous Controller
    "AutonomousArchitectureController",
    
    # Knowledge Graph
    "ArchitectureKnowledgeGraph",
    "KnowledgeNode",
    "Relationship",
    "NodeType",
    "KnowledgeRelationshipType",
    
    # Learning System
    "ArchitectureLearningSystem",
    "LearningFeedback",
]

__version__ = "1.0.0"
