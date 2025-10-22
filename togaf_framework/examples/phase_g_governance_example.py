"""
Phase G: Implementation Governance - Complete Example

Demonstrates comprehensive implementation governance including:
- Architecture contracts
- Compliance assessments
- Deviation management
- Implementation reviews
- Metrics tracking
"""

import json
from datetime import date, timedelta

from togaf_framework.adm.phase_g_governance import (
    PhaseGImplementationGovernance,
    ArchitectureContract, ComplianceCheck, ArchitectureDeviation,
    ImplementationReview, ImplementationMetrics,
    ContractType, ComplianceType, DeviationType, ReviewType,
    ComplianceStatus, RiskLevel
)


def main():
    print("Phase G: Implementation Governance - Complete Example")
    print("=" * 60)
    
    # Initialize Phase G
    phase_g = PhaseGImplementationGovernance()
    
    # Step 1: Define Architecture Contracts
    print("\nStep 1: Defining architecture contracts...")
    
    contract1 = ArchitectureContract(
        name="Cloud Platform Implementation Contract",
        description="Contract for cloud infrastructure implementation",
        contract_type=ContractType.IMPLEMENTATION_CONTRACT,
        party_a="Enterprise Architecture Team",
        party_b="Cloud Platform Team",
        start_date=date(2025, 1, 1),
        end_date=date(2025, 6, 30)
    )
    contract1.add_term("All infrastructure must use approved Terraform modules")
    contract1.add_term("Multi-region deployment required for critical services")
    contract1.add_term("Security baseline must be applied to all resources")
    contract1.add_obligation("Cloud Platform Team", "Implement infrastructure as code")
    contract1.add_obligation("Cloud Platform Team", "Document all architecture decisions")
    contract1.add_obligation("Enterprise Architecture Team", "Provide reference architectures")
    contract1.add_obligation("Enterprise Architecture Team", "Review designs within 5 business days")
    contract1.add_success_criterion("99.9% infrastructure availability")
    contract1.add_success_criterion("100% compliance with security baseline")
    contract1.add_success_criterion("Zero critical security findings")
    phase_g.add_architecture_contract(contract1)
    
    contract2 = ArchitectureContract(
        name="Microservices Development Contract",
        description="Contract for microservices application development",
        contract_type=ContractType.DESIGN_CONTRACT,
        party_a="Enterprise Architecture Team",
        party_b="Application Development Team",
        start_date=date(2025, 2, 1),
        end_date=date(2025, 8, 31)
    )
    contract2.add_term("All services must expose RESTful APIs")
    contract2.add_term("API documentation required using OpenAPI 3.0")
    contract2.add_term("Service mesh integration mandatory")
    contract2.add_obligation("Application Development Team", "Follow 12-factor app principles")
    contract2.add_obligation("Application Development Team", "Implement distributed tracing")
    contract2.add_obligation("Enterprise Architecture Team", "Provide API templates")
    contract2.add_success_criterion("API response time < 100ms for 95th percentile")
    contract2.add_success_criterion("100% API documentation coverage")
    phase_g.add_architecture_contract(contract2)
    
    print(f"Defined {len(phase_g.architecture_contracts)} architecture contracts")
    
    # Step 2: Configure Compliance Checks
    print("\nStep 2: Configuring compliance checks...")
    
    check1 = ComplianceCheck(
        name="Cloud Infrastructure Compliance",
        description="Verify cloud infrastructure meets architecture standards",
        compliance_type=ComplianceType.TECHNICAL_COMPLIANCE,
        target_component="Cloud Platform"
    )
    check1.reviewer = "Senior Cloud Architect"
    check1.add_finding("All resources deployed using IaC - compliant")
    check1.add_finding("Multi-region configuration implemented correctly")
    check1.add_finding("Security groups follow least privilege principle")
    check1.add_recommendation("Consider implementing automated compliance scanning")
    check1.set_result(ComplianceStatus.COMPLIANT, 92.0)
    phase_g.add_compliance_check(check1)
    
    check2 = ComplianceCheck(
        name="API Design Compliance",
        description="Verify API designs follow standards",
        compliance_type=ComplianceType.DESIGN_COMPLIANCE,
        target_component="Microservices APIs"
    )
    check2.reviewer = "Lead Application Architect"
    check2.add_finding("OpenAPI documentation complete for all endpoints")
    check2.add_finding("RESTful conventions followed")
    check2.add_finding("Minor: Inconsistent error response format in 2 services")
    check2.add_recommendation("Standardize error responses across all services")
    check2.set_result(ComplianceStatus.PARTIALLY_COMPLIANT, 85.0)
    phase_g.add_compliance_check(check2)
    
    check3 = ComplianceCheck(
        name="Security Baseline Compliance",
        description="Verify security controls implementation",
        compliance_type=ComplianceType.SECURITY_COMPLIANCE,
        target_component="All Systems"
    )
    check3.reviewer = "Security Architect"
    check3.add_finding("Encryption at rest enabled for all data stores")
    check3.add_finding("Encryption in transit enforced")
    check3.add_finding("Identity and access management properly configured")
    check3.add_finding("Logging and monitoring comprehensive")
    check3.set_result(ComplianceStatus.COMPLIANT, 95.0)
    phase_g.add_compliance_check(check3)
    
    check4 = ComplianceCheck(
        name="Data Architecture Compliance",
        description="Verify data architecture standards",
        compliance_type=ComplianceType.DATA_COMPLIANCE,
        target_component="Data Platform"
    )
    check4.reviewer = "Data Architect"
    check4.add_finding("Data models documented")
    check4.add_finding("Critical: Data retention policies not fully implemented")
    check4.add_finding("GDPR compliance gaps identified")
    check4.add_recommendation("Implement automated data retention")
    check4.add_recommendation("Complete GDPR compliance assessment")
    check4.set_result(ComplianceStatus.NON_COMPLIANT, 65.0)
    phase_g.add_compliance_check(check4)
    
    print(f"Configured {len(phase_g.compliance_checks)} compliance checks")
    
    # Step 3: Track Architecture Deviations
    print("\nStep 3: Tracking architecture deviations...")
    
    deviation1 = ArchitectureDeviation(
        name="Database Technology Deviation",
        description="Use of PostgreSQL instead of standard MySQL",
        deviation_type=DeviationType.TECHNICAL,
        component="Customer Service Database"
    )
    deviation1.set_severity(RiskLevel.MEDIUM, "May impact support and maintenance")
    deviation1.set_justification("PostgreSQL required for advanced geospatial features")
    deviation1.set_mitigation("Team trained on PostgreSQL, documentation provided")
    deviation1.approve("Chief Architect")
    phase_g.add_deviation(deviation1)
    
    deviation2 = ArchitectureDeviation(
        name="Direct Database Access",
        description="Mobile app directly accessing database",
        deviation_type=DeviationType.TECHNICAL,
        component="Mobile Application"
    )
    deviation2.set_severity(RiskLevel.HIGH, "Violates API-first principle, security concern")
    deviation2.set_justification("Performance requirements for offline sync")
    deviation2.set_mitigation("Implementing API layer, database access to be removed in next release")
    deviation2.approve("Chief Architect")
    phase_g.add_deviation(deviation2)
    
    deviation3 = ArchitectureDeviation(
        name="Custom Authentication",
        description="Custom auth instead of SSO",
        deviation_type=DeviationType.SECURITY,
        component="Legacy Integration"
    )
    deviation3.set_severity(RiskLevel.MEDIUM, "Increases security management complexity")
    deviation3.set_justification("Legacy system doesn't support SAML/OAuth2")
    deviation3.set_mitigation("Isolated network segment, additional monitoring")
    deviation3.approve("Security Architect")
    phase_g.add_deviation(deviation3)
    
    print(f"Tracked {len(phase_g.deviations)} architecture deviations")
    
    # Step 4: Conduct Implementation Reviews
    print("\nStep 4: Conducting implementation reviews...")
    
    review1 = ImplementationReview(
        name="Cloud Platform Design Review",
        description="Review of cloud infrastructure design",
        review_type=ReviewType.DESIGN_REVIEW,
        project="Cloud Migration"
    )
    review1.add_reviewer("Chief Architect")
    review1.add_reviewer("Senior Cloud Architect")
    review1.add_attendee("Cloud Platform Lead")
    review1.add_attendee("Security Architect")
    review1.add_artifact("Infrastructure Architecture Diagram")
    review1.add_artifact("Network Design Document")
    review1.add_artifact("Security Controls Matrix")
    review1.add_finding("design", "Multi-region architecture well designed", "info")
    review1.add_finding("security", "Missing DDoS protection configuration", "high")
    review1.add_finding("cost", "Over-provisioned compute resources", "medium")
    review1.add_decision("Approve design with conditions")
    review1.add_action_item("Configure DDoS protection", "Cloud Platform Lead", "2025-11-01")
    review1.add_action_item("Right-size compute resources", "Cloud Platform Lead", "2025-11-15")
    review1.set_outcome("Conditionally Approved")
    phase_g.add_review(review1)
    
    review2 = ImplementationReview(
        name="Microservices Code Review",
        description="Architecture review of microservices implementation",
        review_type=ReviewType.CODE_REVIEW,
        project="Microservices Development"
    )
    review2.add_reviewer("Lead Application Architect")
    review2.add_attendee("Development Team Lead")
    review2.add_artifact("Service Source Code")
    review2.add_artifact("API Contracts")
    review2.add_finding("architecture", "Service boundaries well defined", "info")
    review2.add_finding("technical", "Missing circuit breaker implementation", "high")
    review2.add_finding("performance", "Inefficient database queries", "medium")
    review2.add_decision("Remediation required before deployment")
    review2.add_action_item("Implement circuit breakers", "Dev Team", "2025-11-10")
    review2.add_action_item("Optimize database queries", "Dev Team", "2025-11-05")
    review2.set_outcome("Remediation Required")
    phase_g.add_review(review2)
    
    print(f"Conducted {len(phase_g.reviews)} implementation reviews")
    
    # Step 5: Track Implementation Metrics
    print("\nStep 5: Tracking implementation metrics...")
    
    metrics1 = ImplementationMetrics(
        name="Cloud Platform Metrics",
        project="Cloud Migration"
    )
    metrics1.set_metric("infrastructure_compliance", 92.0, 90.0)
    metrics1.set_metric("security_score", 95.0, 90.0)
    metrics1.set_metric("availability", 99.92, 99.9)
    metrics1.set_metric("deployment_frequency", 15.0, 10.0)  # per week
    metrics1.set_metric("mean_time_to_recovery", 12.0, 15.0)  # minutes
    phase_g.add_metrics(metrics1)
    
    metrics2 = ImplementationMetrics(
        name="Application Development Metrics",
        project="Microservices Development"
    )
    metrics2.set_metric("api_compliance", 85.0, 90.0)
    metrics2.set_metric("test_coverage", 78.0, 80.0)
    metrics2.set_metric("api_response_time", 95.0, 100.0)  # ms
    metrics2.set_metric("error_rate", 0.5, 1.0)  # percentage
    metrics2.set_metric("documentation_coverage", 100.0, 100.0)
    phase_g.add_metrics(metrics2)
    
    metrics3 = ImplementationMetrics(
        name="Security Implementation Metrics",
        project="Security Baseline"
    )
    metrics3.set_metric("security_controls_implemented", 95.0, 100.0)
    metrics3.set_metric("vulnerability_remediation_time", 3.0, 5.0)  # days
    metrics3.set_metric("security_incidents", 0.0, 0.0)
    metrics3.set_metric("compliance_score", 92.0, 95.0)
    phase_g.add_metrics(metrics3)
    
    print(f"Tracking metrics for {len(phase_g.metrics)} projects")
    
    # Step 6: Define Governance Framework
    print("\nStep 6: Defining governance framework...")
    
    phase_g.add_governance_policy("All architecture decisions must be documented in ADR format")
    phase_g.add_governance_policy("Design reviews required for all new components")
    phase_g.add_governance_policy("Compliance checks mandatory before production deployment")
    phase_g.add_governance_policy("Deviations require Architecture Board approval")
    phase_g.add_governance_policy("Monthly architecture compliance reporting")
    
    phase_g.schedule_review("Cloud Migration", "Bi-weekly design reviews")
    phase_g.schedule_review("Microservices Development", "Weekly architecture syncs")
    phase_g.schedule_review("Security Baseline", "Monthly security assessments")
    
    phase_g.add_escalation_procedure(
        "Critical compliance violation",
        "Immediate notification to Chief Architect and CTO",
        "Architecture Governance Lead"
    )
    phase_g.add_escalation_procedure(
        "Unapproved deviation discovered",
        "Architecture Board review within 48 hours",
        "Architecture Governance Lead"
    )
    phase_g.add_escalation_procedure(
        "Project behind schedule",
        "Weekly status review with stakeholders",
        "PMO"
    )
    
    print(f"Defined {len(phase_g.governance_policies)} governance policies")
    print(f"Scheduled reviews for {len(phase_g.review_schedule)} projects")
    print(f"Configured {len(phase_g.escalation_procedures)} escalation procedures")
    
    # Step 7: Execute Phase G
    print("\nStep 7: Executing Phase G...")
    results = phase_g.execute()
    
    print(f"\nPhase Status: {results['status']}")
    print(f"Completion: {results['completion_percentage']}%")
    
    # Summary
    print("\n" + "=" * 60)
    print("GOVERNANCE SUMMARY")
    print("=" * 60)
    
    compliance_summary = results['summaries']['compliance']
    print(f"\nCompliance Overview:")
    print(f"  Total Checks: {compliance_summary['total']}")
    print(f"  Compliant: {compliance_summary['compliant']}")
    print(f"  Non-Compliant: {compliance_summary['non_compliant']}")
    print(f"  Pending: {compliance_summary['pending']}")
    print(f"  Average Score: {compliance_summary['average_score']:.1f}%")
    
    deviation_summary = results['summaries']['deviations']
    print(f"\nDeviation Overview:")
    print(f"  Total Deviations: {deviation_summary['total']}")
    print(f"  Approved: {deviation_summary['approved']}")
    print(f"  Resolved: {deviation_summary['resolved']}")
    print(f"  By Severity: {deviation_summary['by_severity']}")
    
    metrics_summary = results['summaries']['metrics']
    print(f"\nMetrics Overview:")
    print(f"  Projects Tracked: {metrics_summary['projects']}")
    print(f"  Overall Compliance: {metrics_summary['overall_compliance']:.1f}%")
    
    print(f"\nActive Contracts: {len(results['contracts'])}")
    print(f"Reviews Conducted: {len(results['reviews'])}")
    
    # Step 8: Generate Deliverables
    print("\n" + "=" * 60)
    print("DELIVERABLES")
    print("=" * 60)
    
    oversight_report = phase_g.generate_implementation_oversight_report()
    compliance_report = phase_g.generate_compliance_assessment_report()
    contract_docs = phase_g.generate_architecture_contract_documentation()
    
    print(f"\n1. {oversight_report.name}")
    print(f"   Type: {oversight_report.deliverable_type.value}")
    
    print(f"\n2. {compliance_report.name}")
    print(f"   Type: {compliance_report.deliverable_type.value}")
    
    print(f"\n3. {contract_docs.name}")
    print(f"   Type: {contract_docs.deliverable_type.value}")
    
    # Save results
    print("\n" + "=" * 60)
    output_file = "phase_g_governance_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Results saved to: {output_file}")
    print(f"File size: {len(json.dumps(results)):,} bytes")
    
    print("\n" + "=" * 60)
    print("KEY ACHIEVEMENTS")
    print("=" * 60)
    print(f"- {len(phase_g.architecture_contracts)} architecture contracts established")
    print(f"- {compliance_summary['total']} compliance assessments completed")
    print(f"- {compliance_summary['average_score']:.1f}% average compliance score")
    print(f"- {deviation_summary['total']} deviations managed and tracked")
    print(f"- {len(phase_g.reviews)} implementation reviews conducted")
    print(f"- {metrics_summary['projects']} projects monitored")
    print(f"- {metrics_summary['overall_compliance']:.1f}% overall compliance rate")
    print(f"- {len(phase_g.governance_policies)} governance policies active")
    
    print("\nPhase G: Implementation Governance completed successfully!")


if __name__ == "__main__":
    main()
