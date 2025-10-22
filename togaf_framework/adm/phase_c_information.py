"""
TOGAF ADM Phase C: Information Systems Architecture

This module implements Phase C of the TOGAF Architecture Development Method (ADM).
Phase C focuses on developing both Application and Data Architecture, including:
- Application portfolio modeling
- Application integration patterns
- Data architecture and data flows
- Information architecture
- API design and management

Reference: TOGAF 10 ADM Phase C
"""

from typing import List, Dict, Optional
from datetime import datetime
import uuid
from ..core.base import ArchitectureElement
from ..core.enums import (
    ADMPhaseType,
    ArchiMateLayerType,
    PriorityLevel,
    ArchitectureStatus
)
from ..core.exceptions import ValidationException
from .adm_phase import ADMPhase
from ..models.application import Application
from ..models.artifact import ArchitectureArtifact


class PhaseCInformationSystems(ADMPhase):
    """
    Phase C: Information Systems Architecture
    
    Develops the Target Application and Data Architectures that support
    the Business Architecture and Architecture Vision.
    
    Key Activities:
    1. Select reference models, viewpoints, and tools
    2. Develop baseline application architecture description
    3. Develop baseline data architecture description  
    4. Develop target application architecture description
    5. Develop target data architecture description
    6. Perform gap analysis
    7. Define candidate roadmap components
    8. Resolve impacts across architecture landscape
    9. Conduct formal stakeholder review
    10. Finalize information systems architecture
    11. Create architecture definition document
    """
    
    phase_type = ADMPhaseType.PHASE_C
    
    def __init__(self, name: str = "Information Systems Architecture", **kwargs):
        super().__init__(name, **kwargs)
        
        # Application Architecture Components
        self.applications: List[Application] = []
        self.application_services: List[Dict] = []
        self.application_interfaces: List[Dict] = []
        self.integration_patterns: List[Dict] = []
        self.apis: List[Dict] = []
        
        # Data Architecture Components
        self.data_entities: List[Dict] = []
        self.data_flows: List[Dict] = []
        self.data_stores: List[Dict] = []
        self.data_quality_rules: List[Dict] = []
        
        # Architecture Models
        self.baseline_application_arch: Optional[Dict] = None
        self.target_application_arch: Optional[Dict] = None
        self.baseline_data_arch: Optional[Dict] = None
        self.target_data_arch: Optional[Dict] = None
        self.gap_analysis: Optional[Dict] = None
        
        # Information Management
        self.information_flows: List[Dict] = []
        self.data_governance: Optional[Dict] = None
    
    def _initialize_phase(self) -> None:
        """Initialize Phase C - called by base class"""
        self._initialize_objectives()
        self._initialize_activities()
    
    def _generate_id(self) -> str:
        """Generate a unique ID"""
        return str(uuid.uuid4())
    
    def _initialize_objectives(self):
        """Initialize Phase C standard objectives"""
        objectives = [
            "Develop Target Application Architecture supporting business capabilities",
            "Develop Target Data Architecture for information management",
            "Define application portfolio and rationalization strategy",
            "Define data entities, flows, and governance",
            "Establish API-first integration architecture",
            "Define microservices architecture patterns",
            "Identify candidate Architecture Roadmap components",
            "Ensure alignment between application and data architectures"
        ]
        for objective in objectives:
            self.add_objective(objective)
    
    def _initialize_activities(self):
        """Initialize Phase C standard activities"""
        activities = [
            {
                "name": "Select Reference Models, Viewpoints and Tools",
                "description": "Select relevant application and data architecture reference models",
                "sequence": 1
            },
            {
                "name": "Develop Baseline Application Architecture",
                "description": "Document current state application architecture (As-Is)",
                "sequence": 2
            },
            {
                "name": "Develop Baseline Data Architecture",
                "description": "Document current state data architecture (As-Is)",
                "sequence": 3
            },
            {
                "name": "Develop Target Application Architecture",
                "description": "Document future state application architecture (To-Be)",
                "sequence": 4
            },
            {
                "name": "Develop Target Data Architecture",
                "description": "Document future state data architecture (To-Be)",
                "sequence": 5
            },
            {
                "name": "Perform Gap Analysis",
                "description": "Identify gaps between baseline and target architectures",
                "sequence": 6
            },
            {
                "name": "Define Candidate Roadmap Components",
                "description": "Identify work packages and transition architectures",
                "sequence": 7
            },
            {
                "name": "Resolve Impacts Across Architecture Landscape",
                "description": "Assess impact on other architecture domains",
                "sequence": 8
            },
            {
                "name": "Conduct Formal Stakeholder Review",
                "description": "Review information systems architecture with stakeholders",
                "sequence": 9
            },
            {
                "name": "Finalize Information Systems Architecture",
                "description": "Complete and approve architecture",
                "sequence": 10
            },
            {
                "name": "Create Architecture Definition Document",
                "description": "Document information systems architecture for delivery",
                "sequence": 11
            }
        ]
        for activity in activities:
            self.add_activity(
                activity["name"],
                activity["description"],
                activity["sequence"]
            )
    
    # ========== Application Management ==========
    
    def add_application(self, application: Application) -> None:
        """Add an application to the architecture"""
        if not isinstance(application, Application):
            raise ValidationException("Must provide Application instance")
        
        self.applications.append(application)
    
    def create_application(
        self,
        name: str,
        description: str,
        app_type: str = "custom",  # custom, cots, saas
        technology_stack: Optional[List[str]] = None,
        lifecycle_status: str = "operational"
    ) -> Application:
        """Create and add an application"""
        app = Application(
            name=name,
            description=description
        )
        
        app.application_type = app_type
        if technology_stack:
            app.technology_stack = technology_stack
        app.lifecycle_status = lifecycle_status
        
        self.add_application(app)
        return app
    
    def add_api(
        self,
        name: str,
        description: str,
        api_type: str,  # REST, GraphQL, gRPC, SOAP
        version: str,
        provider_app: str,
        consumer_apps: List[str],
        endpoints: List[str]
    ) -> None:
        """Add an API definition"""
        api = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "api_type": api_type,
            "version": version,
            "provider_app": provider_app,
            "consumer_apps": consumer_apps,
            "endpoints": endpoints,
            "status": "active",
            "created_at": datetime.now().isoformat()
        }
        
        self.apis.append(api)
    
    def add_integration_pattern(
        self,
        name: str,
        pattern_type: str,  # synchronous, asynchronous, batch, event_driven
        source_app: str,
        target_app: str,
        description: str,
        technology: Optional[str] = None
    ) -> None:
        """Add an integration pattern"""
        pattern = {
            "id": self._generate_id(),
            "name": name,
            "pattern_type": pattern_type,
            "source_app": source_app,
            "target_app": target_app,
            "description": description,
            "technology": technology,
            "created_at": datetime.now().isoformat()
        }
        
        self.integration_patterns.append(pattern)
    
    def get_applications_by_type(self, app_type: str) -> List[Application]:
        """Get all applications of a specific type"""
        return [app for app in self.applications if app.application_type == app_type]
    
    def get_application_portfolio_summary(self) -> Dict:
        """Get summary of application portfolio"""
        if not self.applications:
            return {"total_applications": 0}
        
        type_counts = {}
        lifecycle_counts = {}
        
        for app in self.applications:
            type_counts[app.application_type] = type_counts.get(app.application_type, 0) + 1
            lifecycle_counts[app.lifecycle_status] = lifecycle_counts.get(app.lifecycle_status, 0) + 1
        
        return {
            "total_applications": len(self.applications),
            "by_type": type_counts,
            "by_lifecycle": lifecycle_counts,
            "total_apis": len(self.apis),
            "integration_patterns": len(self.integration_patterns)
        }
    
    # ========== Data Architecture Management ==========
    
    def add_data_entity(
        self,
        name: str,
        description: str,
        entity_type: str,  # master, transactional, reference, analytical
        attributes: List[str],
        owner: str,
        sensitivity: str = "internal"  # public, internal, confidential, restricted
    ) -> None:
        """Add a data entity"""
        entity = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "entity_type": entity_type,
            "attributes": attributes,
            "owner": owner,
            "sensitivity": sensitivity,
            "created_at": datetime.now().isoformat()
        }
        
        self.data_entities.append(entity)
    
    def add_data_flow(
        self,
        name: str,
        source: str,
        target: str,
        data_entities: List[str],
        frequency: str,  # real-time, batch, on-demand
        volume: Optional[str] = None
    ) -> None:
        """Add a data flow"""
        flow = {
            "id": self._generate_id(),
            "name": name,
            "source": source,
            "target": target,
            "data_entities": data_entities,
            "frequency": frequency,
            "volume": volume,
            "created_at": datetime.now().isoformat()
        }
        
        self.data_flows.append(flow)
    
    def add_data_store(
        self,
        name: str,
        store_type: str,  # relational, nosql, data_warehouse, data_lake, cache
        technology: str,
        data_entities: List[str],
        capacity: Optional[str] = None,
        location: str = "azure"
    ) -> None:
        """Add a data store"""
        store = {
            "id": self._generate_id(),
            "name": name,
            "store_type": store_type,
            "technology": technology,
            "data_entities": data_entities,
            "capacity": capacity,
            "location": location,
            "created_at": datetime.now().isoformat()
        }
        
        self.data_stores.append(store)
    
    def define_data_governance(
        self,
        data_stewards: List[str],
        policies: List[str],
        quality_standards: Dict[str, str],
        retention_policies: Dict[str, str]
    ) -> None:
        """Define data governance framework"""
        self.data_governance = {
            "data_stewards": data_stewards,
            "policies": policies,
            "quality_standards": quality_standards,
            "retention_policies": retention_policies,
            "defined_at": datetime.now().isoformat()
        }
    
    def get_data_architecture_summary(self) -> Dict:
        """Get summary of data architecture"""
        entity_types = {}
        store_types = {}
        
        for entity in self.data_entities:
            entity_types[entity["entity_type"]] = entity_types.get(entity["entity_type"], 0) + 1
        
        for store in self.data_stores:
            store_types[store["store_type"]] = store_types.get(store["store_type"], 0) + 1
        
        return {
            "total_entities": len(self.data_entities),
            "entities_by_type": entity_types,
            "total_data_stores": len(self.data_stores),
            "stores_by_type": store_types,
            "total_data_flows": len(self.data_flows),
            "governance_defined": self.data_governance is not None
        }
    
    # ========== Architecture Models ==========
    
    def set_baseline_application_architecture(self, description: Dict) -> None:
        """Set the baseline (As-Is) application architecture"""
        self.baseline_application_arch = {
            "description": description,
            "applications": [app.to_dict() for app in self.applications],
            "apis": self.apis,
            "integration_patterns": self.integration_patterns,
            "created_at": datetime.now().isoformat()
        }
    
    def set_target_application_architecture(self, description: Dict) -> None:
        """Set the target (To-Be) application architecture"""
        self.target_application_arch = {
            "description": description,
            "applications": [app.to_dict() for app in self.applications],
            "apis": self.apis,
            "integration_patterns": self.integration_patterns,
            "improvements": description.get("improvements", []),
            "created_at": datetime.now().isoformat()
        }
    
    def set_baseline_data_architecture(self, description: Dict) -> None:
        """Set the baseline (As-Is) data architecture"""
        self.baseline_data_arch = {
            "description": description,
            "data_entities": self.data_entities,
            "data_stores": self.data_stores,
            "data_flows": self.data_flows,
            "created_at": datetime.now().isoformat()
        }
    
    def set_target_data_architecture(self, description: Dict) -> None:
        """Set the target (To-Be) data architecture"""
        self.target_data_arch = {
            "description": description,
            "data_entities": self.data_entities,
            "data_stores": self.data_stores,
            "data_flows": self.data_flows,
            "governance": self.data_governance,
            "improvements": description.get("improvements", []),
            "created_at": datetime.now().isoformat()
        }
    
    def perform_gap_analysis(self) -> Dict:
        """Perform gap analysis between baseline and target architectures"""
        if not all([
            self.baseline_application_arch,
            self.target_application_arch,
            self.baseline_data_arch,
            self.target_data_arch
        ]):
            raise ValidationException("All baseline and target architectures must be defined")
        
        gaps = {
            "application_gaps": self._analyze_application_gaps(),
            "data_gaps": self._analyze_data_gaps(),
            "integration_gaps": self._analyze_integration_gaps(),
            "performed_at": datetime.now().isoformat()
        }
        
        self.gap_analysis = gaps
        return gaps
    
    def _analyze_application_gaps(self) -> List[Dict]:
        """Analyze gaps in application architecture"""
        gaps = []
        
        # Example gap: Legacy applications needing modernization
        legacy_apps = [app for app in self.applications if app.lifecycle_status == "legacy"]
        for app in legacy_apps:
            gaps.append({
                "application": app.name,
                "current_status": app.lifecycle_status,
                "target_status": "operational",
                "gap_type": "modernization",
                "priority": "high"
            })
        
        # Gap: Missing API management
        if len(self.apis) < 10:  # Arbitrary threshold
            gaps.append({
                "gap_type": "api_coverage",
                "current": len(self.apis),
                "target": "comprehensive API coverage",
                "priority": "critical"
            })
        
        return gaps
    
    def _analyze_data_gaps(self) -> List[Dict]:
        """Analyze gaps in data architecture"""
        gaps = []
        
        # Gap: Data governance
        if not self.data_governance:
            gaps.append({
                "gap_type": "data_governance",
                "description": "Data governance framework not defined",
                "priority": "critical"
            })
        
        # Gap: Master data management
        master_entities = [e for e in self.data_entities if e["entity_type"] == "master"]
        if len(master_entities) < 5:  # Arbitrary threshold
            gaps.append({
                "gap_type": "master_data",
                "current": len(master_entities),
                "target": "comprehensive master data catalog",
                "priority": "high"
            })
        
        return gaps
    
    def _analyze_integration_gaps(self) -> Dict:
        """Analyze integration architecture gaps"""
        api_first = len(self.apis) > len(self.applications) * 0.5
        event_driven = len([p for p in self.integration_patterns if p["pattern_type"] == "event_driven"]) > 0
        
        return {
            "api_first_adoption": api_first,
            "event_driven_adoption": event_driven,
            "total_integrations": len(self.integration_patterns),
            "gaps": [] if (api_first and event_driven) else [
                "Need more API-first patterns" if not api_first else None,
                "Need event-driven architecture" if not event_driven else None
            ]
        }
    
    # ========== Deliverables ==========
    
    def generate_application_architecture_document(self) -> ArchitectureArtifact:
        """Generate the Application Architecture Definition Document"""
        content = {
            "executive_summary": {
                "phase": self.phase_type.name,
                "applications": len(self.applications),
                "apis": len(self.apis),
                "integration_patterns": len(self.integration_patterns)
            },
            "application_portfolio": [app.to_dict() for app in self.applications],
            "apis": self.apis,
            "integration_patterns": self.integration_patterns,
            "application_services": self.application_services,
            "baseline_architecture": self.baseline_application_arch,
            "target_architecture": self.target_application_arch,
            "portfolio_summary": self.get_application_portfolio_summary()
        }
        
        artifact = ArchitectureArtifact(
            name="Application Architecture Definition Document",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Complete application architecture documentation",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_data_architecture_document(self) -> ArchitectureArtifact:
        """Generate the Data Architecture Definition Document"""
        content = {
            "executive_summary": {
                "phase": self.phase_type.name,
                "data_entities": len(self.data_entities),
                "data_stores": len(self.data_stores),
                "data_flows": len(self.data_flows)
            },
            "data_entities": self.data_entities,
            "data_stores": self.data_stores,
            "data_flows": self.data_flows,
            "data_governance": self.data_governance,
            "baseline_architecture": self.baseline_data_arch,
            "target_architecture": self.target_data_arch,
            "data_summary": self.get_data_architecture_summary()
        }
        
        artifact = ArchitectureArtifact(
            name="Data Architecture Definition Document",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Complete data architecture documentation",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_integration_architecture_matrix(self) -> ArchitectureArtifact:
        """Generate Integration Architecture Matrix"""
        # Build integration matrix
        matrix = {}
        for app in self.applications:
            matrix[app.name] = {
                "provides_apis": [api for api in self.apis if api["provider_app"] == app.name],
                "consumes_apis": [api for api in self.apis if app.name in api["consumer_apps"]],
                "integrations": [p for p in self.integration_patterns 
                               if p["source_app"] == app.name or p["target_app"] == app.name]
            }
        
        content = {
            "integration_matrix": matrix,
            "total_apis": len(self.apis),
            "total_integrations": len(self.integration_patterns),
            "api_types": list(set(api["api_type"] for api in self.apis)),
            "integration_patterns": list(set(p["pattern_type"] for p in self.integration_patterns))
        }
        
        artifact = ArchitectureArtifact(
            name="Integration Architecture Matrix",
            artifact_type="matrix",
            phase=self.phase_type.value,
            description="Application integration relationships and patterns",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    # ========== Phase Execution ==========
    
    def validate_phase(self) -> bool:
        """Validate that Phase C has minimum required content"""
        validations = [
            (len(self.applications) > 0, "At least one application required"),
            (len(self.data_entities) > 0, "At least one data entity required"),
            (self.baseline_application_arch is not None, "Baseline application architecture must be defined"),
            (self.target_application_arch is not None, "Target application architecture must be defined"),
            (self.baseline_data_arch is not None, "Baseline data architecture must be defined"),
            (self.target_data_arch is not None, "Target data architecture must be defined")
        ]
        
        for is_valid, message in validations:
            if not is_valid:
                raise ValidationException(f"Phase C validation failed: {message}")
        
        return True
    
    def execute(self) -> Dict:
        """
        Execute Phase C: Information Systems Architecture
        
        Returns comprehensive results including applications, data, APIs,
        gap analysis, and deliverables.
        """
        self.start_phase()
        
        try:
            # Validate prerequisites
            self.validate_phase()
            
            # Generate deliverables
            app_doc = self.generate_application_architecture_document()
            data_doc = self.generate_data_architecture_document()
            integration_matrix = self.generate_integration_architecture_matrix()
            
            # Complete phase
            self.complete_phase()
            
            results = {
                "phase": self.phase_type.name,
                "status": self.status.name,
                "progress": self.progress,
                "application_architecture": {
                    "portfolio_summary": self.get_application_portfolio_summary(),
                    "applications": [app.to_dict() for app in self.applications],
                    "apis": self.apis,
                    "integration_patterns": self.integration_patterns
                },
                "data_architecture": {
                    "summary": self.get_data_architecture_summary(),
                    "entities": self.data_entities,
                    "stores": self.data_stores,
                    "flows": self.data_flows,
                    "governance": self.data_governance
                },
                "gap_analysis": self.gap_analysis,
                "deliverables": {
                    "application_architecture_document": app_doc.to_dict(),
                    "data_architecture_document": data_doc.to_dict(),
                    "integration_architecture_matrix": integration_matrix.to_dict()
                },
                "activities": self.get_activities_status(),
                "completed_at": datetime.now().isoformat()
            }
            
            return results
            
        except Exception as e:
            raise
