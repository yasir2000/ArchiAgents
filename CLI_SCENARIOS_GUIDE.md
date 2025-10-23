# ArchiAgents CLI - Real-World Business Scenarios

## Overview

This document describes 7 comprehensive, end-to-end real-world business scenarios that demonstrate the full capabilities of the ArchiAgents CLI. Each scenario represents actual enterprise architecture challenges across different industries.

## Test Scripts

Three test scripts are provided for different environments:

1. **`test_cli_scenarios.py`** - Python script (cross-platform)
2. **`test-cli-scenarios.sh`** - Bash script (Linux/Mac/Git Bash)
3. **`test-cli-scenarios.bat`** - Batch script (Windows CMD/PowerShell)

## Running the Tests

### Python (Recommended)
```bash
python test_cli_scenarios.py
```

### Bash (Linux/Mac)
```bash
chmod +x test-cli-scenarios.sh
./test-cli-scenarios.sh
```

### Windows Batch
```cmd
test-cli-scenarios.bat
```

---

## Scenario 1: Digital Banking Transformation

### Business Context
- **Company**: GlobalBank International
- **Industry**: Financial Services / Retail Banking
- **Challenge**: Losing market share to digital-first competitors (Revolut, N26, Chime)
- **Current State**: Legacy mainframe systems, limited mobile capabilities
- **Goal**: Complete digital transformation
- **Timeline**: 18 months
- **Budget**: $15 Million
- **Team Size**: 50+ people (architects, developers, business analysts)

### Expected Outcomes
- 50% operational cost reduction
- 3x customer base growth
- 90% customer satisfaction score
- 24/7 availability
- Real-time transaction processing

### CLI Commands Demonstrated

```bash
# 1. Initialize project
archiagents project init \
  --name "Digital Banking Modernization" \
  --enterprise "GlobalBank International" \
  --description "Complete digital transformation" \
  --budget 15000000 \
  --timeline "18 months"

# 2. Configure AI (FREE local inference)
archiagents ai configure --provider ollama --model llama3.1

# 3. Execute TOGAF Phase A - Architecture Vision
archiagents phase run phase-a \
  --project "Digital Banking Modernization" \
  --use-ai \
  --scope "Retail banking digital transformation"

# 4. Generate stakeholder map (ArchiMate Motivation Layer)
archiagents model generate \
  --type archimate-motivation \
  --name "Stakeholder Value Map" \
  --format mermaid

# 5. Execute Phase B - Business Architecture
archiagents phase run phase-b \
  --project "Digital Banking Modernization"

# 6. Generate BPMN business process
archiagents model generate \
  --type bpmn-process \
  --name "Digital Account Opening" \
  --format mermaid

# 7-9. Execute Phases C & D (Information Systems & Technology)
archiagents phase run phase-c --project "Digital Banking Modernization"
archiagents phase run phase-d --project "Digital Banking Modernization"

# 10. AI-powered architecture health analysis
archiagents intelligence health \
  --project "Digital Banking Modernization" \
  --analyze-gaps \
  --analyze-risks

# 11. Execute Phase E & F (Opportunities & Migration)
archiagents phase run phase-e --project "Digital Banking Modernization"
archiagents phase run phase-f --project "Digital Banking Modernization"

# 12. Generate comprehensive PDF report
archiagents report generate \
  --type comprehensive \
  --project "Digital Banking Modernization" \
  --format pdf

# 13. Validate TOGAF compliance
archiagents validate architecture \
  --standard togaf \
  --project "Digital Banking Modernization"

# 14. Export to Archi tool
archiagents export to-archi \
  --project "Digital Banking Modernization" \
  --output "./exports/digital-banking.xml"
```

### Deliverables Generated
- Architecture Vision document
- Stakeholder value map (Mermaid diagram)
- Business capability model
- BPMN process models
- Application landscape (current & target)
- Technology architecture diagrams
- Gap analysis report
- Migration roadmap
- Comprehensive PDF report (100+ pages)
- Archi XML export

---

## Scenario 2: E-Commerce Platform Cloud Migration

### Business Context
- **Company**: TechRetail Corp
- **Industry**: E-Commerce / Retail
- **Challenge**: On-premise infrastructure can't scale for peak traffic
- **Current State**: 3 data centers, 200+ servers, monolithic architecture
- **Goal**: Migrate to AWS cloud
- **Timeline**: 12 months
- **Budget**: $8 Million
- **Migration Strategy**: Lift-and-shift followed by optimization

### Expected Outcomes
- 99.99% availability (from current 99.5%)
- Auto-scaling for Black Friday traffic
- 40% cost reduction in 2 years
- Global content delivery (CDN)
- Disaster recovery capability

### CLI Commands Demonstrated

```bash
# 1. Initialize project
archiagents project init \
  --name "E-Commerce Cloud Migration" \
  --enterprise "TechRetail Corp" \
  --budget 8000000

# 2. Run pre-built cloud migration scenario
archiagents scenario run cloud-migration \
  --enterprise "TechRetail Corp" \
  --source-environment "On-Premise Data Center" \
  --target-cloud "AWS" \
  --migration-strategy "lift-and-shift"

# 3. Generate AWS infrastructure model
archiagents model generate \
  --type archimate-technology \
  --name "AWS Cloud Architecture" \
  --format mermaid

# 4. AI-powered risk analysis
archiagents intelligence analyze \
  --project "E-Commerce Cloud Migration" \
  --analyze-risks \
  --analyze-dependencies

# 5. Generate migration roadmap
archiagents model generate \
  --type archimate-implementation \
  --name "Cloud Migration Roadmap" \
  --format mermaid

# 6. Validate architecture quality
archiagents validate quality \
  --project "E-Commerce Cloud Migration" \
  --check-consistency
```

### Deliverables Generated
- AWS infrastructure architecture
- Migration risk assessment
- Dependency analysis
- Phased migration roadmap (3 phases)
- Cost-benefit analysis
- Mermaid diagrams

---

## Scenario 3: Healthcare Digital Transformation (Saudi NORA)

### Business Context
- **Company**: HealthCare Plus (Saudi Arabia)
- **Industry**: Healthcare / Digital Health
- **Challenge**: Build national health information exchange
- **Current State**: Fragmented hospital systems, paper records
- **Goal**: Unified digital health platform
- **Timeline**: 24 months
- **Budget**: $20 Million
- **Compliance**: Saudi NORA, PDPL, HIPAA, ISO 27001

### Expected Outcomes
- Vision 2030 alignment
- 90% digital health services
- Real-time patient data exchange
- Arabic-first UI/UX
- Data sovereignty compliance
- National interoperability

### CLI Commands Demonstrated

```bash
# 1. Initialize with compliance requirements
archiagents project init \
  --name "Digital Health Platform" \
  --enterprise "HealthCare Plus KSA" \
  --compliance "NORA,PDPL,HIPAA" \
  --budget 20000000

# 2. Configure AI with Arabic support
archiagents ai configure \
  --provider openai \
  --model gpt-4 \
  --language ar \
  --region "Middle East"

# 3. Execute Phase A with NORA alignment
archiagents phase run phase-a \
  --project "Digital Health Platform" \
  --use-ai \
  --compliance-frameworks "NORA,PDPL" \
  --vision "Vision 2030 digital health services"

# 4. Generate NORA-compliant architecture
archiagents model generate \
  --type archimate-strategy \
  --name "NORA Strategic Architecture" \
  --format mermaid

# 5. Validate NORA compliance
archiagents validate architecture \
  --standard nora \
  --project "Digital Health Platform" \
  --check-data-sovereignty \
  --check-arabic-support

# 6. Generate multi-standard compliance report
archiagents report generate \
  --type compliance \
  --project "Digital Health Platform" \
  --standards "NORA,PDPL,HIPAA" \
  --format pdf
```

### Deliverables Generated
- NORA-compliant strategic architecture
- Data sovereignty validation
- Arabic-first design specifications
- Multi-standard compliance report
- Vision 2030 alignment matrix

---

## Scenario 4: Microservices Modernization

### Business Context
- **Company**: FinTech Innovations
- **Industry**: Financial Technology / Payments
- **Challenge**: Monolithic Java application limiting innovation
- **Current State**: Single codebase, 500K LOC, 30-minute builds
- **Goal**: Microservices architecture
- **Timeline**: 15 months
- **Budget**: $10 Million
- **Target**: 100+ microservices on Kubernetes

### Expected Outcomes
- Independent service deployment
- 15-minute deployment cycles
- Team autonomy
- Technology diversity
- Better scalability and resilience

### CLI Commands Demonstrated

```bash
# 1. Initialize project
archiagents project init \
  --name "Microservices Modernization" \
  --enterprise "FinTech Innovations"

# 2. AI analysis for service decomposition
archiagents intelligence analyze \
  --project "Microservices Modernization" \
  --current-architecture "Monolithic Java" \
  --target-architecture "Microservices on K8s" \
  --recommend-decomposition

# 3. Generate microservices model
archiagents model generate \
  --type archimate-application \
  --name "Microservices Architecture" \
  --format mermaid

# 4. Generate API catalog (UML)
archiagents model generate \
  --type uml-component \
  --name "API Gateway & Services" \
  --format kroki

# 5. AI-driven migration strategy decision
archiagents intelligence decide \
  --decision-type "migration-strategy" \
  --options "Strangler Fig, Big Bang, Incremental" \
  --criteria "Risk, Cost, Time"
```

### Deliverables Generated
- Service boundary recommendations
- Domain model decomposition
- API specifications (REST/GraphQL)
- Migration strategy decision matrix
- UML component diagrams

---

## Scenario 5: Smart City IoT Platform

### Business Context
- **Company**: Smart City Solutions
- **Industry**: Government / Smart Cities
- **Challenge**: City-wide IoT infrastructure
- **Current State**: Siloed city systems (traffic, energy, waste)
- **Goal**: Integrated IoT platform
- **Timeline**: 36 months
- **Budget**: $50 Million
- **Scale**: 50,000+ IoT devices, 10M+ daily events

### Expected Outcomes
- 30% traffic congestion reduction
- 25% energy consumption reduction
- Real-time city monitoring
- Citizen engagement portal
- Predictive maintenance

### CLI Commands Demonstrated

```bash
# 1. Initialize smart city project
archiagents project init \
  --name "Smart City IoT Platform" \
  --enterprise "Smart City Solutions"

# 2. Execute all TOGAF phases
archiagents phase run phase-a --project "Smart City IoT Platform"
archiagents phase run phase-b --project "Smart City IoT Platform"
archiagents phase run phase-c --project "Smart City IoT Platform"
archiagents phase run phase-d --project "Smart City IoT Platform"

# 3. Generate physical IoT architecture
archiagents model generate \
  --type archimate-physical \
  --name "IoT Infrastructure" \
  --description "Sensors, gateways, edge devices" \
  --format mermaid

# 4. Generate data architecture
archiagents model generate \
  --type archimate-data \
  --name "Smart City Data Architecture" \
  --format mermaid

# 5. Compare architectures
archiagents report compare-architectures \
  --project "Smart City IoT Platform" \
  --baseline "Current City Systems" \
  --target "Integrated IoT Platform"
```

### Deliverables Generated
- Physical infrastructure model (sensors, gateways)
- Data flow architecture
- Real-time analytics platform design
- Edge computing architecture
- Baseline vs target comparison

---

## Scenario 6: AI-Driven Decision Making

### Business Context
**Purpose**: Demonstrate autonomous AI agent capabilities

### CLI Commands Demonstrated

```bash
# 1. List available AI models
archiagents ai list-models

# 2. List specialized AI agent roles
archiagents ai list-agents

# 3. Configure multiple providers
archiagents ai configure --provider openai --model gpt-4o
archiagents ai configure --provider anthropic --model claude-3-5-sonnet
archiagents ai configure --provider google --model gemini-pro

# 4. AI agent collaboration
archiagents ai run-task \
  --task "Design microservices for payment system" \
  --agents "solution-architect,security-architect,data-architect" \
  --collaboration-mode "debate"

# 5. Autonomous architecture decisions
archiagents intelligence decide \
  --decision-type "architecture-pattern" \
  --context "High-traffic platform, 10M users" \
  --autonomous-mode \
  --confidence-threshold 0.85
```

### Capabilities Demonstrated
- Multi-provider AI support
- AI agent collaboration (debate mode)
- Autonomous decision-making
- Confidence-based recommendations
- 20+ specialized agent roles

---

## Scenario 7: Tool Interoperability

### Business Context
**Purpose**: Import, validate, and export across multiple tools

### CLI Commands Demonstrated

```bash
# 1. Import from Archi tool
archiagents import from-archi \
  --file "./existing-architecture.xml" \
  --project "Legacy System Architecture"

# 2. Validate imported architecture
archiagents validate completeness \
  --project "Legacy System Architecture" \
  --check-relationships \
  --check-views

# 3. AI enhancement
archiagents intelligence analyze \
  --project "Legacy System Architecture" \
  --identify-gaps \
  --recommend-improvements

# 4. Export to multiple formats
archiagents export batch \
  --project "Legacy System Architecture" \
  --formats "archi,mermaid,gojs,ea" \
  --output-dir "./exports/multi-format"
```

### Capabilities Demonstrated
- Archi XML import
- Enterprise Architect XMI import/export
- JSON import/export
- Mermaid diagram generation
- GoJS JSON export
- Kroki diagram generation
- Batch export to multiple formats

---

## Summary of CLI Features Tested

### Command Groups (11)
1. ✅ **project** - Project lifecycle management
2. ✅ **phase** - TOGAF ADM phase execution
3. ✅ **ai** - AI configuration and tasks
4. ✅ **intelligence** - Runtime intelligence
5. ✅ **model** - Model generation (21 types)
6. ✅ **report** - Report generation
7. ✅ **scenario** - Pre-built scenarios
8. ✅ **validate** - Quality validation
9. ✅ **import** - Import from tools
10. ✅ **export** - Export to tools
11. ✅ **config** - Configuration management

### Model Types Tested (12 of 21)
- ArchiMate: Motivation, Business, Application, Technology, Data, Physical, Strategy, Implementation
- BPMN: Process
- UML: Component

### Export Formats Tested (5 of 6)
- Mermaid diagrams
- Kroki diagrams
- Archi XML
- GoJS JSON
- PDF reports

### AI Providers Tested
- Ollama (FREE local models)
- OpenAI GPT-4
- Anthropic Claude
- Google Gemini

### Standards Validated
- TOGAF 10 ADM
- ArchiMate 3.2
- Saudi NORA
- PDPL (Saudi Privacy Law)
- HIPAA

---

## Expected Output

Each scenario generates:
1. **Project artifacts** in `./projects/[project-name]/`
2. **Models** in `./models/`
3. **Reports** in `./reports/`
4. **Exports** in `./exports/`
5. **Logs** in `./logs/`

### Sample Directory Structure
```
ArchiAgents/
├── projects/
│   ├── digital-banking-modernization/
│   ├── e-commerce-cloud-migration/
│   ├── digital-health-platform/
│   ├── microservices-modernization/
│   ├── smart-city-iot/
│   └── legacy-system-architecture/
├── models/
│   ├── stakeholder-value-map.mermaid
│   ├── digital-account-opening.bpmn.mermaid
│   ├── application-architecture.archimate.mermaid
│   ├── aws-cloud-architecture.mermaid
│   └── iot-infrastructure.mermaid
├── reports/
│   ├── digital-banking-comprehensive.pdf
│   ├── cloud-migration-risks.json
│   ├── nora-compliance-report.pdf
│   └── architecture-comparison.html
├── exports/
│   ├── digital-banking-archi.xml
│   ├── multi-format/
│   │   ├── archi/
│   │   ├── mermaid/
│   │   ├── gojs/
│   │   └── ea/
└── logs/
    ├── ai-agent-collaboration.log
    └── autonomous-decisions.log
```

---

## Running Individual Scenarios

You can run individual scenarios by extracting the relevant commands:

```bash
# Just run Digital Banking scenario
python test_cli_scenarios.py --scenario 1

# Or manually execute specific commands
python -m togaf_framework.cli.main project init \
  --name "My Project" \
  --enterprise "My Company"
```

---

## Troubleshooting

### Common Issues

1. **Module not found**
   ```bash
   export PYTHONPATH="${PWD}:${PWD}/togaf_framework:${PYTHONPATH}"
   ```

2. **AI provider not configured**
   ```bash
   archiagents ai configure --provider ollama --model llama3.1
   ```

3. **Permission denied (bash script)**
   ```bash
   chmod +x test-cli-scenarios.sh
   ```

---

## Next Steps

After running these scenarios:

1. **Review Generated Models**
   - Open `.mermaid` files in Mermaid Live Editor
   - Import `.xml` files into Archi tool
   - View PDF reports

2. **Customize for Your Needs**
   - Modify scenarios for your enterprise
   - Add your own compliance standards
   - Configure your AI providers

3. **Extend with More Scenarios**
   - Add industry-specific scenarios
   - Create custom validation rules
   - Build organization-specific templates

---

## Additional Resources

- [CLI Complete Reference](./CLI_COMPLETE_REFERENCE.md)
- [Brand Guidelines](./BRAND_GUIDELINES.md)
- [TOGAF Framework Guide](./Docs/TOGAF_Guide.md)
- [AI Multi-Provider Guide](./LLM_PROVIDERS_GUIDE.md)

---

*Last Updated: October 23, 2025*
