"""
Phase B: Business Architecture - Comprehensive Example

This example demonstrates the complete implementation of Phase B,
building upon Phase A and focusing on business capability modeling,
process optimization, and organizational architecture.

Scenario: Digital Transformation Initiative for Saudi Enterprise
Following Vision 2030 and NORA compliance requirements
"""

import json
from datetime import datetime
from togaf_framework.adm import ADMCycle, PhaseAArchitectureVision, PhaseBBusinessArchitecture
from togaf_framework.models import (
    Stakeholder,
    ArchitecturePrinciple,
    Requirement,
    BusinessCapability,
    BusinessProcess
)
from togaf_framework.core.enums import (
    StakeholderType,
    PrincipleCategory,
    PriorityLevel,
    RequirementType,
    MaturityLevel,
    ProcessType,
    ArchiMateLayerType
)


def create_business_architecture_example():
    """
    Complete Phase B implementation example demonstrating:
    1. Business capability modeling (hierarchical)
    2. Business process modeling with automation tracking
    3. Value stream mapping
    4. Gap analysis
    5. KPI tracking
    """
    
    print("="*80)
    print("TOGAF Phase B: Business Architecture - Complete Example")
    print("Digital Transformation Initiative 2025")
    print("="*80)
    print()
    
    # ========== Create ADM Cycle ==========
    print("Creating ADM Cycle...")
    adm_cycle = ADMCycle(
        name="Digital Transformation Initiative 2025",
        description="Enterprise-wide transformation to cloud-native, API-first architecture"
    )
    
    # ========== Phase A: Quick Setup (Already Completed) ==========
    print("Setting up Phase A (Architecture Vision)...")
    phase_a = PhaseAArchitectureVision()
    phase_a.set_vision_statement(
        "Transform into a digital-first enterprise with 99.9% availability, "
        "<100ms API response times, and 70% process automation by 2026"
    )
    
    # Add key stakeholder for continuity
    ceo = Stakeholder(
        name="CEO - Digital Transformation",
        stakeholder_type=StakeholderType.EXECUTIVE,
        description="Chief Executive Officer leading digital transformation"
    )
    ceo.add_concern("Strategic alignment")
    ceo.add_concern("ROI")
    ceo.add_concern("Vision 2030 compliance")
    ceo.influence_level = "high"
    ceo.interest_level = "high"
    phase_a.add_key_stakeholder(ceo)
    
    adm_cycle.add_phase(phase_a)
    print("✓ Phase A configured\n")
    
    # ========== Phase B: Business Architecture ==========
    print("Initializing Phase B (Business Architecture)...")
    phase_b = PhaseBBusinessArchitecture()
    
    print("\n" + "="*80)
    print("STEP 1: Define Business Capability Model (3 Levels)")
    print("="*80)
    
    # Level 1: Strategic Capabilities
    print("\n📊 Level 1 Capabilities (Strategic):")
    
    customer_mgmt = phase_b.create_capability_hierarchy(
        name="Customer Management",
        description="End-to-end customer lifecycle management",
        level=1,
        maturity_level=MaturityLevel.DEFINED,
        strategic_importance=PriorityLevel.CRITICAL
    )
    print(f"  ✓ {customer_mgmt.name} (Maturity: {customer_mgmt.maturity_level})")
    
    product_mgmt = phase_b.create_capability_hierarchy(
        name="Product & Service Management",
        description="Product portfolio and service delivery management",
        level=1,
        maturity_level=MaturityLevel.MANAGED,
        strategic_importance=PriorityLevel.CRITICAL
    )
    print(f"  ✓ {product_mgmt.name} (Maturity: {product_mgmt.maturity_level})")
    
    operations = phase_b.create_capability_hierarchy(
        name="Operations Management",
        description="Day-to-day operational excellence",
        level=1,
        maturity_level=MaturityLevel.DEFINED,
        strategic_importance=PriorityLevel.HIGH
    )
    print(f"  ✓ {operations.name} (Maturity: {operations.maturity_level})")
    
    digital_channels = phase_b.create_capability_hierarchy(
        name="Digital Channel Management",
        description="Omni-channel digital customer engagement",
        level=1,
        maturity_level=MaturityLevel.INITIAL,
        strategic_importance=PriorityLevel.CRITICAL
    )
    print(f"  ✓ {digital_channels.name} (Maturity: {digital_channels.maturity_level})")
    
    # Level 2: Tactical Capabilities
    print("\n📊 Level 2 Capabilities (Tactical):")
    
    customer_onboarding = phase_b.create_capability_hierarchy(
        name="Customer Onboarding",
        description="Streamlined digital customer onboarding with KYC",
        level=2,
        parent_id=customer_mgmt.id,
        maturity_level=MaturityLevel.DEFINED,
        strategic_importance=PriorityLevel.HIGH
    )
    print(f"  ✓ {customer_onboarding.name} → Parent: {customer_mgmt.name}")
    
    customer_service = phase_b.create_capability_hierarchy(
        name="Customer Service & Support",
        description="24/7 customer support across all channels",
        level=2,
        parent_id=customer_mgmt.id,
        maturity_level=MaturityLevel.MANAGED,
        strategic_importance=PriorityLevel.HIGH
    )
    print(f"  ✓ {customer_service.name} → Parent: {customer_mgmt.name}")
    
    order_fulfillment = phase_b.create_capability_hierarchy(
        name="Order Fulfillment",
        description="End-to-end order processing and fulfillment",
        level=2,
        parent_id=operations.id,
        maturity_level=MaturityLevel.DEFINED,
        strategic_importance=PriorityLevel.HIGH
    )
    print(f"  ✓ {order_fulfillment.name} → Parent: {operations.name}")
    
    mobile_app = phase_b.create_capability_hierarchy(
        name="Mobile Application",
        description="Native iOS and Android applications",
        level=2,
        parent_id=digital_channels.id,
        maturity_level=MaturityLevel.INITIAL,
        strategic_importance=PriorityLevel.CRITICAL
    )
    print(f"  ✓ {mobile_app.name} → Parent: {digital_channels.name}")
    
    web_portal = phase_b.create_capability_hierarchy(
        name="Web Portal",
        description="Responsive web portal with Arabic-first design",
        level=2,
        parent_id=digital_channels.id,
        maturity_level=MaturityLevel.DEFINED,
        strategic_importance=PriorityLevel.CRITICAL
    )
    print(f"  ✓ {web_portal.name} → Parent: {digital_channels.name}")
    
    # Level 3: Operational Capabilities
    print("\n📊 Level 3 Capabilities (Operational):")
    
    kyc_verification = phase_b.create_capability_hierarchy(
        name="KYC Verification",
        description="Automated identity verification with Absher integration",
        level=3,
        parent_id=customer_onboarding.id,
        maturity_level=MaturityLevel.INITIAL,
        strategic_importance=PriorityLevel.CRITICAL
    )
    print(f"  ✓ {kyc_verification.name} → Parent: {customer_onboarding.name}")
    
    # Show capability maturity assessment
    print("\n" + "="*80)
    print("CAPABILITY MATURITY ASSESSMENT")
    print("="*80)
    maturity = phase_b.get_capability_maturity_assessment()
    print(f"Total Capabilities: {maturity['total_capabilities']}")
    print(f"Average Maturity Level: {maturity['average_maturity']:.2f}")
    print(f"Target Maturity: {maturity['target_maturity']}")
    print("\nCapabilities by Maturity:")
    for level, count in maturity['capabilities_by_maturity'].items():
        print(f"  {level}: {count}")
    
    # ========== Define Business Processes ==========
    print("\n" + "="*80)
    print("STEP 2: Define Business Processes with Automation Tracking")
    print("="*80)
    
    # Core Processes
    print("\n🔄 Core Business Processes:")
    
    customer_registration = phase_b.create_business_process(
        name="Customer Registration",
        description="End-to-end customer registration with KYC verification",
        process_type=ProcessType.CORE,
        automation_level=45.0,  # Current: 45%, Target: 70%
        cycle_time_hours=2.5
    )
    customer_registration.add_step("Initiate Registration", 1, "Customer submits application via web/mobile")
    customer_registration.add_step("Absher Verification", 2, "Verify identity via Absher integration")
    customer_registration.add_step("KYC Check", 3, "Automated KYC verification")
    customer_registration.add_step("Manual Review", 4, "Manual review for flagged cases")
    customer_registration.add_step("Account Activation", 5, "Activate customer account")
    customer_registration.add_input("Customer Application")
    customer_registration.add_output("Active Customer Account")
    print(f"  ✓ {customer_registration.name} - Automation: {customer_registration.automation_level}% - Steps: {len(customer_registration.steps)}")
    
    order_processing = phase_b.create_business_process(
        name="Order Processing",
        description="Real-time order processing with payment integration",
        process_type=ProcessType.CORE,
        automation_level=60.0,
        cycle_time_hours=0.5
    )
    order_processing.add_step("Receive Order", 1, "Customer places order via channel")
    order_processing.add_step("Validate Inventory", 2, "Check product availability")
    order_processing.add_step("Process Payment", 3, "SADAD payment processing")
    order_processing.add_step("Confirm Order", 4, "Send confirmation to customer")
    order_processing.add_step("Queue Fulfillment", 5, "Queue order for fulfillment")
    print(f"  ✓ {order_processing.name} - Automation: {order_processing.automation_level}%")
    
    # Supporting Processes
    print("\n🔧 Supporting Processes:")
    
    customer_support = phase_b.create_business_process(
        name="Customer Support",
        description="Multi-channel customer support with AI chatbot",
        process_type=ProcessType.SUPPORTING,
        automation_level=35.0,
        cycle_time_hours=1.0
    )
    customer_support.add_step("Receive Inquiry", 1, "Customer contacts support")
    customer_support.add_step("AI Chatbot Triage", 2, "AI attempts to resolve")
    customer_support.add_step("Agent Assignment", 3, "Escalate to human agent if needed")
    customer_support.add_step("Resolution", 4, "Agent resolves issue")
    customer_support.add_step("Follow-up", 5, "Automated satisfaction survey")
    print(f"  ✓ {customer_support.name} - Automation: {customer_support.automation_level}%")
    
    inventory_management = phase_b.create_business_process(
        name="Inventory Management",
        description="Real-time inventory tracking and replenishment",
        process_type=ProcessType.SUPPORTING,
        automation_level=55.0,
        cycle_time_hours=24.0
    )
    print(f"  ✓ {inventory_management.name} - Automation: {inventory_management.automation_level}%")
    
    # Management Processes
    print("\n📋 Management Processes:")
    
    performance_monitoring = phase_b.create_business_process(
        name="Performance Monitoring",
        description="Real-time business performance monitoring",
        process_type=ProcessType.MANAGEMENT,
        automation_level=80.0,
        cycle_time_hours=0.08  # Near real-time
    )
    print(f"  ✓ {performance_monitoring.name} - Automation: {performance_monitoring.automation_level}%")
    
    compliance_reporting = phase_b.create_business_process(
        name="Compliance Reporting",
        description="Automated NORA and regulatory compliance reporting",
        process_type=ProcessType.MANAGEMENT,
        automation_level=65.0,
        cycle_time_hours=4.0
    )
    print(f"  ✓ {compliance_reporting.name} - Automation: {compliance_reporting.automation_level}%")
    
    # Show automation assessment
    print("\n" + "="*80)
    print("AUTOMATION ASSESSMENT")
    print("="*80)
    automation = phase_b.get_automation_assessment()
    print(f"Total Processes: {automation['total_processes']}")
    print(f"Current Average Automation: {automation['average_automation']:.1f}%")
    print(f"Target Average Automation: {automation['target_automation']:.1f}%")
    print(f"Manual Processes (<25%): {automation['manual_processes']}")
    print(f"Partially Automated (25-75%): {automation['partially_automated']}")
    print(f"Highly Automated (>75%): {automation['automated_processes']}")
    print(f"Gap to Target: {automation['target_automation'] - automation['average_automation']:.1f}%")
    
    # ========== Define Value Streams ==========
    print("\n" + "="*80)
    print("STEP 3: Define Value Streams")
    print("="*80)
    
    phase_b.add_value_stream(
        name="Customer Acquisition",
        description="End-to-end customer acquisition from awareness to activation",
        stages=[
            "Awareness",
            "Consideration",
            "Registration",
            "Onboarding",
            "First Transaction",
            "Activation"
        ],
        value_proposition="Seamless digital onboarding in under 5 minutes",
        stakeholder_value={
            "Customer": "Quick, secure, Arabic-first registration",
            "Business": "Reduced acquisition cost, increased conversion",
            "Regulator": "Complete KYC compliance and audit trail"
        }
    )
    print("✓ Customer Acquisition value stream defined")
    
    phase_b.add_value_stream(
        name="Order to Cash",
        description="Complete order fulfillment and payment cycle",
        stages=[
            "Order Placement",
            "Payment Processing",
            "Order Fulfillment",
            "Delivery",
            "Payment Settlement"
        ],
        value_proposition="Real-time order processing with <100ms response",
        stakeholder_value={
            "Customer": "Instant order confirmation and tracking",
            "Business": "Improved cash flow and customer satisfaction",
            "Finance": "Automated reconciliation and reporting"
        }
    )
    print("✓ Order to Cash value stream defined")
    
    # ========== Define Business KPIs ==========
    print("\n" + "="*80)
    print("STEP 4: Define Business KPIs (Aligned with Repository Targets)")
    print("="*80)
    
    phase_b.add_kpi(
        name="System Availability",
        description="Overall system uptime percentage",
        target_value=99.9,
        current_value=99.5,
        unit="%",
        category="Performance"
    )
    print("✓ System Availability: 99.5% → 99.9% (Gap: 0.4%)")
    
    phase_b.add_kpi(
        name="API Response Time",
        description="Average API response time",
        target_value=100.0,
        current_value=200.0,
        unit="ms",
        category="Performance"
    )
    print("✓ API Response Time: 200ms → 100ms (Gap: 100ms)")
    
    phase_b.add_kpi(
        name="Process Automation",
        description="Percentage of automated business processes",
        target_value=70.0,
        current_value=45.0,
        unit="%",
        category="Efficiency"
    )
    print("✓ Process Automation: 45% → 70% (Gap: 25%)")
    
    phase_b.add_kpi(
        name="Event Processing Capacity",
        description="Events processed per hour",
        target_value=10000000.0,
        current_value=1000000.0,
        unit="events/hour",
        category="Scalability"
    )
    print("✓ Event Processing: 1M → 10M events/hour (Gap: 9M)")
    
    phase_b.add_kpi(
        name="Customer Onboarding Time",
        description="Average time to complete customer onboarding",
        target_value=5.0,
        current_value=150.0,
        unit="minutes",
        category="Customer Experience"
    )
    print("✓ Onboarding Time: 150min → 5min (Gap: 145min)")
    
    phase_b.add_kpi(
        name="NORA Compliance Score",
        description="Saudi NORA framework compliance percentage",
        target_value=95.0,
        current_value=75.0,
        unit="%",
        category="Compliance"
    )
    print("✓ NORA Compliance: 75% → 95% (Gap: 20%)")
    
    # ========== Define Architecture Models ==========
    print("\n" + "="*80)
    print("STEP 5: Define Baseline and Target Architectures")
    print("="*80)
    
    phase_b.set_baseline_architecture({
        "description": "Current As-Is Business Architecture",
        "characteristics": [
            "Manual processes with 45% automation",
            "Siloed capabilities with low maturity",
            "Limited digital channels",
            "200ms average API response time",
            "99.5% system availability"
        ],
        "challenges": [
            "Low process automation",
            "Inconsistent customer experience",
            "Limited scalability",
            "Manual compliance reporting"
        ]
    })
    print("✓ Baseline (As-Is) Architecture documented")
    
    phase_b.set_target_architecture({
        "description": "Target To-Be Business Architecture",
        "characteristics": [
            "70% process automation with AI/ML",
            "Optimized capabilities at managed maturity",
            "Omni-channel digital experience",
            "<100ms API response time",
            "99.9% system availability",
            "10M events/hour processing capacity"
        ],
        "improvements": [
            "API-first microservices architecture",
            "Event-driven real-time processing",
            "Automated KYC with Absher integration",
            "AI-powered customer support",
            "Cloud-native scalable infrastructure",
            "Automated NORA compliance reporting"
        ],
        "enablers": [
            "Azure/AWS multi-cloud",
            "Kubernetes container orchestration",
            "Apache Kafka event streaming",
            "AI/ML for process automation",
            "Zero-trust security"
        ]
    })
    print("✓ Target (To-Be) Architecture documented")
    
    # ========== Perform Gap Analysis ==========
    print("\n" + "="*80)
    print("STEP 6: Perform Comprehensive Gap Analysis")
    print("="*80)
    
    gap_analysis = phase_b.perform_gap_analysis()
    
    print("\n📊 Capability Gaps:")
    print(f"  Capabilities needing improvement: {len(gap_analysis['capability_gaps'])}")
    for gap in gap_analysis['capability_gaps'][:3]:  # Show top 3
        print(f"    • {gap['capability']}: {gap['current_maturity']} → {gap['target_maturity']} (Priority: {gap['priority']})")
    
    print("\n📊 Process Automation Gaps:")
    print(f"  Processes needing automation: {len(gap_analysis['process_gaps'])}")
    for gap in gap_analysis['process_gaps'][:3]:  # Show top 3
        print(f"    • {gap['process']}: {gap['current_automation']:.0f}% → {gap['target_automation']:.0f}% (Gap: {gap['gap']:.0f}%)")
    
    print("\n📊 Overall Automation Gap:")
    auto_gap = gap_analysis['automation_gaps']
    print(f"  Current: {auto_gap['current_average']:.1f}%")
    print(f"  Target: {auto_gap['target_average']:.1f}%")
    print(f"  Gap: {auto_gap['gap']:.1f}%")
    print(f"  Processes needing work: {auto_gap['processes_needing_automation']}")
    
    print("\n📊 Maturity Gap:")
    maturity_gap = gap_analysis['maturity_gaps']
    print(f"  Current Average: {maturity_gap['current_average']:.2f}")
    print(f"  Target Average: {maturity_gap['target_average']:.2f}")
    print(f"  Gap: {maturity_gap['gap']:.2f}")
    print(f"  Capabilities needing work: {maturity_gap['capabilities_needing_improvement']}")
    
    # ========== Add to ADM Cycle ==========
    adm_cycle.add_phase(phase_b)
    
    # ========== Execute Phase B ==========
    print("\n" + "="*80)
    print("STEP 7: Execute Phase B")
    print("="*80)
    
    results = phase_b.execute()
    
    print(f"\n✓ Phase B Execution Complete")
    print(f"  Status: {results['status']}")
    print(f"  Progress: {results['progress']:.1f}%")
    print(f"  Deliverables Generated: {len(results['deliverables'])}")
    
    # ========== Show KPI Dashboard ==========
    print("\n" + "="*80)
    print("KPI DASHBOARD")
    print("="*80)
    
    kpi_dashboard = results['kpi_dashboard']
    print(f"Total KPIs: {kpi_dashboard['total_kpis']}")
    print(f"On Target: {kpi_dashboard['on_target']}")
    print(f"Needs Improvement: {kpi_dashboard['needs_improvement']}")
    print("\nKPI Details:")
    for kpi in kpi_dashboard['kpis']:
        status = "✓" if kpi['current_value'] >= kpi['target_value'] else "⚠"
        print(f"  {status} {kpi['name']}: {kpi['current_value']}{kpi['unit']} → {kpi['target_value']}{kpi['unit']}")
    
    # ========== Show Activities Status ==========
    print("\n" + "="*80)
    print("PHASE B ACTIVITIES STATUS")
    print("="*80)
    
    for activity in results['activities']:
        status_icon = "✓" if activity['status'] == 'completed' else "○"
        print(f"{status_icon} {activity['name']}: {activity['status'].upper()}")
    
    # ========== Save Results ==========
    print("\n" + "="*80)
    print("Saving Results...")
    print("="*80)
    
    output_file = "phase_b_business_architecture_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"✓ Results saved to: {output_file}")
    
    # ========== Summary ==========
    print("\n" + "="*80)
    print("PHASE B SUMMARY")
    print("="*80)
    print(f"""
Business Capabilities: {results['business_capabilities']['count']}
  • Average Maturity: {results['business_capabilities']['maturity_assessment']['average_maturity']:.2f}
  • Target Maturity: {results['business_capabilities']['maturity_assessment']['target_maturity']}

Business Processes: {results['business_processes']['count']}
  • Average Automation: {results['business_processes']['automation_assessment']['average_automation']:.1f}%
  • Target Automation: {results['business_processes']['automation_assessment']['target_automation']:.1f}%
  • Manual Processes: {results['business_processes']['automation_assessment']['manual_processes']}

Value Streams: {len(results['value_streams'])}

Gap Analysis: ✓ Complete
  • Capability Gaps: {len(gap_analysis['capability_gaps'])}
  • Process Gaps: {len(gap_analysis['process_gaps'])}
  • Automation Gap: {gap_analysis['automation_gaps']['gap']:.1f}%

KPIs Tracked: {kpi_dashboard['total_kpis']}
  • On Target: {kpi_dashboard['on_target']}
  • Needs Improvement: {kpi_dashboard['needs_improvement']}

Deliverables:
  ✓ Business Architecture Definition Document
  ✓ Business Capability Catalog
  ✓ Business Process Catalog

Phase Status: {results['status']}
Progress: {results['progress']:.1f}%
    """)
    
    print("="*80)
    print("Phase B: Business Architecture - Complete!")
    print("="*80)
    print(f"\nNext Step: Phase C - Information Systems Architecture")
    print(f"Focus: Application architecture, data architecture, integration patterns")
    
    return results


if __name__ == "__main__":
    results = create_business_architecture_example()
