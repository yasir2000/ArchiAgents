# ArchiAgents CLI - Complete User Guide

## Overview

The **ArchiAgents CLI** provides a comprehensive command-line interface for enterprise architecture management using the TOGAF framework, AI-powered agents, and intelligent runtime decision-making.

## Installation

```bash
# Navigate to the togaf_framework directory
cd togaf_framework

# Install required dependencies
pip install click pyyaml

# Verify installation
python archiagents.py --version
```

## Quick Start

```bash
# 1. Initialize a new project
python archiagents.py project init --name "Digital Transformation" --enterprise "TechCorp"

# 2. Navigate to project directory
cd ~/archiagents_projects/digital_transformation

# 3. Execute Phase A
python archiagents.py phase run phase-a

# 4. Check architecture health
python archiagents.py intelligence health

# 5. Run a complete scenario
python archiagents.py scenario run cloud-migration --enterprise "TechCorp"
```

## Command Structure

```
archiagents [OPTIONS] COMMAND [ARGS]...

Commands:
  project      - Manage architecture projects
  phase        - Execute TOGAF ADM phases
  ai           - Configure and run AI agents
  intelligence - Runtime intelligence and autonomous decision-making
  model        - ArchiMate model management
  report       - Generate architecture reports
  scenario     - Run predefined real-world scenarios
  config       - Manage CLI configuration
```

## Global Options

- `--help` - Show help message and exit
- `--version` - Show version and exit
- `--config PATH` - Path to custom configuration file
- `--verbose` - Enable verbose output

## Command Reference

### Project Management

#### `project init`

Initialize a new architecture project.

**Usage:**
```bash
python archiagents.py project init [OPTIONS]
```

**Options:**
- `--name TEXT` - Project name (required)
- `--enterprise TEXT` - Enterprise name (required)
- `--description TEXT` - Project description
- `--scope TEXT` - Architecture scope
- `--path PATH` - Custom project directory path

**Example:**
```bash
python archiagents.py project init \
  --name "Digital Transformation" \
  --enterprise "GlobalTech Corporation" \
  --description "Enterprise-wide digital transformation initiative" \
  --scope "All business units and IT systems"
```

#### `project list`

List all architecture projects.

**Usage:**
```bash
python archiagents.py project list [OPTIONS]
```

**Options:**
- `--format [table|json|yaml]` - Output format (default: table)

**Example:**
```bash
# Table format
python archiagents.py project list

# JSON format
python archiagents.py project list --format json
```

#### `project status`

Show detailed project status and progress.

**Usage:**
```bash
python archiagents.py project status [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory (default: current directory)
- `--format [table|json|tree]` - Output format

**Example:**
```bash
# Status of current project
python archiagents.py project status

# Status of specific project
python archiagents.py project status --project ~/archiagents_projects/my_project
```

#### `project delete`

Delete an architecture project.

**Usage:**
```bash
python archiagents.py project delete NAME [OPTIONS]
```

**Options:**
- `--force` - Force deletion without confirmation

**Example:**
```bash
python archiagents.py project delete digital_transformation --force
```

### TOGAF Phase Execution

#### `phase run`

Execute a TOGAF ADM phase.

**Usage:**
```bash
python archiagents.py phase run PHASE [OPTIONS]
```

**Phases:**
- `preliminary` - Preliminary Phase
- `phase-a` - Architecture Vision
- `phase-b` - Business Architecture
- `phase-c` - Information Systems Architecture
- `phase-d` - Technology Architecture
- `phase-e` - Opportunities and Solutions
- `phase-f` - Migration Planning
- `phase-g` - Implementation Governance
- `phase-h` - Architecture Change Management

**Options:**
- `--project PATH` - Project directory
- `--use-ai` - Use AI agents for execution
- `--autonomous` - Enable autonomous mode
- `--output PATH` - Save results to file

**Examples:**
```bash
# Execute Phase A manually
python archiagents.py phase run phase-a

# Execute Phase A with AI agents
python archiagents.py phase run phase-a --use-ai

# Execute Phase B with autonomous mode and save output
python archiagents.py phase run phase-b --autonomous --output results.json
```

#### `phase list`

List all TOGAF ADM phases and their status.

**Usage:**
```bash
python archiagents.py phase list [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory

**Example:**
```bash
python archiagents.py phase list
```

#### `phase status`

Show status and deliverables for a specific phase.

**Usage:**
```bash
python archiagents.py phase status PHASE [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory
- `--format [table|json|yaml]` - Output format

**Example:**
```bash
python archiagents.py phase status phase-a --format json
```

#### `phase reset`

Reset a phase or all phases to restart.

**Usage:**
```bash
python archiagents.py phase reset PHASE [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory
- `--force` - Force reset without confirmation

**Example:**
```bash
# Reset specific phase
python archiagents.py phase reset phase-a --force

# Reset all phases
python archiagents.py phase reset all
```

### Runtime Intelligence

#### `intelligence analyze`

Analyze architecture using Runtime Intelligence Layer.

**Usage:**
```bash
python archiagents.py intelligence analyze [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory
- `--autonomous` - Enable autonomous mode
- `--format [table|json|tree]` - Output format

**Analysis Types:**
- **Gap Analysis** - Missing layers, orphaned elements, weak alignment
- **Dependency Analysis** - High coupling, circular dependencies
- **Pattern Recognition** - Layered architecture, microservices patterns
- **Optimization Detection** - Redundancy detection

**Example:**
```bash
# Analyze current project
python archiagents.py intelligence analyze

# Analyze with autonomous mode
python archiagents.py intelligence analyze --autonomous --format json
```

#### `intelligence decide`

Make an architecture decision using AI-driven decision engine.

**Usage:**
```bash
python archiagents.py intelligence decide [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory
- `--title TEXT` - Decision title (required)
- `--type [strategic|tactical|technical|organizational|governance|risk|compliance|optimization]` - Decision type
- `--priority [critical|high|medium|low]` - Decision priority
- `--autonomous` - Enable autonomous decision-making

**Interactive Process:**
1. Provide decision title, type, and priority
2. Enter 2+ decision options with details:
   - Name and description
   - Feasibility (0-1)
   - Cost ($)
   - Time (days)
   - Complexity (0-1)
   - Risk (0-1)
3. System analyzes options and recommends best choice
4. Decision saved with reasoning and implementation plan

**Example:**
```bash
python archiagents.py intelligence decide \
  --title "Cloud Migration Strategy" \
  --type strategic \
  --priority high \
  --autonomous
```

#### `intelligence health`

Check architecture health score.

**Usage:**
```bash
python archiagents.py intelligence health [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory
- `--format [table|json]` - Output format

**Health Scoring:**
- **80-100**: Healthy - Architecture in good condition
- **60-79**: Fair - Some issues to address
- **40-59**: At Risk - Significant issues requiring attention
- **<40**: Critical - Urgent action required

**Calculation:**
```
Health Score = 100 - (Critical × 20 + High × 10 + Medium × 5)
```

**Example:**
```bash
python archiagents.py intelligence health
```

#### `intelligence report`

Generate comprehensive intelligence report.

**Usage:**
```bash
python archiagents.py intelligence report [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory
- `--output PATH` - Save report to file

**Example:**
```bash
python archiagents.py intelligence report --output intelligence_report.txt
```

### Real-World Scenarios

#### `scenario list`

List all available real-world scenarios.

**Usage:**
```bash
python archiagents.py scenario list
```

**Available Scenarios:**
- `digital-transformation` - Complete digital transformation journey
- `cloud-migration` - Migration to cloud platform
- `microservices` - Transformation to microservices architecture
- `modernization` - Enterprise modernization initiative
- `merger-integration` - M&A integration

**Example:**
```bash
python archiagents.py scenario list
```

#### `scenario describe`

Describe a specific scenario in detail.

**Usage:**
```bash
python archiagents.py scenario describe SCENARIO [OPTIONS]
```

**Options:**
- `--format [table|json|yaml]` - Output format

**Example:**
```bash
# Table format (detailed view)
python archiagents.py scenario describe cloud-migration

# JSON format (for automation)
python archiagents.py scenario describe cloud-migration --format json
```

#### `scenario run`

Run a complete real-world scenario end-to-end.

**Usage:**
```bash
python archiagents.py scenario run SCENARIO [OPTIONS]
```

**Options:**
- `--project PATH` - Project directory (creates new if not exists)
- `--enterprise TEXT` - Enterprise name (required)
- `--use-ai` - Use AI agents for execution
- `--autonomous` - Enable autonomous mode
- `--fast` - Run in fast mode (skip confirmations)

**Execution Steps:**
1. Initialize project (if needed)
2. Execute all TOGAF phases in sequence
3. Generate architecture artifacts
4. Run intelligence analysis (if autonomous)
5. Generate final report

**Examples:**
```bash
# Basic scenario execution
python archiagents.py scenario run cloud-migration --enterprise "TechCorp"

# With AI and autonomous mode
python archiagents.py scenario run digital-transformation \
  --enterprise "GlobalTech" \
  --use-ai \
  --autonomous

# Fast mode (no confirmations)
python archiagents.py scenario run microservices \
  --enterprise "StartupCo" \
  --fast
```

## Real-World Scenarios Detailed

### 1. Digital Transformation

**Description:** Complete digital transformation journey from legacy to modern digital enterprise

**Duration:** 18-24 months

**Phases Involved:**
- Preliminary Phase
- Phase A: Architecture Vision
- Phase B: Business Architecture
- Phase C: Information Systems Architecture
- Phase D: Technology Architecture
- Phase E: Opportunities and Solutions
- Phase F: Migration Planning

**Strategic Objectives:**
- Modernize legacy applications
- Implement omnichannel customer experience
- Adopt cloud-native architecture
- Enable data-driven decision making
- Automate business processes

**KPIs:**
- Customer satisfaction: >85%
- Time to market: <2 weeks
- Process automation: >70%
- Cloud adoption: 80%
- Digital revenue: 50% of total

**Usage:**
```bash
python archiagents.py scenario run digital-transformation \
  --enterprise "GlobalTech Corporation" \
  --use-ai \
  --autonomous
```

### 2. Cloud Migration

**Description:** Migration from on-premises infrastructure to cloud platform

**Duration:** 6-12 months

**Phases Involved:**
- Preliminary Phase
- Phase A: Architecture Vision
- Phase C: Information Systems Architecture
- Phase D: Technology Architecture
- Phase E: Opportunities and Solutions
- Phase F: Migration Planning

**Strategic Objectives:**
- Assess cloud readiness
- Select cloud provider and services
- Design cloud architecture
- Migrate applications and data
- Optimize cloud costs

**KPIs:**
- Infrastructure cost reduction: 40%
- Scalability: 10x capacity
- Availability: 99.9%
- Migration success rate: 100%
- Performance improvement: 30%

**Usage:**
```bash
python archiagents.py scenario run cloud-migration \
  --enterprise "TechCorp" \
  --use-ai
```

### 3. Microservices Adoption

**Description:** Transformation from monolithic to microservices architecture

**Duration:** 12-18 months

**Phases Involved:**
- Preliminary Phase
- Phase A: Architecture Vision
- Phase B: Business Architecture
- Phase C: Information Systems Architecture
- Phase D: Technology Architecture
- Phase F: Migration Planning

**Strategic Objectives:**
- Decompose monolithic applications
- Design microservices architecture
- Implement API gateway
- Setup container orchestration
- Establish DevOps practices

**KPIs:**
- Deployment frequency: Daily
- Lead time: <1 day
- Service independence: 100%
- Fault tolerance: 99.95%
- Development velocity: 3x faster

**Usage:**
```bash
python archiagents.py scenario run microservices \
  --enterprise "StartupCo" \
  --fast
```

### 4. Enterprise Modernization

**Description:** Modernization of legacy enterprise systems and processes

**Duration:** 24-36 months

**Strategic Objectives:**
- Replace legacy core systems
- Modernize user interfaces
- Implement modern integration patterns
- Adopt agile methodologies
- Establish enterprise data platform

**Usage:**
```bash
python archiagents.py scenario run modernization \
  --enterprise "LegacyCorp" \
  --use-ai \
  --autonomous
```

### 5. Merger & Acquisition Integration

**Description:** Integration of IT systems and processes following M&A

**Duration:** 12-18 months

**Strategic Objectives:**
- Assess and rationalize IT portfolios
- Design target integration architecture
- Merge critical business systems
- Harmonize business processes
- Achieve operational synergies

**Usage:**
```bash
python archiagents.py scenario run merger-integration \
  --enterprise "MergedCorp" \
  --use-ai
```

## Output Formats

### Table Format

Human-readable ASCII table format (default for most commands).

```
+-------------------+-------------------+-------------+
| Name              | Enterprise        | Status      |
+-------------------+-------------------+-------------+
| Digital Transform | GlobalTech Corp   | in-progress |
| Cloud Migration   | TechCorp          | completed   |
+-------------------+-------------------+-------------+
```

### JSON Format

Machine-readable JSON format (useful for automation and scripting).

```json
[
  {
    "name": "Digital Transformation",
    "enterprise": "GlobalTech Corporation",
    "status": "in-progress"
  }
]
```

### YAML Format

Human and machine-readable YAML format.

```yaml
- name: Digital Transformation
  enterprise: GlobalTech Corporation
  status: in-progress
```

### Tree Format

Hierarchical tree structure for nested data.

```
project
├── name: Digital Transformation
├── enterprise: GlobalTech Corporation
├── togaf
│   ├── completed_phases (3 items)
│   │   ├── preliminary
│   │   ├── phase-a
│   │   └── phase-b
│   └── active_phase: phase-c
```

## Configuration

### Configuration File

Default location: `~/.archiagents/config.yaml`

```yaml
enterprise:
  name: My Organization
  domain: myorg.com

ai:
  provider: openai
  model: gpt-4
  api_key: null
  temperature: 0.7
  max_tokens: 4000

runtime_intelligence:
  autonomous_mode: false
  auto_approve_low_risk: false
  health_check_interval: 300

output:
  format: table
  color: true
  verbose: false

projects:
  default_path: ~/archiagents_projects
```

### Managing Configuration

```bash
# Show current configuration
python archiagents.py config show

# Set a value
python archiagents.py config set ai.provider openai

# Get a value
python archiagents.py config get ai.provider

# Reset to defaults
python archiagents.py config reset
```

## Examples & Use Cases

### Example 1: Complete Digital Transformation

```bash
# Step 1: Initialize project
python archiagents.py project init \
  --name "Digital Transformation 2025" \
  --enterprise "GlobalTech Corporation"

# Step 2: Execute all phases
python archiagents.py phase run preliminary --use-ai
python archiagents.py phase run phase-a --use-ai
python archiagents.py phase run phase-b --use-ai
python archiagents.py phase run phase-c --use-ai
python archiagents.py phase run phase-d --use-ai
python archiagents.py phase run phase-e --use-ai
python archiagents.py phase run phase-f --use-ai

# Step 3: Check progress
python archiagents.py project status

# Step 4: Analyze architecture
python archiagents.py intelligence analyze

# Step 5: Check health
python archiagents.py intelligence health

# Step 6: Generate report
python archiagents.py intelligence report --output final_report.txt
```

### Example 2: Quick Cloud Migration

```bash
# Run complete scenario in one command
python archiagents.py scenario run cloud-migration \
  --enterprise "TechCorp" \
  --use-ai \
  --fast
```

### Example 3: Architecture Decision with AI

```bash
# Make a strategic decision
python archiagents.py intelligence decide \
  --title "Cloud Provider Selection" \
  --type strategic \
  --priority critical \
  --autonomous

# Follow interactive prompts to enter options:
# - AWS (cost: $1M, time: 180 days, risk: 0.3)
# - Azure (cost: $1.2M, time: 200 days, risk: 0.4)
# - GCP (cost: $900K, time: 150 days, risk: 0.5)
```

### Example 4: Microservices Architecture

```bash
# Run microservices scenario
python archiagents.py scenario run microservices \
  --enterprise "StartupCo" \
  --use-ai \
  --autonomous \
  --fast

# Review results
cd ~/archiagents_projects/microservices_*
ls -la artifacts/
cat reports/microservices_report.md
```

## Best Practices

### 1. Project Initialization

- Use descriptive project names
- Define clear architecture scope
- Set realistic objectives and KPIs

### 2. Phase Execution

- Execute phases in sequence
- Use AI for complex phases (A, B, C, D)
- Save outputs for documentation
- Review deliverables before next phase

### 3. Runtime Intelligence

- Run analysis after each major phase
- Monitor architecture health regularly
- Use autonomous mode for low-risk decisions
- Document all major decisions

### 4. Scenario Execution

- Choose scenario matching your needs
- Run with `--fast` for demos
- Use `--autonomous` for POCs
- Review generated artifacts thoroughly

### 5. Output Management

- Use JSON format for automation
- Use table format for human review
- Save important outputs to files
- Keep decision logs organized

## Troubleshooting

### Issue: Command Not Found

**Solution:**
```bash
# Ensure you're in the correct directory
cd togaf_framework

# Run with python explicitly
python archiagents.py --help
```

### Issue: Project Not Found

**Solution:**
```bash
# Specify project path explicitly
python archiagents.py project status --project ~/archiagents_projects/my_project

# Or navigate to project directory first
cd ~/archiagents_projects/my_project
python archiagents.py project status
```

### Issue: Import Errors

**Solution:**
```bash
# Install required dependencies
pip install click pyyaml

# Verify Python path
python -c "import sys; print(sys.path)"
```

### Issue: Permission Denied

**Solution:**
```bash
# On Unix/Linux/Mac
chmod +x archiagents.py

# Or always use python explicitly
python archiagents.py
```

## Advanced Usage

### Automation with Scripts

```bash
#!/bin/bash
# automated_transformation.sh

PROJECT="digital_transform_$(date +%Y%m%d)"

# Initialize
python archiagents.py project init \
  --name "$PROJECT" \
  --enterprise "AutoCorp"

# Execute phases
for phase in preliminary phase-a phase-b phase-c phase-d; do
  python archiagents.py phase run $phase --use-ai
  python archiagents.py intelligence health
done

# Generate final report
python archiagents.py intelligence report --output "${PROJECT}_report.txt"
```

### Integration with CI/CD

```yaml
# .github/workflows/architecture.yml
name: Architecture Validation

on: [push]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Analyze Architecture
        run: |
          cd togaf_framework
          python archiagents.py intelligence analyze --format json > analysis.json
      - name: Check Health
        run: |
          cd togaf_framework
          HEALTH=$(python archiagents.py intelligence health --format json | jq '.score')
          if [ $HEALTH -lt 60 ]; then
            echo "Architecture health critical: $HEALTH"
            exit 1
          fi
```

## Summary

The ArchiAgents CLI provides a powerful, flexible command-line interface for:

✅ **Project Management** - Initialize, manage, and track architecture projects
✅ **TOGAF Execution** - Execute all 8 ADM phases with or without AI
✅ **Runtime Intelligence** - AI-driven analysis, decisions, and health monitoring
✅ **Real-World Scenarios** - Pre-built scenarios for common use cases
✅ **Comprehensive Reporting** - Generate detailed architecture reports

**Key Features:**
- 🤖 AI-powered architecture automation
- 📊 Real-time health monitoring
- 🎯 Autonomous decision-making
- 📋 5 pre-built real-world scenarios
- 🔄 Complete TOGAF ADM support
- 📈 Comprehensive analytics and reporting

For more information, use `--help` with any command:
```bash
python archiagents.py --help
python archiagents.py project --help
python archiagents.py phase run --help
python archiagents.py intelligence --help
python archiagents.py scenario --help
```

---

**ArchiAgents CLI** - Enterprise Architecture Management Made Simple
