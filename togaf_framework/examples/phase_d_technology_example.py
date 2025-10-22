"""
TOGAF Phase D: Technology Architecture - Complete Example

This example demonstrates a comprehensive implementation of Phase D,
including cloud infrastructure, security, DevOps, and multi-cloud strategy
aligned with the ArchiAgents repository architecture.

Features demonstrated:
- Multi-cloud strategy (Azure primary, AWS secondary)
- Kubernetes container orchestration
- Zero-trust security architecture
- Infrastructure as Code
- CI/CD automation
- Comprehensive monitoring
- Gap analysis
"""

import json
import os
from togaf_framework.adm import PhaseDTechnologyArchitecture
from togaf_framework.adm.adm_cycle import ADMCycle
from togaf_framework.models.technology import TechnologyComponent

print("=" * 80)
print("TOGAF Phase D: Technology Architecture - Complete Example")
print("=" * 80)

# Create ADM Cycle
print("\nCreating ADM Cycle...")
adm_cycle = ADMCycle("Digital Transformation - Technology Architecture")

# Initialize Phase D (we focus on Phase D in this example)
print("Initializing Phase D (Technology Architecture)...\n")
phase_d = PhaseDTechnologyArchitecture("Technology Architecture")

# ================================================================================
# STEP 1: Define Cloud Strategy
# ================================================================================
print("=" * 80)
print("STEP 1: Define Multi-Cloud Strategy")
print("=" * 80)

phase_d.define_cloud_strategy(
    primary_provider="azure",
    secondary_provider="aws",
    strategy_type="multi_cloud",
    rationale="Azure for primary workloads with government compliance, AWS for specialized AI/ML services and disaster recovery",
    disaster_recovery=True
)

print(f"OK Multi-cloud strategy defined")
print(f"  Primary: {phase_d.cloud_strategy['primary_provider']}")
print(f"  Secondary: {phase_d.cloud_strategy['secondary_provider']}")
print(f"  Strategy: {phase_d.cloud_strategy['strategy_type']}")

# ================================================================================
# STEP 2: Define Cloud Services
# ================================================================================
print("\n" + "=" * 80)
print("STEP 2: Define Cloud Services")
print("=" * 80)

# Azure Services
azure_services = [
    ("Azure Kubernetes Service", "compute", "azure", "standard", "saudi-central", 99.95),
    ("Azure Container Registry", "compute", "azure", "premium", "saudi-central", 99.9),
    ("Azure Cosmos DB", "database", "azure", "standard", "saudi-central", 99.99),
    ("Azure Storage", "storage", "azure", "premium", "saudi-central", 99.9),
    ("Azure API Management", "networking", "azure", "premium", "saudi-central", 99.95),
    ("Azure Key Vault", "security", "azure", "premium", "saudi-central", 99.99),
    ("Azure Monitor", "observability", "azure", "standard", "saudi-central", 99.9),
    ("Azure Application Gateway", "networking", "azure", "standard", "saudi-central", 99.95)
]

print("\nAzure Services:")
for name, service_type, provider, tier, region, sla in azure_services:
    phase_d.add_cloud_service(name, service_type, provider, tier, region, sla)
    print(f"  OK {name} ({service_type}, SLA: {sla}%)")

# AWS Services (Secondary/DR)
aws_services = [
    ("AWS EKS", "compute", "aws", "standard", "me-south-1", 99.95),
    ("AWS S3", "storage", "aws", "standard", "me-south-1", 99.99),
    ("AWS SageMaker", "ai_ml", "aws", "standard", "me-south-1", 99.9)
]

print("\nAWS Services (DR & Specialized):")
for name, service_type, provider, tier, region, sla in aws_services:
    phase_d.add_cloud_service(name, service_type, provider, tier, region, sla)
    print(f"  OK {name} ({service_type}, SLA: {sla}%)")

# ================================================================================
# STEP 3: Define Compute Resources
# ================================================================================
print("\n" + "=" * 80)
print("STEP 3: Define Compute Resources")
print("=" * 80)

compute_configs = [
    ("AKS Node Pool - Production", "kubernetes", "azure", 8, 32, "auto_horizontal"),
    ("AKS Node Pool - Staging", "kubernetes", "azure", 4, 16, "auto_horizontal"),
    ("Azure Functions - API Gateway", "serverless", "azure", 0, 0, "auto_horizontal"),
    ("Azure Container Instances - Batch", "container", "azure", 4, 8, "manual"),
    ("AWS EKS Node Pool - DR", "kubernetes", "aws", 4, 16, "auto_horizontal")
]

for name, resource_type, provider, vcpus, memory_gb, scaling in compute_configs:
    phase_d.add_compute_resource(name, resource_type, provider, vcpus, memory_gb, scaling)
    if vcpus > 0:
        print(f"  OK {name} - {vcpus} vCPUs, {memory_gb} GB RAM ({scaling})")
    else:
        print(f"  OK {name} - Serverless ({scaling})")

# ================================================================================
# STEP 4: Define Storage Resources
# ================================================================================
print("\n" + "=" * 80)
print("STEP 4: Define Storage Resources")
print("=" * 80)

storage_configs = [
    ("Azure Blob Storage - Hot Tier", "object", "azure", 10.0, "hot", "zone_redundant"),
    ("Azure Blob Storage - Archive", "archive", "azure", 50.0, "archive", "geo_redundant"),
    ("Azure Files - Premium", "file", "azure", 2.0, "hot", "zone_redundant"),
    ("Azure Managed Disks", "block", "azure", 5.0, "hot", "zone_redundant"),
    ("AWS S3 - DR Backup", "object", "aws", 10.0, "cool", "geo_redundant")
]

for name, storage_type, provider, capacity, tier, redundancy in storage_configs:
    phase_d.add_storage_resource(name, storage_type, provider, capacity, tier, redundancy)
    print(f"  OK {name} - {capacity} TB ({tier}, {redundancy})")

# ================================================================================
# STEP 5: Define Network Resources
# ================================================================================
print("\n" + "=" * 80)
print("STEP 5: Define Network Resources")
print("=" * 80)

network_configs = [
    ("Azure VNet - Production", "vnet", "azure", "10.0.0.0/16", 1000),
    ("AKS Subnet", "subnet", "azure", "10.0.1.0/24", None),
    ("Application Gateway Subnet", "subnet", "azure", "10.0.2.0/24", None),
    ("Azure VPN Gateway", "vpn", "azure", None, 1000),
    ("Azure CDN", "cdn", "azure", None, 10000),
    ("Azure Application Gateway", "load_balancer", "azure", None, 5000),
    ("Azure Firewall", "firewall", "azure", None, 2000)
]

for name, network_type, provider, address_space, bandwidth in network_configs:
    phase_d.add_network_resource(name, network_type, provider, address_space, bandwidth)
    if address_space:
        print(f"  OK {name} - {address_space}")
    else:
        print(f"  OK {name}")

# ================================================================================
# STEP 6: Define Platforms
# ================================================================================
print("\n" + "=" * 80)
print("STEP 6: Define Container & Platform Services")
print("=" * 80)

platforms = [
    ("Kubernetes Orchestration", "container_orchestration", "AKS", "azure", True),
    ("Serverless Platform", "serverless", "Azure Functions", "azure", True),
    ("API Gateway", "api_gateway", "Azure API Management", "azure", True),
    ("Message Broker", "messaging", "Azure Service Bus", "azure", True)
]

for name, platform_type, technology, provider, ha in platforms:
    phase_d.add_platform(name, platform_type, technology, provider, ha)
    ha_status = "HA Enabled" if ha else "HA Disabled"
    print(f"  OK {name} ({technology}, {ha_status})")

# ================================================================================
# STEP 7: Define Security Controls (Zero-Trust Architecture)
# ================================================================================
print("\n" + "=" * 80)
print("STEP 7: Define Security Controls (Zero-Trust)")
print("=" * 80)

security_controls = [
    ("Network Segmentation", "network", "Implement micro-segmentation with NSGs and Azure Firewall", 
     "Azure Firewall + NSGs", ["ISO27001", "NORA"]),
    ("Identity & Access Management", "identity", "Azure AD with MFA and conditional access",
     "Azure AD + RBAC", ["ISO27001", "SOC2", "NORA"]),
    ("Data Encryption at Rest", "data", "All data encrypted with customer-managed keys",
     "Azure Key Vault + Disk Encryption", ["ISO27001", "GDPR", "NORA"]),
    ("Data Encryption in Transit", "data", "TLS 1.3 for all communications",
     "Application Gateway + TLS", ["ISO27001", "PCI_DSS", "NORA"]),
    ("Container Security", "application", "Image scanning and runtime protection",
     "Azure Defender for Containers", ["ISO27001", "NORA"]),
    ("Infrastructure Hardening", "infrastructure", "CIS benchmarks and security baselines",
     "Azure Security Center", ["ISO27001", "SOC2", "NORA"]),
    ("API Security", "application", "OAuth 2.0, rate limiting, threat protection",
     "Azure API Management", ["NORA"])
]

print("\nZero-Trust Security Controls:")
for name, control_type, description, implementation, standards in security_controls:
    phase_d.add_security_control(name, control_type, description, implementation, standards)
    print(f"  OK {name} ({control_type})")
    print(f"    Standards: {', '.join(standards)}")

# ================================================================================
# STEP 8: Define Compliance Requirements
# ================================================================================
print("\n" + "=" * 80)
print("STEP 8: Define Compliance Requirements")
print("=" * 80)

compliance_reqs = [
    ("ISO27001", "Information Security Management", ["Identity & Access Management", "Data Encryption at Rest"], "in_progress"),
    ("SOC2", "Service Organization Controls", ["Identity & Access Management", "Infrastructure Hardening"], "in_progress"),
    ("GDPR", "Data Protection Regulation", ["Data Encryption at Rest", "Data Encryption in Transit"], "compliant"),
    ("PCI_DSS", "Payment Card Industry", ["Data Encryption in Transit", "Network Segmentation"], "in_progress"),
    ("NORA", "Saudi National Overall Reference Architecture", 
     ["Network Segmentation", "Identity & Access Management", "Data Encryption at Rest", "Container Security"], "in_progress")
]

for standard, description, controls, status in compliance_reqs:
    phase_d.add_compliance_requirement(standard, description, controls, status)
    print(f"  OK {standard}: {status}")

# ================================================================================
# STEP 9: Define CI/CD Pipelines
# ================================================================================
print("\n" + "=" * 80)
print("STEP 9: Define CI/CD Pipelines")
print("=" * 80)

pipelines = [
    ("Microservices Pipeline", "github_actions", 
     ["Build", "Test", "Security Scan", "Deploy to Staging", "Integration Tests", "Deploy to Production"],
     ["AKS-Production", "AKS-Staging"], 100.0),
    ("Infrastructure Pipeline", "azure_devops",
     ["Validate", "Plan", "Security Check", "Apply"],
     ["Azure Subscription"], 100.0),
    ("Data Pipeline", "azure_devops",
     ["Extract", "Transform", "Load", "Validate"],
     ["Azure Data Lake", "Cosmos DB"], 85.0)
]

for name, tool, stages, targets, automation in pipelines:
    phase_d.add_ci_cd_pipeline(name, tool, stages, targets, automation)
    print(f"  OK {name} ({tool}, {automation}% automated)")
    print(f"    Stages: {' -> '.join(stages)}")

# ================================================================================
# STEP 10: Define Infrastructure as Code
# ================================================================================
print("\n" + "=" * 80)
print("STEP 10: Define Infrastructure as Code")
print("=" * 80)

iac_templates = [
    ("AKS Cluster", "terraform", "azure", 
     ["Virtual Network", "Subnets", "AKS Cluster", "Node Pools", "Container Registry"], True),
    ("Storage Infrastructure", "bicep", "azure",
     ["Storage Accounts", "Blob Containers", "File Shares"], True),
    ("Network Security", "terraform", "azure",
     ["NSGs", "Azure Firewall", "Application Gateway"], True),
    ("Monitoring Stack", "terraform", "azure",
     ["Log Analytics", "Application Insights", "Alerts"], True)
]

for name, tool, provider, resources, vc in iac_templates:
    phase_d.add_iac_template(name, tool, provider, resources, vc)
    print(f"  OK {name} ({tool})")
    print(f"    Resources: {', '.join(resources)}")

# ================================================================================
# STEP 11: Define Monitoring & Observability
# ================================================================================
print("\n" + "=" * 80)
print("STEP 11: Define Monitoring & Observability")
print("=" * 80)

monitoring_tools = [
    ("Metrics Collection", "metrics", "prometheus", 
     ["AKS", "Applications", "Infrastructure"], True),
    ("Metrics Visualization", "observability", "grafana",
     ["Dashboards", "Alerting"], True),
    ("Centralized Logging", "logging", "elk",
     ["Application Logs", "Infrastructure Logs", "Security Logs"], True),
    ("Distributed Tracing", "tracing", "jaeger",
     ["Microservices", "API Calls"], True),
    ("Application Performance", "observability", "azure_monitor",
     ["Applications", "Databases", "Infrastructure"], True)
]

for name, tool_type, tool, targets, alerting in monitoring_tools:
    phase_d.add_monitoring_tool(name, tool_type, tool, targets, alerting)
    print(f"  OK {name} ({tool})")

# ================================================================================
# STEP 12: Set Baseline Architecture (As-Is)
# ================================================================================
print("\n" + "=" * 80)
print("STEP 12: Define Baseline Architecture (As-Is)")
print("=" * 80)

baseline_desc = {
    "overview": "Current on-premises and limited cloud infrastructure",
    "characteristics": [
        "Single on-premises data center",
        "Limited cloud adoption (Azure only)",
        "Manual deployment processes",
        "Basic monitoring with limited observability",
        "Network security via traditional firewall",
        "99.5% availability SLA"
    ],
    "limitations": [
        "No disaster recovery",
        "No auto-scaling",
        "Manual infrastructure provisioning",
        "Limited security controls",
        "No container orchestration"
    ]
}

phase_d.set_baseline_architecture(baseline_desc)
print("OK Baseline architecture documented")

# ================================================================================
# STEP 13: Set Target Architecture (To-Be)
# ================================================================================
print("\n" + "=" * 80)
print("STEP 13: Define Target Architecture (To-Be)")
print("=" * 80)

target_desc = {
    "overview": "Cloud-native, multi-cloud architecture with zero-trust security",
    "characteristics": [
        "Multi-cloud (Azure primary, AWS secondary)",
        "Container orchestration with Kubernetes",
        "100% automated CI/CD pipelines",
        "Comprehensive observability (metrics, logs, traces)",
        "Zero-trust network architecture",
        "99.9% availability SLA",
        "Auto-scaling compute resources",
        "Infrastructure as Code for all resources"
    ],
    "improvements": [
        "Achieve 99.9% availability (from 99.5%)",
        "Reduce deployment time from hours to minutes",
        "Enable auto-scaling for all workloads",
        "Implement comprehensive monitoring",
        "Multi-region disaster recovery",
        "Zero-trust security model",
        "100% infrastructure automation"
    ]
}

phase_d.set_target_architecture(target_desc)
print("OK Target architecture documented")

# ================================================================================
# STEP 14: Perform Gap Analysis
# ================================================================================
print("\n" + "=" * 80)
print("STEP 14: Perform Gap Analysis")
print("=" * 80)

gap_analysis = phase_d.perform_gap_analysis()

print("\n[ANALYSIS] Gap Analysis Results:")
print(f"\nCloud Migration Gaps: {len(gap_analysis['cloud_migration_gaps'])} gaps")
for gap in gap_analysis['cloud_migration_gaps']:
    print(f"  * {gap['description']} (Priority: {gap['priority']})")

print(f"\nSecurity Gaps: {len(gap_analysis['security_gaps'])} gaps")
for gap in gap_analysis['security_gaps']:
    print(f"  * {gap['description']} (Priority: {gap['priority']})")

automation_gap = gap_analysis['automation_gaps']
print(f"\nAutomation Gaps:")
print(f"  Current: {automation_gap['current_automation']:.1f}%")
print(f"  Target: {automation_gap['target_automation']:.1f}%")
print(f"  Gap: {automation_gap['gap']:.1f}%")
print(f"  IaC Coverage: {'OK' if automation_gap['iac_coverage'] else 'X'}")
print(f"  Monitoring Coverage: {'OK' if automation_gap['monitoring_coverage'] else 'X'}")

print(f"\nScalability Gaps: {len(gap_analysis['scalability_gaps'])} gaps")
for gap in gap_analysis['scalability_gaps']:
    print(f"  * {gap['description']} (Priority: {gap['priority']})")

# ================================================================================
# STEP 15: Display Summaries
# ================================================================================
print("\n" + "=" * 80)
print("STEP 15: Architecture Summaries")
print("=" * 80)

infra_summary = phase_d.get_infrastructure_summary()
print("\n[INFRA]  Infrastructure Summary:")
print(f"  Total Components: {infra_summary['total_components']}")
print(f"  Cloud Providers: {', '.join(infra_summary['cloud_providers'])}")
print(f"  Compute Resources: {infra_summary['compute_resources']}")
print(f"  Storage Resources: {infra_summary['storage_resources']}")
print(f"  Network Resources: {infra_summary['network_resources']}")
print(f"  Cloud Services: {infra_summary['cloud_services']}")
print(f"  Platforms: {infra_summary['platforms']}")

security_summary = phase_d.get_security_summary()
print("\n[SECURITY] Security Summary:")
print(f"  Total Controls: {security_summary['total_controls']}")
print(f"  Controls by Type:")
for control_type, count in security_summary['controls_by_type'].items():
    print(f"    * {control_type}: {count}")
print(f"  Compliance Requirements: {security_summary['compliance_requirements']}")

devops_summary = phase_d.get_devops_summary()
print("\n[DEVOPS]  DevOps Summary:")
print(f"  CI/CD Pipelines: {devops_summary['ci_cd_pipelines']}")
print(f"  IaC Templates: {devops_summary['iac_templates']}")
print(f"  Monitoring Tools: {devops_summary['monitoring_tools']}")
print(f"  Automation Coverage: {devops_summary['automation_coverage']:.1f}%")

# ================================================================================
# STEP 16: Execute Phase D
# ================================================================================
print("\n" + "=" * 80)
print("STEP 16: Execute Phase D")
print("=" * 80)

results = phase_d.execute()

print(f"\nOK Phase D Execution Complete!")
print(f"  Status: {results['status']}")
print(f"  Progress: {results['progress']:.1f}%")

# ================================================================================
# STEP 17: Save Results
# ================================================================================
print("\n" + "=" * 80)
print("STEP 17: Save Results to JSON")
print("=" * 80)

output_file = "phase_d_technology_architecture_results.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, default=str)

print(f"\nOK Results saved to: {output_file}")
print(f"  File size: {os.path.getsize(output_file):,} bytes")

# ================================================================================
# FINAL SUMMARY
# ================================================================================
print("\n" + "=" * 80)
print("PHASE D TECHNOLOGY ARCHITECTURE - COMPLETE")
print("=" * 80)

print("\n[DOCS] Deliverables Generated:")
for deliverable_name in results['deliverables'].keys():
    print(f"  OK {deliverable_name.replace('_', ' ').title()}")

print("\n[GOALS] Key Achievements:")
print(f"  OK Multi-cloud strategy defined (Azure + AWS)")
print(f"  OK {len(phase_d.cloud_services)} cloud services configured")
print(f"  OK {len(phase_d.compute_resources)} compute resources defined")
print(f"  OK {len(phase_d.security_controls)} security controls implemented")
print(f"  OK {len(phase_d.ci_cd_pipelines)} CI/CD pipelines configured")
print(f"  OK {len(phase_d.iac_templates)} IaC templates created")
print(f"  OK {len(phase_d.monitoring_tools)} monitoring tools configured")
print(f"  OK Zero-trust security architecture")
print(f"  OK 100% infrastructure automation")
print(f"  OK Comprehensive gap analysis")

print("\n" + "=" * 80)
print("Phase D: Technology Architecture execution completed successfully!")
print("=" * 80)
