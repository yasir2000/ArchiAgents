"""
TOGAF ADM Phase E: Opportunities & Solutions

This module implements Phase E of the TOGAF Architecture Development Method (ADM).
Phase E focuses on identifying solution alternatives and planning the implementation:
- Solution building blocks (SBBs)
- Work packages and projects
- Implementation and migration strategy
- Transition architectures
- Cost-benefit analysis

Reference: TOGAF 10 ADM Phase E
"""

from typing import List, Dict, Optional
from datetime import datetime
import uuid
from ..core.base import ArchitectureElement
from ..core.enums import (
    ADMPhaseType,
    PriorityLevel
)
from ..core.exceptions import ValidationException
from .adm_phase import ADMPhase
from ..models.artifact import ArchitectureArtifact


class PhaseEOpportunitiesAndSolutions(ADMPhase):
    """
    Phase E: Opportunities and Solutions
    
    Evaluates implementation approaches, identifies solution building blocks,
    and defines work packages for architecture implementation.
    
    Key Activities:
    1. Determine/confirm key corporate change attributes
    2. Determine business constraints for implementation
    3. Review and consolidate gap analysis results
    4. Review consolidated requirements
    5. Consolidate and reconcile interoperability requirements
    6. Refine and validate dependencies
    7. Confirm readiness and risk for business transformation
    8. Formulate implementation and migration strategy
    9. Identify and group major work packages
    """
    
    phase_type = ADMPhaseType.PHASE_E
    
    def __init__(self, name: str = "Opportunities and Solutions", **kwargs):
        super().__init__(name, **kwargs)
        
        # Solution Building Blocks
        self.solution_building_blocks: List[Dict] = []
        self.work_packages: List[Dict] = []
        self.projects: List[Dict] = []
        
        # Implementation Strategy
        self.implementation_strategy: Optional[Dict] = None
        self.migration_approach: Optional[str] = None  # big_bang, phased, parallel
        
        # Transition Architectures
        self.transition_architectures: List[Dict] = []
        
        # Constraints and Dependencies
        self.business_constraints: List[Dict] = []
        self.technical_constraints: List[Dict] = []
        self.dependencies: List[Dict] = []
        
        # Risk and Readiness
        self.implementation_risks: List[Dict] = []
        self.readiness_assessments: List[Dict] = []
        
        # Cost-Benefit Analysis
        self.cost_estimates: List[Dict] = []
        self.benefit_estimates: List[Dict] = []
        self.roi_analysis: Optional[Dict] = None
        
        # Consolidated Gap Analysis
        self.consolidated_gaps: List[Dict] = []
    
    def _initialize_phase(self) -> None:
        """Initialize Phase E - called by base class"""
        self._initialize_objectives()
        self._initialize_activities()
    
    def _generate_id(self) -> str:
        """Generate a unique ID"""
        return str(uuid.uuid4())
    
    def _initialize_objectives(self):
        """Initialize Phase E standard objectives"""
        objectives = [
            "Identify solution building blocks to implement target architecture",
            "Define work packages and implementation projects",
            "Establish implementation and migration strategy",
            "Define transition architectures",
            "Assess implementation risks and organizational readiness",
            "Perform cost-benefit analysis",
            "Prioritize initiatives based on business value"
        ]
        for objective in objectives:
            self.add_objective(objective)
    
    def _initialize_activities(self):
        """Initialize Phase E standard activities"""
        activities = [
            {
                "name": "Determine Key Corporate Change Attributes",
                "description": "Identify organizational change capabilities and constraints",
                "sequence": 1
            },
            {
                "name": "Determine Business Constraints",
                "description": "Document business constraints for implementation",
                "sequence": 2
            },
            {
                "name": "Review Gap Analysis Results",
                "description": "Consolidate gaps from previous phases",
                "sequence": 3
            },
            {
                "name": "Review Consolidated Requirements",
                "description": "Review all architecture requirements",
                "sequence": 4
            },
            {
                "name": "Consolidate Interoperability Requirements",
                "description": "Identify and reconcile integration requirements",
                "sequence": 5
            },
            {
                "name": "Refine and Validate Dependencies",
                "description": "Identify and validate solution dependencies",
                "sequence": 6
            },
            {
                "name": "Confirm Readiness and Risk",
                "description": "Assess organizational readiness and implementation risks",
                "sequence": 7
            },
            {
                "name": "Formulate Implementation Strategy",
                "description": "Define implementation and migration strategy",
                "sequence": 8
            },
            {
                "name": "Identify Major Work Packages",
                "description": "Group solutions into work packages and projects",
                "sequence": 9
            }
        ]
        for activity in activities:
            self.add_activity(
                activity["name"],
                activity["description"],
                activity["sequence"]
            )
    
    # ========== Solution Building Blocks ==========
    
    def add_solution_building_block(
        self,
        name: str,
        description: str,
        sbb_type: str,  # custom_development, cots, saas, open_source, cloud_service
        category: str,  # application, data, technology, security
        implementation_effort: str,  # low, medium, high
        cost_estimate: float,
        timeframe_months: int,
        dependencies: Optional[List[str]] = None
    ) -> None:
        """Add a solution building block"""
        sbb = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "type": sbb_type,
            "category": category,
            "implementation_effort": implementation_effort,
            "cost_estimate": cost_estimate,
            "timeframe_months": timeframe_months,
            "dependencies": dependencies or [],
            "created_at": datetime.now().isoformat()
        }
        
        self.solution_building_blocks.append(sbb)
    
    # ========== Work Packages & Projects ==========
    
    def add_work_package(
        self,
        name: str,
        description: str,
        objectives: List[str],
        solution_blocks: List[str],
        priority: str,  # critical, high, medium, low
        estimated_cost: float,
        estimated_duration_months: int,
        resource_requirements: Dict,
        dependencies: Optional[List[str]] = None
    ) -> None:
        """Add a work package"""
        work_package = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "objectives": objectives,
            "solution_blocks": solution_blocks,
            "priority": priority,
            "estimated_cost": estimated_cost,
            "estimated_duration_months": estimated_duration_months,
            "resource_requirements": resource_requirements,
            "dependencies": dependencies or [],
            "created_at": datetime.now().isoformat()
        }
        
        self.work_packages.append(work_package)
    
    def add_project(
        self,
        name: str,
        description: str,
        work_packages: List[str],
        start_date: str,
        end_date: str,
        budget: float,
        business_value: str,  # high, medium, low
        strategic_alignment: str,
        success_criteria: List[str]
    ) -> None:
        """Add an implementation project"""
        project = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "work_packages": work_packages,
            "start_date": start_date,
            "end_date": end_date,
            "budget": budget,
            "business_value": business_value,
            "strategic_alignment": strategic_alignment,
            "success_criteria": success_criteria,
            "created_at": datetime.now().isoformat()
        }
        
        self.projects.append(project)
    
    # ========== Implementation Strategy ==========
    
    def define_implementation_strategy(
        self,
        approach: str,  # big_bang, phased, parallel, pilot
        rationale: str,
        phases: List[Dict],
        critical_success_factors: List[str],
        governance_approach: str
    ) -> None:
        """Define the implementation and migration strategy"""
        self.implementation_strategy = {
            "approach": approach,
            "rationale": rationale,
            "phases": phases,
            "critical_success_factors": critical_success_factors,
            "governance_approach": governance_approach,
            "defined_at": datetime.now().isoformat()
        }
        self.migration_approach = approach
    
    # ========== Transition Architectures ==========
    
    def add_transition_architecture(
        self,
        name: str,
        description: str,
        version: str,
        timeframe: str,
        capabilities_delivered: List[str],
        architecture_state: Dict,
        dependencies: Optional[List[str]] = None
    ) -> None:
        """Add a transition architecture state"""
        transition = {
            "id": self._generate_id(),
            "name": name,
            "description": description,
            "version": version,
            "timeframe": timeframe,
            "capabilities_delivered": capabilities_delivered,
            "architecture_state": architecture_state,
            "dependencies": dependencies or [],
            "created_at": datetime.now().isoformat()
        }
        
        self.transition_architectures.append(transition)
    
    # ========== Constraints ==========
    
    def add_business_constraint(
        self,
        constraint_type: str,  # budget, time, resource, regulatory, organizational
        description: str,
        impact: str,  # high, medium, low
        mitigation: str
    ) -> None:
        """Add a business constraint"""
        constraint = {
            "id": self._generate_id(),
            "type": constraint_type,
            "description": description,
            "impact": impact,
            "mitigation": mitigation,
            "created_at": datetime.now().isoformat()
        }
        
        self.business_constraints.append(constraint)
    
    def add_technical_constraint(
        self,
        constraint_type: str,  # technology, integration, performance, security
        description: str,
        impact: str,
        mitigation: str
    ) -> None:
        """Add a technical constraint"""
        constraint = {
            "id": self._generate_id(),
            "type": constraint_type,
            "description": description,
            "impact": impact,
            "mitigation": mitigation,
            "created_at": datetime.now().isoformat()
        }
        
        self.technical_constraints.append(constraint)
    
    def add_dependency(
        self,
        from_component: str,
        to_component: str,
        dependency_type: str,  # technical, business, data, temporal
        description: str,
        criticality: str  # critical, high, medium, low
    ) -> None:
        """Add a dependency between components"""
        dependency = {
            "id": self._generate_id(),
            "from": from_component,
            "to": to_component,
            "type": dependency_type,
            "description": description,
            "criticality": criticality,
            "created_at": datetime.now().isoformat()
        }
        
        self.dependencies.append(dependency)
    
    # ========== Risk and Readiness ==========
    
    def add_implementation_risk(
        self,
        risk_name: str,
        category: str,  # technical, organizational, financial, external
        description: str,
        probability: str,  # high, medium, low
        impact: str,  # high, medium, low
        mitigation_strategy: str,
        owner: str
    ) -> None:
        """Add an implementation risk"""
        risk = {
            "id": self._generate_id(),
            "name": risk_name,
            "category": category,
            "description": description,
            "probability": probability,
            "impact": impact,
            "risk_score": self._calculate_risk_score(probability, impact),
            "mitigation_strategy": mitigation_strategy,
            "owner": owner,
            "created_at": datetime.now().isoformat()
        }
        
        self.implementation_risks.append(risk)
    
    def _calculate_risk_score(self, probability: str, impact: str) -> int:
        """Calculate risk score from probability and impact"""
        scores = {"low": 1, "medium": 2, "high": 3}
        return scores.get(probability, 1) * scores.get(impact, 1)
    
    def add_readiness_assessment(
        self,
        area: str,  # organizational, technical, cultural, financial
        current_state: str,
        target_state: str,
        gap_description: str,
        readiness_level: str,  # ready, needs_improvement, not_ready
        actions_required: List[str]
    ) -> None:
        """Add a readiness assessment"""
        assessment = {
            "id": self._generate_id(),
            "area": area,
            "current_state": current_state,
            "target_state": target_state,
            "gap_description": gap_description,
            "readiness_level": readiness_level,
            "actions_required": actions_required,
            "created_at": datetime.now().isoformat()
        }
        
        self.readiness_assessments.append(assessment)
    
    # ========== Cost-Benefit Analysis ==========
    
    def add_cost_estimate(
        self,
        category: str,  # development, infrastructure, licensing, operations, training
        description: str,
        one_time_cost: float,
        annual_recurring_cost: float,
        year_1_cost: Optional[float] = None
    ) -> None:
        """Add a cost estimate"""
        cost = {
            "id": self._generate_id(),
            "category": category,
            "description": description,
            "one_time_cost": one_time_cost,
            "annual_recurring_cost": annual_recurring_cost,
            "year_1_cost": year_1_cost or (one_time_cost + annual_recurring_cost),
            "created_at": datetime.now().isoformat()
        }
        
        self.cost_estimates.append(cost)
    
    def add_benefit_estimate(
        self,
        category: str,  # cost_savings, revenue_increase, efficiency_gain, risk_reduction
        description: str,
        annual_value: float,
        timeframe_years: int,
        confidence_level: str  # high, medium, low
    ) -> None:
        """Add a benefit estimate"""
        benefit = {
            "id": self._generate_id(),
            "category": category,
            "description": description,
            "annual_value": annual_value,
            "timeframe_years": timeframe_years,
            "total_value": annual_value * timeframe_years,
            "confidence_level": confidence_level,
            "created_at": datetime.now().isoformat()
        }
        
        self.benefit_estimates.append(benefit)
    
    def calculate_roi_analysis(
        self,
        analysis_period_years: int = 5
    ) -> Dict:
        """Calculate ROI analysis"""
        total_one_time_costs = sum(c["one_time_cost"] for c in self.cost_estimates)
        total_annual_recurring = sum(c["annual_recurring_cost"] for c in self.cost_estimates)
        total_costs = total_one_time_costs + (total_annual_recurring * analysis_period_years)
        
        total_benefits = sum(b["total_value"] for b in self.benefit_estimates)
        
        net_benefit = total_benefits - total_costs
        roi_percentage = (net_benefit / total_costs * 100) if total_costs > 0 else 0
        payback_period = total_one_time_costs / (total_benefits / analysis_period_years) if total_benefits > 0 else 0
        
        self.roi_analysis = {
            "analysis_period_years": analysis_period_years,
            "total_one_time_costs": total_one_time_costs,
            "total_annual_recurring_costs": total_annual_recurring,
            "total_costs": total_costs,
            "total_benefits": total_benefits,
            "net_benefit": net_benefit,
            "roi_percentage": roi_percentage,
            "payback_period_years": payback_period,
            "calculated_at": datetime.now().isoformat()
        }
        
        return self.roi_analysis
    
    # ========== Gap Consolidation ==========
    
    def consolidate_gaps(
        self,
        business_gaps: List[Dict],
        data_gaps: List[Dict],
        application_gaps: List[Dict],
        technology_gaps: List[Dict]
    ) -> None:
        """Consolidate gaps from all architecture domains"""
        self.consolidated_gaps = []
        
        for gap in business_gaps:
            self.consolidated_gaps.append({
                "domain": "business",
                "gap": gap,
                "priority": gap.get("priority", "medium")
            })
        
        for gap in data_gaps:
            self.consolidated_gaps.append({
                "domain": "data",
                "gap": gap,
                "priority": gap.get("priority", "medium")
            })
        
        for gap in application_gaps:
            self.consolidated_gaps.append({
                "domain": "application",
                "gap": gap,
                "priority": gap.get("priority", "medium")
            })
        
        for gap in technology_gaps:
            self.consolidated_gaps.append({
                "domain": "technology",
                "gap": gap,
                "priority": gap.get("priority", "medium")
            })
    
    # ========== Summary and Analysis ==========
    
    def get_solution_summary(self) -> Dict:
        """Get summary of solution building blocks"""
        sbb_by_type = {}
        sbb_by_category = {}
        
        for sbb in self.solution_building_blocks:
            sbb_type = sbb["type"]
            sbb_category = sbb["category"]
            
            sbb_by_type[sbb_type] = sbb_by_type.get(sbb_type, 0) + 1
            sbb_by_category[sbb_category] = sbb_by_category.get(sbb_category, 0) + 1
        
        total_cost = sum(sbb["cost_estimate"] for sbb in self.solution_building_blocks)
        avg_timeframe = sum(sbb["timeframe_months"] for sbb in self.solution_building_blocks) / len(self.solution_building_blocks) if self.solution_building_blocks else 0
        
        return {
            "total_sbbs": len(self.solution_building_blocks),
            "by_type": sbb_by_type,
            "by_category": sbb_by_category,
            "total_estimated_cost": total_cost,
            "average_timeframe_months": avg_timeframe
        }
    
    def get_work_package_summary(self) -> Dict:
        """Get summary of work packages"""
        by_priority = {}
        for wp in self.work_packages:
            priority = wp["priority"]
            by_priority[priority] = by_priority.get(priority, 0) + 1
        
        total_cost = sum(wp["estimated_cost"] for wp in self.work_packages)
        total_duration = sum(wp["estimated_duration_months"] for wp in self.work_packages)
        
        return {
            "total_work_packages": len(self.work_packages),
            "by_priority": by_priority,
            "total_estimated_cost": total_cost,
            "total_estimated_duration_months": total_duration
        }
    
    def get_risk_summary(self) -> Dict:
        """Get summary of implementation risks"""
        high_risks = [r for r in self.implementation_risks if r["risk_score"] >= 6]
        medium_risks = [r for r in self.implementation_risks if 3 <= r["risk_score"] < 6]
        low_risks = [r for r in self.implementation_risks if r["risk_score"] < 3]
        
        by_category = {}
        for risk in self.implementation_risks:
            category = risk["category"]
            by_category[category] = by_category.get(category, 0) + 1
        
        return {
            "total_risks": len(self.implementation_risks),
            "high_risks": len(high_risks),
            "medium_risks": len(medium_risks),
            "low_risks": len(low_risks),
            "by_category": by_category
        }
    
    # ========== Deliverables ==========
    
    def generate_implementation_plan(self) -> ArchitectureArtifact:
        """Generate Implementation and Migration Plan"""
        content = {
            "executive_summary": {
                "phase": self.phase_type.name,
                "approach": self.migration_approach,
                "total_work_packages": len(self.work_packages),
                "total_projects": len(self.projects)
            },
            "implementation_strategy": self.implementation_strategy,
            "transition_architectures": self.transition_architectures,
            "work_package_summary": self.get_work_package_summary(),
            "work_packages": self.work_packages,
            "projects": self.projects,
            "dependencies": self.dependencies,
            "constraints": {
                "business": self.business_constraints,
                "technical": self.technical_constraints
            }
        }
        
        artifact = ArchitectureArtifact(
            name="Implementation and Migration Plan",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Complete implementation strategy and migration plan",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_solution_catalog(self) -> ArchitectureArtifact:
        """Generate Solution Building Blocks Catalog"""
        content = {
            "solution_building_blocks": self.solution_building_blocks,
            "summary": self.get_solution_summary(),
            "consolidated_gaps": self.consolidated_gaps
        }
        
        artifact = ArchitectureArtifact(
            name="Solution Building Blocks Catalog",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Catalog of all solution building blocks",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    def generate_business_case(self) -> ArchitectureArtifact:
        """Generate Business Case and ROI Analysis"""
        content = {
            "cost_estimates": self.cost_estimates,
            "benefit_estimates": self.benefit_estimates,
            "roi_analysis": self.roi_analysis,
            "risk_summary": self.get_risk_summary(),
            "implementation_risks": self.implementation_risks,
            "readiness_assessments": self.readiness_assessments
        }
        
        artifact = ArchitectureArtifact(
            name="Business Case and ROI Analysis",
            artifact_type="catalog",
            phase=self.phase_type.value,
            description="Financial justification and risk assessment",
            content=content
        )
        
        self.add_output(artifact)
        return artifact
    
    # ========== Phase Execution ==========
    
    def validate_phase(self) -> bool:
        """Validate that Phase E has minimum required content"""
        validations = [
            (len(self.solution_building_blocks) > 0, "At least one solution building block required"),
            (len(self.work_packages) > 0, "At least one work package required"),
            (self.implementation_strategy is not None, "Implementation strategy must be defined"),
            (len(self.cost_estimates) > 0, "Cost estimates required"),
            (self.roi_analysis is not None, "ROI analysis must be calculated")
        ]
        
        for is_valid, message in validations:
            if not is_valid:
                raise ValidationException(f"Phase E validation failed: {message}")
        
        return True
    
    def execute(self) -> Dict:
        """
        Execute Phase E: Opportunities and Solutions
        
        Returns comprehensive results including solutions, work packages,
        implementation strategy, risks, and business case.
        """
        self.start_phase()
        
        try:
            # Validate prerequisites
            self.validate_phase()
            
            # Generate deliverables
            impl_plan = self.generate_implementation_plan()
            solution_catalog = self.generate_solution_catalog()
            business_case = self.generate_business_case()
            
            # Complete phase
            self.complete_phase()
            
            results = {
                "phase": self.phase_type.name,
                "status": self.status.name,
                "progress": self.completion_percentage,
                "solutions": {
                    "summary": self.get_solution_summary(),
                    "building_blocks": self.solution_building_blocks
                },
                "work_packages": {
                    "summary": self.get_work_package_summary(),
                    "packages": self.work_packages,
                    "projects": self.projects
                },
                "implementation_strategy": self.implementation_strategy,
                "transition_architectures": self.transition_architectures,
                "constraints": {
                    "business": self.business_constraints,
                    "technical": self.technical_constraints
                },
                "dependencies": self.dependencies,
                "risks": {
                    "summary": self.get_risk_summary(),
                    "risks": self.implementation_risks,
                    "readiness": self.readiness_assessments
                },
                "financial": {
                    "costs": self.cost_estimates,
                    "benefits": self.benefit_estimates,
                    "roi": self.roi_analysis
                },
                "deliverables": {
                    "implementation_plan": impl_plan.to_dict(),
                    "solution_catalog": solution_catalog.to_dict(),
                    "business_case": business_case.to_dict()
                },
                "completed_at": datetime.now().isoformat()
            }
            
            return results
            
        except Exception as e:
            raise
