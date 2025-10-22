"""
TOGAF ADM Phase D: Technology Architecture

This module implements Phase D of the TOGAF Architecture Development Method (ADM).
Phase D focuses on developing the Technology Architecture, including:
- Cloud infrastructure and platform architecture
- Network architecture and connectivity
- Security architecture and controls
- DevOps and automation
- Infrastructure as Code (IaC)

Reference: TOGAF 10 ADM Phase D
"""

from typing import List, Dict, Optional
from datetime import datetime
import uuid
from ..core.base import ArchitectureElement
from ..core.enums import (
    ADMPhaseType,
    ArchiMateLayerType,
    PriorityLevel,
    CloudProvider
)
from ..core.exceptions import ValidationException
from .adm_phase import ADMPhase
from ..models.technology import TechnologyComponent
from ..models.artifact import ArchitectureArtifact


class PhaseDTechnologyArchitecture(ADMPhase):
    """
    Phase D: Technology Architecture
    
    Develops the Target Technology Architecture that supports the 
    Application and Data Architectures and Architecture Vision.
    
    Key Activities:
    1. Select reference models, viewpoints, and tools
    2. Develop baseline technology architecture description
    3. Develop target technology architecture description
    4. Perform gap analysis
    5. Define candidate roadmap components
    6. Resolve impacts across architecture landscape
    7. Conduct formal stakeholder review
    8. Finalize technology architecture
    9. Create architecture definition document
    """
    
    phase_type = ADMPhaseType.PHASE_D
    
    def __init__(self, name: str = "Technology Architecture", **kwargs):
        super().__init__(name, **kwargs)
        
        # Technology Components
        self.technology_components: List[TechnologyComponent] = []
        self.infrastructure_services: List[Dict] = []
        self.platforms: List[Dict] = []
        
        # Cloud Architecture
        self.cloud_services: List[Dict] = []
        self.compute_resources: List[Dict] = []
        self.storage_resources: List[Dict] = []
        self.network_resources: List[Dict] = []
        
        # Security & Compliance
        self.security_controls: List[Dict] = []
        self.compliance_requirements: List[Dict] = []
        
        # DevOps & Automation
        self.ci_cd_pipelines: List[Dict] = []
        self.iac_templates: List[Dict] = []
        self.monitoring_tools: List[Dict] = []
        
        # Architecture Models
        self.baseline_architecture: Optional[Dict] = None
        self.target_architecture: Optional[Dict] = None
        self.gap_analysis: Optional[Dict] = None
        
        # Multi-cloud Strategy
        self.cloud_strategy: Optional[Dict] = None
        self.cloud_providers: List[str] = []
    
    def _initialize_phase(self) -> None:
        """Initialize Phase D - called by base class"""
        self._initialize_objectives()
        self._initialize_activities()
    
    def _generate_id(self) -> str:
        """Generate a unique ID"""
        return str(uuid.uuid4())
    
    def _initialize_objectives(self):
        """Initialize Phase D standard objectives"""
        objectives = [
            "Develop Target Technology Architecture supporting information systems",
            "Define cloud infrastructure and platform strategy",
            "Establish network architecture and connectivity patterns",
            "Define security architecture and controls",
            "Define DevOps and automation architecture",
            "Establish multi-cloud strategy and governance",
            "Define infrastructure as code approach",
            "Ensure scalability, reliability, and performance targets"
        ]
        for objective in objectives:
            self.add_objective(objective)
    
    def _initialize_activities(self):
        """Initialize Phase D standard activities"""
        activities = [
            {
                "name": "Select Reference Models, Viewpoints and Tools",
                "description": "Select relevant technology architecture reference models",
                "sequence": 1
            },
            {
                "name": "Develop Baseline Technology Architecture",
                "description": "Document current state technology architecture (As-Is)",
                "sequence": 2
            },
            {
                "name": "Develop Target Technology Architecture",
                "description": "Document future state technology architecture (To-Be)",
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
                "description": "Review technology architecture with stakeholders",
                "sequence": 7
            },
            {
                "name": "Finalize Technology Architecture",
                "description": "Complete and approve technology architecture",
                "sequence": 8
            },
            {
                "name": "Create Architecture Definition Document",
                "description": "Document technology architecture for delivery",
                "sequence": 9
            }
        ]
        for activity in activities:
            self.add_activity(
                activity["name"],
                activity["description"],
                activity["sequence"]
            )
    
    # ========== Technology Component Management ==========
    
    def add_technology_component(self, component: TechnologyComponent) -> None:
        """Add a technology component to the architecture"""
        if not isinstance(component, TechnologyComponent):
            raise ValidationException("Must provide TechnologyComponent instance")
        
        self.technology_components.append(component)
    
    def create_technology_component(
        self,
        name: str,
        description: str,
        component_type: str,  # server, network, storage, platform, tool
        cloud_provider: str = "azure",
        specifications: Optional[Dict] = None
    ) -> TechnologyComponent:
        """Create and add a technology component"""
        component = TechnologyComponent(
            name=name,
            description=description
        )
        
        component.component_type = component_type
        component.cloud_provider = cloud_provider
        if specifications:
            component.specifications = specifications
        
        self.add_technology_component(component)
        return component
    
    # ========== Cloud Services Management ==========
    
    def add_cloud_service(
        self,
        name: str,
        service_type: str,  # compute, storage, database, networking, security, ai_ml
        provider: str,  # azure, aws, gcp
        tier: str,  # free, basic, standard, premium
        region: str,
        sla: float = 99.9
    ) -> None:
        """Add a cloud service"""
        service = {
            "id": self._generate_id(),
            "name": name,
            "service_type": service_type,
            "provider": provider,
            "tier": tier,
            "region": region,
            "sla": sla,
            "created_at": datetime.now().isoformat()
        }
        
        self.cloud_services.append(service)
        if provider not in self.cloud_providers:
            self.cloud_providers.append(provider)
    
    def add_compute_resource(
        self,
        name: str,
        resource_type: str,  # vm, container, serverless, kubernetes
        provider: str,
        vcpus: int,
        memory_gb: int,
        scaling_type: str = "manual"  # manual, auto_horizontal, auto_vertical
    ) -> None:
        """Add a compute resource"""
        resource = {
            "id": self._generate_id(),
            "name": name,
            "resource_type": resource_type,
            "provider": provider,
            "vcpus": vcpus,
            "memory_gb": memory_gb,
            "scaling_type": scaling_type,
            "created_at": datetime.now().isoformat()
        }
        
        self.compute_resources.append(resource)
    
    def add_storage_resource(
        self,
        name: str,
        storage_type: str,  # block, file, object, archive
        provider: str,
        capacity_tb: float,
        performance_tier: str = "standard",  # hot, cool, archive
        redundancy: str = "zone_redundant"
    ) -> None:
        """Add a storage resource"""
        resource = {
            "id": self._generate_id(),
            "name": name,
            "storage_type": storage_type,
            "provider": provider,
            "capacity_tb": capacity_tb,
            "performance_tier": performance_tier,
            "redundancy": redundancy,
            "created_at": datetime.now().isoformat()
        }
        
        self.storage_resources.append(resource)
    
    def add_network_resource(
        self,
        name: str,
        network_type: str,  # vnet, subnet, vpn, cdn, load_balancer, firewall
        provider: str,
        address_space: Optional[str] = None,
        bandwidth_mbps: Optional[int] = None
    ) -> None:
        """Add a network resource"""
        resource = {
            "id": self._generate_id(),
            "name": name,
            "network_type": network_type,
            "provider": provider,
            "address_space": address_space,
            "bandwidth_mbps": bandwidth_mbps,
            "created_at": datetime.now().isoformat()
        }
        
        self.network_resources.append(resource)
    
    def define_cloud_strategy(
        self,
        primary_provider: str,
        secondary_provider: Optional[str] = None,
        strategy_type: str = "multi_cloud",  # single_cloud, multi_cloud, hybrid
        rationale: str = "",
        disaster_recovery: bool = True
    ) -> None:
        """Define cloud strategy"""
        self.cloud_strategy = {
            "primary_provider": primary_provider,
            "secondary_provider": secondary_provider,
            "strategy_type": strategy_type,
            "rationale": rationale,
            "disaster_recovery": disaster_recovery,
            "providers": list(set([primary_provider] + ([secondary_provider] if secondary_provider else []))),
            "defined_at": datetime.now().isoformat()
        }
    
    # ========== Security & Compliance ==========
    
    def add_security_control(
        self,
        name: str,
        control_type: str,  # network, identity, data, application, infrastructure
        description: str,
        implementation: str,
        compliance_standards: List[str]
    ) -> None:
        """Add a security control"""
        control = {
            "id": self._generate_id(),
            "name": name,
            "control_type": control_type,
            "description": description,
            "implementation": implementation,
            "compliance_standards": compliance_standards,
            "created_at": datetime.now().isoformat()
        }
        
        self.security_controls.append(control)
    
    def add_compliance_requirement(
        self,
        standard: str,  # ISO27001, SOC2, GDPR, PCI_DSS, NORA
        description: str,
        controls: List[str],
        status: str = "planned"  # planned, in_progress, compliant
    ) -> None:
        """Add a compliance requirement"""
        requirement = {
            "id": self._generate_id(),
            "standard": standard,
            "description": description,
            "controls": controls,
            "status": status,
            "created_at": datetime.now().isoformat()
        }
        
        self.compliance_requirements.append(requirement)
    
    # ========== DevOps & Automation ==========
    
    def add_ci_cd_pipeline(
        self,
        name: str,
        tool: str,  # azure_devops, github_actions, jenkins, gitlab_ci
        stages: List[str],
        deployment_targets: List[str],
        automation_level: float = 100.0
    ) -> None:
        """Add a CI/CD pipeline"""
        pipeline = {
            "id": self._generate_id(),
            "name": name,
            "tool": tool,
            "stages": stages,
            "deployment_targets": deployment_targets,
            "automation_level": automation_level,
            "created_at": datetime.now().isoformat()
        }
        
        self.ci_cd_pipelines.append(pipeline)
    
    def add_iac_template(
        self,
        name: str,
        tool: str,  # terraform, bicep, arm, cloudformation, pulumi
        provider: str,
        resources: List[str],
        version_control: bool = True
    ) -> None:
        """Add an Infrastructure as Code template"""
        template = {
            "id": self._generate_id(),
            "name": name,
            "tool": tool,
            "provider": provider,
            "resources": resources,
            "version_control": version_control,
            "created_at": datetime.now().isoformat()
        }
        
        self.iac_templates.append(template)
    
    def add_monitoring_tool(
        self,
        name: str,
        tool_type: str,  # observability, logging, metrics, tracing, alerting
        tool: str,  # prometheus, grafana, elk, jaeger, datadog, azure_monitor
        targets: List[str],
        alerting_enabled: bool = True
    ) -> None:
        """Add a monitoring tool"""
        monitoring = {
            "id": self._generate_id(),
            "name": name,
            "tool_type": tool_type,
            "tool": tool,
            "targets": targets,
            "alerting_enabled": alerting_enabled,
            "created_at": datetime.now().isoformat()
        }
        
        self.monitoring_tools.append(monitoring)
    
    # ========== Platform Management ==========
    
    def add_platform(
        self,
        name: str,
        platform_type: str,  # container_orchestration, serverless, paas, api_gateway
        technology: str,  # kubernetes, azure_functions, azure_app_service, apim
        provider: str,
        high_availability: bool = True
    ) -> None:
        """Add a platform"""
        platform = {
            "id": self._generate_id(),
            "name": name,
            "platform_type": platform_type,
            "technology": technology,
            "provider": provider,
            "high_availability": high_availability,
            "created_at": datetime.now().isoformat()
        }
        
        self.platforms.append(platform)
    
    # ========== Summary and Analysis ==========
    
    def get_infrastructure_summary(self) -> Dict:
        """Get summary of infrastructure architecture"""
        provider_distribution = {}
        for provider in self.cloud_providers:
            provider_distribution[provider] = {
                "compute": len([c for c in self.compute_resources if c["provider"] == provider]),
                "storage": len([s for s in self.storage_resources if s["provider"] == provider]),
                "network": len([n for n in self.network_resources if n["provider"] == provider]),
                "services": len([s for s in self.cloud_services if s["provider"] == provider])
            }
        
        return {
            "total_components": len(self.technology_components),
            "cloud_providers": self.cloud_providers,
            "provider_distribution": provider_distribution,
            "compute_resources": len(self.compute_resources),
            "storage_resources": len(self.storage_resources),
            "network_resources": len(self.network_resources),
            "cloud_services": len(self.cloud_services),
            "platforms": len(self.platforms)
        }
    
    def get_security_summary(self) -> Dict:
        """Get summary of security architecture"""
        control_types = {}
        for control in self.security_controls:
            control_type = control["control_type"]
            control_types[control_type] = control_types.get(control_type, 0) + 1
        
        compliance_status = {}
        for req in self.compliance_requirements:
            compliance_status[req["standard"]] = req["status"]
        
        return {
            "total_controls": len(self.security_controls),
            "controls_by_type": control_types,
            "compliance_requirements": len(self.compliance_requirements),
            "compliance_status": compliance_status
        }
    
    def get_devops_summary(self) -> Dict:
        """Get summary of DevOps architecture"""
        return {
            "ci_cd_pipelines": len(self.ci_cd_pipelines),
            "iac_templates": len(self.iac_templates),
            "monitoring_tools": len(self.monitoring_tools),
            "automation_coverage": sum(p["automation_level"] for p in self.ci_cd_pipelines) / len(self.ci_cd_pipelines) if self.ci_cd_pipelines else 0
        }
    
    # ========== Architecture Models ==========
    
    def set_baseline_architecture(self, description: Dict) -> None:
        """Set the baseline (As-Is) technology architecture"""
        self.baseline_architecture = {
            "description": description,
            "components": [c.to_dict() for c in self.technology_components],
            "cloud_services": self.cloud_services,
            "compute": self.compute_resources,
            "storage": self.storage_resources,
            "network": self.network_resources,
            "security": self.security_controls,
            "created_at": datetime.now().isoformat()
        }
    
    def set_target_architecture(self, description: Dict) -> None:
        """Set the target (To-Be) technology architecture"""
        self.target_architecture = {
            "description": description,
            "components": [c.to_dict() for c in self.technology_components],
            "cloud_strategy": self.cloud_strategy,
            "cloud_services": self.cloud_services,
            "compute": self.compute_resources,
            "storage": self.storage_resources,
            "network": self.network_resources,
            "security": self.security_controls,
            "platforms": self.platforms,
            "devops": {
                "ci_cd": self.ci_cd_pipelines,
                "iac": self.iac_templates,
                "monitoring": self.monitoring_tools
            },
            "improvements": description.get("improvements", []),
            "created_at": datetime.now().isoformat()
        }
    
    def perform_gap_analysis(self) -> Dict:
        """Perform gap analysis between baseline and target architectures"""
        if not self.baseline_architecture or not self.target_architecture:
            raise ValidationException("Both baseline and target architectures must be defined")
        
        gaps = {
            "cloud_migration_gaps": self._analyze_cloud_gaps(),
            "security_gaps": self._analyze_security_gaps(),
            "automation_gaps": self._analyze_automation_gaps(),
            "scalability_gaps": self._analyze_scalability_gaps(),
            "performed_at": datetime.now().isoformat()
        }
        
        self.gap_analysis = gaps
        return gaps
    
    def _analyze_cloud_gaps(self) -> List[Dict]:
        """Analyze cloud architecture gaps"""
        gaps = []
        
        # Multi-cloud strategy gap
        if len(self.cloud_providers) < 2:
            gaps.append({
                "gap_type": "multi_cloud",
                "description": "Single cloud provider - consider multi-cloud for resilience",
                "current_providers": self.cloud_providers,
                "target_providers": ["azure", "aws"],
                "priority": "high"
            })
        
        # High availability gap
        ha_platforms = [p for p in self.platforms if p.get("high_availability")]
        if len(ha_platforms) < len(self.platforms):
            gaps.append({
                "gap_type": "high_availability",
                "description": "Some platforms lack high availability configuration",
                "current": len(ha_platforms),
                "target": len(self.platforms),
                "priority": "critical"
            })
        
        return gaps
    
    def _analyze_security_gaps(self) -> List[Dict]:
        """Analyze security architecture gaps"""
        gaps = []
        
        # Required security control types
        required_types = ["network", "identity", "data", "application", "infrastructure"]
        implemented_types = set(c["control_type"] for c in self.security_controls)
        missing_types = set(required_types) - implemented_types
        
        if missing_types:
            gaps.append({
                "gap_type": "security_controls",
                "description": "Missing security control types",
                "missing_controls": list(missing_types),
                "priority": "critical"
            })
        
        # Compliance gaps
        non_compliant = [r for r in self.compliance_requirements if r["status"] != "compliant"]
        if non_compliant:
            gaps.append({
                "gap_type": "compliance",
                "description": "Non-compliant requirements",
                "requirements": [r["standard"] for r in non_compliant],
                "priority": "high"
            })
        
        return gaps
    
    def _analyze_automation_gaps(self) -> Dict:
        """Analyze automation gaps"""
        total_automation = sum(p["automation_level"] for p in self.ci_cd_pipelines)
        avg_automation = total_automation / len(self.ci_cd_pipelines) if self.ci_cd_pipelines else 0
        
        return {
            "current_automation": avg_automation,
            "target_automation": 100.0,
            "gap": 100.0 - avg_automation,
            "iac_coverage": len(self.iac_templates) > 0,
            "monitoring_coverage": len(self.monitoring_tools) >= 3  # Metrics, logs, traces
        }
    
    def _analyze_scalability_gaps(self) -> List[Dict]:
        """Analyze scalability gaps"""
        gaps = []
        
        # Auto-scaling gap
        auto_scaled = [c for c in self.compute_resources if c.get("scaling_type", "manual").startswith("auto_")]
        if len(auto_scaled) < len(self.compute_resources):
            gaps.append({
                "gap_type": "auto_scaling",
                "description": "Some compute resources lack auto-scaling",
                "current": len(auto_scaled),
                "target": len(self.compute_resources),
                "priority": "medium"
            })
        
        return gaps
    
    # ========== Deliverables ==========
    
    def generate_technology_architecture_document(self) -> ArchitectureArtifact:
        """Generate the Technology Architecture Definition Document"""
        content = {
            "executive_summary": {
                "phase": self.phase_type.name,
                "components": len(self.technology_components),
                "cloud_providers": self.cloud_providers,
                "platforms": len(self.platforms)
            },
            "infrastructure_summary": self.get_infrastructure_summary(),
            "cloud_strategy": self.cloud_strategy,
            "compute_resources": self.compute_resources,
            "storage_resources": self.storage_resources,
            "network_resources": self.network_resources,
            "platforms": self.platforms,
            "security_summary": self.get_security_summary(),
            "security_controls": self.security_controls,
            "compliance_requirements": self.compliance_requirements,
            "devops_summary": self.get_devops_summary(),
            "ci_cd_pipelines": self.ci_cd_pipelines,
            "iac_templates": self.iac_templates,
            "monitoring_tools": self.monitoring_tools,
            "baseline_architecture": self.baseline_architecture,
            "target_architecture": self.target_architecture,
            "gap_analysis": self.gap_analysis
        }
        
        artifact = ArchitectureArtifact(
            name="Technology Architecture Definition Document",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Complete technology architecture documentation",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_infrastructure_catalog(self) -> ArchitectureArtifact:
        """Generate Infrastructure Catalog"""
        content = {
            "technology_components": [c.to_dict() for c in self.technology_components],
            "compute_resources": self.compute_resources,
            "storage_resources": self.storage_resources,
            "network_resources": self.network_resources,
            "cloud_services": self.cloud_services,
            "platforms": self.platforms,
            "summary": self.get_infrastructure_summary()
        }
        
        artifact = ArchitectureArtifact(
            name="Infrastructure Catalog",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Complete infrastructure component catalog",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_security_architecture_document(self) -> ArchitectureArtifact:
        """Generate Security Architecture Document"""
        content = {
            "security_controls": self.security_controls,
            "compliance_requirements": self.compliance_requirements,
            "security_summary": self.get_security_summary(),
            "zero_trust_implementation": {
                "identity_controls": [c for c in self.security_controls if c["control_type"] == "identity"],
                "network_controls": [c for c in self.security_controls if c["control_type"] == "network"],
                "data_controls": [c for c in self.security_controls if c["control_type"] == "data"]
            }
        }
        
        artifact = ArchitectureArtifact(
            name="Security Architecture Document",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Complete security architecture and controls",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    # ========== Phase Execution ==========
    
    def validate_phase(self) -> bool:
        """Validate that Phase D has minimum required content"""
        validations = [
            (len(self.technology_components) > 0 or len(self.cloud_services) > 0, 
             "At least one technology component or cloud service required"),
            (len(self.security_controls) > 0, "At least one security control required"),
            (self.baseline_architecture is not None, "Baseline architecture must be defined"),
            (self.target_architecture is not None, "Target architecture must be defined")
        ]
        
        for is_valid, message in validations:
            if not is_valid:
                raise ValidationException(f"Phase D validation failed: {message}")
        
        return True
    
    def execute(self) -> Dict:
        """
        Execute Phase D: Technology Architecture
        
        Returns comprehensive results including infrastructure, security,
        DevOps, gap analysis, and deliverables.
        """
        self.start_phase()
        
        try:
            # Validate prerequisites
            self.validate_phase()
            
            # Generate deliverables
            tech_doc = self.generate_technology_architecture_document()
            infra_catalog = self.generate_infrastructure_catalog()
            security_doc = self.generate_security_architecture_document()
            
            # Complete phase
            self.complete_phase()
            
            results = {
                "phase": self.phase_type.name,
                "status": self.status.name,
                "progress": self.completion_percentage,
                "infrastructure": {
                    "summary": self.get_infrastructure_summary(),
                    "components": [c.to_dict() for c in self.technology_components],
                    "compute": self.compute_resources,
                    "storage": self.storage_resources,
                    "network": self.network_resources,
                    "cloud_services": self.cloud_services,
                    "platforms": self.platforms
                },
                "security": {
                    "summary": self.get_security_summary(),
                    "controls": self.security_controls,
                    "compliance": self.compliance_requirements
                },
                "devops": {
                    "summary": self.get_devops_summary(),
                    "ci_cd": self.ci_cd_pipelines,
                    "iac": self.iac_templates,
                    "monitoring": self.monitoring_tools
                },
                "cloud_strategy": self.cloud_strategy,
                "gap_analysis": self.gap_analysis,
                "deliverables": {
                    "technology_architecture_document": tech_doc.to_dict(),
                    "infrastructure_catalog": infra_catalog.to_dict(),
                    "security_architecture_document": security_doc.to_dict()
                },
                "completed_at": datetime.now().isoformat()
            }
            
            return results
            
        except Exception as e:
            raise
