"""
TOGAF Phase F: Migration Planning - Complete Example
"""
import json
import os
from togaf_framework.adm import PhaseFMigrationPlanning

print('='*80)
print('TOGAF Phase F: Migration Planning - Complete Example')
print('='*80)

phase_f = PhaseFMigrationPlanning('Migration Planning')

# Projects
print('\nStep 1: Define Migration Projects...')
projects = [
    ('Cloud Foundation Setup', 'Deploy Azure/AWS infrastructure', '2025-01-15', '2025-06-30', 167,
     ['WP1'], ['Cloud operational', 'Security baseline'], [], 'critical', 450000),
    ('Security Implementation', 'Zero-trust security', '2025-02-01', '2025-05-31', 120,
     ['WP2'], ['IAM deployed', 'Controls active'], ['Cloud Foundation Setup'], 'critical', 220000),
    ('Data Platform Deployment', 'Build data lake', '2025-04-01', '2025-11-30', 244,
     ['WP3'], ['Data lake operational'], ['Cloud Foundation Setup'], 'high', 380000),
    ('Application Modernization', 'Customer portal and mobile', '2025-05-01', '2026-04-30', 365,
     ['WP4'], ['Portal live', 'Mobile app'], ['Security Implementation'], 'high', 900000),
    ('DevOps Setup', 'CI/CD automation', '2025-03-01', '2025-06-30', 122,
     ['WP5'], ['Pipelines operational'], ['Cloud Foundation Setup'], 'medium', 200000),
]

for name, desc, start, end, days, wps, delivs, deps, pri, budget in projects:
    phase_f.add_migration_project(name, desc, start, end, days, wps, delivs, deps, pri, budget)
    print(f'  OK {name}')

# Portfolio
phase_f.define_project_portfolio(2300000, 18, ['Digital Transform', 'Vision 2030'], ['Budget constraints', 'Timeline critical'])
print(f'OK Portfolio defined: ${2300000:,} over 18 months')

# Roadmap phases
print('\nStep 2: Define Roadmap Phases...')
phases = [
    ('Foundation Phase', 'Cloud & Security', '2025-Q1', '2025-Q2', 6,
     ['Deploy cloud infrastructure', 'Implement security'], 
     ['Cloud platform', 'Security framework'], 
     ['Infrastructure operational', 'Security compliant']),
    ('Core Systems Phase', 'Data & Applications', '2025-Q2', '2025-Q4', 6,
     ['Deploy data platform', 'Build customer portal'],
     ['Data lake', 'Customer portal beta'],
     ['Systems operational', 'Users onboarded']),
    ('Integration Phase', 'Legacy & Testing', '2025-Q4', '2026-Q1', 3,
     ['Integrate legacy systems', 'End-to-end testing'],
     ['Integration complete', 'Testing passed'],
     ['All systems integrated', 'Quality validated']),
    ('Deployment Phase', 'Production Rollout', '2026-Q1', '2026-Q2', 3,
     ['Production deployment', 'User training'],
     ['Full production', 'Users trained'],
     ['100% operational', 'Support ready']),
]

for name, desc, start, end, months, objs, delivs, criteria in phases:
    phase_f.add_roadmap_phase(name, desc, start, end, months, objs, delivs, criteria)
    print(f'  OK {name} ({start} to {end})')

# Milestones
print('\nStep 3: Define Key Milestones...')
milestones = [
    ('Cloud Go-Live', 'Production cloud infrastructure', '2025-06-30', 'phase',
     ['Cloud infrastructure', 'Network configured'], ['99.9% uptime achieved'], 'Cloud Architect'),
    ('Security Certification', 'NORA compliance achieved', '2025-05-31', 'governance',
     ['Security controls', 'Audit report'], ['NORA compliant'], 'Security Officer'),
    ('Data Platform Ready', 'Data lake operational', '2025-11-30', 'project',
     ['Data lake', 'ETL pipelines', 'Analytics'], ['Data flowing', 'Reports available'], 'Data Architect'),
    ('Portal Launch', 'Customer portal production', '2026-04-30', 'business',
     ['Portal deployed', 'Mobile app'], ['Users active', '80% adoption'], 'Product Manager'),
]

for name, desc, date, mtype, delivs, criteria, owner in milestones:
    phase_f.add_milestone(name, desc, date, mtype, delivs, criteria, owner)
    print(f'  OK {name} - {date}')

# Resources
print('\nStep 4: Define Resource Requirements...')
resources = [
    ('Cloud Foundation Setup', 'cloud_architect', 2, 'senior', '2025-01-15', '2025-06-30', 100),
    ('Cloud Foundation Setup', 'cloud_engineer', 4, 'mid', '2025-01-15', '2025-06-30', 100),
    ('Security Implementation', 'security_architect', 2, 'senior', '2025-02-01', '2025-05-31', 100),
    ('Security Implementation', 'security_engineer', 3, 'mid', '2025-02-01', '2025-05-31', 100),
    ('Data Platform Deployment', 'data_architect', 2, 'senior', '2025-04-01', '2025-11-30', 100),
    ('Data Platform Deployment', 'data_engineer', 4, 'mid', '2025-04-01', '2025-11-30', 100),
    ('Application Modernization', 'solution_architect', 2, 'senior', '2025-05-01', '2026-04-30', 100),
    ('Application Modernization', 'developer', 8, 'mid', '2025-05-01', '2026-04-30', 100),
    ('DevOps Setup', 'devops_engineer', 3, 'senior', '2025-03-01', '2025-06-30', 100),
]

for proj, role, count, level, start, end, pct in resources:
    phase_f.add_resource_requirement(proj, role, count, level, start, end, pct)

print(f'OK {len(resources)} resource requirements defined')

# Resource pool
print('\nStep 5: Define Resource Pool...')
pool = [
    ('Sarah Chen', 'cloud_architect', 'senior', 100, 1500),
    ('Mohammed Ali', 'cloud_architect', 'senior', 100, 1500),
    ('Ahmed Hassan', 'security_architect', 'senior', 100, 1400),
    ('Fatima Al-Said', 'data_architect', 'senior', 100, 1400),
]

for name, role, level, avail, cost in pool:
    phase_f.add_resource_to_pool(name, role, level, avail, cost)

print(f'OK {len(pool)} resources in pool')

# Dependencies
print('\nStep 6: Define Project Dependencies...')
deps = [
    ('Cloud Foundation Setup', 'Security Implementation', 'finish_to_start', 0, 'Security needs cloud platform'),
    ('Cloud Foundation Setup', 'Data Platform Deployment', 'finish_to_start', 0, 'Data platform needs cloud'),
    ('Security Implementation', 'Application Modernization', 'finish_to_start', 0, 'Apps need security'),
    ('Cloud Foundation Setup', 'DevOps Setup', 'finish_to_start', 0, 'DevOps needs cloud'),
]

for from_proj, to_proj, dep_type, lag, desc in deps:
    phase_f.add_project_dependency(from_proj, to_proj, dep_type, lag, desc)

print(f'OK {len(deps)} dependencies defined')

# Critical path
print('\nStep 7: Calculate Critical Path...')
critical = phase_f.calculate_critical_path()
print(f'OK Critical path: {len(critical)} projects')
for proj in critical:
    print(f'  -> {proj}')

# Value assessments
print('\nStep 8: Value Assessments...')
values = [
    ('Cloud Foundation Setup', 9, 10, 8, 7),
    ('Security Implementation', 8, 10, 9, 6),
    ('Data Platform Deployment', 7, 8, 7, 8),
    ('Application Modernization', 9, 9, 8, 9),
    ('DevOps Setup', 6, 7, 7, 5),
]

for proj, biz, strat, risk, complex in values:
    phase_f.add_value_assessment(proj, biz, strat, risk, complex)

print(f'OK {len(values)} value assessments completed')

# Risks
print('\nStep 9: Define Migration Risks...')
risks = [
    ('Cloud Migration Delays', 'technical', ['Cloud Foundation Setup'], 'medium', 'high',
     'Add buffer time, engage cloud migration specialists', 'Cloud Architect'),
    ('Resource Constraints', 'organizational', ['All Projects'], 'high', 'medium',
     'Build resource pipeline, cross-train team', 'Program Manager'),
    ('Integration Complexity', 'technical', ['Application Modernization'], 'high', 'high',
     'Early POC, allocate buffer time', 'Integration Lead'),
]

for name, cat, projs, prob, impact, mit, owner in risks:
    phase_f.add_migration_risk(name, cat, projs, prob, impact, mit, owner)
    print(f'  OK {name} ({prob}/{impact})')

# Risk mitigation plans
print('\nStep 10: Define Risk Mitigation Plans...')
mitigation_plans = [
    ('Cloud Migration Delays', 
     ['Conduct pilot migration', 'Engage vendor early', 'Weekly progress reviews'],
     'Activate secondary vendor if delays exceed 2 weeks',
     'Cloud Architect', '2025-02-01', 50000),
]

for risk, actions, contingency, responsible, target, budget in mitigation_plans:
    phase_f.add_risk_mitigation_plan(risk, actions, contingency, responsible, target, budget)

print(f'OK {len(mitigation_plans)} mitigation plans defined')

# Change initiatives
print('\nStep 11: Define Change Management Initiatives...')
changes = [
    ('DevOps Culture Transformation', 'Transform to DevOps and agile practices',
     'IT Operations and Development Teams', 'organizational', 'high',
     ['DevOps training', 'Agile coaching', 'Tool adoption'],
     '2025-Q1 to 2025-Q3', ['Team adoption >80%', 'Deployment frequency increased']),
    ('Cloud Skills Development', 'Build cloud engineering capabilities',
     'Technical Teams', 'technology', 'high',
     ['Cloud certifications', 'Hands-on labs', 'Vendor training'],
     '2025-Q1 to 2025-Q2', ['50% team certified', 'Cloud proficiency achieved']),
]

for name, desc, audience, ctype, impact, activities, timeline, metrics in changes:
    phase_f.add_change_initiative(name, desc, audience, ctype, impact, activities, timeline, metrics)

print(f'OK {len(changes)} change initiatives defined')

# Stakeholder engagement
print('\nStep 12: Define Stakeholder Engagement Plan...')
stakeholder_groups = [
    {'group': 'Executive Leadership', 'engagement': 'Monthly steering committee'},
    {'group': 'Business Users', 'engagement': 'Bi-weekly demos and feedback'},
    {'group': 'IT Operations', 'engagement': 'Weekly stand-ups'},
    {'group': 'External Partners', 'engagement': 'Quarterly reviews'},
]

phase_f.define_stakeholder_engagement_plan(
    stakeholder_groups,
    'Multi-channel communication strategy with regular touchpoints',
    'Weekly to Monthly based on stakeholder group',
    ['Surveys', 'Town halls', 'Office hours', 'Feedback portal']
)

print('OK Stakeholder engagement plan defined')

# Governance checkpoints
print('\nStep 13: Define Governance Checkpoints...')
checkpoints = [
    ('Phase Gate 1 - Foundation', 'phase_gate', '2025-06-30', 'Foundation Phase Completion',
     ['Cloud infrastructure operational', 'Security controls implemented', '99.9% uptime achieved'],
     ['CTO', 'CISO', 'Architecture Board']),
    ('Phase Gate 2 - Core Systems', 'phase_gate', '2025-12-31', 'Core Systems Completion',
     ['Data platform operational', 'Portal beta deployed', 'Integration tested'],
     ['CTO', 'CIO', 'Business Sponsors']),
    ('Architecture Review 1', 'architecture_review', '2025-09-30', 'Mid-program Architecture Review',
     ['Architecture principles followed', 'Standards compliance', 'Technical debt managed'],
     ['Chief Architect', 'Architecture Board']),
]

for name, ctype, date, scope, criteria, approvers in checkpoints:
    phase_f.add_governance_checkpoint(name, ctype, date, scope, criteria, approvers)
    print(f'  OK {name} - {date}')

# Success metrics
print('\nStep 14: Define Success Metrics...')
metrics = [
    ('On-Time Delivery', 'Percentage of milestones delivered on schedule', 'schedule',
     '100%', 'Project tracking system', 'Weekly'),
    ('Budget Variance', 'Actual vs planned costs', 'cost',
     '<5% variance', 'Financial reports', 'Monthly'),
    ('Quality Score', 'Defect density and test coverage', 'quality',
     '<2 defects per 1000 LOC, >80% coverage', 'Quality metrics dashboard', 'Sprint'),
    ('Business Value Realized', 'Benefits achieved vs planned', 'business_value',
     '>90% of planned benefits', 'Benefits tracking', 'Quarterly'),
]

for name, desc, cat, target, method, freq in metrics:
    phase_f.add_success_metric(name, desc, cat, target, method, freq)

print(f'OK {len(metrics)} success metrics defined')

# Execute
print('\n' + '='*80)
print('Step 15: Execute Phase F')
print('='*80)

results = phase_f.execute()

print(f"\nOK Phase F Execution Complete!")
print(f"  Status: {results['status']}")
print(f"  Progress: {results['progress']:.1f}%")

# Display summaries
print('\n' + '='*80)
print('PHASE F MIGRATION PLANNING - RESULTS SUMMARY')
print('='*80)

print('\n[PROJECTS] Project Summary:')
proj_summary = results['projects']['summary']
print(f"  Total Projects: {proj_summary['total_projects']}")
print(f"  By Status: {proj_summary['by_status']}")
print(f"  By Priority: {proj_summary['by_priority']}")
print(f"  Total Budget: ${proj_summary['total_budget']:,}")

print('\n[TIMELINE] Timeline Summary:')
timeline_summary = results['timeline']['summary']
print(f"  Roadmap Phases: {timeline_summary['total_phases']}")
print(f"  Milestones: {timeline_summary['total_milestones']}")
print(f"  Governance Checkpoints: {timeline_summary['governance_checkpoints']}")
print(f"  Critical Path Length: {timeline_summary['critical_path_length']} projects")

print('\n[RESOURCES] Resource Summary:')
resource_summary = results['resources']['summary']
print(f"  Resource Requirements: {resource_summary['total_requirements']}")
print(f"  Resource Allocations: {resource_summary['total_allocations']}")
print(f"  Resource Pool Size: {resource_summary['resource_pool_size']}")

print('\n[RISKS] Risk Summary:')
risk_summary = results['risks']['summary']
print(f"  Total Risks: {risk_summary['total_risks']}")
print(f"  High Risks: {risk_summary['high_risks']}")
print(f"  Medium Risks: {risk_summary['medium_risks']}")
print(f"  Low Risks: {risk_summary['low_risks']}")
print(f"  Mitigation Plans: {risk_summary['mitigation_plans']}")

# Save results
print('\n' + '='*80)
print('Step 16: Save Results')
print('='*80)

output_file = 'phase_f_migration_planning_results.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, default=str)

print(f"\nOK Results saved to: {output_file}")
print(f"  File size: {os.path.getsize(output_file):,} bytes")

# Final summary
print('\n' + '='*80)
print('PHASE F MIGRATION PLANNING - COMPLETE')
print('='*80)

print('\n[DOCS] Deliverables Generated:')
for deliverable_name in results['deliverables'].keys():
    print(f"  OK {deliverable_name.replace('_', ' ').title()}")

print('\n[GOALS] Key Achievements:')
print(f"  OK {len(results['projects']['projects'])} migration projects planned")
print(f"  OK {len(results['timeline']['roadmap'])} roadmap phases defined")
print(f"  OK {len(results['timeline']['milestones'])} key milestones established")
print(f"  OK {len(results['timeline']['critical_path'])} projects on critical path")
print(f"  OK {len(results['resources']['requirements'])} resource requirements defined")
print(f"  OK {len(results['risks']['risks'])} risks identified with mitigation")
print(f"  OK {len(results['governance']['checkpoints'])} governance checkpoints")
print(f"  OK {len(results['governance']['success_metrics'])} success metrics tracking")
print(f"  OK ${proj_summary['total_budget']:,} total budget allocated")
print(f"  OK 18-month implementation timeline")

print('\n' + '='*80)
print('Phase F: Migration Planning execution completed successfully!')
print('='*80)
