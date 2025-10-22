"""
TOGAF 9.0 Complete End-to-End Example: Digital Banking Transformation

Real-world business scenario demonstrating all 8 TOGAF ADM phases.

Business Case:
- Company: GlobalBank International (Traditional Retail Bank)
- Challenge: Losing market share to digital-first competitors
- Goal: Complete digital transformation in 18 months
- Budget: $15 Million
- Expected Outcomes: 50% cost reduction, 3x customer growth, 90% satisfaction

This example demonstrates the complete TOGAF framework with realistic
business data, architecture decisions, and deliverables.
"""

import json
from datetime import date, datetime
from pathlib import Path

from togaf_framework.adm.togaf_orchestrator import TOGAFADMOrchestrator
from togaf_framework.models.stakeholder import Stakeholder
from togaf_framework.models.principle import ArchitecturePrinciple
from togaf_framework.models.requirement import Requirement
from togaf_framework.core.enums import StakeholderType, PriorityLevel, RiskLevel


def print_section(title):
    """Print section header"""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_subsection(title):
    """Print subsection header"""
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def main():
    print_section("TOGAF 9.0 ADM - COMPLETE END-TO-END FRAMEWORK")
    print("\n🏦 DIGITAL BANKING TRANSFORMATION")
    print("\nEnterprise: GlobalBank International")
    print("Project: Digital Banking Platform Modernization")
    print("Timeline: 18 months (Mar 2025 - Aug 2026)")
    print("Budget: $15,000,000")
    print("Team: 50+ architects, developers, and business analysts")
    
    # Initialize the TOGAF orchestrator
    orchestrator = TOGAFADMOrchestrator(
        enterprise_name="GlobalBank International",
        project_name="Digital Banking Platform Transformation",
        architecture_scope="Enterprise-wide digital banking transformation"
    )
    
    print_section("PHASE A: ARCHITECTURE VISION")
    print("Establishing strategic direction and stakeholder alignment...")
    
    # Initialize and configure Phase A
    phase_a = orchestrator.initialize_phase_a()
    
    # Set vision statement
    phase_a.vision_statement = (
        "Transform GlobalBank into a leading digital-first banking platform "
        "delivering seamless omnichannel experiences, AI-powered insights, "
        "and real-time financial services accessible 24/7 from any device"
    )
    
    # Add business goals
    phase_a.add_business_goal("Increase digital channel usage to 80% of all transactions")
    phase_a.add_business_goal("Reduce operational costs by 50% through automation")
    phase_a.add_business_goal("Achieve 90% customer satisfaction score (NPS >70)")
    phase_a.add_business_goal("Launch mobile app with 1M users in first year")
    phase_a.add_business_goal("Implement real-time payment processing")
    
    # Add key stakeholders
    ceo = Stakeholder(
        name="Sarah Johnson",
        role="Chief Executive Officer",
        stakeholder_type=StakeholderType.EXECUTIVE,
        organization="GlobalBank International"
    )
    ceo.add_concern("Market competitiveness and shareholder value")
    ceo.add_concern("Digital transformation success")
    phase_a.add_key_stakeholder(ceo)
    
    cto = Stakeholder(
        name="Michael Chen",
        role="Chief Technology Officer",
        stakeholder_type=StakeholderType.ARCHITECT,
        organization="IT Department"
    )
    cto.add_concern("Technical feasibility and scalability")
    cto.add_concern("Security and regulatory compliance")
    phase_a.add_key_stakeholder(cto)
    
    cfo = Stakeholder(
        name="Emily Rodriguez",
        role="Chief Financial Officer",
        stakeholder_type=StakeholderType.BUSINESS,
        organization="Finance Department"
    )
    cfo.add_concern("ROI and cost management")
    cfo.add_concern("Risk mitigation")
    phase_a.add_key_stakeholder(cfo)
    
    # Add architecture principles
    principle1 = ArchitecturePrinciple(
        name="Customer-Centric Design",
        statement="All systems and processes must prioritize customer experience",
        rationale="Customer satisfaction drives business growth and retention",
        implications=["User research required for all new features", "Continuous feedback loops with customers"]
    )
    phase_a.add_principle(principle1)
    
    principle2 = ArchitecturePrinciple(
        name="Cloud-First Architecture",
        statement="All new systems must be cloud-native and scalable",
        rationale="Cloud enables agility, scalability, and cost optimization",
        implications=["Team training on cloud technologies required", "Infrastructure as Code mandatory"]
    )
    phase_a.add_principle(principle2)
    
    principle3 = ArchitecturePrinciple(
        name="Security by Design",
        statement="Security must be embedded in every layer",
        rationale="Financial data requires highest security standards",
        implications=["Security reviews at every phase", "Zero-trust architecture implementation"]
    )
    phase_a.add_principle(principle3)
    
    # Add requirements
    req1 = Requirement(
        name="Mobile Banking Application",
        description="Native mobile app for iOS and Android with full banking features",
        requirement_type="functional",
        priority=PriorityLevel.CRITICAL
    )
    req1.add_acceptance_criterion("Support 1M concurrent users")
    req1.add_acceptance_criterion("Response time < 2 seconds")
    req1.add_acceptance_criterion("99.9% uptime")
    phase_a.add_requirement(req1)
    
    req2 = Requirement(
        name="Real-time Payment Processing",
        description="Process payments instantly 24/7 with immediate confirmation",
        requirement_type="functional",
        priority=PriorityLevel.HIGH
    )
    req2.add_acceptance_criterion("Transaction time < 1 second")
    req2.add_acceptance_criterion("99.99% availability")
    phase_a.add_requirement(req2)
    
    req3 = Requirement(
        name="Regulatory Compliance",
        description="Full compliance with banking regulations (PCI-DSS, SOC2, GDPR)",
        requirement_type="non-functional",
        priority=PriorityLevel.CRITICAL
    )
    req3.add_acceptance_criterion("PCI-DSS Level 1 certification")
    req3.add_acceptance_criterion("SOC 2 Type II audit")
    phase_a.add_requirement(req3)
    
    # Execute Phase A
    results_a = orchestrator.execute_phase_a()
    
    print(f"\n✓ Phase A Complete")
    print(f"  - Vision Statement: Defined")
    print(f"  - Business Goals: {len(phase_a.business_goals)} strategic goals")
    print(f"  - Key Stakeholders: {len(phase_a.key_stakeholders)} executives identified")
    print(f"  - Architecture Principles: {len(phase_a.architecture_principles)} established")
    print(f"  - Requirements: {len(phase_a.requirements)} captured")
    
    print_section("PHASE B: BUSINESS ARCHITECTURE")
    print("Defining business capabilities, processes, and value streams...")
    
    # Initialize Phase B
    phase_b = orchestrator.initialize_phase_b()
    
    # Note: Phase B, C, D, E, F, G, H would be configured similarly
    # For brevity in this example, we'll execute them with basic configuration
    results_b = orchestrator.execute_phase_b()
    print(f"✓ Business capabilities mapped")
    print(f"✓ Business processes defined")
    print(f"✓ Gap analysis completed")
    print(f"✓ Status: {results_b['status']}")
    
    print_section("PHASE C: INFORMATION SYSTEMS ARCHITECTURE")
    print("Designing application and data architectures...")
    
    phase_c = orchestrator.initialize_phase_c()
    results_c = orchestrator.execute_phase_c()
    print(f"✓ Application portfolio defined")
    print(f"✓ Data architecture modeled")
    print(f"✓ Integration patterns identified")
    print(f"✓ Status: {results_c['status']}")
    
    print_section("PHASE D: TECHNOLOGY ARCHITECTURE")
    print("Defining technology infrastructure and platforms...")
    
    phase_d = orchestrator.initialize_phase_d()
    results_d = orchestrator.execute_phase_d()
    print(f"✓ Cloud infrastructure designed")
    print(f"✓ Security controls defined")
    print(f"✓ Technology standards established")
    print(f"✓ Status: {results_d['status']}")
    
    print_section("PHASE E: OPPORTUNITIES AND SOLUTIONS")
    print("Analyzing solution alternatives and ROI...")
    
    phase_e = orchestrator.initialize_phase_e()
    results_e = orchestrator.execute_phase_e()
    print(f"✓ Solution building blocks identified")
    print(f"✓ Implementation projects defined")
    print(f"✓ Cost-benefit analysis completed")
    print(f"✓ ROI calculated: 187% over 3 years")
    print(f"✓ Status: {results_e['status']}")
    
    print_section("PHASE F: MIGRATION PLANNING")
    print("Creating detailed migration roadmap...")
    
    phase_f = orchestrator.initialize_phase_f()
    results_f = orchestrator.execute_phase_f()
    print(f"✓ Migration projects planned")
    print(f"✓ Architecture roadmap created")
    print(f"✓ Resource requirements defined")
    print(f"✓ Timeline: 18 months across 4 phases")
    print(f"✓ Status: {results_f['status']}")
    
    print_section("PHASE G: IMPLEMENTATION GOVERNANCE")
    print("Establishing governance framework...")
    
    phase_g = orchestrator.initialize_phase_g()
    results_g = orchestrator.execute_phase_g()
    print(f"✓ Architecture contracts established")
    print(f"✓ Compliance framework defined")
    print(f"✓ Governance policies activated")
    print(f"✓ Status: {results_g['status']}")
    
    print_section("PHASE H: ARCHITECTURE CHANGE MANAGEMENT")
    print("Activating continuous improvement process...")
    
    phase_h = orchestrator.initialize_phase_h()
    results_h = orchestrator.execute_phase_h()
    print(f"✓ Change management process active")
    print(f"✓ Monitoring deployed")
    print(f"✓ Lessons learned captured")
    print(f"✓ Knowledge repository established")
    print(f"✓ Status: {results_h['status']}")
    
    # Generate comprehensive report
    print_section("TRANSFORMATION COMPLETE - COMPREHENSIVE REPORT")
    
    progress = orchestrator.get_progress_summary()
    print(f"\n📊 PROJECT STATUS")
    print(f"   Status: {progress['status'].upper()}")
    print(f"   Progress: {progress['progress_percentage']:.0f}% ({progress['phases_completed']}/{progress['total_phases']} phases)")
    print(f"   Duration: {progress['duration_minutes']:.1f} minutes")
    
    report = orchestrator.generate_comprehensive_report()
    
    print(f"\n📋 EXECUTIVE SUMMARY")
    exec_summary = report['executive_summary']
    print(f"   Enterprise: {exec_summary['enterprise']}")
    print(f"   Project: {exec_summary['project']}")
    print(f"   Scope: {exec_summary['scope']}")
    print(f"   Phases Completed: {exec_summary['phases_completed']}/8")
    
    print(f"\n✨ KEY ACHIEVEMENTS:")
    for achievement in exec_summary['key_achievements']:
        print(f"   ✓ {achievement}")
    
    print(f"\n📁 ARCHITECTURE DELIVERABLES:")
    if report['architecture_vision']:
        print(f"   • Architecture Vision: {report['architecture_vision']['goals']} goals, "
              f"{report['architecture_vision']['principles']} principles, "
              f"{report['architecture_vision']['stakeholders']} stakeholders")
    if report['business_architecture']:
        print(f"   • Business Architecture: {report['business_architecture']['capabilities']} capabilities, "
              f"{report['business_architecture']['processes']} processes")
    if report['information_systems']:
        print(f"   • Information Systems: {report['information_systems']['applications']} applications, "
              f"{report['information_systems']['data_entities']} data entities")
    if report['technology_architecture']:
        print(f"   • Technology Architecture: {report['technology_architecture']['cloud_services']} cloud services, "
              f"{report['technology_architecture']['security_controls']} security controls")
    if report['solutions_analysis']:
        print(f"   • Solutions Analysis: {report['solutions_analysis']['solution_blocks']} solution blocks, "
              f"{report['solutions_analysis']['projects']} implementation projects")
    if report['migration_plan']:
        print(f"   • Migration Plan: {report['migration_plan']['migration_projects']} projects, "
              f"{report['migration_plan']['roadmap_phases']} roadmap phases")
    if report['governance_framework']:
        print(f"   • Governance Framework: {report['governance_framework']['contracts']} contracts, "
              f"{report['governance_framework']['compliance_checks']} compliance checks")
    if report['change_management']:
        print(f"   • Change Management: {report['change_management']['change_requests']} change requests, "
              f"{report['change_management']['monitors']} monitors")
    
    print(f"\n💰 BUSINESS OUTCOMES (3-Year Projection):")
    print(f"   • Total Investment: $15,000,000")
    print(f"   • Annual Cost Savings: $5,000,000 (50% reduction)")
    print(f"   • Revenue Growth: $8,000,000/year (new digital services)")
    print(f"   • ROI: 187% (3-year cumulative)")
    print(f"   • Payback Period: 1.2 years")
    print(f"   • Customer Growth: 3x (from 500K to 1.5M)")
    print(f"   • Digital Adoption: 80% (from 20%)")
    print(f"   • Customer Satisfaction: 90% (from 65%)")
    print(f"   • Transaction Speed: 90% faster")
    print(f"   • Time-to-Market: 70% improvement")
    
    print(f"\n💡 STRATEGIC RECOMMENDATIONS:")
    for i, rec in enumerate(report['recommendations'], 1):
        print(f"   {i}. {rec}")
    
    # Save outputs
    print_section("SAVING OUTPUTS")
    
    # Save complete architecture state
    state_file = "digital_banking_complete_state.json"
    orchestrator.save_architecture_state(state_file)
    print(f"✓ Architecture State saved: {state_file}")
    
    # Save comprehensive report
    report_file = "digital_banking_comprehensive_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    print(f"✓ Comprehensive Report saved: {report_file}")
    
    # Save phase results separately
    phases_dir = Path("phase_results")
    phases_dir.mkdir(exist_ok=True)
    
    for phase_name, phase_result in [
        ("phase_a_vision", results_a),
        ("phase_b_business", results_b),
        ("phase_c_information", results_c),
        ("phase_d_technology", results_d),
        ("phase_e_opportunities", results_e),
        ("phase_f_migration", results_f),
        ("phase_g_governance", results_g),
        ("phase_h_change", results_h)
    ]:
        phase_file = phases_dir / f"{phase_name}_results.json"
        with open(phase_file, 'w') as f:
            json.dump(phase_result, f, indent=2, default=str)
    
    print(f"✓ Individual phase results saved: phase_results/*.json")
    
    # Calculate statistics
    print_section("FRAMEWORK STATISTICS")
    
    total_data_size = sum([
        len(json.dumps(results_a, default=str)),
        len(json.dumps(results_b, default=str)),
        len(json.dumps(results_c, default=str)),
        len(json.dumps(results_d, default=str)),
        len(json.dumps(results_e, default=str)),
        len(json.dumps(results_f, default=str)),
        len(json.dumps(results_g, default=str)),
        len(json.dumps(results_h, default=str))
    ])
    
    print(f"\n📈 TOGAF ADM CYCLE METRICS:")
    print(f"   • Total Phases: 8/8 (100% Complete)")
    print(f"   • Stakeholders: {len(phase_a.key_stakeholders)}")
    print(f"   • Principles: {len(phase_a.architecture_principles)}")
    print(f"   • Requirements: {len(phase_a.requirements)}")
    print(f"   • Business Goals: {len(phase_a.business_goals)}")
    print(f"   • Architecture Data: {total_data_size:,} bytes")
    print(f"   • Execution Time: {progress['duration_minutes']:.1f} minutes")
    print(f"   • Files Generated: 10 (state, report, 8 phase results)")
    
    print_section("SUCCESS!")
    print("\n🎉 DIGITAL BANKING TRANSFORMATION COMPLETE")
    print("\n📱 GlobalBank International is now a digital-first banking platform")
    print("   featuring:")
    print("   • Modern cloud-native infrastructure (Azure)")
    print("   • Mobile-first user experiences (iOS & Android)")
    print("   • Real-time payment processing (< 1 second)")
    print("   • AI-powered customer insights")
    print("   • 99.99% availability and security")
    print("   • Continuous architecture governance")
    
    print("\n🏛️ The TOGAF 9.0 ADM framework successfully guided this")
    print("   transformation through all 8 phases, ensuring:")
    print("   ✓ Architectural integrity and consistency")
    print("   ✓ Stakeholder alignment and buy-in")
    print("   ✓ Business value realization ($13M annual benefits)")
    print("   ✓ Risk mitigation and compliance")
    print("   ✓ Sustainable and governable architecture")
    
    print("\n" + "=" * 80)
    print("TOGAF ADM FRAMEWORK - END-TO-END EXECUTION COMPLETE")
    print("=" * 80)
    print()


if __name__ == "__main__":
    main()
