"""
Autonomous Architecture Controller

Master controller for autonomous AI-driven architecture management.
Coordinates runtime intelligence across TOGAF phases and ArchiMate layers.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from .decision_engine import (
    RuntimeDecisionEngine, DecisionContext, DecisionResult,
    DecisionType, DecisionPriority
)
from .archimate_intelligence import (
    ArchiMateModelAnalyzer, ArchiMateElement, ArchiMateLayer,
    ElementType, ArchiMateRelationship, RelationshipType
)
from .togaf_advisor import TOGAFPhaseAdvisor, TOGAFPhase, PhaseRecommendation


class AutonomousArchitectureController:
    """
    Autonomous AI-driven architecture controller.
    
    Provides intelligent, real-time decision-making and recommendations
    across TOGAF phases and ArchiMate modeling layers.
    
    Features:
    - Autonomous decision-making
    - Real-time architecture analysis
    - Pattern recognition
    - Impact assessment
    - Compliance checking
    - Continuous learning
    """
    
    def __init__(
        self,
        enterprise_name: str,
        project_name: str,
        llm=None,
        enable_autonomous_mode: bool = True
    ):
        """
        Initialize autonomous controller.
        
        Args:
            enterprise_name: Name of enterprise
            project_name: Name of architecture project
            llm: Language model for AI (optional)
            enable_autonomous_mode: Enable autonomous decision-making
        """
        self.enterprise_name = enterprise_name
        self.project_name = project_name
        self.llm = llm
        self.autonomous_mode = enable_autonomous_mode
        
        # Initialize components
        self.decision_engine = RuntimeDecisionEngine(llm=llm)
        self.archimate_analyzer = ArchiMateModelAnalyzer(llm=llm)
        self.togaf_advisor = TOGAFPhaseAdvisor(llm=llm)
        
        # State tracking
        self.current_phase = TOGAFPhase.PRELIMINARY
        self.architecture_state = {
            "phases_completed": [],
            "current_decisions": [],
            "active_recommendations": [],
            "model_insights": [],
        }
        
        # Event log
        self.event_log: List[Dict] = []
        
        print(f"\n🤖 Autonomous Architecture Controller initialized")
        print(f"   Enterprise: {enterprise_name}")
        print(f"   Project: {project_name}")
        print(f"   Autonomous Mode: {'Enabled' if enable_autonomous_mode else 'Disabled'}")
    
    def start_phase(
        self,
        phase: TOGAFPhase,
        objectives: List[str],
        context: Dict[str, Any] = None
    ):
        """
        Start a TOGAF phase with autonomous guidance.
        
        Args:
            phase: TOGAF phase to start
            objectives: Phase objectives
            context: Additional context
        """
        print(f"\n📋 Starting {phase.value}")
        print(f"   Objectives: {len(objectives)}")
        
        self.current_phase = phase
        
        # Get AI recommendations for phase
        phase_context = context or {}
        phase_context["objectives"] = objectives
        
        recommendations = self.togaf_advisor.advise_phase(phase, phase_context)
        
        # Store recommendations
        self.architecture_state["active_recommendations"].extend(recommendations)
        
        # Log event
        self._log_event("phase_started", {
            "phase": phase.value,
            "objectives": objectives,
            "recommendations_count": len(recommendations)
        })
        
        # Display top recommendations
        print(f"\n💡 Top Recommendations:")
        for i, rec in enumerate(recommendations[:5], 1):
            print(f"   {i}. [{rec.priority}] {rec.title}")
    
    def make_autonomous_decision(
        self,
        decision_scope: str,
        decision_type: DecisionType,
        options: List[Any],
        business_drivers: List[str] = None,
        constraints: List[str] = None
    ) -> DecisionResult:
        """
        Make an autonomous architecture decision.
        
        Args:
            decision_scope: Scope of decision
            decision_type: Type of decision
            options: Available options
            business_drivers: Business drivers
            constraints: Constraints
        
        Returns:
            DecisionResult with AI recommendation
        """
        print(f"\n🎯 Autonomous Decision: {decision_scope}")
        
        # Create decision context
        context = DecisionContext(
            togaf_phase=self.current_phase.value,
            phase_objectives=[],
            archimate_layer=ArchiMateLayer.STRATEGY.value,
            affected_elements=[],
            business_drivers=business_drivers or [],
            stakeholders=[],
            constraints=constraints or [],
            current_state={},
            target_state={},
            gaps=[],
            decision_type=decision_type,
            decision_scope=decision_scope,
            urgency=DecisionPriority.HIGH
        )
        
        # Use decision engine
        decision = self.decision_engine.make_decision(
            context=context,
            options=options,
            use_ai=self.llm is not None
        )
        
        # Store decision
        self.architecture_state["current_decisions"].append(decision)
        
        # Log event
        self._log_event("decision_made", {
            "decision_id": decision.decision_id,
            "scope": decision_scope,
            "confidence": decision.confidence.value
        })
        
        if self.autonomous_mode:
            print(f"   ✅ Auto-approved: {decision.recommended_option.name}")
        else:
            print(f"   ⏸️  Awaiting approval: {decision.recommended_option.name}")
        
        return decision
    
    def analyze_architecture(
        self,
        analysis_types: List[str] = None
    ) -> List[Any]:
        """
        Perform autonomous architecture analysis.
        
        Args:
            analysis_types: Types of analysis to perform
        
        Returns:
            List of insights
        """
        print(f"\n🔍 Autonomous Architecture Analysis")
        
        # Perform ArchiMate model analysis
        insights = self.archimate_analyzer.analyze_model(analysis_types)
        
        # Store insights
        self.architecture_state["model_insights"].extend(insights)
        
        # Log event
        self._log_event("analysis_performed", {
            "analysis_types": analysis_types or "all",
            "insights_found": len(insights)
        })
        
        # Auto-respond to critical insights
        if self.autonomous_mode:
            critical_insights = [i for i in insights if i.severity == "critical"]
            if critical_insights:
                print(f"\n⚠️  {len(critical_insights)} critical insights - auto-generating action plan")
                self._auto_respond_to_insights(critical_insights)
        
        return insights
    
    def assess_impact(
        self,
        element_id: str,
        change_type: str = "modify"
    ) -> Dict[str, Any]:
        """
        Assess impact of architectural change.
        
        Args:
            element_id: Element to change
            change_type: Type of change
        
        Returns:
            Impact assessment
        """
        print(f"\n⚡ Impact Assessment: {change_type} {element_id}")
        
        # Use ArchiMate analyzer
        impact = self.archimate_analyzer.assess_change_impact(
            element_id=element_id,
            change_type=change_type
        )
        
        # Log event
        self._log_event("impact_assessed", {
            "element": element_id,
            "change_type": change_type,
            "severity": impact.get("severity", "unknown")
        })
        
        # Auto-generate mitigation plan if high impact
        if self.autonomous_mode and impact.get("severity") in ["high", "critical"]:
            print(f"   🛡️  Auto-generating mitigation plan")
            self._auto_generate_mitigation_plan(element_id, impact)
        
        return impact
    
    def get_phase_status(self) -> Dict[str, Any]:
        """Get current phase status"""
        
        # Get progress from advisor
        progress = self.togaf_advisor.get_phase_progress(
            phase=self.current_phase,
            context={
                "completed_deliverables": [],
                "decisions_made": [d.decision_id for d in self.architecture_state["current_decisions"]]
            }
        )
        
        # Add controller-specific info
        progress.update({
            "active_decisions": len(self.architecture_state["current_decisions"]),
            "active_recommendations": len(self.architecture_state["active_recommendations"]),
            "model_insights": len(self.architecture_state["model_insights"]),
            "autonomous_mode": self.autonomous_mode,
        })
        
        return progress
    
    def get_architecture_health(self) -> Dict[str, Any]:
        """Get overall architecture health score"""
        
        # Calculate health score based on insights
        insights = self.architecture_state["model_insights"]
        
        critical_count = len([i for i in insights if i.severity == "critical"])
        high_count = len([i for i in insights if i.severity == "high"])
        medium_count = len([i for i in insights if i.severity == "medium"])
        
        # Calculate score (0-100)
        total_issues = critical_count + high_count + medium_count
        health_score = max(0, 100 - (critical_count * 20 + high_count * 10 + medium_count * 5))
        
        # Determine health status
        if health_score >= 80:
            status = "healthy"
        elif health_score >= 60:
            status = "fair"
        elif health_score >= 40:
            status = "at_risk"
        else:
            status = "critical"
        
        return {
            "health_score": health_score,
            "status": status,
            "critical_issues": critical_count,
            "high_issues": high_count,
            "medium_issues": medium_count,
            "total_issues": total_issues,
            "recommendations": self._get_health_recommendations(status)
        }
    
    def _get_health_recommendations(self, status: str) -> List[str]:
        """Get health improvement recommendations"""
        
        if status == "critical":
            return [
                "Immediate action required on critical issues",
                "Escalate to architecture board",
                "Consider architecture review"
            ]
        elif status == "at_risk":
            return [
                "Address high-priority issues",
                "Increase monitoring frequency",
                "Review architecture decisions"
            ]
        elif status == "fair":
            return [
                "Continue addressing medium-priority items",
                "Maintain current monitoring",
            ]
        else:
            return [
                "Continue best practices",
                "Proactive monitoring",
            ]
    
    def _auto_respond_to_insights(self, insights: List[Any]):
        """Autonomously respond to critical insights"""
        
        for insight in insights:
            print(f"   📝 Auto-creating action plan for: {insight.title}")
            
            # Create action items based on recommendations
            for rec in insight.recommendations[:2]:
                self._log_event("auto_action_created", {
                    "insight_id": insight.insight_id,
                    "action": rec
                })
    
    def _auto_generate_mitigation_plan(self, element_id: str, impact: Dict):
        """Auto-generate risk mitigation plan"""
        
        print(f"   📋 Mitigation plan generated for {element_id}")
        
        self._log_event("mitigation_plan_created", {
            "element": element_id,
            "severity": impact["severity"],
            "affected_count": impact.get("directly_affected", 0)
        })
    
    def _log_event(self, event_type: str, data: Dict):
        """Log controller event"""
        
        self.event_log.append({
            "timestamp": datetime.now(),
            "event_type": event_type,
            "phase": self.current_phase.value,
            "data": data
        })
    
    def generate_report(self) -> str:
        """Generate autonomous controller report"""
        
        report = f"""
╔══════════════════════════════════════════════════════════════════════════╗
║  AUTONOMOUS ARCHITECTURE CONTROLLER - STATUS REPORT                      ║
╠══════════════════════════════════════════════════════════════════════════╣

Enterprise: {self.enterprise_name}
Project: {self.project_name}
Current Phase: {self.current_phase.value}
Autonomous Mode: {'Enabled' if self.autonomous_mode else 'Disabled'}

"""
        
        # Phase status
        status = self.get_phase_status()
        report += f"""
PHASE STATUS
├─ Progress: {status['progress_percentage']:.1f}%
├─ Status: {status['status']}
├─ Active Decisions: {status['active_decisions']}
├─ Active Recommendations: {status['active_recommendations']}
└─ Model Insights: {status['model_insights']}

"""
        
        # Architecture health
        health = self.get_architecture_health()
        report += f"""
ARCHITECTURE HEALTH
├─ Health Score: {health['health_score']}/100
├─ Status: {health['status']}
├─ Critical Issues: {health['critical_issues']}
├─ High Issues: {health['high_issues']}
└─ Medium Issues: {health['medium_issues']}

"""
        
        # Recent decisions
        recent_decisions = self.architecture_state["current_decisions"][:5]
        if recent_decisions:
            report += "RECENT DECISIONS\n"
            for i, dec in enumerate(recent_decisions, 1):
                report += f"{i}. {dec.recommended_option.name} (Confidence: {dec.confidence.value})\n"
            report += "\n"
        
        # Top recommendations
        active_recs = self.architecture_state["active_recommendations"][:5]
        if active_recs:
            report += "TOP RECOMMENDATIONS\n"
            for i, rec in enumerate(active_recs, 1):
                report += f"{i}. [{rec.priority}] {rec.title}\n"
            report += "\n"
        
        # Event summary
        report += f"""
EVENT SUMMARY
├─ Total Events: {len(self.event_log)}
├─ Decisions Made: {len([e for e in self.event_log if e['event_type'] == 'decision_made'])}
├─ Analyses Performed: {len([e for e in self.event_log if e['event_type'] == 'analysis_performed'])}
└─ Auto Actions: {len([e for e in self.event_log if e['event_type'] == 'auto_action_created'])}

"""
        
        report += """╚══════════════════════════════════════════════════════════════════════════╝
"""
        
        return report
