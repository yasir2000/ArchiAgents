# ArchiAgents CLI - Quick Reference Card

## 🚀 Quick Start (3 Commands)

```bash
# 1. Initialize project
archiagents project init --name "My Project" --enterprise "MyCompany"

# 2. Configure AI (use FREE local Ollama)
archiagents ai configure --provider ollama --model llama3.1

# 3. Run Phase A with AI
archiagents phase run phase-a --use-ai
```

## 📋 Command Groups (11 Total)

```
archiagents [OPTIONS] COMMAND [ARGS]

Command Groups:
  project       Project lifecycle (init, list, status, delete)
  phase         TOGAF phases (run, list, status, reset)
  ai            AI agents (configure, test, run, agents, list-models)
  intelligence  Runtime intelligence (analyze, decide, health, report)
  model         Model generation (generate, list, validate, export, improve)
  report        Reports (generate, list, compare)
  scenario      Scenarios (list, describe, run)
  validate      Validation (architecture, completeness, quality)
  import        Import (from-archi, from-ea, from-json)
  export        Export (to-archi, to-ea, to-mermaid, batch)
  config        Configuration (show, set, get, reset, validate, export, import)
```

## 🎯 Most Used Commands

### Project Setup
```bash
archiagents project init --name "Digital Banking" --enterprise "GlobalBank"
archiagents project list
archiagents project status
```

### AI Configuration
```bash
# Cloud provider
archiagents ai configure --provider openai --model gpt-4 --api-key sk-...

# FREE local (recommended for learning)
archiagents ai configure --provider ollama --model llama3.1

# Test connection
archiagents ai test

# List agent roles
archiagents ai agents
```

### TOGAF Phases
```bash
# Run with AI
archiagents phase run phase-a --use-ai
archiagents phase run phase-b --use-ai --autonomous

# Run complete scenario
archiagents scenario run cloud-migration --enterprise "TechCorp" --use-ai
```

### Model Generation
```bash
# ArchiMate models
archiagents model generate --type archimate-business --name "Business Layer"
archiagents model generate --type archimate-application --name "App Layer"

# UML models
archiagents model generate --type uml-class --name "Domain Model"
archiagents model generate --type uml-sequence --name "User Login"

# BPMN process
archiagents model generate --type bpmn-process --name "Order Processing"

# List all models
archiagents model list
```

### Validation & Quality
```bash
# Validate standards
archiagents validate architecture --standard togaf
archiagents validate architecture --standard all

# Check completeness
archiagents validate completeness

# Check quality
archiagents validate quality
```

### Reports
```bash
# Generate reports
archiagents report generate --type architecture-overview --format pdf
archiagents report generate --type gap-analysis --format html
archiagents report generate --type executive-summary --format docx

# List reports
archiagents report list

# Compare architectures
archiagents report compare --baseline current --target future
```

### Import/Export
```bash
# Import
archiagents import from-archi model.archimate
archiagents import from-ea model.xmi

# Export
archiagents export to-archi --model-id my-model
archiagents export to-mermaid --model-id my-model

# Batch export
archiagents export batch --format all
```

## 🤖 AI Providers (6 Total)

| Provider | Models | Cost | Setup |
|----------|--------|------|-------|
| **Ollama** | llama3.1, mistral, mixtral, phi-2 | **FREE** | `ollama pull llama3.1` |
| OpenAI | gpt-4, gpt-3.5-turbo | $$$ | API key required |
| Anthropic | claude-3-opus/sonnet/haiku | $$$ | API key required |
| Google | gemini-1.5-pro/flash | $$ | API key required |
| Azure | gpt-4, gpt-35-turbo | $$$ | API key + endpoint |
| Mistral | mistral-large/medium/small | $$ | API key required |

## 📊 Model Types (21 Total)

### ArchiMate (7)
- `archimate-strategy` - Goals, capabilities
- `archimate-business` - Processes, services
- `archimate-application` - Applications, data
- `archimate-technology` - Infrastructure
- `archimate-physical` - Facilities, equipment
- `archimate-implementation` - Work packages
- `archimate-multi-layer` - Cross-layer

### BPMN (3)
- `bpmn-process` - Business processes
- `bpmn-collaboration` - Inter-org processes
- `bpmn-choreography` - Message exchanges

### UML (12)
- `uml-class`, `uml-sequence`, `uml-use-case`
- `uml-activity`, `uml-state`, `uml-component`
- `uml-deployment`, `uml-object`, `uml-package`
- `uml-composite`, `uml-timing`, `uml-interaction`

## 📋 Report Types (12 Total)

```bash
architecture-overview    # Complete overview
phase-summary           # TOGAF phases summary
gap-analysis            # Gap identification
risk-assessment         # Risk analysis
roadmap                 # Transformation roadmap
compliance              # Standards compliance
portfolio               # Application portfolio
health-check            # Architecture health
executive-summary       # Executive report
technical-deep-dive     # Technical details
cost-benefit            # Cost-benefit analysis
stakeholder             # Stakeholder analysis
```

## ✅ Validation Standards

```bash
--standard togaf        # TOGAF 10 compliance
--standard archimate    # ArchiMate 3.2 compliance
--standard nora         # Saudi NORA compliance
--standard all          # All standards
```

## 🎬 Real-World Scenarios (5)

```bash
digital-transformation  # 18-24 months
cloud-migration        # 6-12 months
microservices          # 12-18 months
modernization          # 24-36 months
merger-integration     # 12-18 months
```

## 🔧 Configuration

```bash
# Show config
archiagents config show

# Set values
archiagents config set ai.provider openai
archiagents config set output.format table

# Export/Import
archiagents config export --output config.yaml
archiagents config import config.yaml
```

## 💡 Pro Tips

1. **Use local Ollama for development** (FREE, no API costs)
   ```bash
   archiagents ai configure --provider ollama --model llama3.1
   ```

2. **Enable verbose mode for debugging**
   ```bash
   archiagents --verbose phase run phase-a
   ```

3. **Batch export for documentation**
   ```bash
   archiagents export batch --format mermaid --output-dir ./docs
   ```

4. **JSON output for automation**
   ```bash
   archiagents project list --format json
   archiagents model list --format json
   ```

5. **Complete TOGAF cycle in one scenario**
   ```bash
   archiagents scenario run digital-transformation --use-ai --autonomous
   ```

## 📚 Documentation

- `CLI_COMPLETE_REFERENCE.md` - Complete command reference (2,000+ lines)
- `CLI_USER_GUIDE.md` - Detailed user guide
- `CLI_ENHANCEMENT_SUMMARY.md` - What's new
- `README.md` - Framework overview

## 🆘 Help Commands

```bash
archiagents --help                      # Main help
archiagents COMMAND --help              # Command group help
archiagents COMMAND SUBCOMMAND --help   # Specific command help
```

## ✨ Features Summary

- ✅ **50+ Commands** across 11 groups
- ✅ **6 AI Providers** (including FREE Ollama)
- ✅ **10 AI Agent Roles**
- ✅ **21 Model Types** (ArchiMate, BPMN, UML)
- ✅ **6 Export Formats**
- ✅ **12 Report Types** in 5 formats
- ✅ **3 Validation Categories**
- ✅ **5 Pre-built Scenarios**
- ✅ **TOGAF 10** complete
- ✅ **ArchiMate 3.2** full coverage
- ✅ **Saudi NORA** compliance
- ✅ **Import/Export** Archi & EA
- ✅ **Real-time Intelligence**
- ✅ **Autonomous Operations**

## 🚀 Get Started

```bash
# Clone repository
git clone <repo-url>
cd ArchiAgents/togaf_framework

# Install
pip install -e .

# Verify installation
archiagents --version

# See all commands
archiagents --help

# Initialize your first project
archiagents project init --name "My EA Project" --enterprise "MyCompany"
```

---

**Status:** ✅ 100% Complete & Production Ready

For full documentation: See `CLI_COMPLETE_REFERENCE.md`
