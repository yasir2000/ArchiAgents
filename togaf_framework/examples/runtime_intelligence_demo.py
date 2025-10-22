"""
Runtime Intelligence Layer Demonstration

Demonstrates autonomous AI-driven decision-making across TOGAF phases
and ArchiMate modeling layers.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from togaf_framework.runtime_intelligence import (
    AutonomousArchitectureController,
    DecisionOption, DecisionType,
    ArchiMateElement, ArchiMateRelationship,
    ArchiMateLayer, ElementType, RelationshipType,
    TOGAFPhase
)


def print_section(title: str):
    """Print formatted section"""
    print(f"\n{'='*80}")
    print(f"{title.upper()}")
    print(f"{'='*80}\n")


def demo_autonomous_controller():
    """Demonstrate autonomous architecture controller"""
    
    print_section("Runtime Intelligence Layer - Autonomous Architecture Control")
    
    print("""
This demonstration shows how the Runtime Intelligence Layer provides
autonomous AI-driven decision-making across TOGAF phases and ArchiMate layers.

Features demonstrated:
1. Autonomous Decision-Making
2. Real-time Architecture Analysis
3. TOGAF Phase Guidance
4. ArchiMate Model Intelligence
5. Impact Assessment
6. Architecture Health Monitoring
""")
    
    # Create autonomous controller
    print_section("1. Initialize Autonomous Controller")
    
    controller = AutonomousArchitectureController(
        enterprise_name="GlobalTech Corporation",
        project_name="Digital Transformation Initiative",
        llm=None,  # Would use actual LLM in production
        enable_autonomous_mode=True
    )
    
    # Start TOGAF Phase A
    print_section("2. Start TOGAF Phase A - Architecture Vision")
    
    controller.start_phase(
        phase=TOGAFPhase.PHASE_A,
        objectives=[
            "Define architecture vision",
            "Identify stakeholders",
            "Establish governance",
            "Create business case"
        ],
        context={
            "completed_deliverables": [],
            "decisions_made": [],
            "stakeholder_engagement": True
        }
    )
    
    # Build ArchiMate Model
    print_section("3. Build ArchiMate Model")
    
    print("Creating ArchiMate elements across layers...")
    
    # Strategy Layer
    capability1 = ArchiMateElement(
        element_id="CAP-001",
        name="Digital Customer Engagement",
        element_type=ElementType.CAPABILITY,
        layer=ArchiMateLayer.STRATEGY,
        description="Capability to engage customers through digital channels"
    )
    controller.archimate_analyzer.add_element(capability1)
    
    # Business Layer
    process1 = ArchiMateElement(
        element_id="PROC-001",
        name="Customer Onboarding Process",
        element_type=ElementType.BUSINESS_PROCESS,
        layer=ArchiMateLayer.BUSINESS,
        description="Process for onboarding new customers"
    )
    controller.archimate_analyzer.add_element(process1)
    
    service1 = ArchiMateElement(
        element_id="SRV-001",
        name="Customer Registration Service",
        element_type=ElementType.BUSINESS_SERVICE,
        layer=ArchiMateLayer.BUSINESS,
        description="Service for customer registration"
    )
    controller.archimate_analyzer.add_element(service1)
    
    # Application Layer
    app1 = ArchiMateElement(
        element_id="APP-001",
        name="Customer Portal",
        element_type=ElementType.APPLICATION_COMPONENT,
        layer=ArchiMateLayer.APPLICATION,
        description="Web-based customer portal application"
    )
    controller.archimate_analyzer.add_element(app1)
    
    app2 = ArchiMateElement(
        element_id="APP-002",
        name="CRM System",
        element_type=ElementType.APPLICATION_COMPONENT,
        layer=ArchiMateLayer.APPLICATION,
        description="Customer relationship management system"
    )
    controller.archimate_analyzer.add_element(app2)
    
    app3 = ArchiMateElement(
        element_id="APP-003",
        name="Mobile App",
        element_type=ElementType.APPLICATION_COMPONENT,
        layer=ArchiMateLayer.APPLICATION,
        description="Mobile application for customers"
    )
    controller.archimate_analyzer.add_element(app3)
    
    # Technology Layer
    tech1 = ArchiMateElement(
        element_id="TECH-001",
        name="Cloud Platform",
        element_type=ElementType.NODE,
        layer=ArchiMateLayer.TECHNOLOGY,
        description="Azure cloud infrastructure"
    )
    controller.archimate_analyzer.add_element(tech1)
    
    # Add relationships
    print("\nCreating relationships...")
    
    rel1 = ArchiMateRelationship(
        relationship_id="REL-001",
        source_id="PROC-001",
        target_id="SRV-001",
        relationship_type=RelationshipType.REALIZATION,
        name="Realizes"
    )
    controller.archimate_analyzer.add_relationship(rel1)
    
    rel2 = ArchiMateRelationship(
        relationship_id="REL-002",
        source_id="APP-001",
        target_id="SRV-001",
        relationship_type=RelationshipType.SERVING,
        name="Supports"
    )
    controller.archimate_analyzer.add_relationship(rel2)
    
    rel3 = ArchiMateRelationship(
        relationship_id="REL-003",
        source_id="APP-001",
        target_id="APP-002",
        relationship_type=RelationshipType.FLOW,
        name="Data flow"
    )
    controller.archimate_analyzer.add_relationship(rel3)
    
    # Analyze Model
    print_section("4. Autonomous Model Analysis")
    
    insights = controller.analyze_architecture(
        analysis_types=["gaps", "dependencies", "patterns", "optimization"]
    )
    
    print(f"\n📊 Analysis Results:")
    print(f"   Total Insights: {len(insights)}")
    
    # Display insights by severity
    for severity in ["critical", "high", "medium", "low"]:
        severity_insights = [i for i in insights if i.severity == severity]
        if severity_insights:
            print(f"\n   {severity.upper()} ({len(severity_insights)}):")
            for insight in severity_insights[:3]:
                print(f"   - {insight.title}")
    
    # Make Autonomous Decision
    print_section("5. Autonomous Decision-Making")
    
    print("Scenario: Selecting cloud migration strategy")
    
    # Define decision options
    options = [
        DecisionOption(
            option_id="OPT-001",
            name="Lift and Shift",
            description="Migrate existing applications as-is to cloud",
            feasibility=0.9,
            cost=500000,
            time_to_implement=90,
            complexity=0.3,
            risk_level=0.2,
            benefits=[
                "Quick migration",
                "Low complexity",
                "Minimal changes to applications"
            ],
            strategic_alignment=0.6,
            technical_fit=0.7,
            dependencies=["Cloud account setup"],
            constraints=["Limited optimization benefits"],
            prerequisites=["Network connectivity"],
            impacted_systems=["All applications"],
            impacted_stakeholders=["IT Operations", "Development"],
            organizational_impact="Low"
        ),
        DecisionOption(
            option_id="OPT-002",
            name="Re-architecture (Cloud-Native)",
            description="Rebuild applications using cloud-native patterns",
            feasibility=0.7,
            cost=2000000,
            time_to_implement=365,
            complexity=0.8,
            risk_level=0.6,
            benefits=[
                "Maximum cloud benefits",
                "Modern architecture",
                "High scalability",
                "Cost optimization"
            ],
            strategic_alignment=0.95,
            technical_fit=0.9,
            dependencies=["Team training", "DevOps setup"],
            constraints=["High cost", "Long timeline"],
            prerequisites=["Architecture skills"],
            impacted_systems=["All applications"],
            impacted_stakeholders=["CTO", "Development", "Operations"],
            organizational_impact="High"
        ),
        DecisionOption(
            option_id="OPT-003",
            name="Hybrid Approach",
            description="Lift-and-shift critical apps, re-architect strategic ones",
            feasibility=0.85,
            cost=1200000,
            time_to_implement=180,
            complexity=0.6,
            risk_level=0.4,
            benefits=[
                "Balanced approach",
                "Faster time-to-value",
                "Strategic modernization",
                "Manageable risk"
            ],
            strategic_alignment=0.85,
            technical_fit=0.85,
            dependencies=["Application assessment"],
            constraints=["Requires dual expertise"],
            prerequisites=["Priority application list"],
            impacted_systems=["Selected applications"],
            impacted_stakeholders=["CTO", "Development", "Operations", "Business"],
            organizational_impact="Medium"
        ),
    ]
    
    decision = controller.make_autonomous_decision(
        decision_scope="Cloud Migration Strategy",
        decision_type=DecisionType.STRATEGIC,
        options=options,
        business_drivers=[
            "Digital transformation",
            "Cost optimization",
            "Scalability",
            "Innovation"
        ],
        constraints=[
            "12-month timeline preference",
            "Budget constraints",
            "Limited cloud expertise"
        ]
    )
    
    print(f"\n✅ Decision Made:")
    print(f"   Selected: {decision.recommended_option.name}")
    print(f"   Confidence: {decision.confidence.value}")
    print(f"   Cost: ${decision.recommended_option.cost:,.0f}")
    print(f"   Timeline: {decision.recommended_option.time_to_implement} days")
    print(f"\n   Reasoning: {decision.reasoning[:200]}...")
    
    print(f"\n   Implementation Phases: {len(decision.implementation_plan)}")
    for phase in decision.implementation_plan:
        print(f"   - {phase['phase']}: {phase['duration_days']} days")
    
    # Impact Assessment
    print_section("6. Impact Assessment")
    
    print("Scenario: Assessing impact of replacing CRM System")
    
    impact = controller.assess_impact(
        element_id="APP-002",
        change_type="replace"
    )
    
    print(f"\n⚡ Impact Analysis:")
    print(f"   Element: {impact['element']}")
    print(f"   Severity: {impact['severity']}")
    print(f"   Directly Affected: {impact['directly_affected']} elements")
    print(f"   Affected Layers: {', '.join([l.value for l in impact['affected_layers']])}")
    
    print(f"\n   Recommendations:")
    for rec in impact['recommendations']:
        print(f"   - {rec}")
    
    # Phase Status
    print_section("7. Phase Status & Progress")
    
    status = controller.get_phase_status()
    
    print(f"📊 Phase A Status:")
    print(f"   Progress: {status['progress_percentage']:.1f}%")
    print(f"   Status: {status['status']}")
    print(f"   Active Decisions: {status['active_decisions']}")
    print(f"   Active Recommendations: {status['active_recommendations']}")
    print(f"   Model Insights: {status['model_insights']}")
    
    # Architecture Health
    print_section("8. Architecture Health Monitoring")
    
    health = controller.get_architecture_health()
    
    print(f"🏥 Architecture Health:")
    print(f"   Health Score: {health['health_score']}/100")
    print(f"   Status: {health['status'].upper()}")
    print(f"   Critical Issues: {health['critical_issues']}")
    print(f"   High Issues: {health['high_issues']}")
    print(f"   Medium Issues: {health['medium_issues']}")
    
    if health['recommendations']:
        print(f"\n   Health Recommendations:")
        for rec in health['recommendations']:
            print(f"   - {rec}")
    
    # Generate Report
    print_section("9. Autonomous Controller Report")
    
    report = controller.generate_report()
    print(report)
    
    # Summary
    print_section("Summary")
    
    print("""
✅ Runtime Intelligence Layer Demonstration Complete!

Key Capabilities Demonstrated:
1. ✓ Autonomous Architecture Controller
2. ✓ Real-time Decision-Making
3. ✓ ArchiMate Model Analysis
4. ✓ TOGAF Phase Guidance
5. ✓ Impact Assessment
6. ✓ Architecture Health Monitoring
7. ✓ Automated Recommendations
8. ✓ Continuous Learning (Framework)

Benefits:
• Autonomous decision support across TOGAF phases
• Intelligent ArchiMate model analysis
• Real-time architecture health monitoring
• Proactive risk identification
• Data-driven recommendations
• Continuous improvement through learning

The Runtime Intelligence Layer provides a closed-loop intelligent system
that autonomously manages architecture decisions and provides real-time
guidance across all TOGAF phases and ArchiMate layers.
""")


if __name__ == "__main__":
    demo_autonomous_controller()
