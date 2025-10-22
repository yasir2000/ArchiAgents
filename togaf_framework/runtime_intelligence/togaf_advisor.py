"""
TOGAF Phase Advisor

Provides phase-specific intelligent recommendations for TOGAF ADM phases.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from enum import Enum
from datetime import datetime


class TOGAFPhase(Enum):
    """TOGAF ADM Phases"""
    PRELIMINARY = "preliminary"
    PHASE_A = "phase_a"  # Architecture Vision
    PHASE_B = "phase_b"  # Business Architecture
    PHASE_C = "phase_c"  # Information Systems
    PHASE_D = "phase_d"  # Technology Architecture
    PHASE_E = "phase_e"  # Opportunities & Solutions
    PHASE_F = "phase_f"  # Migration Planning
    PHASE_G = "phase_g"  # Implementation Governance
    PHASE_H = "phase_h"  # Architecture Change Management
    REQUIREMENTS = "requirements"


@dataclass
class PhaseRecommendation:
    """Recommendation for TOGAF phase"""
    
    recommendation_id: str
    phase: TOGAFPhase
    category: str  # deliverable, activity, decision, risk
    priority: str  # critical, high, medium, low
    
    title: str
    description: str
    rationale: str
    
    # Implementation
    action_items: List[str]
    estimated_effort: str
    dependencies: List[str]
    
    # Metadata
    created_at: datetime
    confidence: float
    metadata: Dict[str, Any] = field(default_factory=dict)


class TOGAFPhaseAdvisor:
    """
    AI-driven advisor for TOGAF ADM phases.
    
    Provides intelligent, context-aware recommendations for each phase.
    """
    
    def __init__(self, llm=None):
        self.llm = llm
        self.recommendations: List[PhaseRecommendation] = []
        
        # Phase-specific templates
        self.phase_templates = self._initialize_phase_templates()
    
    def _initialize_phase_templates(self) -> Dict:
        """Initialize templates for each phase"""
        
        return {
            TOGAFPhase.PHASE_A: {
                "key_deliverables": [
                    "Architecture Vision",
                    "Stakeholder Map",
                    "Business Principles",
                    "Architecture Charter",
                ],
                "critical_decisions": [
                    "Architecture scope definition",
                    "Stakeholder identification",
                    "Success metrics definition",
                ],
            },
            TOGAFPhase.PHASE_B: {
                "key_deliverables": [
                    "Business Architecture",
                    "Business Process Models",
                    "Organizational Structure",
                    "Value Stream Maps",
                ],
                "critical_decisions": [
                    "Process optimization approach",
                    "Organizational changes needed",
                    "Business capability investments",
                ],
            },
            # Add templates for other phases...
        }
    
    def advise_phase(
        self,
        phase: TOGAFPhase,
        context: Dict[str, Any]
    ) -> List[PhaseRecommendation]:
        """
        Provide recommendations for a TOGAF phase.
        
        Args:
            phase: TOGAF phase
            context: Phase context (objectives, constraints, etc.)
        
        Returns:
            List of recommendations
        """
        print(f"\n💡 Generating recommendations for {phase.value}...")
        
        recommendations = []
        
        # Get phase template
        template = self.phase_templates.get(phase, {})
        
        # Check deliverables
        deliverable_recs = self._check_deliverables(phase, template, context)
        recommendations.extend(deliverable_recs)
        
        # Check critical decisions
        decision_recs = self._check_decisions(phase, template, context)
        recommendations.extend(decision_recs)
        
        # Check risks
        risk_recs = self._identify_phase_risks(phase, context)
        recommendations.extend(risk_recs)
        
        # Store recommendations
        self.recommendations.extend(recommendations)
        
        print(f"✅ Generated {len(recommendations)} recommendations")
        
        return recommendations
    
    def _check_deliverables(
        self,
        phase: TOGAFPhase,
        template: Dict,
        context: Dict
    ) -> List[PhaseRecommendation]:
        """Check deliverable completeness"""
        
        recommendations = []
        deliverables = template.get("key_deliverables", [])
        completed = context.get("completed_deliverables", [])
        
        for deliverable in deliverables:
            if deliverable not in completed:
                recommendations.append(PhaseRecommendation(
                    recommendation_id=f"REC-{len(recommendations)+1}",
                    phase=phase,
                    category="deliverable",
                    priority="high",
                    title=f"Complete {deliverable}",
                    description=f"Required deliverable '{deliverable}' is not yet complete",
                    rationale=f"{deliverable} is essential for {phase.value} completion",
                    action_items=[
                        f"Create {deliverable} document",
                        "Review with stakeholders",
                        "Obtain approval",
                    ],
                    estimated_effort="3-5 days",
                    dependencies=[],
                    created_at=datetime.now(),
                    confidence=0.95
                ))
        
        return recommendations
    
    def _check_decisions(
        self,
        phase: TOGAFPhase,
        template: Dict,
        context: Dict
    ) -> List[PhaseRecommendation]:
        """Check critical decisions"""
        
        recommendations = []
        decisions = template.get("critical_decisions", [])
        made_decisions = context.get("decisions_made", [])
        
        for decision in decisions:
            if decision not in made_decisions:
                recommendations.append(PhaseRecommendation(
                    recommendation_id=f"REC-{len(recommendations)+1}",
                    phase=phase,
                    category="decision",
                    priority="critical",
                    title=f"Make decision: {decision}",
                    description=f"Critical decision '{decision}' needs to be made",
                    rationale="Blocking progress on phase activities",
                    action_items=[
                        "Gather decision criteria",
                        "Analyze options",
                        "Consult stakeholders",
                        "Make and document decision",
                    ],
                    estimated_effort="1-2 weeks",
                    dependencies=[],
                    created_at=datetime.now(),
                    confidence=0.9
                ))
        
        return recommendations
    
    def _identify_phase_risks(
        self,
        phase: TOGAFPhase,
        context: Dict
    ) -> List[PhaseRecommendation]:
        """Identify phase-specific risks"""
        
        recommendations = []
        
        # Generic risk checks
        if not context.get("stakeholder_engagement"):
            recommendations.append(PhaseRecommendation(
                recommendation_id=f"REC-{len(recommendations)+1}",
                phase=phase,
                category="risk",
                priority="high",
                title="Improve stakeholder engagement",
                description="Low stakeholder engagement detected",
                rationale="Success requires active stakeholder participation",
                action_items=[
                    "Identify key stakeholders",
                    "Schedule regular meetings",
                    "Establish communication plan",
                ],
                estimated_effort="1 week",
                dependencies=[],
                created_at=datetime.now(),
                confidence=0.85
            ))
        
        return recommendations
    
    def get_phase_progress(
        self,
        phase: TOGAFPhase,
        context: Dict
    ) -> Dict[str, Any]:
        """Calculate phase progress"""
        
        template = self.phase_templates.get(phase, {})
        deliverables = template.get("key_deliverables", [])
        decisions = template.get("critical_decisions", [])
        
        completed_deliverables = context.get("completed_deliverables", [])
        made_decisions = context.get("decisions_made", [])
        
        total_items = len(deliverables) + len(decisions)
        completed_items = len(completed_deliverables) + len(made_decisions)
        
        progress = (completed_items / total_items * 100) if total_items > 0 else 0
        
        return {
            "phase": phase.value,
            "progress_percentage": progress,
            "completed_deliverables": len(completed_deliverables),
            "total_deliverables": len(deliverables),
            "completed_decisions": len(made_decisions),
            "total_decisions": len(decisions),
            "status": "on_track" if progress > 60 else "at_risk",
        }
