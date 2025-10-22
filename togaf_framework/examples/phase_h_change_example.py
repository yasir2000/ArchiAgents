"""
Phase H: Architecture Change Management - Complete Example

Demonstrates comprehensive architecture change management including:
- Change request processing
- Architecture monitoring
- Lessons learned capture
- Knowledge repository management
"""

import json
from datetime import date, datetime, timedelta

from togaf_framework.adm.phase_h_change import (
    PhaseHChangeManagement,
    ArchitectureChangeRequest, ArchitectureMonitor,
    LessonLearned, KnowledgeAsset,
    ChangeRequestStatus, ChangeImpact, MonitoringType
)
from togaf_framework.core.enums import ChangeType, PriorityLevel


def main():
    print("Phase H: Architecture Change Management - Complete Example")
    print("=" * 60)
    
    # Initialize Phase H
    phase_h = PhaseHChangeManagement()
    
    # Step 1: Define Change Requests
    print("\nStep 1: Creating architecture change requests...")
    
    request1 = ArchitectureChangeRequest(
        name="Adopt Kubernetes for Container Orchestration",
        description="Migrate from Docker Swarm to Kubernetes",
        change_type=ChangeType.STRATEGIC,
        requestor="Cloud Platform Team",
        priority=PriorityLevel.HIGH
    )
    request1.assess_impact(
        "Requires retraining team, changes deployment processes, improves scalability",
        ChangeImpact.HIGH
    )
    request1.add_affected_component("Container Platform")
    request1.add_affected_component("CI/CD Pipeline")
    request1.add_affected_component("Monitoring Infrastructure")
    request1.set_estimates("6 months", 450000)
    request1.add_benefit("Better scalability and resilience")
    request1.add_benefit("Industry standard with large ecosystem")
    request1.add_benefit("Advanced networking and service mesh")
    request1.add_risk("Team learning curve")
    request1.add_risk("Migration complexity")
    request1.approve()
    phase_h.add_change_request(request1)
    
    request2 = ArchitectureChangeRequest(
        name="Implement GraphQL API Layer",
        description="Add GraphQL alongside REST APIs",
        change_type=ChangeType.TACTICAL,
        requestor="Application Team",
        priority=PriorityLevel.MEDIUM
    )
    request2.assess_impact(
        "Provides flexible querying, requires API gateway updates",
        ChangeImpact.MEDIUM
    )
    request2.add_affected_component("API Gateway")
    request2.add_affected_component("Backend Services")
    request2.set_estimates("3 months", 180000)
    request2.add_benefit("Flexible client-driven queries")
    request2.add_benefit("Reduced over-fetching")
    request2.add_risk("Additional complexity in API management")
    request2.approve()
    request2.implement()
    phase_h.add_change_request(request2)
    
    request3 = ArchitectureChangeRequest(
        name="Adopt Serverless Functions",
        description="Introduce AWS Lambda for event processing",
        change_type=ChangeType.TACTICAL,
        requestor="Data Team",
        priority=PriorityLevel.MEDIUM
    )
    request3.assess_impact(
        "Reduces operational overhead, changes deployment model",
        ChangeImpact.MEDIUM
    )
    request3.add_affected_component("Event Processing")
    request3.add_affected_component("Data Pipeline")
    request3.set_estimates("2 months", 120000)
    request3.add_benefit("Pay-per-use cost model")
    request3.add_benefit("Auto-scaling built-in")
    request3.add_risk("Vendor lock-in concerns")
    phase_h.add_change_request(request3)
    
    request4 = ArchitectureChangeRequest(
        name="Upgrade PostgreSQL to Version 15",
        description="Upgrade database platform for performance and features",
        change_type=ChangeType.OPERATIONAL,
        requestor="Database Team",
        priority=PriorityLevel.LOW
    )
    request4.assess_impact(
        "Requires testing and validation, minimal application changes",
        ChangeImpact.LOW
    )
    request4.add_affected_component("Database Platform")
    request4.set_estimates("1 month", 50000)
    request4.add_benefit("Performance improvements")
    request4.add_benefit("New SQL features")
    request4.approve()
    request4.implement()
    phase_h.add_change_request(request4)
    
    print(f"Created {len(phase_h.change_requests)} change requests")
    
    # Step 2: Deploy Monitoring
    print("\nStep 2: Deploying architecture monitors...")
    
    monitor1 = ArchitectureMonitor(
        name="Cloud Cost Monitor",
        description="Track cloud infrastructure costs",
        monitoring_type=MonitoringType.TECHNOLOGY,
        target="Cloud Platform"
    )
    monitor1.set_frequency("Daily")
    monitor1.add_metric("monthly_cost", 100000.0)
    monitor1.add_metric("cost_per_transaction", 0.05)
    monitor1.record_observation("monthly_cost", 95000.0, datetime.now())
    monitor1.record_observation("cost_per_transaction", 0.048, datetime.now())
    phase_h.add_monitor(monitor1)
    
    monitor2 = ArchitectureMonitor(
        name="API Performance Monitor",
        description="Track API response times and throughput",
        monitoring_type=MonitoringType.PERFORMANCE,
        target="API Platform"
    )
    monitor2.set_frequency("Continuous")
    monitor2.add_metric("p95_response_time", 100.0)  # ms
    monitor2.add_metric("requests_per_second", 1000.0)
    monitor2.add_metric("error_rate", 1.0)  # percentage
    monitor2.record_observation("p95_response_time", 85.0, datetime.now())
    monitor2.record_observation("requests_per_second", 1250.0, datetime.now())
    monitor2.record_observation("error_rate", 0.5, datetime.now())
    phase_h.add_monitor(monitor2)
    
    monitor3 = ArchitectureMonitor(
        name="Security Compliance Monitor",
        description="Monitor security posture and compliance",
        monitoring_type=MonitoringType.COMPLIANCE,
        target="Security Infrastructure"
    )
    monitor3.set_frequency("Weekly")
    monitor3.add_metric("compliance_score", 90.0)
    monitor3.add_metric("critical_vulnerabilities", 0.0)
    monitor3.add_metric("patch_coverage", 95.0)
    monitor3.record_observation("compliance_score", 94.0, datetime.now())
    monitor3.record_observation("critical_vulnerabilities", 0.0, datetime.now())
    monitor3.record_observation("patch_coverage", 97.0, datetime.now())
    phase_h.add_monitor(monitor3)
    
    monitor4 = ArchitectureMonitor(
        name="Business Capability Monitor",
        description="Track business capability maturity",
        monitoring_type=MonitoringType.CAPABILITY,
        target="Digital Capabilities"
    )
    monitor4.set_frequency("Monthly")
    monitor4.add_metric("automation_rate", 70.0)
    monitor4.add_metric("process_efficiency", 85.0)
    monitor4.record_observation("automation_rate", 72.0, datetime.now())
    monitor4.record_observation("process_efficiency", 87.0, datetime.now())
    phase_h.add_monitor(monitor4)
    
    # Simulate threshold breach
    monitor2.record_observation("p95_response_time", 120.0, datetime.now())
    
    print(f"Deployed {len(phase_h.monitors)} architecture monitors")
    print(f"Total observations: {sum(len(m.observations) for m in phase_h.monitors.values())}")
    print(f"Active alerts: {sum(len(m.alerts) for m in phase_h.monitors.values())}")
    
    # Step 3: Capture Lessons Learned
    print("\nStep 3: Capturing lessons learned...")
    
    lesson1 = LessonLearned(
        name="Microservices Communication Patterns",
        description="Service mesh greatly simplifies microservices networking",
        category="Architecture Pattern",
        source_project="Microservices Migration"
    )
    lesson1.set_impact("Reduced network configuration complexity by 60%")
    lesson1.add_recommendation("Adopt service mesh (Istio) early in microservices journey")
    lesson1.add_recommendation("Invest in team training on service mesh concepts")
    lesson1.apply_to_project("Payment Services Modernization")
    phase_h.add_lesson_learned(lesson1)
    
    lesson2 = LessonLearned(
        name="Database Migration Strategy",
        description="Dual-write pattern effective for zero-downtime migration",
        category="Migration Strategy",
        source_project="Database Platform Upgrade"
    )
    lesson2.set_impact("Achieved zero-downtime migration for critical databases")
    lesson2.add_recommendation("Use dual-write with eventual consistency checks")
    lesson2.add_recommendation("Maintain rollback capability for 2 weeks post-migration")
    lesson2.apply_to_project("Customer Database Migration")
    lesson2.apply_to_project("Order Management Migration")
    phase_h.add_lesson_learned(lesson2)
    
    lesson3 = LessonLearned(
        name="Cloud Cost Optimization",
        description="Reserved instances and autoscaling reduced costs significantly",
        category="Cost Management",
        source_project="Cloud Cost Optimization"
    )
    lesson3.set_impact("30% reduction in cloud infrastructure costs")
    lesson3.add_recommendation("Use reserved instances for baseline workloads")
    lesson3.add_recommendation("Implement aggressive autoscaling for variable workloads")
    lesson3.add_recommendation("Regular review of unused resources")
    phase_h.add_lesson_learned(lesson3)
    
    lesson4 = LessonLearned(
        name="API Versioning Strategy",
        description="URL-based versioning worked better than header-based",
        category="API Design",
        source_project="API Platform Redesign"
    )
    lesson4.set_impact("Improved API adoption and reduced client confusion")
    lesson4.add_recommendation("Use URL-based versioning (v1, v2) for clarity")
    lesson4.add_recommendation("Maintain 2 versions simultaneously during transitions")
    lesson4.apply_to_project("Partner API Development")
    phase_h.add_lesson_learned(lesson4)
    
    print(f"Captured {len(phase_h.lessons_learned)} lessons learned")
    
    # Step 4: Populate Knowledge Repository
    print("\nStep 4: Building knowledge repository...")
    
    asset1 = KnowledgeAsset(
        name="Microservices Reference Architecture",
        description="Standard pattern for microservices implementation",
        asset_type="reference",
        category="Architecture Patterns"
    )
    asset1.add_tag("microservices")
    asset1.add_tag("cloud-native")
    asset1.add_tag("kubernetes")
    for _ in range(15):
        asset1.increment_usage()
    phase_h.add_knowledge_asset(asset1)
    
    asset2 = KnowledgeAsset(
        name="API Design Template",
        description="OpenAPI template with security and versioning",
        asset_type="template",
        category="API Design"
    )
    asset2.add_tag("api")
    asset2.add_tag("rest")
    asset2.add_tag("openapi")
    for _ in range(22):
        asset2.increment_usage()
    phase_h.add_knowledge_asset(asset2)
    
    asset3 = KnowledgeAsset(
        name="Security Baseline Model",
        description="Zero-trust security architecture model",
        asset_type="model",
        category="Security"
    )
    asset3.add_tag("security")
    asset3.add_tag("zero-trust")
    for _ in range(8):
        asset3.increment_usage()
    phase_h.add_knowledge_asset(asset3)
    
    asset4 = KnowledgeAsset(
        name="CI/CD Pipeline Pattern",
        description="GitOps-based deployment pipeline",
        asset_type="pattern",
        category="DevOps"
    )
    asset4.add_tag("cicd")
    asset4.add_tag("gitops")
    asset4.add_tag("automation")
    for _ in range(12):
        asset4.increment_usage()
    phase_h.add_knowledge_asset(asset4)
    
    asset5 = KnowledgeAsset(
        name="Data Architecture Reference",
        description="Data mesh and data lake patterns",
        asset_type="reference",
        category="Data Architecture"
    )
    asset5.add_tag("data")
    asset5.add_tag("data-mesh")
    asset5.add_tag("data-lake")
    for _ in range(6):
        asset5.increment_usage()
    phase_h.add_knowledge_asset(asset5)
    
    print(f"Added {len(phase_h.knowledge_assets)} knowledge assets")
    total_usage = sum(a.usage_count for a in phase_h.knowledge_assets.values())
    print(f"Total asset usage: {total_usage}")
    
    # Step 5: Define Change Management Framework
    print("\nStep 5: Defining change management framework...")
    
    phase_h.add_change_policy("All architecture changes require impact assessment")
    phase_h.add_change_policy("High-impact changes require Architecture Board approval")
    phase_h.add_change_policy("Changes must be documented in architecture repository")
    phase_h.add_change_policy("Post-implementation review mandatory for all changes")
    phase_h.add_change_policy("Lessons learned must be captured and shared")
    
    phase_h.set_approval_threshold("low", "Lead Architect")
    phase_h.set_approval_threshold("medium", "Architecture Review Board")
    phase_h.set_approval_threshold("high", "Architecture Board + CTO")
    phase_h.set_approval_threshold("critical", "Executive Committee")
    
    phase_h.set_review_cycle("Technology Architecture", "Quarterly")
    phase_h.set_review_cycle("Application Architecture", "Monthly")
    phase_h.set_review_cycle("Data Architecture", "Quarterly")
    phase_h.set_review_cycle("Security Architecture", "Monthly")
    
    print(f"Defined {len(phase_h.change_policies)} change policies")
    print(f"Configured {len(phase_h.approval_thresholds)} approval thresholds")
    print(f"Set {len(phase_h.review_cycles)} review cycles")
    
    # Step 6: Execute Phase H
    print("\nStep 6: Executing Phase H...")
    results = phase_h.execute()
    
    print(f"\nPhase Status: {results['status']}")
    print(f"Completion: {results['completion_percentage']}%")
    
    # Summary
    print("\n" + "=" * 60)
    print("CHANGE MANAGEMENT SUMMARY")
    print("=" * 60)
    
    change_summary = results['summaries']['change_requests']
    print(f"\nChange Requests:")
    print(f"  Total: {change_summary['total']}")
    print(f"  Approved: {change_summary['approved']}")
    print(f"  Implemented: {change_summary['implemented']}")
    print(f"  By Priority: {change_summary['by_priority']}")
    print(f"  By Status: {change_summary['by_status']}")
    
    monitoring_summary = results['summaries']['monitoring']
    print(f"\nMonitoring:")
    print(f"  Total Monitors: {monitoring_summary['total']}")
    print(f"  Active: {monitoring_summary['active']}")
    print(f"  Total Alerts: {monitoring_summary['total_alerts']}")
    print(f"  Unresolved Alerts: {monitoring_summary['unresolved_alerts']}")
    print(f"  By Type: {monitoring_summary['by_type']}")
    
    knowledge_summary = results['summaries']['knowledge']
    print(f"\nKnowledge Repository:")
    print(f"  Lessons Learned: {knowledge_summary['lessons_learned']}")
    print(f"  Knowledge Assets: {knowledge_summary['knowledge_assets']}")
    print(f"  Total Asset Usage: {knowledge_summary['asset_usage']}")
    if 'by_type' in knowledge_summary:
        print(f"  Assets by Type: {knowledge_summary['by_type']}")
    
    # Step 7: Generate Deliverables
    print("\n" + "=" * 60)
    print("DELIVERABLES")
    print("=" * 60)
    
    change_report = phase_h.generate_change_management_report()
    lessons_catalog = phase_h.generate_lessons_learned_catalog()
    repository_report = phase_h.generate_architecture_repository_report()
    
    print(f"\n1. {change_report.name}")
    print(f"   Phase: {change_report.phase}")
    
    print(f"\n2. {lessons_catalog.name}")
    print(f"   Phase: {lessons_catalog.phase}")
    
    print(f"\n3. {repository_report.name}")
    print(f"   Phase: {repository_report.phase}")
    
    # Save results
    print("\n" + "=" * 60)
    output_file = "phase_h_change_management_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Results saved to: {output_file}")
    print(f"File size: {len(json.dumps(results)):,} bytes")
    
    print("\n" + "=" * 60)
    print("KEY ACHIEVEMENTS")
    print("=" * 60)
    print(f"- {change_summary['total']} architecture change requests processed")
    print(f"- {change_summary['implemented']} changes successfully implemented")
    print(f"- {monitoring_summary['total']} monitors deployed across architecture")
    print(f"- {knowledge_summary['lessons_learned']} lessons learned captured")
    print(f"- {knowledge_summary['knowledge_assets']} knowledge assets maintained")
    print(f"- {knowledge_summary['asset_usage']} total asset reuses")
    print(f"- {len(phase_h.change_policies)} change policies established")
    print(f"- Continuous architecture improvement process active")
    
    print("\nPhase H: Architecture Change Management completed successfully!")
    print("\n" + "=" * 60)
    print("TOGAF ADM 8-PHASE CYCLE COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    main()
