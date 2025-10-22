"""
TOGAF Phase E: Opportunities and Solutions - Complete Example

This example demonstrates Phase E implementation including:
- Solution building blocks
- Work packages and projects
- Implementation strategy
- Transition architectures
- Cost-benefit analysis
- Risk assessment
- Readiness evaluation
"""

import json
import os
from togaf_framework.adm import PhaseEOpportunitiesAndSolutions
from togaf_framework.adm.adm_cycle import ADMCycle

print("=" * 80)
print("TOGAF Phase E: Opportunities and Solutions - Complete Example")
print("=" * 80)

# Create ADM Cycle
print("\nCreating ADM Cycle...")
adm_cycle = ADMCycle("Digital Transformation - Opportunities and Solutions")

# Initialize Phase E
print("Initializing Phase E (Opportunities and Solutions)...\n")
phase_e = PhaseEOpportunitiesAndSolutions("Opportunities and Solutions")

# ================================================================================
# STEP 1: Define Solution Building Blocks
# ================================================================================
print("=" * 80)
print("STEP 1: Define Solution Building Blocks")
print("=" * 80)

solutions = [
    ("Microservices Platform", "Container orchestration and service mesh", 
     "cloud_service", "technology", "medium", 250000, 6, ["Cloud Infrastructure"]),
    
    ("Customer Portal", "Modern web portal with mobile app",
     "custom_development", "application", "high", 500000, 12, ["API Gateway", "Identity Management"]),
    
    ("API Management Platform", "Enterprise API gateway and management",
     "cots", "technology", "medium", 150000, 4, ["Cloud Infrastructure"]),
    
    ("Data Lake", "Centralized data storage and analytics",
     "cloud_service", "data", "medium", 200000, 8, ["Cloud Infrastructure", "Data Migration"]),
    
    ("Identity and Access Management", "Enterprise SSO and RBAC",
     "saas", "security", "low", 100000, 3, []),
    
    ("CI/CD Pipeline", "Automated build and deployment",
     "open_source", "technology", "medium", 80000, 4, ["Cloud Infrastructure"]),
    
    ("Monitoring and Observability", "Full-stack monitoring solution",
     "cloud_service", "technology", "low", 120000, 3, ["Cloud Infrastructure"]),
    
    ("Legacy System Integration", "Integration adapters for legacy systems",
     "custom_development", "application", "high", 400000, 10, ["API Gateway"]),
    
    ("Data Migration Tools", "ETL and data migration utilities",
     "custom_development", "data", "medium", 180000, 6, ["Data Lake"]),
    
    ("Training and Documentation", "User training and system documentation",
     "custom_development", "application", "low", 150000, 4, ["Customer Portal"])
]

print("\nSolution Building Blocks:")
for name, desc, sbb_type, category, effort, cost, months, deps in solutions:
    phase_e.add_solution_building_block(
        name, desc, sbb_type, category, effort, cost, months, deps
    )
    print(f"  OK {name}")
    print(f"     Type: {sbb_type}, Cost: ${cost:,}, Duration: {months} months")

# ================================================================================
# STEP 2: Consolidate Gaps from Previous Phases
# ================================================================================
print("\n" + "=" * 80)
print("STEP 2: Consolidate Architecture Gaps")
print("=" * 80)

business_gaps = [
    {"description": "Process automation gap of 13.3%", "priority": "high"},
    {"description": "Customer onboarding time reduction needed", "priority": "high"}
]

data_gaps = [
    {"description": "Data integration across systems", "priority": "high"},
    {"description": "Real-time analytics capability", "priority": "medium"}
]

application_gaps = [
    {"description": "Legacy system modernization", "priority": "high"},
    {"description": "Mobile application development", "priority": "medium"}
]

technology_gaps = [
    {"description": "Cloud infrastructure setup", "priority": "critical"},
    {"description": "Security controls implementation", "priority": "high"}
]

phase_e.consolidate_gaps(business_gaps, data_gaps, application_gaps, technology_gaps)
print(f"OK Consolidated {len(phase_e.consolidated_gaps)} gaps across all domains")

# ================================================================================
# STEP 3: Define Work Packages
# ================================================================================
print("\n" + "=" * 80)
print("STEP 3: Define Work Packages")
print("=" * 80)

work_packages = [
    ("WP1: Cloud Foundation", 
     "Establish cloud infrastructure and platform services",
     ["Deploy Azure/AWS infrastructure", "Setup Kubernetes clusters", "Configure networking"],
     ["Microservices Platform", "API Management Platform", "Cloud Infrastructure"],
     "critical", 450000, 6,
     {"architects": 2, "engineers": 4, "cloud_specialists": 2},
     []),
    
    ("WP2: Security Foundation",
     "Implement security controls and IAM",
     ["Deploy identity management", "Configure zero-trust", "Setup security monitoring"],
     ["Identity and Access Management", "Monitoring and Observability"],
     "critical", 220000, 4,
     {"security_architects": 2, "engineers": 3},
     ["WP1: Cloud Foundation"]),
    
    ("WP3: Data Platform",
     "Build data lake and migration tools",
     ["Setup data lake", "Develop ETL pipelines", "Migrate data"],
     ["Data Lake", "Data Migration Tools"],
     "high", 380000, 8,
     {"data_architects": 2, "data_engineers": 4},
     ["WP1: Cloud Foundation"]),
    
    ("WP4: Application Modernization",
     "Develop customer portal and integrate legacy systems",
     ["Build customer portal", "Develop mobile app", "Integrate legacy systems"],
     ["Customer Portal", "Legacy System Integration"],
     "high", 900000, 12,
     {"solution_architects": 2, "developers": 8, "qa_engineers": 3},
     ["WP1: Cloud Foundation", "WP2: Security Foundation"]),
    
    ("WP5: DevOps Automation",
     "Implement CI/CD and monitoring",
     ["Setup CI/CD pipelines", "Configure monitoring", "Automate deployments"],
     ["CI/CD Pipeline", "Monitoring and Observability"],
     "medium", 200000, 4,
     {"devops_engineers": 3, "sre": 2},
     ["WP1: Cloud Foundation"]),
    
    ("WP6: Training and Transition",
     "Train users and transition to new systems",
     ["Develop training materials", "Conduct training", "Support transition"],
     ["Training and Documentation"],
     "medium", 150000, 4,
     {"trainers": 3, "support_staff": 4},
     ["WP4: Application Modernization"])
]

print("\nWork Packages:")
for name, desc, objectives, sbbs, priority, cost, duration, resources, deps in work_packages:
    phase_e.add_work_package(
        name, desc, objectives, sbbs, priority, cost, duration, resources, deps
    )
    print(f"  OK {name} (Priority: {priority})")
    print(f"     Cost: ${cost:,}, Duration: {duration} months")

# ================================================================================
# STEP 4: Define Implementation Projects
# ================================================================================
print("\n" + "=" * 80)
print("STEP 4: Define Implementation Projects")
print("=" * 80)

projects = [
    ("Digital Platform Transformation",
     "Comprehensive digital transformation program",
     ["WP1: Cloud Foundation", "WP2: Security Foundation", "WP5: DevOps Automation"],
     "2025-Q1", "2026-Q1", 870000, "high",
     "Enables cloud-native architecture and supports Vision 2030 goals",
     ["Cloud infrastructure operational", "Security compliance achieved", "CI/CD automation 100%"]),
    
    ("Customer Experience Modernization",
     "Transform customer-facing applications",
     ["WP4: Application Modernization", "WP6: Training and Transition"],
     "2025-Q2", "2026-Q2", 1050000, "high",
     "Improves customer satisfaction and reduces onboarding time",
     ["Customer portal launched", "Mobile app available", "Legacy integration complete", "User adoption >80%"]),
    
    ("Data and Analytics Platform",
     "Build enterprise data platform",
     ["WP3: Data Platform"],
     "2025-Q2", "2026-Q1", 380000, "medium",
     "Enables data-driven decision making",
     ["Data lake operational", "Real-time analytics available", "Data migration complete"])
]

print("\nImplementation Projects:")
for name, desc, wps, start, end, budget, value, alignment, criteria in projects:
    phase_e.add_project(name, desc, wps, start, end, budget, value, alignment, criteria)
    print(f"  OK {name}")
    print(f"     Budget: ${budget:,}, Timeline: {start} to {end}")
    print(f"     Business Value: {value}")

# ================================================================================
# STEP 5: Define Implementation Strategy
# ================================================================================
print("\n" + "=" * 80)
print("STEP 5: Define Implementation Strategy")
print("=" * 80)

implementation_phases = [
    {
        "phase": "Foundation (Q1 2025 - Q2 2025)",
        "focus": "Cloud infrastructure and security",
        "deliverables": ["Cloud platform", "Security framework", "DevOps foundation"]
    },
    {
        "phase": "Core Systems (Q2 2025 - Q4 2025)",
        "focus": "Data platform and application development",
        "deliverables": ["Data lake", "Customer portal", "API gateway"]
    },
    {
        "phase": "Integration (Q4 2025 - Q1 2026)",
        "focus": "Legacy integration and testing",
        "deliverables": ["Legacy connectors", "End-to-end testing", "Performance optimization"]
    },
    {
        "phase": "Deployment (Q1 2026 - Q2 2026)",
        "focus": "Production deployment and training",
        "deliverables": ["Production rollout", "User training", "Support transition"]
    }
]

phase_e.define_implementation_strategy(
    approach="phased",
    rationale="Phased approach reduces risk, allows for iterative feedback, and ensures stable foundation before building dependent systems",
    phases=implementation_phases,
    critical_success_factors=[
        "Executive sponsorship and governance",
        "Adequate funding and resource allocation",
        "Strong change management",
        "Technical expertise and vendor support",
        "Clear communication and stakeholder engagement"
    ],
    governance_approach="Architecture Board oversight with monthly reviews and phase-gate approvals"
)

print(f"OK Implementation Strategy: {phase_e.migration_approach}")
print(f"   {len(implementation_phases)} phases defined")

# ================================================================================
# STEP 6: Define Transition Architectures
# ================================================================================
print("\n" + "=" * 80)
print("STEP 6: Define Transition Architectures")
print("=" * 80)

transitions = [
    ("Transition Architecture 1.0", "Foundation phase completion", "1.0", "Q2 2025",
     ["Cloud infrastructure", "Security foundation", "DevOps tooling"],
     {"cloud": "operational", "security": "compliant", "automation": "50%"},
     []),
    
    ("Transition Architecture 2.0", "Core systems deployment", "2.0", "Q4 2025",
     ["Data platform", "Customer portal beta", "API management"],
     {"cloud": "optimized", "security": "enhanced", "automation": "75%", "data": "operational"},
     ["Transition Architecture 1.0"]),
    
    ("Transition Architecture 3.0", "Full integration", "3.0", "Q1 2026",
     ["Legacy integration", "Full portal features", "Analytics"],
     {"cloud": "optimized", "security": "enhanced", "automation": "95%", "data": "optimized", "integration": "complete"},
     ["Transition Architecture 2.0"]),
    
    ("Target Architecture", "Final production state", "4.0", "Q2 2026",
     ["All capabilities operational", "Full automation", "Continuous improvement"],
     {"cloud": "optimized", "security": "zero-trust", "automation": "100%", "data": "optimized", "integration": "complete", "monitoring": "comprehensive"},
     ["Transition Architecture 3.0"])
]

print("\nTransition Architectures:")
for name, desc, version, timeframe, capabilities, state, deps in transitions:
    phase_e.add_transition_architecture(name, desc, version, timeframe, capabilities, state, deps)
    print(f"  OK {name} - {timeframe}")
    print(f"     Capabilities: {len(capabilities)}")

# ================================================================================
# STEP 7: Define Constraints
# ================================================================================
print("\n" + "=" * 80)
print("STEP 7: Define Constraints")
print("=" * 80)

business_constraints = [
    ("budget", "Total budget limited to $2.5M for year 1", "high", 
     "Prioritize critical work packages and negotiate vendor discounts"),
    ("time", "Must deliver customer portal by Q2 2026 for business critical deadline", "high",
     "Adopt phased approach with MVP delivery"),
    ("resource", "Limited availability of cloud architects (only 2 available)", "medium",
     "Engage external consultants and provide training"),
    ("regulatory", "NORA compliance required for all systems", "high",
     "Include compliance reviews in all phases")
]

technical_constraints = [
    ("technology", "Must integrate with legacy mainframe systems", "high",
     "Use proven integration patterns and adapters"),
    ("integration", "APIs must support 100ms response time SLA", "medium",
     "Implement caching and optimize data access"),
    ("security", "Zero-trust architecture required", "high",
     "Phased security implementation with foundation first")
]

print("\nBusiness Constraints:")
for c_type, desc, impact, mitigation in business_constraints:
    phase_e.add_business_constraint(c_type, desc, impact, mitigation)
    print(f"  OK {c_type}: {impact} impact")

print("\nTechnical Constraints:")
for c_type, desc, impact, mitigation in technical_constraints:
    phase_e.add_technical_constraint(c_type, desc, impact, mitigation)
    print(f"  OK {c_type}: {impact} impact")

# ================================================================================
# STEP 8: Define Dependencies
# ================================================================================
print("\n" + "=" * 80)
print("STEP 8: Define Key Dependencies")
print("=" * 80)

dependencies = [
    ("Customer Portal", "Identity and Access Management", "technical", 
     "Portal requires SSO and user authentication", "critical"),
    ("Data Lake", "Cloud Infrastructure", "technical",
     "Data lake requires cloud storage and compute", "critical"),
    ("Legacy Integration", "API Gateway", "technical",
     "Legacy systems connect through API gateway", "high"),
    ("Application Modernization", "Security Foundation", "business",
     "Cannot deploy applications without security controls", "critical")
]

print("\nCritical Dependencies:")
for from_comp, to_comp, dep_type, desc, criticality in dependencies:
    phase_e.add_dependency(from_comp, to_comp, dep_type, desc, criticality)
    print(f"  OK {from_comp} -> {to_comp} ({criticality})")

# ================================================================================
# STEP 9: Define Implementation Risks
# ================================================================================
print("\n" + "=" * 80)
print("STEP 9: Define Implementation Risks")
print("=" * 80)

risks = [
    ("Cloud Migration Complexity", "technical", 
     "Complexity of migrating legacy workloads to cloud", "medium", "high",
     "Pilot migration with non-critical systems first, engage cloud migration specialists",
     "Cloud Architect"),
    
    ("Resource Availability", "organizational",
     "Key technical resources may not be available when needed", "medium", "medium",
     "Build resource pipeline early, cross-train team members",
     "Program Manager"),
    
    ("Integration Challenges", "technical",
     "Legacy system integration may be more complex than anticipated", "high", "medium",
     "Conduct integration POC early, allocate buffer time",
     "Integration Lead"),
    
    ("Budget Overrun", "financial",
     "Costs may exceed estimates", "medium", "high",
     "Establish contingency reserve, monthly budget reviews",
     "Finance Director"),
    
    ("Change Resistance", "organizational",
     "Users may resist new systems and processes", "medium", "medium",
     "Strong change management program, early user involvement",
     "Change Manager"),
    
    ("Security Compliance", "external",
     "May not achieve NORA compliance on schedule", "low", "high",
     "Engage compliance experts, conduct early assessments",
     "Security Officer")
]

print("\nImplementation Risks:")
for name, category, desc, prob, impact, mitigation, owner in risks:
    phase_e.add_implementation_risk(name, category, desc, prob, impact, mitigation, owner)
    risk_score = phase_e._calculate_risk_score(prob, impact)
    print(f"  OK {name} (Score: {risk_score}/9)")

# ================================================================================
# STEP 10: Define Readiness Assessments
# ================================================================================
print("\n" + "=" * 80)
print("STEP 10: Define Readiness Assessments")
print("=" * 80)

readiness = [
    ("organizational", "Traditional IT operations", "DevOps culture and practices",
     "Need cultural shift and new skills", "needs_improvement",
     ["DevOps training", "Hire cloud-native engineers", "Agile transformation"]),
    
    ("technical", "On-premises infrastructure", "Cloud-native architecture",
     "Limited cloud experience in team", "needs_improvement",
     ["Cloud certifications", "POC projects", "Vendor workshops"]),
    
    ("financial", "Adequate budget allocated", "Multi-year funding commitment",
     "Year 1 budget secured, future years pending", "ready",
     ["Demonstrate ROI", "Secure multi-year commitment"]),
    
    ("cultural", "Risk-averse culture", "Innovation and experimentation",
     "Organization cautious about change", "needs_improvement",
     ["Leadership communications", "Quick wins", "Celebrate successes"])
]

print("\nReadiness Assessments:")
for area, current, target, gap, level, actions in readiness:
    phase_e.add_readiness_assessment(area, current, target, gap, level, actions)
    print(f"  OK {area}: {level}")

# ================================================================================
# STEP 11: Define Cost Estimates
# ================================================================================
print("\n" + "=" * 80)
print("STEP 11: Define Cost Estimates")
print("=" * 80)

costs = [
    ("development", "Custom application development", 1100000, 0, None),
    ("infrastructure", "Cloud infrastructure and services", 350000, 200000, None),
    ("licensing", "COTS and SaaS licenses", 250000, 150000, None),
    ("operations", "Managed services and support", 0, 180000, 180000),
    ("training", "User and technical training", 200000, 50000, None)
]

print("\nCost Estimates:")
for category, desc, one_time, recurring, year1 in costs:
    phase_e.add_cost_estimate(category, desc, one_time, recurring, year1)
    print(f"  OK {category}: One-time: ${one_time:,}, Annual: ${recurring:,}")

# ================================================================================
# STEP 12: Define Benefit Estimates
# ================================================================================
print("\n" + "=" * 80)
print("STEP 12: Define Benefit Estimates")
print("=" * 80)

benefits = [
    ("cost_savings", "Reduced infrastructure and operations costs", 400000, 5, "high"),
    ("efficiency_gain", "Process automation and efficiency improvements", 600000, 5, "high"),
    ("revenue_increase", "New digital channels and improved customer experience", 800000, 5, "medium"),
    ("risk_reduction", "Improved security and compliance", 200000, 5, "medium"),
    ("cost_savings", "Reduced customer onboarding costs", 300000, 5, "high")
]

print("\nBenefit Estimates:")
for category, desc, annual, years, confidence in benefits:
    phase_e.add_benefit_estimate(category, desc, annual, years, confidence)
    total = annual * years
    print(f"  OK {desc}")
    print(f"     Annual: ${annual:,}, {years}-year total: ${total:,} ({confidence} confidence)")

# ================================================================================
# STEP 13: Calculate ROI Analysis
# ================================================================================
print("\n" + "=" * 80)
print("STEP 13: Calculate ROI Analysis")
print("=" * 80)

roi = phase_e.calculate_roi_analysis(analysis_period_years=5)

print("\n[FINANCIAL] ROI Analysis (5-year period):")
print(f"  Total One-Time Costs: ${roi['total_one_time_costs']:,.0f}")
print(f"  Total Annual Recurring: ${roi['total_annual_recurring_costs']:,.0f}")
print(f"  Total Costs (5 years): ${roi['total_costs']:,.0f}")
print(f"  Total Benefits (5 years): ${roi['total_benefits']:,.0f}")
print(f"  Net Benefit: ${roi['net_benefit']:,.0f}")
print(f"  ROI: {roi['roi_percentage']:.1f}%")
print(f"  Payback Period: {roi['payback_period_years']:.1f} years")

# ================================================================================
# STEP 14: Display Summaries
# ================================================================================
print("\n" + "=" * 80)
print("STEP 14: Architecture Summaries")
print("=" * 80)

solution_summary = phase_e.get_solution_summary()
print("\n[SOLUTIONS] Solution Building Blocks:")
print(f"  Total SBBs: {solution_summary['total_sbbs']}")
print(f"  By Type: {solution_summary['by_type']}")
print(f"  By Category: {solution_summary['by_category']}")
print(f"  Total Cost: ${solution_summary['total_estimated_cost']:,.0f}")

wp_summary = phase_e.get_work_package_summary()
print("\n[WORKPLAN] Work Packages:")
print(f"  Total Packages: {wp_summary['total_work_packages']}")
print(f"  By Priority: {wp_summary['by_priority']}")
print(f"  Total Cost: ${wp_summary['total_estimated_cost']:,.0f}")
print(f"  Total Duration: {wp_summary['total_estimated_duration_months']} months")

risk_summary = phase_e.get_risk_summary()
print("\n[RISKS] Risk Summary:")
print(f"  Total Risks: {risk_summary['total_risks']}")
print(f"  High Risks: {risk_summary['high_risks']}")
print(f"  Medium Risks: {risk_summary['medium_risks']}")
print(f"  Low Risks: {risk_summary['low_risks']}")
print(f"  By Category: {risk_summary['by_category']}")

# ================================================================================
# STEP 15: Execute Phase E
# ================================================================================
print("\n" + "=" * 80)
print("STEP 15: Execute Phase E")
print("=" * 80)

results = phase_e.execute()

print(f"\nOK Phase E Execution Complete!")
print(f"  Status: {results['status']}")
print(f"  Progress: {results['progress']:.1f}%")

# ================================================================================
# STEP 16: Save Results
# ================================================================================
print("\n" + "=" * 80)
print("STEP 16: Save Results to JSON")
print("=" * 80)

output_file = "phase_e_opportunities_solutions_results.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, default=str)

print(f"\nOK Results saved to: {output_file}")
print(f"  File size: {os.path.getsize(output_file):,} bytes")

# ================================================================================
# FINAL SUMMARY
# ================================================================================
print("\n" + "=" * 80)
print("PHASE E OPPORTUNITIES AND SOLUTIONS - COMPLETE")
print("=" * 80)

print("\n[DOCS] Deliverables Generated:")
for deliverable_name in results['deliverables'].keys():
    print(f"  OK {deliverable_name.replace('_', ' ').title()}")

print("\n[GOALS] Key Achievements:")
print(f"  OK {len(phase_e.solution_building_blocks)} solution building blocks defined")
print(f"  OK {len(phase_e.work_packages)} work packages created")
print(f"  OK {len(phase_e.projects)} implementation projects planned")
print(f"  OK {len(phase_e.transition_architectures)} transition architectures defined")
print(f"  OK Phased implementation strategy with 4 phases")
print(f"  OK ROI of {roi['roi_percentage']:.1f}% over 5 years")
print(f"  OK Payback period of {roi['payback_period_years']:.1f} years")
print(f"  OK {len(phase_e.implementation_risks)} risks identified and mitigated")
print(f"  OK Complete cost-benefit analysis")
print(f"  OK Organizational readiness assessed")

print("\n" + "=" * 80)
print("Phase E: Opportunities and Solutions execution completed successfully!")
print("=" * 80)
