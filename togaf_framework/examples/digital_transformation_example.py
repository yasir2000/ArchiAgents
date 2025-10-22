"""
Comprehensive Example: Digital Transformation Architecture

This example demonstrates a complete TOGAF ADM cycle for a digital
transformation initiative including all phases, stakeholders, principles,
and deliverables.
"""

from datetime import datetime
from togaf_framework.adm import (
    ADMCycle,
    PhaseAArchitectureVision,
)
from togaf_framework.models import (
    Stakeholder,
    ArchitecturePrinciple,
    Requirement,
)
from togaf_framework.core.enums import (
    StakeholderType,
    PriorityLevel,
)


def create_digital_transformation_architecture():
    """
    Create a complete digital transformation architecture using TOGAF framework.
    """
    
    print("="*80)
    print("TOGAF Framework - Digital Transformation Initiative")
    print("="*80)
    print()
    
    # =========================================================================
    # Step 1: Create ADM Cycle
    # =========================================================================
    print("Step 1: Creating ADM Cycle...")
    
    adm_cycle = ADMCycle(
        name="Digital Transformation Initiative 2025",
        description="Enterprise-wide digital transformation aligned with Vision 2030",
        metadata={
            'organization': 'Example Enterprise',
            'timeline': '24 months',
            'budget': '$5M',
        }
    )
    
    print(f"✓ Created ADM Cycle: {adm_cycle.name}")
    print()
    
    # =========================================================================
    # Step 2: Phase A - Architecture Vision
    # =========================================================================
    print("Step 2: Creating Phase A - Architecture Vision...")
    
    phase_a = PhaseAArchitectureVision(
        name="Architecture Vision",
        description="Define strategic direction and obtain approval",
        owner="Chief Enterprise Architect"
    )
    
    # Set vision statement
    vision = """
    Transform the enterprise into a cloud-native, data-driven organization 
    delivering exceptional digital experiences through:
    - 99.9% system availability
    - <100ms API response times
    - 70% process automation
    - Real-time analytics capabilities
    - Zero-trust security architecture
    """
    phase_a.set_vision_statement(vision.strip())
    
    # Add business goals aligned with repository targets
    business_goals = [
        "Achieve 99.9% system availability (from current 99.5%)",
        "Reduce API response time to <100ms (from current 200ms)",
        "Increase process automation to 70% (from current 45%)",
        "Scale data processing to 10M events/hour (from current 1M)",
        "Reduce security incidents to <2/month (from current 5)",
        "Deploy multi-cloud architecture (Azure primary, AWS secondary)",
        "Implement microservices architecture across all applications",
        "Achieve full Saudi NORA compliance for government services",
    ]
    
    for goal in business_goals:
        phase_a.add_business_goal(goal)
    
    print(f"✓ Set vision statement")
    print(f"✓ Added {len(business_goals)} business goals")
    
    # =========================================================================
    # Step 3: Define Key Stakeholders
    # =========================================================================
    print("\nStep 3: Defining Key Stakeholders...")
    
    stakeholders = [
        {
            'name': 'CEO',
            'type': StakeholderType.EXECUTIVE,
            'role': 'Chief Executive Officer',
            'organization': 'Executive Leadership',
            'email': 'ceo@example.com',
            'concerns': [
                'Strategic alignment with business goals',
                'Return on investment',
                'Competitive advantage',
            ],
            'influence': 'high',
            'interest': 'high',
        },
        {
            'name': 'CTO',
            'type': StakeholderType.EXECUTIVE,
            'role': 'Chief Technology Officer',
            'organization': 'Technology',
            'email': 'cto@example.com',
            'concerns': [
                'Technology stack modernization',
                'Cloud migration strategy',
                'Technical debt reduction',
            ],
            'influence': 'high',
            'interest': 'high',
        },
        {
            'name': 'Chief Architect',
            'type': StakeholderType.ARCHITECT,
            'role': 'Enterprise Architect',
            'organization': 'Architecture Office',
            'email': 'chief-architect@example.com',
            'concerns': [
                'Architecture standards and principles',
                'Technology governance',
                'Integration patterns',
            ],
            'influence': 'high',
            'interest': 'high',
        },
        {
            'name': 'CISO',
            'type': StakeholderType.SECURITY,
            'role': 'Chief Information Security Officer',
            'organization': 'Security',
            'email': 'ciso@example.com',
            'concerns': [
                'Zero-trust security implementation',
                'Data protection and privacy',
                'Compliance with regulations',
            ],
            'influence': 'high',
            'interest': 'high',
        },
        {
            'name': 'Head of Development',
            'type': StakeholderType.DEVELOPER,
            'role': 'Development Lead',
            'organization': 'Engineering',
            'email': 'dev-lead@example.com',
            'concerns': [
                'Microservices adoption',
                'DevOps practices',
                'Developer experience',
            ],
            'influence': 'medium',
            'interest': 'high',
        },
    ]
    
    for s_data in stakeholders:
        stakeholder = Stakeholder(
            name=s_data['name'],
            stakeholder_type=s_data['type'],
            role=s_data['role'],
            organization=s_data['organization'],
            contact_email=s_data['email']
        )
        
        for concern in s_data['concerns']:
            stakeholder.add_concern(concern)
        
        stakeholder.set_influence_level(s_data['influence'])
        stakeholder.set_interest_level(s_data['interest'])
        
        phase_a.add_key_stakeholder(stakeholder)
        
        print(f"✓ Added stakeholder: {s_data['name']} ({s_data['role']})")
        print(f"  Power Matrix: {stakeholder.get_stakeholder_power()}")
    
    # =========================================================================
    # Step 4: Define Architecture Principles
    # =========================================================================
    print("\nStep 4: Defining Architecture Principles...")
    
    principles = [
        {
            'name': 'API-First Design',
            'statement': 'All services must expose well-defined, versioned APIs',
            'rationale': 'Enables integration, composability, and ecosystem development',
            'implications': [
                'Requires API management platform (Azure API Management)',
                'Need API governance and standards',
                'API documentation must be maintained',
                'Implement rate limiting and security',
            ],
            'category': 'application',
        },
        {
            'name': 'Cloud-First Strategy',
            'statement': 'All new applications must be cloud-native',
            'rationale': 'Leverage cloud scalability, resilience, and managed services',
            'implications': [
                'Multi-cloud strategy (Azure primary, AWS secondary)',
                'Container orchestration with Kubernetes',
                'Serverless for event-driven workloads',
                'Cloud cost optimization required',
            ],
            'category': 'technology',
        },
        {
            'name': 'Zero-Trust Security',
            'statement': 'Never trust, always verify - assume breach',
            'rationale': 'Modern security posture for distributed architecture',
            'implications': [
                'Identity verification for all access',
                'Network microsegmentation',
                'Encryption everywhere (rest, transit, use)',
                'Continuous security monitoring',
            ],
            'category': 'security',
        },
        {
            'name': 'Data-Driven Decisions',
            'statement': 'All business decisions must be supported by data analytics',
            'rationale': 'Enable evidence-based decision making and continuous improvement',
            'implications': [
                'Real-time analytics infrastructure required',
                'Data governance framework needed',
                'Data quality management essential',
                'Self-service BI tools deployment',
            ],
            'category': 'data',
        },
        {
            'name': 'Automation First',
            'statement': 'Automate everything that can be automated',
            'rationale': 'Reduce manual effort, errors, and increase efficiency',
            'implications': [
                'CI/CD pipelines for all applications',
                'Infrastructure as Code (IaC)',
                'Automated testing and quality gates',
                'RPA for business processes',
            ],
            'category': 'process',
        },
    ]
    
    for p_data in principles:
        principle = ArchitecturePrinciple(
            name=p_data['name'],
            statement=p_data['statement'],
            rationale=p_data['rationale'],
            implications=p_data['implications'],
            category=p_data['category']
        )
        principle.set_priority('high')
        phase_a.add_principle(principle)
        
        print(f"✓ Added principle: {p_data['name']}")
        print(f"  Category: {p_data['category']}")
    
    # =========================================================================
    # Step 5: Define High-Level Requirements
    # =========================================================================
    print("\nStep 5: Defining High-Level Requirements...")
    
    requirements = [
        {
            'name': 'REQ-001',
            'description': 'System must achieve 99.9% availability',
            'type': 'non-functional',
            'priority': PriorityLevel.CRITICAL,
            'source': 'Business Goal',
            'criteria': [
                'Maximum 43.8 minutes downtime per month',
                'Automated failover within 30 seconds',
                'Multi-region deployment',
            ],
        },
        {
            'name': 'REQ-002',
            'description': 'API response time must be <100ms (p95)',
            'type': 'non-functional',
            'priority': PriorityLevel.HIGH,
            'source': 'Performance Target',
            'criteria': [
                '95th percentile response time under 100ms',
                'Measured at API gateway',
                'Includes authentication overhead',
            ],
        },
        {
            'name': 'REQ-003',
            'description': 'Support 10M events/hour data processing',
            'type': 'non-functional',
            'priority': PriorityLevel.HIGH,
            'source': 'Scalability Target',
            'criteria': [
                'Sustained throughput of 10M events/hour',
                'Auto-scaling based on load',
                'End-to-end latency <5 seconds',
            ],
        },
        {
            'name': 'REQ-004',
            'description': 'Implement zero-trust security architecture',
            'type': 'non-functional',
            'priority': PriorityLevel.CRITICAL,
            'source': 'Security Principle',
            'criteria': [
                'Identity verification for all access',
                'Network microsegmentation',
                'Encryption at rest and in transit',
                'MFA for all user access',
            ],
        },
        {
            'name': 'REQ-005',
            'description': 'Achieve Saudi NORA compliance',
            'type': 'constraint',
            'priority': PriorityLevel.CRITICAL,
            'source': 'Regulatory Requirement',
            'criteria': [
                'Data localization in Saudi Arabia',
                'Arabic-first interface design',
                'Integration with Absher platform',
                'PDPL compliance',
            ],
        },
    ]
    
    for r_data in requirements:
        requirement = Requirement(
            name=r_data['name'],
            description=r_data['description'],
            requirement_type=r_data['type'],
            source=r_data['source'],
            priority=r_data['priority']
        )
        
        for criterion in r_data['criteria']:
            requirement.add_acceptance_criterion(criterion)
        
        phase_a.add_requirement(requirement)
        
        print(f"✓ Added requirement: {r_data['name']}")
        print(f"  Priority: {r_data['priority'].value}")
    
    # =========================================================================
    # Step 6: Define Constraints and Assumptions
    # =========================================================================
    print("\nStep 6: Defining Constraints and Assumptions...")
    
    constraints = [
        "Budget limit of $5M for Year 1",
        "Must maintain existing system availability during migration",
        "Limited to Azure and AWS cloud providers (no GCP)",
        "Must comply with Saudi NORA requirements",
        "24-month timeline for complete transformation",
        "Current team size cannot exceed 50% growth",
    ]
    
    for constraint in constraints:
        phase_a.add_constraint(constraint)
        print(f"✓ Constraint: {constraint}")
    
    assumptions = [
        "Executive sponsorship remains consistent",
        "Budget approved as requested",
        "Key technical staff retained throughout project",
        "Cloud services remain available and stable",
        "Third-party vendors deliver as contracted",
        "Regulatory requirements remain stable",
    ]
    
    for assumption in assumptions:
        phase_a.add_assumption(assumption)
        print(f"✓ Assumption: {assumption}")
    
    # =========================================================================
    # Step 7: Execute Phase A
    # =========================================================================
    print("\n" + "="*80)
    print("Executing Phase A: Architecture Vision")
    print("="*80)
    
    phase_a.start_phase()
    results = phase_a.execute()
    
    print(f"\nPhase A Execution Results:")
    print(f"  Vision Statement: {results['vision_statement'][:100]}...")
    print(f"  Business Goals: {len(results['business_goals'])}")
    print(f"  Principles: {results['principles_count']}")
    print(f"  Stakeholders: {results['stakeholders_count']}")
    print(f"  Requirements: {results['requirements_count']}")
    print(f"  Constraints: {len(results['constraints'])}")
    print(f"  Assumptions: {len(results['assumptions'])}")
    
    # Mark activities as completed
    for activity in phase_a.activities:
        phase_a.complete_activity(activity['name'])
        print(f"✓ Completed activity: {activity['name']}")
    
    phase_a.complete_phase()
    
    # =========================================================================
    # Step 8: Add Phase to Cycle and Execute
    # =========================================================================
    print("\n" + "="*80)
    print("Adding Phase A to ADM Cycle")
    print("="*80)
    
    adm_cycle.add_phase(phase_a)
    
    # =========================================================================
    # Step 9: Generate Summary Report
    # =========================================================================
    print("\n" + "="*80)
    print("ARCHITECTURE VISION SUMMARY REPORT")
    print("="*80)
    
    print(f"\n📋 Project Information:")
    print(f"  Name: {adm_cycle.name}")
    print(f"  Description: {adm_cycle.description}")
    print(f"  Status: {phase_a.status.value if hasattr(phase_a.status, 'value') else phase_a.status}")
    print(f"  Progress: {phase_a.completion_percentage}%")
    print(f"  Started: {phase_a.start_date}")
    print(f"  Completed: {phase_a.end_date}")
    
    print(f"\n🎯 Vision Statement:")
    print(f"  {phase_a.vision_statement}")
    
    print(f"\n📊 Business Goals ({len(phase_a.business_goals)}):")
    for i, goal in enumerate(phase_a.business_goals, 1):
        print(f"  {i}. {goal}")
    
    print(f"\n👥 Key Stakeholders ({len(phase_a.key_stakeholders)}):")
    for stakeholder in phase_a.key_stakeholders:
        print(f"  • {stakeholder.name} ({stakeholder.role})")
        print(f"    Power: {stakeholder.get_stakeholder_power()}")
        print(f"    Concerns: {', '.join(stakeholder.concerns[:2])}...")
    
    print(f"\n📐 Architecture Principles ({len(phase_a.architecture_principles)}):")
    for principle in phase_a.architecture_principles:
        print(f"  • {principle.name}")
        print(f"    {principle.statement}")
    
    print(f"\n📋 Requirements ({len(phase_a.requirements)}):")
    for req in phase_a.requirements:
        print(f"  • {req.name}: {req.description}")
        print(f"    Priority: {req.priority.value}, Type: {req.requirement_type}")
    
    print(f"\n📦 Deliverables ({len(phase_a.outputs)}):")
    for deliverable in phase_a.outputs:
        print(f"  • {deliverable.name}")
        print(f"    Status: {deliverable.approval_status}")
    
    print(f"\n⚙️ Activities Completed ({len(phase_a.activities)}):")
    for activity in phase_a.activities:
        status_icon = "✓" if activity['status'] == 'completed' else "○"
        print(f"  {status_icon} {activity['name']}")
    
    print(f"\n🎯 Next Steps:")
    print(f"  1. Obtain formal approval from Architecture Board")
    print(f"  2. Secure executive sign-off on Statement of Architecture Work")
    print(f"  3. Proceed to Phase B: Business Architecture")
    print(f"  4. Begin detailed capability and process modeling")
    print(f"  5. Establish governance checkpoints")
    
    print("\n" + "="*80)
    print("Phase A: Architecture Vision - COMPLETED SUCCESSFULLY")
    print("="*80)
    print()
    
    return adm_cycle, phase_a


if __name__ == "__main__":
    # Execute the example
    adm_cycle, phase_a = create_digital_transformation_architecture()
    
    # Save results to file
    import json
    from datetime import datetime
    
    results_file = f"architecture_vision_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(results_file, 'w') as f:
        json.dump({
            'adm_cycle': adm_cycle.to_dict(),
            'phase_a': phase_a.to_dict(),
            'deliverables': phase_a.get_deliverables_summary(),
        }, f, indent=2, default=str)
    
    print(f"\n💾 Results saved to: {results_file}")
    print(f"\n✨ Example completed successfully!")
