"""
TOGAF Phase G: Implementation Governance

This module implements Phase G of the TOGAF ADM, focusing on providing
architecture oversight and governance during implementation.

Key Activities:
- Confirm scope and priorities with implementation teams
- Identify deployment resources and skills
- Guide development of solutions deployment
- Perform Enterprise Architecture compliance reviews
- Implement business and IT operations
- Perform post-implementation review and close the implementation

Standards Compliance:
- TOGAF 10 ADM Phase G
- ArchiMate 3.2 Implementation & Migration Layer
- ISO/IEC/IEEE 42010:2011 Architecture Governance
"""

from typing import Dict, List, Optional, Set
from datetime import datetime, date
from enum import Enum

from ..adm.adm_phase import ADMPhase
from ..core.base import ArchitectureElement, Deliverable
from ..core.enums import (
    ArchitectureStatus, RiskLevel, PriorityLevel
)


class PhaseStatus(str, Enum):
    """Status of phase execution"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    APPROVED = "approved"
    COMPLETED = "completed"


class ComplianceStatus(str, Enum):
    """Status of compliance checks"""
    PENDING = "pending"
    COMPLIANT = "compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"


class DeliverableType(str, Enum):
    """Types of deliverables"""
    DOCUMENT = "document"
    REPORT = "report"
    MODEL = "model"
    MATRIX = "matrix"
    CATALOG = "catalog"


class ComplianceType(str, Enum):
    """Types of architecture compliance checks"""
    DESIGN_COMPLIANCE = "design_compliance"
    TECHNICAL_COMPLIANCE = "technical_compliance"
    BUSINESS_COMPLIANCE = "business_compliance"
    SECURITY_COMPLIANCE = "security_compliance"
    DATA_COMPLIANCE = "data_compliance"
    INTEGRATION_COMPLIANCE = "integration_compliance"


class ContractType(str, Enum):
    """Types of architecture contracts"""
    DESIGN_CONTRACT = "design_contract"
    IMPLEMENTATION_CONTRACT = "implementation_contract"
    DEPLOYMENT_CONTRACT = "deployment_contract"
    OPERATIONS_CONTRACT = "operations_contract"


class DeviationType(str, Enum):
    """Types of architecture deviations"""
    TECHNICAL = "technical"
    BUSINESS = "business"
    SECURITY = "security"
    PERFORMANCE = "performance"
    COST = "cost"


class ReviewType(str, Enum):
    """Types of architecture reviews"""
    DESIGN_REVIEW = "design_review"
    CODE_REVIEW = "code_review"
    DEPLOYMENT_REVIEW = "deployment_review"
    POST_IMPLEMENTATION = "post_implementation"


class ArchitectureContract(ArchitectureElement):
    """Formal agreement between development teams and architecture function"""
    
    def __init__(
        self,
        name: str,
        description: str,
        contract_type: ContractType,
        party_a: str,
        party_b: str,
        start_date: date,
        end_date: date
    ):
        super().__init__(name, description)
        self.contract_type = contract_type
        self.party_a = party_a
        self.party_b = party_b
        self.start_date = start_date
        self.end_date = end_date
        self.terms: List[str] = []
        self.obligations: Dict[str, List[str]] = {}
        self.success_criteria: List[str] = []
        self.status = ArchitectureStatus.DRAFT
    
    def add_term(self, term: str):
        """Add contractual term"""
        self.terms.append(term)
    
    def add_obligation(self, party: str, obligation: str):
        """Add party obligation"""
        if party not in self.obligations:
            self.obligations[party] = []
        self.obligations[party].append(obligation)
    
    def add_success_criterion(self, criterion: str):
        """Add success criterion"""
        self.success_criteria.append(criterion)
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'contract_type': self.contract_type.value,
            'party_a': self.party_a,
            'party_b': self.party_b,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'terms': self.terms,
            'obligations': self.obligations,
            'success_criteria': self.success_criteria,
            'status': self.status.value
        }


class ComplianceCheck(ArchitectureElement):
    """Architecture compliance assessment"""
    
    def __init__(
        self,
        name: str,
        description: str,
        compliance_type: ComplianceType,
        target_component: str
    ):
        super().__init__(name, description)
        self.compliance_type = compliance_type
        self.target_component = target_component
        self.review_date: Optional[date] = None
        self.reviewer: Optional[str] = None
        self.status = ComplianceStatus.PENDING
        self.findings: List[str] = []
        self.recommendations: List[str] = []
        self.score: Optional[float] = None  # 0-100
    
    def add_finding(self, finding: str):
        """Add compliance finding"""
        self.findings.append(finding)
    
    def add_recommendation(self, recommendation: str):
        """Add recommendation"""
        self.recommendations.append(recommendation)
    
    def set_result(self, status: ComplianceStatus, score: float):
        """Set compliance result"""
        self.status = status
        self.score = score
        self.review_date = date.today()
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'compliance_type': self.compliance_type.value,
            'target_component': self.target_component,
            'review_date': self.review_date.isoformat() if self.review_date else None,
            'reviewer': self.reviewer,
            'status': self.status.value,
            'findings': self.findings,
            'recommendations': self.recommendations,
            'score': self.score
        }


class ArchitectureDeviation(ArchitectureElement):
    """Deviation from architecture standards"""
    
    def __init__(
        self,
        name: str,
        description: str,
        deviation_type: DeviationType,
        component: str
    ):
        super().__init__(name, description)
        self.deviation_type = deviation_type
        self.component = component
        self.identified_date = date.today()
        self.severity = RiskLevel.MEDIUM
        self.impact: Optional[str] = None
        self.justification: Optional[str] = None
        self.mitigation: Optional[str] = None
        self.approved = False
        self.approved_by: Optional[str] = None
        self.resolution_date: Optional[date] = None
    
    def set_severity(self, severity: RiskLevel, impact: str):
        """Set deviation severity"""
        self.severity = severity
        self.impact = impact
    
    def set_justification(self, justification: str):
        """Set deviation justification"""
        self.justification = justification
    
    def set_mitigation(self, mitigation: str):
        """Set mitigation plan"""
        self.mitigation = mitigation
    
    def approve(self, approver: str):
        """Approve deviation"""
        self.approved = True
        self.approved_by = approver
    
    def resolve(self):
        """Mark deviation as resolved"""
        self.resolution_date = date.today()
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'deviation_type': self.deviation_type.value,
            'component': self.component,
            'identified_date': self.identified_date.isoformat(),
            'severity': self.severity.value,
            'impact': self.impact,
            'justification': self.justification,
            'mitigation': self.mitigation,
            'approved': self.approved,
            'approved_by': self.approved_by,
            'resolution_date': self.resolution_date.isoformat() if self.resolution_date else None
        }


class ImplementationReview(ArchitectureElement):
    """Architecture review during implementation"""
    
    def __init__(
        self,
        name: str,
        description: str,
        review_type: ReviewType,
        project: str
    ):
        super().__init__(name, description)
        self.review_type = review_type
        self.project = project
        self.review_date: Optional[date] = None
        self.reviewers: List[str] = []
        self.attendees: List[str] = []
        self.artifacts_reviewed: List[str] = []
        self.findings: List[Dict[str, str]] = []
        self.decisions: List[str] = []
        self.action_items: List[Dict[str, str]] = []
        self.outcome: Optional[str] = None
    
    def add_reviewer(self, reviewer: str):
        """Add reviewer"""
        self.reviewers.append(reviewer)
    
    def add_attendee(self, attendee: str):
        """Add attendee"""
        self.attendees.append(attendee)
    
    def add_artifact(self, artifact: str):
        """Add reviewed artifact"""
        self.artifacts_reviewed.append(artifact)
    
    def add_finding(self, category: str, description: str, severity: str):
        """Add review finding"""
        self.findings.append({
            'category': category,
            'description': description,
            'severity': severity
        })
    
    def add_decision(self, decision: str):
        """Add review decision"""
        self.decisions.append(decision)
    
    def add_action_item(self, action: str, owner: str, due_date: str):
        """Add action item"""
        self.action_items.append({
            'action': action,
            'owner': owner,
            'due_date': due_date,
            'status': 'open'
        })
    
    def set_outcome(self, outcome: str):
        """Set review outcome"""
        self.outcome = outcome
        self.review_date = date.today()
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'review_type': self.review_type.value,
            'project': self.project,
            'review_date': self.review_date.isoformat() if self.review_date else None,
            'reviewers': self.reviewers,
            'attendees': self.attendees,
            'artifacts_reviewed': self.artifacts_reviewed,
            'findings': self.findings,
            'decisions': self.decisions,
            'action_items': self.action_items,
            'outcome': self.outcome
        }


class ImplementationMetrics(ArchitectureElement):
    """Metrics tracking implementation progress"""
    
    def __init__(self, name: str, project: str):
        super().__init__(name, f"Implementation metrics for {project}")
        self.project = project
        self.metrics: Dict[str, float] = {}
        self.targets: Dict[str, float] = {}
        self.trends: Dict[str, List[Dict]] = {}
    
    def set_metric(self, metric_name: str, value: float, target: Optional[float] = None):
        """Set metric value"""
        self.metrics[metric_name] = value
        if target is not None:
            self.targets[metric_name] = target
        
        # Track trend
        if metric_name not in self.trends:
            self.trends[metric_name] = []
        self.trends[metric_name].append({
            'date': date.today().isoformat(),
            'value': value
        })
    
    def get_metric(self, metric_name: str) -> Optional[float]:
        """Get metric value"""
        return self.metrics.get(metric_name)
    
    def get_compliance_rate(self) -> float:
        """Calculate overall compliance rate"""
        if not self.metrics:
            return 0.0
        
        compliant = sum(1 for k, v in self.metrics.items() 
                       if k in self.targets and v >= self.targets[k])
        return (compliant / len(self.targets)) * 100 if self.targets else 0.0
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'project': self.project,
            'metrics': self.metrics,
            'targets': self.targets,
            'trends': self.trends,
            'compliance_rate': self.get_compliance_rate()
        }


class PhaseGImplementationGovernance(ADMPhase):
    """
    Phase G: Implementation Governance
    
    Provides architectural oversight during implementation to ensure
    delivery complies with the defined architecture.
    """
    
    def __init__(self):
        super().__init__(
            name="Phase G: Implementation Governance",
            description="Provide architectural oversight during implementation"
        )
        
        # Core components
        self.architecture_contracts: Dict[str, ArchitectureContract] = {}
        self.compliance_checks: Dict[str, ComplianceCheck] = {}
        self.deviations: Dict[str, ArchitectureDeviation] = {}
        self.reviews: Dict[str, ImplementationReview] = {}
        self.metrics: Dict[str, ImplementationMetrics] = {}
        
        # Governance framework
        self.governance_policies: List[str] = []
        self.review_schedule: Dict[str, str] = {}
        self.escalation_procedures: List[Dict[str, str]] = []
    
    def _initialize_phase(self) -> None:
        """Initialize phase-specific objectives and activities"""
        self.objectives = [
            "Ensure implementation projects comply with target architecture",
            "Perform architecture compliance reviews",
            "Implement architecture contracts with development teams",
            "Manage architecture deviations and changes",
            "Monitor and report on implementation progress",
            "Support solution deployment"
        ]
        
        self.activities = [
            {'name': 'Confirm scope and priorities with implementation teams', 'status': 'pending'},
            {'name': 'Identify deployment resources and skills', 'status': 'pending'},
            {'name': 'Guide development of solutions deployment', 'status': 'pending'},
            {'name': 'Perform Enterprise Architecture compliance reviews', 'status': 'pending'},
            {'name': 'Implement business and IT operations', 'status': 'pending'},
            {'name': 'Perform post-implementation review', 'status': 'pending'}
        ]
    
    def add_architecture_contract(self, contract: ArchitectureContract):
        """Add architecture contract"""
        self.architecture_contracts[contract.id] = contract
    
    def add_compliance_check(self, check: ComplianceCheck):
        """Add compliance check"""
        self.compliance_checks[check.id] = check
    
    def add_deviation(self, deviation: ArchitectureDeviation):
        """Add architecture deviation"""
        self.deviations[deviation.id] = deviation
    
    def add_review(self, review: ImplementationReview):
        """Add implementation review"""
        self.reviews[review.id] = review
    
    def add_metrics(self, metrics: ImplementationMetrics):
        """Add implementation metrics"""
        self.metrics[metrics.id] = metrics
    
    def add_governance_policy(self, policy: str):
        """Add governance policy"""
        self.governance_policies.append(policy)
    
    def schedule_review(self, project: str, schedule: str):
        """Schedule review for project"""
        self.review_schedule[project] = schedule
    
    def add_escalation_procedure(self, trigger: str, action: str, owner: str):
        """Add escalation procedure"""
        self.escalation_procedures.append({
            'trigger': trigger,
            'action': action,
            'owner': owner
        })
    
    def get_compliance_summary(self) -> Dict:
        """Get compliance summary across all checks"""
        if not self.compliance_checks:
            return {'total': 0, 'compliant': 0, 'non_compliant': 0, 'pending': 0}
        
        summary = {
            'total': len(self.compliance_checks),
            'compliant': 0,
            'non_compliant': 0,
            'pending': 0,
            'average_score': 0.0
        }
        
        scores = []
        for check in self.compliance_checks.values():
            if check.status == ComplianceStatus.COMPLIANT:
                summary['compliant'] += 1
            elif check.status == ComplianceStatus.NON_COMPLIANT:
                summary['non_compliant'] += 1
            else:
                summary['pending'] += 1
            
            if check.score is not None:
                scores.append(check.score)
        
        if scores:
            summary['average_score'] = sum(scores) / len(scores)
        
        return summary
    
    def get_deviation_summary(self) -> Dict:
        """Get deviation summary"""
        if not self.deviations:
            return {'total': 0, 'by_severity': {}, 'approved': 0, 'resolved': 0}
        
        summary = {
            'total': len(self.deviations),
            'by_severity': {},
            'approved': 0,
            'resolved': 0
        }
        
        for deviation in self.deviations.values():
            severity = deviation.severity.value
            summary['by_severity'][severity] = summary['by_severity'].get(severity, 0) + 1
            
            if deviation.approved:
                summary['approved'] += 1
            if deviation.resolution_date:
                summary['resolved'] += 1
        
        return summary
    
    def get_metrics_summary(self) -> Dict:
        """Get metrics summary across all projects"""
        if not self.metrics:
            return {'projects': 0, 'metrics': {}}
        
        summary = {
            'projects': len(self.metrics),
            'metrics': {},
            'overall_compliance': 0.0
        }
        
        compliance_rates = []
        for metrics in self.metrics.values():
            compliance_rates.append(metrics.get_compliance_rate())
            
            for metric_name, value in metrics.metrics.items():
                if metric_name not in summary['metrics']:
                    summary['metrics'][metric_name] = {
                        'values': [],
                        'average': 0.0
                    }
                summary['metrics'][metric_name]['values'].append(value)
        
        # Calculate averages
        for metric_name, data in summary['metrics'].items():
            data['average'] = sum(data['values']) / len(data['values'])
        
        if compliance_rates:
            summary['overall_compliance'] = sum(compliance_rates) / len(compliance_rates)
        
        return summary
    
    def execute(self) -> Dict:
        """Execute Phase G"""
        self.status = ArchitectureStatus.IN_PROGRESS
        
        results = {
            'phase': self.name,
            'status': self.status.value,
            'execution_date': datetime.now().isoformat(),
            'contracts': {k: v.to_dict() for k, v in self.architecture_contracts.items()},
            'compliance_checks': {k: v.to_dict() for k, v in self.compliance_checks.items()},
            'deviations': {k: v.to_dict() for k, v in self.deviations.items()},
            'reviews': {k: v.to_dict() for k, v in self.reviews.items()},
            'metrics': {k: v.to_dict() for k, v in self.metrics.items()},
            'governance_framework': {
                'policies': self.governance_policies,
                'review_schedule': self.review_schedule,
                'escalation_procedures': self.escalation_procedures
            },
            'summaries': {
                'compliance': self.get_compliance_summary(),
                'deviations': self.get_deviation_summary(),
                'metrics': self.get_metrics_summary()
            }
        }
        
        # Check if phase objectives met
        compliance_summary = self.get_compliance_summary()
        if compliance_summary.get('average_score', 0) >= 80:
            self.status = ArchitectureStatus.APPROVED
        
        results['status'] = self.status.value
        results['completion_percentage'] = 100.0
        
        return results
    
    def generate_implementation_oversight_report(self) -> Deliverable:
        """Generate Implementation Oversight Report"""
        content = {
            'contracts': len(self.architecture_contracts),
            'compliance_checks': len(self.compliance_checks),
            'deviations': len(self.deviations),
            'reviews': len(self.reviews),
            'compliance_summary': self.get_compliance_summary(),
            'deviation_summary': self.get_deviation_summary(),
            'metrics_summary': self.get_metrics_summary()
        }
        
        return Deliverable(
            name="Implementation Oversight Report",
            description="Comprehensive oversight report for architecture implementation",
            deliverable_type=DeliverableType.REPORT,
            content=content
        )
    
    def generate_compliance_assessment_report(self) -> Deliverable:
        """Generate Compliance Assessment Report"""
        content = {
            'compliance_checks': {k: v.to_dict() for k, v in self.compliance_checks.items()},
            'summary': self.get_compliance_summary(),
            'recommendations': []
        }
        
        # Add recommendations based on findings
        for check in self.compliance_checks.values():
            if check.status == ComplianceStatus.NON_COMPLIANT:
                content['recommendations'].extend(check.recommendations)
        
        return Deliverable(
            name="Compliance Assessment Report",
            description="Architecture compliance assessment findings and recommendations",
            deliverable_type=DeliverableType.REPORT,
            content=content
        )
    
    def generate_architecture_contract_documentation(self) -> Deliverable:
        """Generate Architecture Contract Documentation"""
        content = {
            'contracts': {k: v.to_dict() for k, v in self.architecture_contracts.items()},
            'active_contracts': sum(1 for c in self.architecture_contracts.values() 
                                   if c.status == ArchitectureStatus.APPROVED),
            'total_obligations': sum(len(c.obligations) for c in self.architecture_contracts.values())
        }
        
        return Deliverable(
            name="Architecture Contract Documentation",
            description="Formal architecture contracts with development teams",
            deliverable_type=DeliverableType.DOCUMENT,
            content=content
        )
