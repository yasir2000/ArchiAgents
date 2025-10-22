"""
ArchiMate Model Intelligence

AI-driven analysis and manipulation of ArchiMate 3.0 models.
Provides intelligent insights across all ArchiMate layers.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Set
from enum import Enum
from datetime import datetime


class ArchiMateLayer(Enum):
    """ArchiMate 3.0 Layers"""
    STRATEGY = "strategy"
    BUSINESS = "business"
    APPLICATION = "application"
    TECHNOLOGY = "technology"
    PHYSICAL = "physical"
    IMPLEMENTATION = "implementation"
    MOTIVATION = "motivation"


class ElementType(Enum):
    """ArchiMate element types"""
    # Strategy Layer
    RESOURCE = "resource"
    CAPABILITY = "capability"
    COURSE_OF_ACTION = "course_of_action"
    VALUE_STREAM = "value_stream"
    
    # Business Layer
    BUSINESS_ACTOR = "business_actor"
    BUSINESS_ROLE = "business_role"
    BUSINESS_PROCESS = "business_process"
    BUSINESS_FUNCTION = "business_function"
    BUSINESS_SERVICE = "business_service"
    BUSINESS_OBJECT = "business_object"
    
    # Application Layer
    APPLICATION_COMPONENT = "application_component"
    APPLICATION_SERVICE = "application_service"
    APPLICATION_INTERFACE = "application_interface"
    DATA_OBJECT = "data_object"
    
    # Technology Layer
    NODE = "node"
    DEVICE = "device"
    SYSTEM_SOFTWARE = "system_software"
    TECHNOLOGY_SERVICE = "technology_service"
    ARTIFACT = "artifact"
    
    # Physical Layer
    EQUIPMENT = "equipment"
    FACILITY = "facility"
    DISTRIBUTION_NETWORK = "distribution_network"
    MATERIAL = "material"
    
    # Motivation Layer
    STAKEHOLDER = "stakeholder"
    DRIVER = "driver"
    ASSESSMENT = "assessment"
    GOAL = "goal"
    OUTCOME = "outcome"
    PRINCIPLE = "principle"
    REQUIREMENT = "requirement"
    CONSTRAINT = "constraint"


class RelationshipType(Enum):
    """ArchiMate relationship types"""
    COMPOSITION = "composition"
    AGGREGATION = "aggregation"
    ASSIGNMENT = "assignment"
    REALIZATION = "realization"
    SERVING = "serving"
    ACCESS = "access"
    INFLUENCE = "influence"
    TRIGGERING = "triggering"
    FLOW = "flow"
    SPECIALIZATION = "specialization"
    ASSOCIATION = "association"


@dataclass
class ArchiMateElement:
    """Represents an ArchiMate element"""
    
    element_id: str
    name: str
    element_type: ElementType
    layer: ArchiMateLayer
    description: str = ""
    
    # Properties
    properties: Dict[str, Any] = field(default_factory=dict)
    
    # Relationships
    relationships: List[Dict] = field(default_factory=list)
    
    # Metadata
    created_by: str = ""
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class ArchiMateRelationship:
    """Represents an ArchiMate relationship"""
    
    relationship_id: str
    source_id: str
    target_id: str
    relationship_type: RelationshipType
    name: str = ""
    description: str = ""
    
    # Properties
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ModelInsight:
    """Insight discovered from model analysis"""
    
    insight_id: str
    insight_type: str              # gap, opportunity, risk, optimization
    severity: str                  # critical, high, medium, low
    title: str
    description: str
    
    # Affected Elements
    affected_elements: List[str]
    affected_layers: List[ArchiMateLayer]
    
    # Recommendations
    recommendations: List[str]
    estimated_impact: str
    estimated_effort: str
    
    # Metadata
    discovered_at: datetime
    confidence: float              # 0-1
    metadata: Dict[str, Any] = field(default_factory=dict)


class ArchiMateModelAnalyzer:
    """
    AI-driven ArchiMate model analyzer.
    
    Provides intelligent analysis of ArchiMate models including:
    - Pattern recognition
    - Gap analysis
    - Dependency analysis
    - Impact assessment
    - Optimization recommendations
    """
    
    def __init__(self, llm=None):
        """
        Initialize model analyzer.
        
        Args:
            llm: Language model for AI analysis (optional)
        """
        self.llm = llm
        self.elements: Dict[str, ArchiMateElement] = {}
        self.relationships: Dict[str, ArchiMateRelationship] = {}
        self.insights: List[ModelInsight] = []
        self.analysis_history: List[Dict] = []
    
    def add_element(self, element: ArchiMateElement):
        """Add element to model"""
        self.elements[element.element_id] = element
        print(f"➕ Added {element.element_type.value}: {element.name}")
    
    def add_relationship(self, relationship: ArchiMateRelationship):
        """Add relationship to model"""
        self.relationships[relationship.relationship_id] = relationship
        
        # Update element relationships
        if relationship.source_id in self.elements:
            self.elements[relationship.source_id].relationships.append({
                "type": relationship.relationship_type.value,
                "target": relationship.target_id,
                "direction": "outgoing"
            })
        
        print(f"🔗 Added {relationship.relationship_type.value}: "
              f"{relationship.source_id} → {relationship.target_id}")
    
    def analyze_model(self, analysis_types: List[str] = None) -> List[ModelInsight]:
        """
        Perform comprehensive model analysis.
        
        Args:
            analysis_types: Types of analysis to perform
                - "gaps": Gap analysis
                - "dependencies": Dependency analysis
                - "patterns": Pattern recognition
                - "compliance": Compliance checking
                - "optimization": Optimization opportunities
        
        Returns:
            List of insights discovered
        """
        print("\n🔍 Analyzing ArchiMate model...")
        
        if not analysis_types:
            analysis_types = ["gaps", "dependencies", "patterns", "optimization"]
        
        insights = []
        
        # Gap analysis
        if "gaps" in analysis_types:
            print("   Performing gap analysis...")
            gaps = self._analyze_gaps()
            insights.extend(gaps)
        
        # Dependency analysis
        if "dependencies" in analysis_types:
            print("   Analyzing dependencies...")
            deps = self._analyze_dependencies()
            insights.extend(deps)
        
        # Pattern recognition
        if "patterns" in analysis_types:
            print("   Recognizing patterns...")
            patterns = self._recognize_patterns()
            insights.extend(patterns)
        
        # Optimization opportunities
        if "optimization" in analysis_types:
            print("   Finding optimization opportunities...")
            opts = self._find_optimizations()
            insights.extend(opts)
        
        # Store insights
        self.insights.extend(insights)
        
        # Store analysis history
        self.analysis_history.append({
            "timestamp": datetime.now(),
            "analysis_types": analysis_types,
            "insights_found": len(insights)
        })
        
        print(f"✅ Analysis complete. Found {len(insights)} insights.")
        
        return insights
    
    def _analyze_gaps(self) -> List[ModelInsight]:
        """Analyze model for gaps"""
        
        gaps = []
        
        # Check for missing layers
        present_layers = set(elem.layer for elem in self.elements.values())
        all_layers = set(ArchiMateLayer)
        missing_layers = all_layers - present_layers
        
        if missing_layers:
            for layer in missing_layers:
                gaps.append(ModelInsight(
                    insight_id=f"GAP-{len(gaps)+1}",
                    insight_type="gap",
                    severity="medium",
                    title=f"Missing {layer.value} layer",
                    description=f"The model does not include elements from the {layer.value} layer",
                    affected_elements=[],
                    affected_layers=[layer],
                    recommendations=[
                        f"Add {layer.value} layer elements to complete the model",
                        f"Assess if {layer.value} layer is required for this architecture"
                    ],
                    estimated_impact="Medium - incomplete architecture view",
                    estimated_effort="2-5 days",
                    discovered_at=datetime.now(),
                    confidence=0.9
                ))
        
        # Check for orphaned elements (no relationships)
        for elem_id, elem in self.elements.items():
            if not elem.relationships:
                # Check if element has any incoming relationships
                incoming = [
                    rel for rel in self.relationships.values()
                    if rel.target_id == elem_id
                ]
                
                if not incoming:
                    gaps.append(ModelInsight(
                        insight_id=f"GAP-{len(gaps)+1}",
                        insight_type="gap",
                        severity="low",
                        title=f"Orphaned element: {elem.name}",
                        description=f"Element '{elem.name}' has no relationships",
                        affected_elements=[elem_id],
                        affected_layers=[elem.layer],
                        recommendations=[
                            "Establish relationships with other elements",
                            "Remove if element is no longer relevant"
                        ],
                        estimated_impact="Low - isolated element",
                        estimated_effort="1-2 hours",
                        discovered_at=datetime.now(),
                        confidence=1.0
                    ))
        
        # Check for missing business-application alignment
        business_elems = [e for e in self.elements.values() 
                         if e.layer == ArchiMateLayer.BUSINESS]
        app_elems = [e for e in self.elements.values() 
                    if e.layer == ArchiMateLayer.APPLICATION]
        
        if business_elems and app_elems:
            # Check for serving relationships
            serving_rels = [
                rel for rel in self.relationships.values()
                if rel.relationship_type == RelationshipType.SERVING
                and rel.source_id in [e.element_id for e in app_elems]
                and rel.target_id in [e.element_id for e in business_elems]
            ]
            
            if len(serving_rels) < len(app_elems) * 0.5:
                gaps.append(ModelInsight(
                    insight_id=f"GAP-{len(gaps)+1}",
                    insight_type="gap",
                    severity="high",
                    title="Weak business-application alignment",
                    description="Less than 50% of applications are linked to business services",
                    affected_elements=[e.element_id for e in app_elems],
                    affected_layers=[ArchiMateLayer.BUSINESS, ArchiMateLayer.APPLICATION],
                    recommendations=[
                        "Establish serving relationships from applications to business services",
                        "Document which applications support which business capabilities"
                    ],
                    estimated_impact="High - unclear application value",
                    estimated_effort="3-5 days",
                    discovered_at=datetime.now(),
                    confidence=0.85
                ))
        
        return gaps
    
    def _analyze_dependencies(self) -> List[ModelInsight]:
        """Analyze model dependencies"""
        
        insights = []
        
        # Find highly coupled elements (many dependencies)
        for elem_id, elem in self.elements.items():
            total_deps = len(elem.relationships)
            total_deps += len([
                rel for rel in self.relationships.values()
                if rel.target_id == elem_id
            ])
            
            if total_deps > 10:
                insights.append(ModelInsight(
                    insight_id=f"DEP-{len(insights)+1}",
                    insight_type="risk",
                    severity="medium",
                    title=f"High coupling: {elem.name}",
                    description=f"Element has {total_deps} dependencies - high coupling detected",
                    affected_elements=[elem_id],
                    affected_layers=[elem.layer],
                    recommendations=[
                        "Consider decomposing into smaller components",
                        "Evaluate if all dependencies are necessary",
                        "Apply loose coupling patterns"
                    ],
                    estimated_impact="Medium - change impact risk",
                    estimated_effort="5-10 days",
                    discovered_at=datetime.now(),
                    confidence=0.8
                ))
        
        # Find circular dependencies
        circles = self._find_circular_dependencies()
        for circle in circles:
            insights.append(ModelInsight(
                insight_id=f"DEP-{len(insights)+1}",
                insight_type="risk",
                severity="high",
                title="Circular dependency detected",
                description=f"Circular dependency: {' → '.join(circle)}",
                affected_elements=circle,
                affected_layers=list(set(
                    self.elements[e].layer for e in circle if e in self.elements
                )),
                recommendations=[
                    "Break circular dependency by introducing abstraction",
                    "Reconsider architecture design to avoid cycles"
                ],
                estimated_impact="High - design issue",
                estimated_effort="3-7 days",
                discovered_at=datetime.now(),
                confidence=0.95
            ))
        
        return insights
    
    def _find_circular_dependencies(self) -> List[List[str]]:
        """Find circular dependencies in model"""
        
        circles = []
        visited = set()
        path = []
        
        def dfs(elem_id: str):
            if elem_id in path:
                # Found circle
                circle_start = path.index(elem_id)
                circles.append(path[circle_start:] + [elem_id])
                return
            
            if elem_id in visited:
                return
            
            visited.add(elem_id)
            path.append(elem_id)
            
            # Visit connected elements
            if elem_id in self.elements:
                for rel in self.elements[elem_id].relationships:
                    dfs(rel["target"])
            
            path.pop()
        
        # Check each element
        for elem_id in self.elements:
            if elem_id not in visited:
                dfs(elem_id)
        
        return circles
    
    def _recognize_patterns(self) -> List[ModelInsight]:
        """Recognize architectural patterns"""
        
        insights = []
        
        # Detect layered architecture pattern
        if self._is_layered_architecture():
            insights.append(ModelInsight(
                insight_id=f"PATTERN-{len(insights)+1}",
                insight_type="pattern",
                severity="info",
                title="Layered architecture detected",
                description="Model follows layered architecture pattern",
                affected_elements=[],
                affected_layers=list(ArchiMateLayer),
                recommendations=[
                    "Maintain clear layer separation",
                    "Enforce dependency rules between layers"
                ],
                estimated_impact="Positive - good architecture",
                estimated_effort="Ongoing maintenance",
                discovered_at=datetime.now(),
                confidence=0.85
            ))
        
        # Detect microservices pattern
        app_components = [
            e for e in self.elements.values()
            if e.element_type == ElementType.APPLICATION_COMPONENT
        ]
        
        if len(app_components) > 5:
            # Check for loose coupling
            avg_coupling = sum(
                len(c.relationships) for c in app_components
            ) / len(app_components)
            
            if avg_coupling < 3:
                insights.append(ModelInsight(
                    insight_id=f"PATTERN-{len(insights)+1}",
                    insight_type="pattern",
                    severity="info",
                    title="Microservices pattern detected",
                    description=f"{len(app_components)} loosely-coupled application components",
                    affected_elements=[c.element_id for c in app_components],
                    affected_layers=[ArchiMateLayer.APPLICATION],
                    recommendations=[
                        "Ensure proper service boundaries",
                        "Implement API gateway pattern",
                        "Consider service mesh for inter-service communication"
                    ],
                    estimated_impact="Positive - scalable architecture",
                    estimated_effort="Ongoing maintenance",
                    discovered_at=datetime.now(),
                    confidence=0.75
                ))
        
        return insights
    
    def _is_layered_architecture(self) -> bool:
        """Check if model follows layered architecture"""
        
        # Count elements per layer
        layer_counts = {}
        for elem in self.elements.values():
            layer_counts[elem.layer] = layer_counts.get(elem.layer, 0) + 1
        
        # Layered if we have at least 3 layers with elements
        return len(layer_counts) >= 3
    
    def _find_optimizations(self) -> List[ModelInsight]:
        """Find optimization opportunities"""
        
        insights = []
        
        # Find redundant elements (same name, type, layer)
        element_signatures = {}
        for elem in self.elements.values():
            sig = f"{elem.name}_{elem.element_type.value}_{elem.layer.value}"
            if sig in element_signatures:
                element_signatures[sig].append(elem.element_id)
            else:
                element_signatures[sig] = [elem.element_id]
        
        for sig, elem_ids in element_signatures.items():
            if len(elem_ids) > 1:
                insights.append(ModelInsight(
                    insight_id=f"OPT-{len(insights)+1}",
                    insight_type="optimization",
                    severity="low",
                    title=f"Potential redundancy: {sig.split('_')[0]}",
                    description=f"Found {len(elem_ids)} elements with similar characteristics",
                    affected_elements=elem_ids,
                    affected_layers=[self.elements[elem_ids[0]].layer],
                    recommendations=[
                        "Verify if elements are truly distinct",
                        "Consider consolidating duplicate elements",
                        "Rename if elements serve different purposes"
                    ],
                    estimated_impact="Low - potential simplification",
                    estimated_effort="2-3 hours",
                    discovered_at=datetime.now(),
                    confidence=0.6
                ))
        
        return insights
    
    def get_element_dependencies(
        self,
        element_id: str,
        depth: int = 1
    ) -> Dict[str, Any]:
        """Get dependencies for an element"""
        
        if element_id not in self.elements:
            return {}
        
        dependencies = {
            "element": self.elements[element_id],
            "outgoing": [],
            "incoming": [],
        }
        
        # Get outgoing relationships
        for rel_info in self.elements[element_id].relationships:
            target_id = rel_info["target"]
            if target_id in self.elements:
                dependencies["outgoing"].append({
                    "type": rel_info["type"],
                    "target": self.elements[target_id],
                })
        
        # Get incoming relationships
        for rel in self.relationships.values():
            if rel.target_id == element_id and rel.source_id in self.elements:
                dependencies["incoming"].append({
                    "type": rel.relationship_type.value,
                    "source": self.elements[rel.source_id],
                })
        
        return dependencies
    
    def assess_change_impact(
        self,
        element_id: str,
        change_type: str = "modify"
    ) -> Dict[str, Any]:
        """
        Assess impact of changing an element.
        
        Args:
            element_id: Element to change
            change_type: Type of change (modify, remove, replace)
        
        Returns:
            Impact assessment
        """
        print(f"\n⚡ Assessing impact of {change_type} on {element_id}")
        
        if element_id not in self.elements:
            return {"error": "Element not found"}
        
        elem = self.elements[element_id]
        
        # Get all dependent elements
        deps = self.get_element_dependencies(element_id)
        
        # Calculate impact
        impact = {
            "element": elem.name,
            "change_type": change_type,
            "directly_affected": len(deps["incoming"]) + len(deps["outgoing"]),
            "affected_layers": list(set(
                [d["target"].layer for d in deps["outgoing"]] +
                [d["source"].layer for d in deps["incoming"]]
            )),
            "severity": "low",
            "recommendations": [],
        }
        
        # Determine severity
        if impact["directly_affected"] > 10:
            impact["severity"] = "critical"
            impact["recommendations"].append("Extensive testing required")
        elif impact["directly_affected"] > 5:
            impact["severity"] = "high"
            impact["recommendations"].append("Thorough impact analysis needed")
        elif impact["directly_affected"] > 2:
            impact["severity"] = "medium"
        
        # Add specific recommendations
        if change_type == "remove":
            impact["recommendations"].append("Migrate dependencies before removal")
        elif change_type == "replace":
            impact["recommendations"].append("Ensure replacement maintains interfaces")
        
        print(f"   Severity: {impact['severity']}")
        print(f"   Directly affected: {impact['directly_affected']} elements")
        
        return impact
    
    def get_layer_statistics(self) -> Dict[ArchiMateLayer, Dict]:
        """Get statistics per ArchiMate layer"""
        
        stats = {}
        
        for layer in ArchiMateLayer:
            layer_elements = [
                e for e in self.elements.values()
                if e.layer == layer
            ]
            
            layer_rels = [
                r for r in self.relationships.values()
                if (r.source_id in [e.element_id for e in layer_elements] or
                    r.target_id in [e.element_id for e in layer_elements])
            ]
            
            stats[layer] = {
                "element_count": len(layer_elements),
                "relationship_count": len(layer_rels),
                "element_types": list(set(e.element_type for e in layer_elements)),
            }
        
        return stats
    
    def export_model(self, format: str = "json") -> str:
        """Export model to specified format"""
        
        if format == "json":
            import json
            model = {
                "elements": [
                    {
                        "id": e.element_id,
                        "name": e.name,
                        "type": e.element_type.value,
                        "layer": e.layer.value,
                    }
                    for e in self.elements.values()
                ],
                "relationships": [
                    {
                        "id": r.relationship_id,
                        "source": r.source_id,
                        "target": r.target_id,
                        "type": r.relationship_type.value,
                    }
                    for r in self.relationships.values()
                ],
            }
            return json.dumps(model, indent=2)
        
        return str(self.elements)
