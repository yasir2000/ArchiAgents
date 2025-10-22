"""
TOGAF ADM Phase B: Business Architecture

This module implements Phase B of the TOGAF Architecture Development Method (ADM).
Phase B focuses on developing the business architecture, including:
- Business capability modeling
- Business process modeling
- Value stream mapping
- Organizational architecture
- Business information needs

Reference: TOGAF 10 ADM Phase B
"""

from typing import List, Dict, Optional, Set
from datetime import datetime
import uuid
from ..core.base import ArchitectureElement
from ..core.enums import (
    ADMPhaseType,
    ArchiMateLayerType,
    PriorityLevel,
    ArchitectureStatus,
    ProcessType,
    MaturityLevel
)
from ..core.exceptions import ValidationException
from .adm_phase import ADMPhase
from ..models.capability import BusinessCapability
from ..models.process import BusinessProcess
from ..models.artifact import ArchitectureArtifact, ArtifactType


class PhaseBBusinessArchitecture(ADMPhase):
    """
    Phase B: Business Architecture
    
    Develops the Target Business Architecture that supports the Architecture Vision,
    describing how the enterprise needs to operate to achieve its business goals.
    
    Key Activities:
    1. Select reference models, viewpoints, and tools
    2. Develop baseline business architecture description
    3. Develop target business architecture description
    4. Perform gap analysis
    5. Define candidate roadmap components
    6. Resolve impacts across architecture landscape
    7. Conduct formal stakeholder review
    8. Finalize business architecture
    9. Create architecture definition document
    """
    
    phase_type = ADMPhaseType.PHASE_B
    
    def __init__(self, name: str = "Business Architecture", **kwargs):
        super().__init__(name, **kwargs)
        
        # Business Architecture Components
        self.business_capabilities: List[BusinessCapability] = []
        self.business_processes: List[BusinessProcess] = []
        self.value_streams: List[Dict] = []
        self.organizational_structure: Optional[Dict] = None
        self.business_functions: List[Dict] = []
        self.business_services: List[Dict] = []
        
        # Architecture Models
        self.baseline_architecture: Optional[Dict] = None
        self.target_architecture: Optional[Dict] = None
        self.gap_analysis: Optional[Dict] = None
        
        # Business Information
        self.information_needs: List[Dict] = []
        self.business_events: List[Dict] = []
        
        # Performance Metrics
        self.kpis: List[Dict] = []
        self.business_metrics: Dict[str, any] = {}
        
    def _initialize_phase(self) -> None:
        """Initialize Phase B - called by base class"""
        self._initialize_objectives()
        self._initialize_activities()
    
    def _generate_id(self) -> str:
        """Generate a unique ID"""
        return str(uuid.uuid4())
    
    def _initialize_objectives(self):
        """Initialize Phase B standard objectives"""
        objectives = [
            "Develop Target Business Architecture describing how the enterprise needs to operate",
            "Identify candidate Architecture Roadmap components based on gaps",
            "Define business capabilities required to support Architecture Vision",
            "Model business processes and identify optimization opportunities",
            "Define organizational structure and business functions",
            "Identify business information needs and data requirements",
            "Establish business performance metrics and KPIs",
            "Validate alignment with business strategy and goals"
        ]
        for objective in objectives:
            self.add_objective(objective)
    
    def _initialize_activities(self):
        """Initialize Phase B standard activities"""
        activities = [
            {
                "name": "Select Reference Models, Viewpoints and Tools",
                "description": "Select relevant business architecture reference models and tools",
                "sequence": 1
            },
            {
                "name": "Develop Baseline Business Architecture Description",
                "description": "Document current state business architecture (As-Is)",
                "sequence": 2
            },
            {
                "name": "Develop Target Business Architecture Description",
                "description": "Document future state business architecture (To-Be)",
                "sequence": 3
            },
            {
                "name": "Perform Gap Analysis",
                "description": "Identify gaps between baseline and target architectures",
                "sequence": 4
            },
            {
                "name": "Define Candidate Roadmap Components",
                "description": "Identify work packages and transition architectures",
                "sequence": 5
            },
            {
                "name": "Resolve Impacts Across Architecture Landscape",
                "description": "Assess impact on other architecture domains",
                "sequence": 6
            },
            {
                "name": "Conduct Formal Stakeholder Review",
                "description": "Review business architecture with stakeholders",
                "sequence": 7
            },
            {
                "name": "Finalize Business Architecture",
                "description": "Complete and approve business architecture",
                "sequence": 8
            },
            {
                "name": "Create Architecture Definition Document",
                "description": "Document business architecture for delivery",
                "sequence": 9
            }
        ]
        for activity in activities:
            self.add_activity(
                activity["name"],
                activity["description"],
                activity["sequence"]
            )
    
    # ========== Capability Management ==========
    
    def add_business_capability(
        self,
        capability: BusinessCapability
    ) -> None:
        """Add a business capability to the architecture"""
        if not isinstance(capability, BusinessCapability):
            raise ValidationException("Must provide BusinessCapability instance")
        
        self.business_capabilities.append(capability)

    
    def create_capability_hierarchy(
        self,
        name: str,
        description: str,
        level: int = 1,
        parent_id: Optional[str] = None,
        maturity_level: MaturityLevel = MaturityLevel.DEFINED,
        strategic_importance: PriorityLevel = PriorityLevel.MEDIUM
    ) -> BusinessCapability:
        """Create and add a business capability with hierarchy support"""
        # Find parent capability if parent_id is provided
        parent_cap = None
        if parent_id:
            parent_cap = self.get_capability_by_id(parent_id)
        
        capability = BusinessCapability(
            name=name,
            description=description,
            level=level,
            parent_capability=parent_cap
        )
        
        # Set maturity and importance using string values
        capability.set_maturity_level(maturity_level.name.lower())
        capability.set_strategic_importance(strategic_importance.name.lower())
        
        self.add_business_capability(capability)
        return capability
    
    def get_capabilities_by_level(self, level: int) -> List[BusinessCapability]:
        """Get all capabilities at a specific hierarchy level"""
        return [cap for cap in self.business_capabilities if cap.level == level]
    
    def get_capability_by_id(self, capability_id: str) -> Optional[BusinessCapability]:
        """Get a specific capability by ID"""
        return next(
            (cap for cap in self.business_capabilities if cap.id == capability_id),
            None
        )
    
    def get_capability_maturity_assessment(self) -> Dict:
        """Assess overall capability maturity"""
        if not self.business_capabilities:
            return {"average_maturity": 0, "capabilities_by_maturity": {}}
        
        maturity_map = {"initial": 1, "defined": 2, "managed": 3, "optimized": 4}
        maturity_counts = {}
        total_maturity = 0
        
        for cap in self.business_capabilities:
            maturity = maturity_map.get(cap.maturity_level, 1)
            maturity_counts[cap.maturity_level] = maturity_counts.get(
                cap.maturity_level, 0
            ) + 1
            total_maturity += maturity
        
        return {
            "total_capabilities": len(self.business_capabilities),
            "average_maturity": total_maturity / len(self.business_capabilities),
            "capabilities_by_maturity": maturity_counts,
            "target_maturity": 4  # Optimized
        }
    
    # ========== Process Management ==========
    
    def add_business_process(self, process: BusinessProcess) -> None:
        """Add a business process to the architecture"""
        if not isinstance(process, BusinessProcess):
            raise ValidationException("Must provide BusinessProcess instance")
        
        self.business_processes.append(process)

    
    def create_business_process(
        self,
        name: str,
        description: str,
        process_type: ProcessType = ProcessType.SUPPORTING,
        automation_level: float = 0.0,
        cycle_time_hours: Optional[float] = None
    ) -> BusinessProcess:
        """Create and add a business process"""
        process = BusinessProcess(
            name=name,
            description=description
        )
        
        # Set process type and automation level
        process.process_type = process_type.name.lower()
        process.set_automation_level(automation_level / 100.0)  # Convert percentage to 0-1 range
        
        if cycle_time_hours:
            process.set_cycle_time(cycle_time_hours)
        
        self.add_business_process(process)
        return process
    
    def get_processes_by_type(self, process_type: ProcessType) -> List[BusinessProcess]:
        """Get all processes of a specific type"""
        type_name = process_type.name.lower()
        return [p for p in self.business_processes if p.process_type == type_name]
    
    def get_automation_assessment(self) -> Dict:
        """Assess process automation levels"""
        if not self.business_processes:
            return {
                "average_automation": 0,
                "manual_processes": 0,
                "automated_processes": 0
            }
        
        # Convert from 0-1 range to percentage
        total_automation = sum(p.automation_level * 100 for p in self.business_processes)
        manual_count = sum(1 for p in self.business_processes if p.automation_level * 100 < 25)
        automated_count = sum(1 for p in self.business_processes if p.automation_level * 100 >= 75)
        
        return {
            "total_processes": len(self.business_processes),
            "average_automation": total_automation / len(self.business_processes),
            "manual_processes": manual_count,
            "partially_automated": len(self.business_processes) - manual_count - automated_count,
            "automated_processes": automated_count,
            "target_automation": 70.0  # From repository targets
        }
    
    # ========== Value Stream Management ==========
    
    def add_value_stream(
        self,
        name: str,
        description: str,
        stages: List[str],
        value_proposition: str,
        stakeholder_value: Dict[str, str]
    ) -> None:
        """Add a value stream to the business architecture"""
        value_stream = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "stages": stages,
            "value_proposition": value_proposition,
            "stakeholder_value": stakeholder_value,
            "created_at": datetime.now().isoformat()
        }
        
        self.value_streams.append(value_stream)

    
    # ========== Organizational Architecture ==========
    
    def define_organizational_structure(
        self,
        divisions: List[Dict],
        departments: List[Dict],
        reporting_structure: Dict
    ) -> None:
        """Define the organizational structure"""
        self.organizational_structure = {
            "divisions": divisions,
            "departments": departments,
            "reporting_structure": reporting_structure,
            "defined_at": datetime.now().isoformat()
        }
        

    
    def add_business_function(
        self,
        name: str,
        description: str,
        owner: str,
        capabilities: List[str],
        processes: List[str]
    ) -> None:
        """Add a business function"""
        function = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "owner": owner,
            "capabilities": capabilities,
            "processes": processes,
            "created_at": datetime.now().isoformat()
        }
        
        self.business_functions.append(function)

    
    # ========== Business Information ==========
    
    def add_information_need(
        self,
        entity: str,
        description: str,
        priority: PriorityLevel,
        required_for: List[str],
        data_quality_requirements: Dict[str, str]
    ) -> None:
        """Add a business information need"""
        info_need = {
            "id": self._generate_id(),
            "entity": entity,
            "description": description,
            "priority": priority.name,
            "required_for": required_for,
            "data_quality_requirements": data_quality_requirements,
            "created_at": datetime.now().isoformat()
        }
        
        self.information_needs.append(info_need)

    
    def add_business_event(
        self,
        name: str,
        description: str,
        trigger: str,
        affected_processes: List[str],
        data_produced: List[str]
    ) -> None:
        """Add a business event"""
        event = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "trigger": trigger,
            "affected_processes": affected_processes,
            "data_produced": data_produced,
            "created_at": datetime.now().isoformat()
        }
        
        self.business_events.append(event)

    
    # ========== Architecture Models ==========
    
    def set_baseline_architecture(self, description: Dict) -> None:
        """Set the baseline (As-Is) business architecture"""
        self.baseline_architecture = {
            "description": description,
            "capabilities": [cap.to_dict() for cap in self.business_capabilities],
            "processes": [proc.to_dict() for proc in self.business_processes],
            "created_at": datetime.now().isoformat()
        }

    
    def set_target_architecture(self, description: Dict) -> None:
        """Set the target (To-Be) business architecture"""
        self.target_architecture = {
            "description": description,
            "capabilities": [cap.to_dict() for cap in self.business_capabilities],
            "processes": [proc.to_dict() for proc in self.business_processes],
            "improvements": description.get("improvements", []),
            "created_at": datetime.now().isoformat()
        }

    
    def perform_gap_analysis(self) -> Dict:
        """Perform gap analysis between baseline and target architectures"""
        if not self.baseline_architecture or not self.target_architecture:
            raise ValidationException("Both baseline and target architectures must be defined")
        
        gaps = {
            "capability_gaps": self._analyze_capability_gaps(),
            "process_gaps": self._analyze_process_gaps(),
            "automation_gaps": self._analyze_automation_gaps(),
            "maturity_gaps": self._analyze_maturity_gaps(),
            "performed_at": datetime.now().isoformat()
        }
        
        self.gap_analysis = gaps

        
        return gaps
    
    def _analyze_capability_gaps(self) -> List[Dict]:
        """Analyze gaps in business capabilities"""
        gaps = []
        maturity_map = {"initial": 1, "defined": 2, "managed": 3, "optimized": 4}
        
        for capability in self.business_capabilities:
            current_maturity = maturity_map.get(capability.maturity_level, 1)
            if current_maturity < 4:  # Not optimized
                gaps.append({
                    "capability": capability.name,
                    "current_maturity": capability.maturity_level,
                    "target_maturity": "optimized",
                    "gap": 4 - current_maturity,
                    "priority": capability.strategic_importance
                })
        
        return gaps
    
    def _analyze_process_gaps(self) -> List[Dict]:
        """Analyze gaps in business processes"""
        gaps = []
        target_automation = 70.0  # From repository targets
        
        for process in self.business_processes:
            current_automation = process.automation_level * 100  # Convert to percentage
            if current_automation < target_automation:
                gaps.append({
                    "process": process.name,
                    "current_automation": current_automation,
                    "target_automation": target_automation,
                    "gap": target_automation - current_automation,
                    "process_type": process.process_type
                })
        
        return gaps
    
    def _analyze_automation_gaps(self) -> Dict:
        """Analyze overall automation gaps"""
        assessment = self.get_automation_assessment()
        
        return {
            "current_average": assessment["average_automation"],
            "target_average": assessment["target_automation"],
            "gap": assessment["target_automation"] - assessment["average_automation"],
            "processes_needing_automation": assessment["manual_processes"] + assessment.get("partially_automated", 0)
        }
    
    def _analyze_maturity_gaps(self) -> Dict:
        """Analyze overall maturity gaps"""
        assessment = self.get_capability_maturity_assessment()
        
        return {
            "current_average": assessment["average_maturity"],
            "target_average": assessment["target_maturity"],
            "gap": assessment["target_maturity"] - assessment["average_maturity"],
            "capabilities_needing_improvement": sum(
                1 for cap in self.business_capabilities
                if cap.maturity_level != MaturityLevel.OPTIMIZED
            )
        }
    
    # ========== KPIs and Metrics ==========
    
    def add_kpi(
        self,
        name: str,
        description: str,
        target_value: float,
        current_value: float,
        unit: str,
        category: str
    ) -> None:
        """Add a business KPI"""
        kpi = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "target_value": target_value,
            "current_value": current_value,
            "unit": unit,
            "category": category,
            "gap": target_value - current_value,
            "created_at": datetime.now().isoformat()
        }
        
        self.kpis.append(kpi)

    
    def get_kpi_dashboard(self) -> Dict:
        """Get KPI dashboard summary"""
        if not self.kpis:
            return {"kpis": [], "summary": {}}
        
        on_target = sum(1 for kpi in self.kpis if kpi["current_value"] >= kpi["target_value"])
        
        return {
            "total_kpis": len(self.kpis),
            "on_target": on_target,
            "needs_improvement": len(self.kpis) - on_target,
            "kpis": self.kpis,
            "categories": list(set(kpi["category"] for kpi in self.kpis))
        }
    
    # ========== Deliverables ==========
    
    def generate_business_architecture_document(self) -> ArchitectureArtifact:
        """Generate the Business Architecture Definition Document"""
        content = {
            "executive_summary": {
                "phase": self.phase_type.name,
                "capabilities": len(self.business_capabilities),
                "processes": len(self.business_processes),
                "value_streams": len(self.value_streams)
            },
            "business_capabilities": [cap.to_dict() for cap in self.business_capabilities],
            "business_processes": [proc.to_dict() for proc in self.business_processes],
            "value_streams": self.value_streams,
            "organizational_structure": self.organizational_structure,
            "business_functions": self.business_functions,
            "information_needs": self.information_needs,
            "business_events": self.business_events,
            "baseline_architecture": self.baseline_architecture,
            "target_architecture": self.target_architecture,
            "gap_analysis": self.gap_analysis,
            "kpis": self.kpis,
            "capability_maturity": self.get_capability_maturity_assessment(),
            "automation_assessment": self.get_automation_assessment()
        }
        
        artifact = ArchitectureArtifact(
            name="Business Architecture Definition Document",
            description="Complete business architecture documentation",
            artifact_type="catalog",
            phase=self.phase_type.value,
            content=content,
        )
        
        self.add_output(artifact)

        
        return artifact
    
    def generate_capability_catalog(self) -> ArchitectureArtifact:
        """Generate Business Capability Catalog"""
        content = {
            "capabilities": [cap.to_dict() for cap in self.business_capabilities],
            "hierarchy": self._build_capability_hierarchy(),
            "maturity_assessment": self.get_capability_maturity_assessment(),
            "strategic_capabilities": [
                cap.to_dict() for cap in self.business_capabilities
                if cap.strategic_importance == PriorityLevel.CRITICAL
            ]
        }
        
        artifact = ArchitectureArtifact(
            name="Business Capability Catalog",
            description="Complete catalog of business capabilities",
            artifact_type="catalog",
            phase=self.phase_type.value,
            content=content,
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_process_catalog(self) -> ArchitectureArtifact:
        """Generate Business Process Catalog"""
        content = {
            "processes": [proc.to_dict() for proc in self.business_processes],
            "core_processes": [p.to_dict() for p in self.get_processes_by_type(ProcessType.CORE)],
            "supporting_processes": [p.to_dict() for p in self.get_processes_by_type(ProcessType.SUPPORTING)],
            "management_processes": [p.to_dict() for p in self.get_processes_by_type(ProcessType.MANAGEMENT)],
            "automation_assessment": self.get_automation_assessment()
        }
        
        artifact = ArchitectureArtifact(
            name="Business Process Catalog",
            description="Complete catalog of business processes",
            artifact_type="catalog",
            phase=self.phase_type.value,
            content=content,
        )
        
        self.add_output(artifact)
        return artifact
    
    def _build_capability_hierarchy(self) -> Dict:
        """Build hierarchical structure of capabilities"""
        hierarchy = {}
        
        # Group by level
        for level in range(1, 5):  # Typical 4-level capability model
            level_caps = self.get_capabilities_by_level(level)
            if level_caps:
                hierarchy[f"level_{level}"] = [cap.to_dict() for cap in level_caps]
        
        return hierarchy
    
    # ========== Phase Execution ==========
    
    def validate_phase(self) -> bool:
        """Validate that Phase B has minimum required content"""
        validations = [
            (len(self.business_capabilities) > 0, "At least one business capability required"),
            (len(self.business_processes) > 0, "At least one business process required"),
            (self.baseline_architecture is not None, "Baseline architecture must be defined"),
            (self.target_architecture is not None, "Target architecture must be defined"),
            (self.gap_analysis is not None, "Gap analysis must be performed")
        ]
        
        for is_valid, message in validations:
            if not is_valid:
                raise ValidationException(f"Phase B validation failed: {message}")
        
        return True
    
    def execute(self) -> Dict:
        """
        Execute Phase B: Business Architecture
        
        Returns comprehensive results including capabilities, processes,
        gap analysis, and deliverables.
        """
        self.start_phase()
        
        try:
            # Validate prerequisites
            self.validate_phase()
            
            # Mark activities as in progress
            
            # Generate deliverables
            business_doc = self.generate_business_architecture_document()
            capability_catalog = self.generate_capability_catalog()
            process_catalog = self.generate_process_catalog()
            
            # Mark remaining activities
            
            # Complete phase
            self.complete_phase()
            
            results = {
                "phase": self.phase_type.name,
                "status": self.status.name,
                "progress": self.progress,
                "business_capabilities": {
                    "count": len(self.business_capabilities),
                    "maturity_assessment": self.get_capability_maturity_assessment(),
                    "capabilities": [cap.to_dict() for cap in self.business_capabilities]
                },
                "business_processes": {
                    "count": len(self.business_processes),
                    "automation_assessment": self.get_automation_assessment(),
                    "processes": [proc.to_dict() for proc in self.business_processes]
                },
                "value_streams": self.value_streams,
                "gap_analysis": self.gap_analysis,
                "kpi_dashboard": self.get_kpi_dashboard(),
                "deliverables": {
                    "business_architecture_document": business_doc.to_dict(),
                    "capability_catalog": capability_catalog.to_dict(),
                    "process_catalog": process_catalog.to_dict()
                },
                "activities": self.get_activities_status(),
                "completed_at": datetime.now().isoformat()
            }
            
    
            return results
            
        except Exception as e:
    
            raise
