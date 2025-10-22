"""
TOGAF ADM Phase F: Migration Planning

This module implements Phase F of the TOGAF Architecture Development Method (ADM).
Phase F focuses on detailed migration planning and execution roadmap:
- Implementation and migration plan
- Project and portfolio management
- Resource planning and allocation
- Timeline and milestone definition
- Risk mitigation planning

Reference: TOGAF 10 ADM Phase F
"""

from typing import List, Dict, Optional
from datetime import datetime
import uuid
from ..core.base import ArchitectureElement
from ..core.enums import ADMPhaseType, PriorityLevel
from ..core.exceptions import ValidationException
from .adm_phase import ADMPhase
from ..models.artifact import ArchitectureArtifact


class PhaseFMigrationPlanning(ADMPhase):
    """
    Phase F: Migration Planning
    
    Develops detailed implementation and migration plans, addressing the
    logistics of implementing the architecture.
    
    Key Activities:
    1. Confirm management framework interactions
    2. Assign business value to each work package
    3. Estimate resource requirements and availability
    4. Prioritize migration projects
    5. Confirm architecture roadmap and update architecture definition
    6. Generate implementation and migration plan
    7. Complete architecture development cycle documentation
    """
    
    phase_type = ADMPhaseType.PHASE_F
    
    def __init__(self, name: str = "Migration Planning", **kwargs):
        super().__init__(name, **kwargs)
        
        # Migration Planning
        self.migration_projects: List[Dict] = []
        self.project_portfolio: Optional[Dict] = None
        
        # Timeline and Milestones
        self.roadmap: List[Dict] = []
        self.milestones: List[Dict] = []
        self.phases: List[Dict] = []
        
        # Resources
        self.resource_requirements: List[Dict] = []
        self.resource_allocations: List[Dict] = []
        self.resource_pool: List[Dict] = []
        
        # Dependencies and Sequencing
        self.project_dependencies: List[Dict] = []
        self.critical_path: Optional[List[str]] = None
        
        # Value and Prioritization
        self.value_assessments: List[Dict] = []
        self.prioritization_criteria: Optional[Dict] = None
        
        # Risk Management
        self.migration_risks: List[Dict] = []
        self.risk_mitigation_plans: List[Dict] = []
        
        # Change Management
        self.change_initiatives: List[Dict] = []
        self.stakeholder_engagement_plan: Optional[Dict] = None
        
        # Governance
        self.governance_checkpoints: List[Dict] = []
        self.success_metrics: List[Dict] = []
    
    def _initialize_phase(self) -> None:
        """Initialize Phase F - called by base class"""
        self._initialize_objectives()
        self._initialize_activities()
    
    def _generate_id(self) -> str:
        """Generate a unique ID"""
        return str(uuid.uuid4())
    
    def _initialize_objectives(self):
        """Initialize Phase F standard objectives"""
        objectives = [
            "Create detailed implementation and migration plan",
            "Prioritize projects based on business value and dependencies",
            "Allocate resources across migration projects",
            "Define timeline with milestones and checkpoints",
            "Establish governance framework for implementation",
            "Develop risk mitigation strategies",
            "Create change management plan"
        ]
        for objective in objectives:
            self.add_objective(objective)
    
    def _initialize_activities(self):
        """Initialize Phase F standard activities"""
        activities = [
            {
                "name": "Confirm Management Framework Interactions",
                "description": "Align with enterprise management frameworks",
                "sequence": 1
            },
            {
                "name": "Assign Business Value to Work Packages",
                "description": "Quantify business value for prioritization",
                "sequence": 2
            },
            {
                "name": "Estimate Resource Requirements",
                "description": "Detail resource needs for each project",
                "sequence": 3
            },
            {
                "name": "Prioritize Migration Projects",
                "description": "Sequence projects based on value and dependencies",
                "sequence": 4
            },
            {
                "name": "Confirm Architecture Roadmap",
                "description": "Validate and update architecture roadmap",
                "sequence": 5
            },
            {
                "name": "Generate Implementation Plan",
                "description": "Create detailed implementation and migration plan",
                "sequence": 6
            },
            {
                "name": "Complete Architecture Documentation",
                "description": "Finalize all architecture documentation",
                "sequence": 7
            }
        ]
        for activity in activities:
            self.add_activity(
                activity["name"],
                activity["description"],
                activity["sequence"]
            )
    
    # ========== Migration Projects ==========
    
    def add_migration_project(
        self,
        name: str,
        description: str,
        start_date: str,
        end_date: str,
        duration_days: int,
        work_packages: List[str],
        deliverables: List[str],
        dependencies: Optional[List[str]] = None,
        priority: str = "medium",
        budget: float = 0,
        status: str = "planned"
    ) -> None:
        """Add a migration project"""
        project = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "duration_days": duration_days,
            "work_packages": work_packages,
            "deliverables": deliverables,
            "dependencies": dependencies or [],
            "priority": priority,
            "budget": budget,
            "status": status,
            "created_at": datetime.now().isoformat()
        }
        
        self.migration_projects.append(project)
    
    def define_project_portfolio(
        self,
        total_budget: float,
        timeframe_months: int,
        strategic_themes: List[str],
        constraints: List[str]
    ) -> None:
        """Define the overall project portfolio"""
        self.project_portfolio = {
            "total_budget": total_budget,
            "timeframe_months": timeframe_months,
            "strategic_themes": strategic_themes,
            "constraints": constraints,
            "total_projects": len(self.migration_projects),
            "defined_at": datetime.now().isoformat()
        }
    
    # ========== Timeline and Milestones ==========
    
    def add_roadmap_phase(
        self,
        phase_name: str,
        description: str,
        start_date: str,
        end_date: str,
        duration_months: int,
        objectives: List[str],
        key_deliverables: List[str],
        success_criteria: List[str]
    ) -> None:
        """Add a phase to the architecture roadmap"""
        phase = {
            "id": self._generate_id(),
            "name": phase_name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "duration_months": duration_months,
            "objectives": objectives,
            "key_deliverables": key_deliverables,
            "success_criteria": success_criteria,
            "created_at": datetime.now().isoformat()
        }
        
        self.phases.append(phase)
        self.roadmap.append(phase)
    
    def add_milestone(
        self,
        name: str,
        description: str,
        target_date: str,
        milestone_type: str,  # project, phase, governance, business
        deliverables: List[str],
        success_criteria: List[str],
        owner: str
    ) -> None:
        """Add a milestone"""
        milestone = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "target_date": target_date,
            "type": milestone_type,
            "deliverables": deliverables,
            "success_criteria": success_criteria,
            "owner": owner,
            "created_at": datetime.now().isoformat()
        }
        
        self.milestones.append(milestone)
    
    # ========== Resource Management ==========
    
    def add_resource_requirement(
        self,
        project_name: str,
        role: str,
        required_count: int,
        skill_level: str,  # junior, mid, senior, expert
        start_date: str,
        end_date: str,
        allocation_percentage: float = 100.0
    ) -> None:
        """Add resource requirement for a project"""
        requirement = {
            "id": self._generate_id(),
            "project_name": project_name,
            "role": role,
            "required_count": required_count,
            "skill_level": skill_level,
            "start_date": start_date,
            "end_date": end_date,
            "allocation_percentage": allocation_percentage,
            "created_at": datetime.now().isoformat()
        }
        
        self.resource_requirements.append(requirement)
    
    def add_resource_allocation(
        self,
        resource_name: str,
        role: str,
        project_name: str,
        start_date: str,
        end_date: str,
        allocation_percentage: float
    ) -> None:
        """Allocate a specific resource to a project"""
        allocation = {
            "id": self._generate_id(),
            "resource_name": resource_name,
            "role": role,
            "project_name": project_name,
            "start_date": start_date,
            "end_date": end_date,
            "allocation_percentage": allocation_percentage,
            "created_at": datetime.now().isoformat()
        }
        
        self.resource_allocations.append(allocation)
    
    def add_resource_to_pool(
        self,
        name: str,
        role: str,
        skill_level: str,
        availability_percentage: float = 100.0,
        cost_per_day: float = 0
    ) -> None:
        """Add a resource to the resource pool"""
        resource = {
            "id": self._generate_id(),
            "name": name,
            "role": role,
            "skill_level": skill_level,
            "availability_percentage": availability_percentage,
            "cost_per_day": cost_per_day,
            "created_at": datetime.now().isoformat()
        }
        
        self.resource_pool.append(resource)
    
    # ========== Dependencies and Sequencing ==========
    
    def add_project_dependency(
        self,
        from_project: str,
        to_project: str,
        dependency_type: str,  # finish_to_start, start_to_start, finish_to_finish
        lag_days: int = 0,
        description: str = ""
    ) -> None:
        """Add dependency between projects"""
        dependency = {
            "id": self._generate_id(),
            "from_project": from_project,
            "to_project": to_project,
            "type": dependency_type,
            "lag_days": lag_days,
            "description": description,
            "created_at": datetime.now().isoformat()
        }
        
        self.project_dependencies.append(dependency)
    
    def calculate_critical_path(self) -> List[str]:
        """Calculate critical path through project network"""
        # Simplified critical path - in real implementation would use proper algorithm
        critical_projects = []
        for project in sorted(self.migration_projects, key=lambda x: x["start_date"]):
            if project["priority"] == "critical" or len(project["dependencies"]) > 0:
                critical_projects.append(project["name"])
        
        self.critical_path = critical_projects
        return critical_projects
    
    # ========== Value and Prioritization ==========
    
    def add_value_assessment(
        self,
        project_name: str,
        business_value_score: int,  # 1-10
        strategic_alignment_score: int,  # 1-10
        risk_reduction_score: int,  # 1-10
        implementation_complexity: int,  # 1-10 (higher = more complex)
        total_value_score: Optional[int] = None
    ) -> None:
        """Add value assessment for a project"""
        if total_value_score is None:
            # Calculate weighted average
            total_value_score = (
                (business_value_score * 0.4) +
                (strategic_alignment_score * 0.3) +
                (risk_reduction_score * 0.2) -
                (implementation_complexity * 0.1)
            )
        
        assessment = {
            "id": self._generate_id(),
            "project_name": project_name,
            "business_value_score": business_value_score,
            "strategic_alignment_score": strategic_alignment_score,
            "risk_reduction_score": risk_reduction_score,
            "implementation_complexity": implementation_complexity,
            "total_value_score": round(total_value_score, 2),
            "created_at": datetime.now().isoformat()
        }
        
        self.value_assessments.append(assessment)
    
    def define_prioritization_criteria(
        self,
        criteria: List[Dict[str, float]]
    ) -> None:
        """Define criteria for project prioritization with weights"""
        total_weight = sum(c["weight"] for c in criteria)
        if abs(total_weight - 1.0) > 0.01:
            raise ValidationException(f"Criteria weights must sum to 1.0, got {total_weight}")
        
        self.prioritization_criteria = {
            "criteria": criteria,
            "defined_at": datetime.now().isoformat()
        }
    
    # ========== Risk Management ==========
    
    def add_migration_risk(
        self,
        risk_name: str,
        category: str,
        affected_projects: List[str],
        probability: str,  # low, medium, high
        impact: str,  # low, medium, high
        mitigation_plan: str,
        owner: str
    ) -> None:
        """Add migration-specific risk"""
        risk = {
            "id": self._generate_id(),
            "name": risk_name,
            "category": category,
            "affected_projects": affected_projects,
            "probability": probability,
            "impact": impact,
            "risk_score": self._calculate_risk_score(probability, impact),
            "mitigation_plan": mitigation_plan,
            "owner": owner,
            "created_at": datetime.now().isoformat()
        }
        
        self.migration_risks.append(risk)
    
    def _calculate_risk_score(self, probability: str, impact: str) -> int:
        """Calculate risk score"""
        scores = {"low": 1, "medium": 2, "high": 3}
        return scores.get(probability, 1) * scores.get(impact, 1)
    
    def add_risk_mitigation_plan(
        self,
        risk_name: str,
        mitigation_actions: List[str],
        contingency_plan: str,
        responsible_party: str,
        target_date: str,
        budget: float = 0
    ) -> None:
        """Add detailed risk mitigation plan"""
        plan = {
            "id": self._generate_id(),
            "risk_name": risk_name,
            "mitigation_actions": mitigation_actions,
            "contingency_plan": contingency_plan,
            "responsible_party": responsible_party,
            "target_date": target_date,
            "budget": budget,
            "created_at": datetime.now().isoformat()
        }
        
        self.risk_mitigation_plans.append(plan)
    
    # ========== Change Management ==========
    
    def add_change_initiative(
        self,
        name: str,
        description: str,
        target_audience: str,
        change_type: str,  # process, technology, organizational, cultural
        impact_level: str,  # low, medium, high
        activities: List[str],
        timeline: str,
        success_metrics: List[str]
    ) -> None:
        """Add change management initiative"""
        initiative = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "target_audience": target_audience,
            "type": change_type,
            "impact_level": impact_level,
            "activities": activities,
            "timeline": timeline,
            "success_metrics": success_metrics,
            "created_at": datetime.now().isoformat()
        }
        
        self.change_initiatives.append(initiative)
    
    def define_stakeholder_engagement_plan(
        self,
        stakeholder_groups: List[Dict],
        communication_approach: str,
        engagement_frequency: str,
        feedback_mechanisms: List[str]
    ) -> None:
        """Define stakeholder engagement plan"""
        self.stakeholder_engagement_plan = {
            "stakeholder_groups": stakeholder_groups,
            "communication_approach": communication_approach,
            "engagement_frequency": engagement_frequency,
            "feedback_mechanisms": feedback_mechanisms,
            "defined_at": datetime.now().isoformat()
        }
    
    # ========== Governance ==========
    
    def add_governance_checkpoint(
        self,
        name: str,
        checkpoint_type: str,  # phase_gate, milestone_review, architecture_review
        date: str,
        scope: str,
        approval_criteria: List[str],
        approvers: List[str]
    ) -> None:
        """Add governance checkpoint"""
        checkpoint = {
            "id": self._generate_id(),
            "name": name,
            "type": checkpoint_type,
            "date": date,
            "scope": scope,
            "approval_criteria": approval_criteria,
            "approvers": approvers,
            "created_at": datetime.now().isoformat()
        }
        
        self.governance_checkpoints.append(checkpoint)
    
    def add_success_metric(
        self,
        metric_name: str,
        description: str,
        category: str,  # quality, schedule, cost, business_value
        target_value: str,
        measurement_method: str,
        frequency: str
    ) -> None:
        """Add success metric"""
        metric = {
            "id": self._generate_id(),
            "name": metric_name,
            "description": description,
            "category": category,
            "target_value": target_value,
            "measurement_method": measurement_method,
            "frequency": frequency,
            "created_at": datetime.now().isoformat()
        }
        
        self.success_metrics.append(metric)
    
    # ========== Summary and Analysis ==========
    
    def get_project_summary(self) -> Dict:
        """Get summary of migration projects"""
        by_status = {}
        by_priority = {}
        total_budget = 0
        
        for project in self.migration_projects:
            status = project["status"]
            priority = project["priority"]
            by_status[status] = by_status.get(status, 0) + 1
            by_priority[priority] = by_priority.get(priority, 0) + 1
            total_budget += project.get("budget", 0)
        
        return {
            "total_projects": len(self.migration_projects),
            "by_status": by_status,
            "by_priority": by_priority,
            "total_budget": total_budget
        }
    
    def get_resource_summary(self) -> Dict:
        """Get summary of resource requirements and allocations"""
        total_requirements = len(self.resource_requirements)
        total_allocations = len(self.resource_allocations)
        pool_size = len(self.resource_pool)
        
        return {
            "total_requirements": total_requirements,
            "total_allocations": total_allocations,
            "resource_pool_size": pool_size,
            "allocation_rate": (total_allocations / total_requirements * 100) if total_requirements > 0 else 0
        }
    
    def get_timeline_summary(self) -> Dict:
        """Get summary of timeline and milestones"""
        return {
            "total_phases": len(self.phases),
            "total_milestones": len(self.milestones),
            "governance_checkpoints": len(self.governance_checkpoints),
            "critical_path_length": len(self.critical_path) if self.critical_path else 0
        }
    
    def get_risk_summary(self) -> Dict:
        """Get summary of migration risks"""
        high_risks = [r for r in self.migration_risks if r["risk_score"] >= 6]
        medium_risks = [r for r in self.migration_risks if 3 <= r["risk_score"] < 6]
        low_risks = [r for r in self.migration_risks if r["risk_score"] < 3]
        
        return {
            "total_risks": len(self.migration_risks),
            "high_risks": len(high_risks),
            "medium_risks": len(medium_risks),
            "low_risks": len(low_risks),
            "mitigation_plans": len(self.risk_mitigation_plans)
        }
    
    # ========== Deliverables ==========
    
    def generate_migration_plan(self) -> ArchitectureArtifact:
        """Generate Implementation and Migration Plan"""
        content = {
            "executive_summary": {
                "phase": self.phase_type.name,
                "total_projects": len(self.migration_projects),
                "timeframe_months": self.project_portfolio.get("timeframe_months") if self.project_portfolio else 0,
                "total_budget": self.project_portfolio.get("total_budget") if self.project_portfolio else 0
            },
            "project_portfolio": self.project_portfolio,
            "migration_projects": self.migration_projects,
            "project_summary": self.get_project_summary(),
            "roadmap": self.roadmap,
            "milestones": self.milestones,
            "dependencies": self.project_dependencies,
            "critical_path": self.critical_path,
            "value_assessments": self.value_assessments,
            "timeline_summary": self.get_timeline_summary()
        }
        
        artifact = ArchitectureArtifact(
            name="Implementation and Migration Plan",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Detailed implementation and migration plan with timeline",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_resource_plan(self) -> ArchitectureArtifact:
        """Generate Resource Plan"""
        content = {
            "resource_requirements": self.resource_requirements,
            "resource_allocations": self.resource_allocations,
            "resource_pool": self.resource_pool,
            "summary": self.get_resource_summary()
        }
        
        artifact = ArchitectureArtifact(
            name="Resource Plan",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Comprehensive resource planning and allocation",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_governance_plan(self) -> ArchitectureArtifact:
        """Generate Governance and Risk Management Plan"""
        content = {
            "governance_checkpoints": self.governance_checkpoints,
            "success_metrics": self.success_metrics,
            "migration_risks": self.migration_risks,
            "risk_mitigation_plans": self.risk_mitigation_plans,
            "risk_summary": self.get_risk_summary(),
            "change_initiatives": self.change_initiatives,
            "stakeholder_engagement": self.stakeholder_engagement_plan
        }
        
        artifact = ArchitectureArtifact(
            name="Governance and Risk Management Plan",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Governance framework and risk management approach",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    # ========== Phase Execution ==========
    
    def validate_phase(self) -> bool:
        """Validate that Phase F has minimum required content"""
        validations = [
            (len(self.migration_projects) > 0, "At least one migration project required"),
            (len(self.roadmap) > 0, "Architecture roadmap must be defined"),
            (len(self.milestones) > 0, "At least one milestone required"),
            (self.project_portfolio is not None, "Project portfolio must be defined")
        ]
        
        for is_valid, message in validations:
            if not is_valid:
                raise ValidationException(f"Phase F validation failed: {message}")
        
        return True
    
    def execute(self) -> Dict:
        """
        Execute Phase F: Migration Planning
        
        Returns comprehensive results including migration plan, resources,
        timeline, risks, and governance.
        """
        self.start_phase()
        
        try:
            # Validate prerequisites
            self.validate_phase()
            
            # Calculate critical path
            if not self.critical_path:
                self.calculate_critical_path()
            
            # Generate deliverables
            migration_plan = self.generate_migration_plan()
            resource_plan = self.generate_resource_plan()
            governance_plan = self.generate_governance_plan()
            
            # Complete phase
            self.complete_phase()
            
            results = {
                "phase": self.phase_type.name,
                "status": self.status.name,
                "progress": self.completion_percentage,
                "projects": {
                    "summary": self.get_project_summary(),
                    "projects": self.migration_projects,
                    "portfolio": self.project_portfolio
                },
                "timeline": {
                    "summary": self.get_timeline_summary(),
                    "roadmap": self.roadmap,
                    "milestones": self.milestones,
                    "critical_path": self.critical_path
                },
                "resources": {
                    "summary": self.get_resource_summary(),
                    "requirements": self.resource_requirements,
                    "allocations": self.resource_allocations,
                    "pool": self.resource_pool
                },
                "dependencies": self.project_dependencies,
                "value_assessments": self.value_assessments,
                "risks": {
                    "summary": self.get_risk_summary(),
                    "risks": self.migration_risks,
                    "mitigation_plans": self.risk_mitigation_plans
                },
                "governance": {
                    "checkpoints": self.governance_checkpoints,
                    "success_metrics": self.success_metrics
                },
                "change_management": {
                    "initiatives": self.change_initiatives,
                    "stakeholder_engagement": self.stakeholder_engagement_plan
                },
                "deliverables": {
                    "migration_plan": migration_plan.to_dict(),
                    "resource_plan": resource_plan.to_dict(),
                    "governance_plan": governance_plan.to_dict()
                },
                "completed_at": datetime.now().isoformat()
            }
            
            return results
            
        except Exception as e:
            raise
