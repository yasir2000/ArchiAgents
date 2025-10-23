# ArchiAgents CLI - Complete Reference Guide

## Overview

The **ArchiAgents CLI** is a comprehensive command-line interface providing **50+ commands** across **11 command groups** for complete enterprise architecture management using TOGAF 10, ArchiMate 3.2, and Saudi NORA compliance.

## Installation

```bash
cd togaf_framework
pip install -e .
# OR
pip install click pyyaml
```

## Quick Start

```bash
# 1. Initialize project
archiagents project init --name "Digital Banking" --enterprise "GlobalBank"

# 2. Configure AI
archiagents ai configure --provider openai --model gpt-4

# 3. Run Phase A with AI
archiagents phase run phase-a --use-ai

# 4. Generate models
archiagents model generate --type archimate-business --name "Business Architecture"

# 5. Validate architecture
archiagents validate architecture --standard all
```

## Command Groups (11 Total)

### 1. Project Management (4 commands)

Manage architecture project lifecycle.

```bash
# Initialize new project
archiagents project init \
  --name "Digital Transformation" \
  --enterprise "TechCorp Global" \
  --description "Enterprise-wide digital transformation" \
  --scope "All business units"

# List all projects
archiagents project list
archiagents project list --format json

# Show project status
archiagents project status
archiagents project status --format tree

# Delete project
archiagents project delete --project /path/to/project --confirm
```

### 2. TOGAF Phase Execution (4 commands)

Execute and manage TOGAF ADM phases.

```bash
# Run phase with AI
archiagents phase run phase-a --use-ai
archiagents phase run phase-b --use-ai --autonomous
archiagents phase run phase-c --output results.json

# List all phases
archiagents phase list

# Check phase status
archiagents phase status phase-a

# Reset phase
archiagents phase reset phase-b --confirm
```

**Available Phases:**
- `preliminary` - Foundation and Principles
- `phase-a` - Architecture Vision
- `phase-b` - Business Architecture
- `phase-c` - Information Systems Architecture
- `phase-d` - Technology Architecture
- `phase-e` - Opportunities and Solutions
- `phase-f` - Migration Planning
- `phase-g` - Implementation Governance
- `phase-h` - Architecture Change Management

### 3. AI Agent Management (5 commands)

Configure and run multi-provider AI agents.

```bash
# Configure AI provider
archiagents ai configure --provider openai --model gpt-4 --api-key sk-...
archiagents ai configure --provider anthropic --model claude-3-opus-20240229
archiagents ai configure --provider ollama --model llama3.1  # FREE local

# Test AI connection
archiagents ai test --prompt "Explain TOGAF ADM in one sentence"

# List available models
archiagents ai list-models
archiagents ai list-models --provider openai

# List AI agent roles
archiagents ai agents
archiagents ai agents --format json

# Run AI task
archiagents ai run --task "Analyze current business processes"
archiagents ai run --task "Design cloud migration" --agent-role solution_architect
archiagents ai run --task "Security assessment" --agent-role security_architect --output results.json
```

**Available Providers:**
- `openai` - GPT-4, GPT-3.5 Turbo
- `anthropic` - Claude 3 (Opus, Sonnet, Haiku)
- `google` - Gemini 1.5 Pro, Flash
- `azure` - Azure OpenAI
- `mistral` - Mistral Large, Medium, Small
- `ollama` - Local models (Llama 3.1, Mistral, Mixtral, Phi-2, CodeLlama) **FREE**

**Agent Roles:**
- `chief_architect` - Strategic planning, stakeholder alignment
- `business_architect` - Process modeling, capability mapping
- `data_architect` - Data modeling, information architecture
- `application_architect` - Application portfolio, integration
- `infrastructure_architect` - Cloud, network, infrastructure
- `security_architect` - Security patterns, threat modeling
- `solution_architect` - Solution design, technology selection
- `migration_specialist` - Migration planning, roadmaps
- `governance_specialist` - Governance frameworks, compliance
- `requirements_analyst` - Requirements elicitation, documentation

### 4. Runtime Intelligence (4 commands)

AI-driven decision-making and autonomous architecture management.

```bash
# Analyze architecture
archiagents intelligence analyze
archiagents intelligence analyze --autonomous
archiagents intelligence analyze --format json

# Make architecture decision
archiagents intelligence decide \
  --title "Cloud Migration Strategy" \
  --type strategic \
  --priority high \
  --autonomous

# Check architecture health
archiagents intelligence health
archiagents intelligence health --format tree

# Generate intelligence report
archiagents intelligence report --output intelligence_report.json
```

### 5. Model Generation (5 commands)

Generate ArchiMate, BPMN, and UML models with AI.

```bash
# Generate ArchiMate model
archiagents model generate \
  --type archimate-business \
  --name "Business Architecture" \
  --format mermaid --format gojs

# Generate UML model
archiagents model generate \
  --type uml-class \
  --name "Domain Model" \
  --format mermaid --format archi

# Generate BPMN model
archiagents model generate \
  --type bpmn-process \
  --name "Order Processing"

# List models
archiagents model list
archiagents model list --format json

# Validate model
archiagents model validate --model-id my-model

# Export model
archiagents model export --model-id my-model --format mermaid

# Improve model with AI
archiagents model improve --model-id my-model
```

**Model Types (21 total):**

*ArchiMate (7 types):*
- `archimate-strategy` - Goals, capabilities, value streams
- `archimate-business` - Processes, functions, services
- `archimate-application` - Applications, interfaces, data
- `archimate-technology` - Infrastructure, platforms, networks
- `archimate-physical` - Facilities, equipment, materials
- `archimate-implementation` - Work packages, deliverables
- `archimate-multi-layer` - Cross-layer models

*BPMN (3 types):*
- `bpmn-process` - Business processes
- `bpmn-collaboration` - Inter-organizational processes
- `bpmn-choreography` - Message exchanges

*UML (12 types):*
- `uml-class` - Class diagrams
- `uml-sequence` - Sequence diagrams
- `uml-use-case` - Use case diagrams
- `uml-activity` - Activity diagrams
- `uml-state` - State machine diagrams
- `uml-component` - Component diagrams
- `uml-deployment` - Deployment diagrams
- `uml-object` - Object diagrams
- `uml-package` - Package diagrams
- `uml-composite` - Composite structure
- `uml-timing` - Timing diagrams
- `uml-interaction` - Interaction overview

**Output Formats (6 total):**
- `text` - Markdown documentation
- `mermaid` - Mermaid diagrams
- `kroki` - PlantUML/Kroki
- `archi` - Archi tool XML
- `gojs` - GoJS JSON
- `ea` - Enterprise Architect XMI

### 6. Report Generation (3 commands)

Generate comprehensive architecture reports.

```bash
# Generate report
archiagents report generate --type architecture-overview --format pdf
archiagents report generate --type gap-analysis --format html
archiagents report generate --type executive-summary --format docx
archiagents report generate --type roadmap --format markdown

# List reports
archiagents report list
archiagents report list --format json

# Compare architectures
archiagents report compare --baseline current --target future --output comparison.md
```

**Report Types:**
- `architecture-overview` - Complete architecture overview
- `phase-summary` - TOGAF phase deliverables summary
- `gap-analysis` - Current vs target gap analysis
- `risk-assessment` - Risk identification and assessment
- `roadmap` - Transformation roadmap
- `compliance` - Compliance assessment (TOGAF, ArchiMate, NORA)
- `portfolio` - Application portfolio analysis
- `health-check` - Architecture health metrics
- `executive-summary` - High-level executive summary
- `technical-deep-dive` - Technical detailed analysis
- `cost-benefit` - Cost-benefit analysis
- `stakeholder` - Stakeholder analysis

**Report Formats:**
- `pdf` - PDF document
- `html` - HTML webpage
- `markdown` - Markdown document
- `docx` - Microsoft Word
- `json` - JSON data

### 7. Scenario Execution (3 commands)

Run pre-built real-world scenarios.

```bash
# List scenarios
archiagents scenario list

# Describe scenario
archiagents scenario describe cloud-migration
archiagents scenario describe digital-transformation --format json

# Run scenario
archiagents scenario run cloud-migration \
  --enterprise "TechCorp" \
  --use-ai \
  --autonomous

archiagents scenario run digital-transformation \
  --enterprise "GlobalBank" \
  --use-ai
```

**Available Scenarios:**
- `digital-transformation` - Complete digital transformation (18-24 months)
- `cloud-migration` - On-premises to cloud migration (6-12 months)
- `microservices` - Monolith to microservices (12-18 months)
- `modernization` - Legacy system modernization (24-36 months)
- `merger-integration` - M&A IT integration (12-18 months)

### 8. Validation & Quality (3 commands)

Validate architecture quality and compliance.

```bash
# Validate against standards
archiagents validate architecture --standard togaf
archiagents validate architecture --standard archimate --strict
archiagents validate architecture --standard nora
archiagents validate architecture --standard all

# Check completeness
archiagents validate completeness

# Validate quality
archiagents validate quality
archiagents validate quality --aspect consistency
archiagents validate quality --aspect traceability
```

**Validation Standards:**
- `togaf` - TOGAF 10 compliance
- `archimate` - ArchiMate 3.2 compliance
- `nora` - Saudi NORA compliance
- `all` - All standards

**Quality Aspects:**
- `consistency` - Naming, uniqueness, relationships
- `coherence` - Layer alignment, patterns
- `traceability` - Requirements, decisions, impacts
- `documentation` - Completeness, quality
- `all` - All aspects

### 9. Import Commands (3 commands)

Import architecture from external tools.

```bash
# Import from Archi tool
archiagents import from-archi model.archimate
archiagents import from-archi model.xml --merge

# Import from Enterprise Architect
archiagents import from-ea model.xmi

# Import from JSON
archiagents import from-json model.json --model-type archimate
```

**Supported Import Formats:**
- Archi Tool (`.archimate`, `.xml`)
- Enterprise Architect (`.xmi`)
- Generic JSON (`.json`)

### 10. Export Commands (4 commands)

Export architecture to external tools.

```bash
# Export to Archi
archiagents export to-archi --model-id my-model --output model.archimate

# Export to Enterprise Architect
archiagents export to-ea --model-id my-model --output model.xmi

# Export to Mermaid
archiagents export to-mermaid --model-id my-model --output diagram.mmd

# Batch export all models
archiagents export batch --format all
archiagents export batch --format mermaid --output-dir ./exports
```

**Supported Export Formats:**
- Archi Tool (`.archimate`)
- Enterprise Architect (`.xmi`)
- Mermaid (`.mmd`)
- GoJS (`.json`)

### 11. Configuration Management (7 commands)

Manage CLI and project configuration.

```bash
# Show configuration
archiagents config show
archiagents config show --global-config
archiagents config show --format json

# Set configuration value
archiagents config set output.format json
archiagents config set ai.provider openai
archiagents config set --global-config projects.default_path /path/to/projects

# Get configuration value
archiagents config get ai.provider
archiagents config get output.format

# Reset configuration
archiagents config reset --confirm
archiagents config reset --global-config --confirm

# Validate configuration
archiagents config validate

# Export configuration
archiagents config export --output config.yaml
archiagents config export --output config.json --format json

# Import configuration
archiagents config import config.yaml
archiagents config import config.json --merge
```

## Global Options

Available for all commands:

```bash
--help              Show help message
--version           Show version
--config PATH       Custom configuration file
--verbose           Enable verbose output
--format FORMAT     Output format (table, json, yaml, tree)
--color / --no-color Enable/disable colored output
```

## Configuration File

Default location: `~/.archiagents/config.yaml`

```yaml
# Global Configuration
projects:
  default_path: ~/archiagents_projects

ai:
  provider: openai
  model: gpt-4
  temperature: 0.7
  max_tokens: 4000

output:
  format: table
  color: true
  verbose: false

runtime_intelligence:
  enabled: true
  autonomous_mode: false
```

Project configuration: `.archiagents/project.yaml`

```yaml
project:
  name: Digital Transformation
  enterprise: TechCorp Global
  description: Enterprise-wide digital transformation
  scope: All business units
  status: in-progress

togaf:
  version: "10"
  completed_phases: ["preliminary", "phase-a", "phase-b"]
  active_phase: "phase-c"

ai:
  enabled: true
  provider: openai
  model: gpt-4

nora:
  compliance_enabled: true
  arabic_support: true
  data_sovereignty: true
```

## Advanced Workflows

### Complete TOGAF Cycle with AI

```bash
# 1. Initialize project
archiagents project init --name "Digital Banking" --enterprise "GlobalBank"

# 2. Configure AI
archiagents ai configure --provider openai --model gpt-4

# 3. Run all phases
for phase in preliminary phase-a phase-b phase-c phase-d phase-e phase-f phase-g phase-h; do
  archiagents phase run $phase --use-ai --autonomous
done

# 4. Generate models
archiagents model generate --type archimate-multi-layer --name "Complete Architecture"

# 5. Validate
archiagents validate architecture --standard all
archiagents validate completeness
archiagents validate quality

# 6. Generate reports
archiagents report generate --type architecture-overview --format pdf
archiagents report generate --type executive-summary --format docx

# 7. Export
archiagents export batch --format all
```

### Cloud Migration Scenario

```bash
# Run complete cloud migration scenario
archiagents scenario run cloud-migration \
  --enterprise "TechCorp" \
  --use-ai \
  --autonomous

# Or step-by-step
archiagents project init --name "Cloud Migration" --enterprise "TechCorp"
archiagents ai configure --provider openai --model gpt-4
archiagents phase run preliminary --use-ai
archiagents phase run phase-a --use-ai
archiagents phase run phase-d --use-ai  # Technology Architecture
archiagents phase run phase-e --use-ai  # Opportunities & Solutions
archiagents phase run phase-f --use-ai  # Migration Planning
archiagents report generate --type roadmap --format pdf
```

### Model Generation & Export

```bash
# Generate multiple models
archiagents model generate --type archimate-strategy --name "Strategy Layer"
archiagents model generate --type archimate-business --name "Business Layer"
archiagents model generate --type archimate-application --name "Application Layer"
archiagents model generate --type archimate-technology --name "Technology Layer"

# Export all to Archi
archiagents export batch --format archi --output-dir ./archi_exports

# Export to Mermaid for documentation
archiagents export batch --format mermaid --output-dir ./docs/diagrams
```

## Troubleshooting

### Common Issues

**AI Configuration Issues:**
```bash
# Test AI connection
archiagents ai test

# Verify configuration
archiagents config show | grep ai

# Reconfigure
archiagents ai configure --provider openai --model gpt-4
```

**Model Generation Failures:**
```bash
# Enable verbose output
archiagents model generate --type archimate-business --name "Test" --verbose

# Validate existing models
archiagents model validate --model-id my-model
```

**Import/Export Issues:**
```bash
# Check file format
file model.archimate

# Try different format
archiagents export to-mermaid --model-id my-model
```

## Performance Tips

1. **Use local Ollama for development** - FREE and private
2. **Enable caching** - Set `cache_enabled: true` in config
3. **Batch operations** - Use `export batch` for multiple files
4. **Selective validation** - Validate specific aspects instead of `--standard all`
5. **JSON output for automation** - Use `--format json` in scripts

## Integration Examples

### GitHub Actions CI/CD

```yaml
- name: Validate Architecture
  run: |
    archiagents validate architecture --standard all
    archiagents validate completeness
    archiagents validate quality
```

### Pre-commit Hook

```bash
#!/bin/bash
archiagents validate architecture --standard togaf --strict
if [ $? -ne 0 ]; then
  echo "Architecture validation failed"
  exit 1
fi
```

### Automated Reporting

```bash
#!/bin/bash
# Generate weekly reports
archiagents report generate --type architecture-overview --format pdf
archiagents report generate --type gap-analysis --format html
archiagents report generate --type roadmap --format markdown
```

## Summary

The ArchiAgents CLI provides:

- ✅ **50+ Commands** across 11 command groups
- ✅ **Multi-Provider AI** - OpenAI, Claude, Gemini, Ollama (FREE local)
- ✅ **21 Model Types** - ArchiMate, BPMN, UML
- ✅ **6 Export Formats** - Text, Mermaid, Kroki, Archi, GoJS, EA
- ✅ **TOGAF 10 Complete** - All 9 phases automated
- ✅ **ArchiMate 3.2** - Full layer coverage
- ✅ **Saudi NORA** - Government compliance
- ✅ **Import/Export** - Archi, Enterprise Architect interoperability
- ✅ **Quality Validation** - Standards compliance, completeness, quality checks
- ✅ **Real-World Scenarios** - 5 pre-built scenarios
- ✅ **Comprehensive Reports** - 12 report types in 5 formats

For more help: `archiagents --help` or `archiagents COMMAND --help`
