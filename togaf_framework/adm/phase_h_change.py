"""
TOGAF Phase H: Architecture Change Management

This module implements Phase H of the TOGAF ADM, focusing on ensuring
that architecture changes are managed in a cohesive and architected way.

Key Activities:
- Establish value realization process
- Deploy monitoring tools
- Manage risks
- Provide analysis for architecture change management
- Develop change requirements to meet performance targets
- Manage governance process
- Activate process to implement change

Standards Compliance:
- TOGAF 10 ADM Phase H
- ArchiMate 3.2 Implementation & Migration Layer
- ISO/IEC/IEEE 42010:2011 Architecture Governance
"""

from typing import Dict, List, Optional, Set
from datetime import datetime, date
from enum import Enum

from ..adm.adm_phase import ADMPhase
from ..core.base import ArchitectureElement, Deliverable
from ..core.enums import (
    ArchitectureStatus, RiskLevel, PriorityLevel, ChangeType
)


class ChangeRequestStatus(str, Enum):
    """Status of change requests"""
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    IMPLEMENTED = "implemented"
    CLOSED = "closed"


class ChangeImpact(str, Enum):
    """Impact level of changes"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class MonitoringType(str, Enum):
    """Types of monitoring"""
    TECHNOLOGY = "technology"
    BUSINESS = "business"
    CAPABILITY = "capability"
    PERFORMANCE = "performance"
    COMPLIANCE = "compliance"


class ArchitectureChangeRequest(ArchitectureElement):
    """Request for architecture change"""
    
    def __init__(
        self,
        name: str,
        description: str,
        change_type: ChangeType,
        requestor: str,
        priority: PriorityLevel
    ):
        super().__init__(name, description)
        self.change_type = change_type
        self.requestor = requestor
        self.priority = priority
        self.submitted_date = date.today()
        self.status = ChangeRequestStatus.SUBMITTED
        self.impact_assessment: Optional[str] = None
        self.impact_level = ChangeImpact.MEDIUM
        self.affected_components: List[str] = []
        self.estimated_effort: Optional[str] = None
        self.estimated_cost: Optional[float] = None
        self.benefits: List[str] = []
        self.risks: List[str] = []
        self.approval_date: Optional[date] = None
        self.implementation_date: Optional[date] = None
    
    def assess_impact(self, impact: str, impact_level: ChangeImpact):
        """Assess change impact"""
        self.impact_assessment = impact
        self.impact_level = impact_level
    
    def add_affected_component(self, component: str):
        """Add affected component"""
        self.affected_components.append(component)
    
    def set_estimates(self, effort: str, cost: float):
        """Set effort and cost estimates"""
        self.estimated_effort = effort
        self.estimated_cost = cost
    
    def add_benefit(self, benefit: str):
        """Add expected benefit"""
        self.benefits.append(benefit)
    
    def add_risk(self, risk: str):
        """Add associated risk"""
        self.risks.append(risk)
    
    def approve(self):
        """Approve change request"""
        self.status = ChangeRequestStatus.APPROVED
        self.approval_date = date.today()
    
    def reject(self):
        """Reject change request"""
        self.status = ChangeRequestStatus.REJECTED
    
    def implement(self):
        """Mark as implemented"""
        self.status = ChangeRequestStatus.IMPLEMENTED
        self.implementation_date = date.today()
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'change_type': self.change_type.value,
            'requestor': self.requestor,
            'priority': self.priority.value,
            'submitted_date': self.submitted_date.isoformat(),
            'status': self.status.value,
            'impact_assessment': self.impact_assessment,
            'impact_level': self.impact_level.value,
            'affected_components': self.affected_components,
            'estimated_effort': self.estimated_effort,
            'estimated_cost': self.estimated_cost,
            'benefits': self.benefits,
            'risks': self.risks,
            'approval_date': self.approval_date.isoformat() if self.approval_date else None,
            'implementation_date': self.implementation_date.isoformat() if self.implementation_date else None
        }


class ArchitectureMonitor(ArchitectureElement):
    """Monitor for tracking architecture and environment changes"""
    
    def __init__(
        self,
        name: str,
        description: str,
        monitoring_type: MonitoringType,
        target: str
    ):
        super().__init__(name, description)
        self.monitoring_type = monitoring_type
        self.target = target
        self.active = True
        self.frequency: Optional[str] = None
        self.metrics: List[str] = []
        self.thresholds: Dict[str, float] = {}
        self.alerts: List[Dict[str, str]] = []
        self.observations: List[Dict] = []
    
    def set_frequency(self, frequency: str):
        """Set monitoring frequency"""
        self.frequency = frequency
    
    def add_metric(self, metric: str, threshold: Optional[float] = None):
        """Add monitoring metric"""
        self.metrics.append(metric)
        if threshold is not None:
            self.thresholds[metric] = threshold
    
    def record_observation(self, metric: str, value: float, timestamp: datetime):
        """Record observation"""
        self.observations.append({
            'metric': metric,
            'value': value,
            'timestamp': timestamp.isoformat()
        })
        
        # Check threshold
        if metric in self.thresholds:
            if value > self.thresholds[metric]:
                self.trigger_alert(f"Threshold exceeded for {metric}: {value} > {self.thresholds[metric]}")
    
    def trigger_alert(self, message: str):
        """Trigger monitoring alert"""
        self.alerts.append({
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'resolved': False
        })
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'monitoring_type': self.monitoring_type.value,
            'target': self.target,
            'active': self.active,
            'frequency': self.frequency,
            'metrics': self.metrics,
            'thresholds': self.thresholds,
            'alerts': self.alerts,
            'observations_count': len(self.observations)
        }


class LessonLearned(ArchitectureElement):
    """Lesson learned from architecture implementation"""
    
    def __init__(
        self,
        name: str,
        description: str,
        category: str,
        source_project: str
    ):
        super().__init__(name, description)
        self.category = category
        self.source_project = source_project
        self.date_captured = date.today()
        self.impact: Optional[str] = None
        self.recommendations: List[str] = []
        self.applied_to_projects: List[str] = []
    
    def set_impact(self, impact: str):
        """Set impact description"""
        self.impact = impact
    
    def add_recommendation(self, recommendation: str):
        """Add recommendation based on lesson"""
        self.recommendations.append(recommendation)
    
    def apply_to_project(self, project: str):
        """Mark lesson as applied to project"""
        if project not in self.applied_to_projects:
            self.applied_to_projects.append(project)
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'category': self.category,
            'source_project': self.source_project,
            'date_captured': self.date_captured.isoformat(),
            'impact': self.impact,
            'recommendations': self.recommendations,
            'applied_to_projects': self.applied_to_projects
        }


class KnowledgeAsset(ArchitectureElement):
    """Knowledge asset in architecture repository"""
    
    def __init__(
        self,
        name: str,
        description: str,
        asset_type: str,
        category: str
    ):
        super().__init__(name, description)
        self.asset_type = asset_type  # pattern, template, reference, model
        self.category = category
        self.version = "1.0"
        self.created_date = date.today()
        self.last_updated = date.today()
        self.usage_count = 0
        self.tags: List[str] = []
        self.related_assets: List[str] = []
    
    def increment_usage(self):
        """Increment usage counter"""
        self.usage_count += 1
    
    def add_tag(self, tag: str):
        """Add tag"""
        if tag not in self.tags:
            self.tags.append(tag)
    
    def add_related_asset(self, asset_id: str):
        """Add related asset"""
        if asset_id not in self.related_assets:
            self.related_assets.append(asset_id)
    
    def update_version(self, version: str):
        """Update version"""
        self.version = version
        self.last_updated = date.today()
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **super().to_dict(),
            'asset_type': self.asset_type,
            'category': self.category,
            'version': self.version,
            'created_date': self.created_date.isoformat(),
            'last_updated': self.last_updated.isoformat(),
            'usage_count': self.usage_count,
            'tags': self.tags,
            'related_assets': self.related_assets
        }


class PhaseHChangeManagement(ADMPhase):
    """
    Phase H: Architecture Change Management
    
    Ensures that architecture changes are managed in a cohesive way and
    that the architecture capability meets current requirements.
    """
    
    def __init__(self):
        super().__init__(
            name="Phase H: Architecture Change Management",
            description="Manage architecture changes and continuous improvement"
        )
        
        # Core components
        self.change_requests: Dict[str, ArchitectureChangeRequest] = {}
        self.monitors: Dict[str, ArchitectureMonitor] = {}
        self.lessons_learned: Dict[str, LessonLearned] = {}
        self.knowledge_assets: Dict[str, KnowledgeAsset] = {}
        
        # Change management framework
        self.change_policies: List[str] = []
        self.approval_thresholds: Dict[str, str] = {}
        self.review_cycles: Dict[str, str] = {}
    
    def _initialize_phase(self) -> None:
        """Initialize phase-specific objectives and activities"""
        self.objectives = [
            "Establish value realization process",
            "Deploy monitoring tools and processes",
            "Manage architecture change requests",
            "Assess impact of technology and business changes",
            "Manage governance process",
            "Activate change implementation process",
            "Maintain architecture repository",
            "Capture and apply lessons learned"
        ]
        
        self.activities = [
            {'name': 'Establish value realization process', 'status': 'pending'},
            {'name': 'Deploy monitoring tools', 'status': 'pending'},
            {'name': 'Manage risks', 'status': 'pending'},
            {'name': 'Provide analysis for architecture change management', 'status': 'pending'},
            {'name': 'Develop change requirements', 'status': 'pending'},
            {'name': 'Manage governance process', 'status': 'pending'},
            {'name': 'Activate change implementation process', 'status': 'pending'},
            {'name': 'Maintain knowledge repository', 'status': 'pending'}
        ]
    
    def add_change_request(self, request: ArchitectureChangeRequest):
        """Add architecture change request"""
        self.change_requests[request.id] = request
    
    def add_monitor(self, monitor: ArchitectureMonitor):
        """Add architecture monitor"""
        self.monitors[monitor.id] = monitor
    
    def add_lesson_learned(self, lesson: LessonLearned):
        """Add lesson learned"""
        self.lessons_learned[lesson.id] = lesson
    
    def add_knowledge_asset(self, asset: KnowledgeAsset):
        """Add knowledge asset"""
        self.knowledge_assets[asset.id] = asset
    
    def add_change_policy(self, policy: str):
        """Add change management policy"""
        self.change_policies.append(policy)
    
    def set_approval_threshold(self, impact_level: str, authority: str):
        """Set approval authority for impact level"""
        self.approval_thresholds[impact_level] = authority
    
    def set_review_cycle(self, component: str, cycle: str):
        """Set review cycle for component"""
        self.review_cycles[component] = cycle
    
    def get_change_request_summary(self) -> Dict:
        """Get summary of change requests"""
        if not self.change_requests:
            return {'total': 0, 'by_status': {}, 'by_priority': {}}
        
        summary = {
            'total': len(self.change_requests),
            'by_status': {},
            'by_priority': {},
            'approved': 0,
            'implemented': 0
        }
        
        for request in self.change_requests.values():
            status = request.status.value
            priority = request.priority.value
            
            summary['by_status'][status] = summary['by_status'].get(status, 0) + 1
            summary['by_priority'][priority] = summary['by_priority'].get(priority, 0) + 1
            
            if request.status == ChangeRequestStatus.APPROVED:
                summary['approved'] += 1
            elif request.status == ChangeRequestStatus.IMPLEMENTED:
                summary['implemented'] += 1
        
        return summary
    
    def get_monitoring_summary(self) -> Dict:
        """Get monitoring summary"""
        if not self.monitors:
            return {'total': 0, 'active': 0, 'alerts': 0}
        
        summary = {
            'total': len(self.monitors),
            'active': sum(1 for m in self.monitors.values() if m.active),
            'by_type': {},
            'total_alerts': 0,
            'unresolved_alerts': 0
        }
        
        for monitor in self.monitors.values():
            mon_type = monitor.monitoring_type.value
            summary['by_type'][mon_type] = summary['by_type'].get(mon_type, 0) + 1
            summary['total_alerts'] += len(monitor.alerts)
            summary['unresolved_alerts'] += sum(1 for a in monitor.alerts if not a.get('resolved', False))
        
        return summary
    
    def get_knowledge_summary(self) -> Dict:
        """Get knowledge repository summary"""
        summary = {
            'lessons_learned': len(self.lessons_learned),
            'knowledge_assets': len(self.knowledge_assets),
            'asset_usage': 0
        }
        
        if self.knowledge_assets:
            summary['asset_usage'] = sum(a.usage_count for a in self.knowledge_assets.values())
            summary['by_type'] = {}
            for asset in self.knowledge_assets.values():
                asset_type = asset.asset_type
                summary['by_type'][asset_type] = summary['by_type'].get(asset_type, 0) + 1
        
        return summary
    
    def execute(self) -> Dict:
        """Execute Phase H"""
        self.status = ArchitectureStatus.UNDER_REVIEW
        
        results = {
            'phase': self.name,
            'status': self.status.value,
            'execution_date': datetime.now().isoformat(),
            'change_requests': {k: v.to_dict() for k, v in self.change_requests.items()},
            'monitors': {k: v.to_dict() for k, v in self.monitors.items()},
            'lessons_learned': {k: v.to_dict() for k, v in self.lessons_learned.items()},
            'knowledge_assets': {k: v.to_dict() for k, v in self.knowledge_assets.items()},
            'change_framework': {
                'policies': self.change_policies,
                'approval_thresholds': self.approval_thresholds,
                'review_cycles': self.review_cycles
            },
            'summaries': {
                'change_requests': self.get_change_request_summary(),
                'monitoring': self.get_monitoring_summary(),
                'knowledge': self.get_knowledge_summary()
            }
        }
        
        # Phase completion check
        if len(self.change_requests) > 0 and len(self.monitors) > 0:
            self.status = ArchitectureStatus.APPROVED
        
        results['status'] = self.status.value
        results['completion_percentage'] = 100.0
        
        return results
    
    def generate_change_management_report(self) -> Deliverable:
        """Generate Change Management Report"""
        content = {
            'change_requests': len(self.change_requests),
            'monitors': len(self.monitors),
            'change_summary': self.get_change_request_summary(),
            'monitoring_summary': self.get_monitoring_summary(),
            'lessons_learned': len(self.lessons_learned),
            'knowledge_assets': len(self.knowledge_assets)
        }
        
        return Deliverable(
            name="Architecture Change Management Report",
            phase="Phase H",
            description="Comprehensive report on architecture change management",
            content=content
        )
    
    def generate_lessons_learned_catalog(self) -> Deliverable:
        """Generate Lessons Learned Catalog"""
        content = {
            'lessons': {k: v.to_dict() for k, v in self.lessons_learned.items()},
            'total_lessons': len(self.lessons_learned),
            'lessons_by_category': {}
        }
        
        for lesson in self.lessons_learned.values():
            category = lesson.category
            content['lessons_by_category'][category] = content['lessons_by_category'].get(category, 0) + 1
        
        return Deliverable(
            name="Lessons Learned Catalog",
            phase="Phase H",
            description="Catalog of lessons learned from architecture implementation",
            content=content
        )
    
    def generate_architecture_repository_report(self) -> Deliverable:
        """Generate Architecture Repository Report"""
        content = {
            'knowledge_assets': {k: v.to_dict() for k, v in self.knowledge_assets.items()},
            'summary': self.get_knowledge_summary(),
            'most_used_assets': sorted(
                [(a.name, a.usage_count) for a in self.knowledge_assets.values()],
                key=lambda x: x[1],
                reverse=True
            )[:10] if self.knowledge_assets else []
        }
        
        return Deliverable(
            name="Architecture Repository Report",
            phase="Phase H",
            description="Report on architecture repository contents and usage",
            content=content
        )
