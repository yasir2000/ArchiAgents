# CLI Testing Quick Start

## Choose Your Platform

### 🐍 Python (Cross-Platform) - **RECOMMENDED**

```bash
python test_cli_scenarios.py
```

**Pros**: 
- ✅ Works on any OS (Windows, Linux, Mac)
- ✅ Colored output with detailed logs
- ✅ Best error handling and timeouts
- ✅ Can run individual scenarios

**Example**:
```bash
# Run all scenarios
python test_cli_scenarios.py

# Run specific scenario
python test_cli_scenarios.py --scenario 1
```

---

### 🐧 Bash (Linux/Mac/Git Bash)

```bash
chmod +x test-cli-scenarios.sh
./test-cli-scenarios.sh
```

**Pros**:
- ✅ Native Unix/Linux experience
- ✅ Colored terminal output
- ✅ Progress indicators
- ✅ Can run on Git Bash (Windows)

**Example Output**:
```
========================================
Scenario 1: Digital Banking Transformation
========================================
[1/14] Initializing project...
✓ Project created: Digital Banking Modernization
[2/14] Configuring AI provider...
✓ AI configured: Ollama (llama3.1)
...
```

---

### 🪟 Windows Batch

```cmd
test-cli-scenarios.bat
```

**Pros**:
- ✅ Native Windows CMD/PowerShell
- ✅ ANSI colors (Windows 10+)
- ✅ Pause between scenarios
- ✅ No additional dependencies

**Example Output**:
```
========================================
Scenario 1: Digital Banking Transformation
========================================
Initializing project...
Configuring AI provider...
...
Press any key to continue to Scenario 2...
```

---

## What Gets Tested

### Scenario 1: Digital Banking ($15M)
```
14 Commands Testing:
├── Project initialization
├── AI configuration (Ollama FREE)
├── TOGAF Phase A (Vision)
├── Stakeholder value map (ArchiMate)
├── TOGAF Phase B (Business)
├── BPMN process model
├── TOGAF Phases C & D
├── AI health analysis
├── TOGAF Phases E & F
├── PDF report generation
├── TOGAF validation
└── Archi XML export
```

### Scenario 2: Cloud Migration ($8M)
```
6 Commands Testing:
├── Project initialization
├── Pre-built cloud scenario
├── AWS infrastructure model
├── AI risk analysis
├── Migration roadmap
└── Quality validation
```

### Scenario 3: Healthcare NORA ($20M)
```
6 Commands Testing:
├── Project with compliance
├── AI with Arabic support
├── Phase A with NORA
├── NORA strategic model
├── NORA compliance validation
└── Multi-standard report
```

### Scenario 4: Microservices ($10M)
```
5 Commands Testing:
├── Project initialization
├── AI decomposition analysis
├── Microservices model
├── API catalog (UML)
└── AI migration decision
```

### Scenario 5: Smart City IoT ($50M)
```
7 Commands Testing:
├── Project initialization
├── TOGAF Phases A-D
├── Physical IoT model
├── Data architecture
└── Architecture comparison
```

### Scenario 6: AI Agents
```
5 Commands Testing:
├── List AI models
├── List AI agent roles
├── Configure multiple providers
├── AI agent collaboration
└── Autonomous decisions
```

### Scenario 7: Interoperability
```
4 Commands Testing:
├── Import from Archi
├── Validate architecture
├── AI enhancement
└── Batch export (5 formats)
```

---

## Expected Runtime

| Scenario | Commands | Est. Time |
|----------|----------|-----------|
| 1. Digital Banking | 14 | 3-5 min |
| 2. Cloud Migration | 6 | 2-3 min |
| 3. Healthcare NORA | 6 | 2-3 min |
| 4. Microservices | 5 | 2-3 min |
| 5. Smart City IoT | 7 | 3-4 min |
| 6. AI Agents | 5 | 2-3 min |
| 7. Interoperability | 4 | 2-3 min |
| **TOTAL** | **47** | **15-25 min** |

*Actual time depends on AI provider response times*

---

## Generated Artifacts

After running all scenarios:

```
📁 projects/                    6 complete projects
📁 models/                      20+ diagrams (.mermaid)
📁 reports/                     PDF and JSON reports
📁 exports/                     Archi XML, GoJS JSON
📁 logs/                        AI agent logs
```

**Estimated disk space**: ~500 MB

---

## Prerequisites

### All Platforms
- ✅ Python 3.8+
- ✅ `togaf_framework` module installed

### Optional (for AI)
- 🆓 **FREE**: Ollama (local models, no API key)
- 💳 **Paid**: OpenAI API key (GPT-4)
- 💳 **Paid**: Anthropic API key (Claude)
- 💳 **Paid**: Google API key (Gemini)

### Setup AI Provider

**Option 1: FREE Local Models (Ollama)**
```bash
# Install Ollama: https://ollama.ai
ollama pull llama3.1

# Configure in ArchiAgents
archiagents ai configure --provider ollama --model llama3.1
```

**Option 2: Cloud Providers**
```bash
# Set API key
export OPENAI_API_KEY="your-key-here"

# Configure
archiagents ai configure --provider openai --model gpt-4
```

---

## Troubleshooting

### Module not found
```bash
export PYTHONPATH="${PWD}:${PWD}/togaf_framework:${PYTHONPATH}"
python -m togaf_framework.cli.main --help
```

### Permission denied (Bash)
```bash
chmod +x test-cli-scenarios.sh
```

### AI provider error
```bash
# Use FREE Ollama
archiagents ai configure --provider ollama --model llama3.1

# Verify configuration
archiagents ai list-models
```

---

## Next Steps

### 1. Run the tests
```bash
python test_cli_scenarios.py
```

### 2. Review generated artifacts
```bash
ls -la projects/
ls -la models/
ls -la reports/
```

### 3. Open diagrams
- Visit [Mermaid Live Editor](https://mermaid.live)
- Paste contents of `.mermaid` files
- Or import `.xml` files into [Archi tool](https://www.archimatetool.com/)

### 4. Read comprehensive reports
```bash
open reports/digital-banking-comprehensive.pdf
open reports/nora-compliance-report.pdf
```

---

## Documentation

- 📘 [Complete Scenarios Guide](./CLI_SCENARIOS_GUIDE.md) - Detailed business context
- 📋 [Execution Summary](./CLI_TEST_EXECUTION_SUMMARY.md) - Technical details
- 🎨 [Brand Guidelines](./BRAND_GUIDELINES.md) - Visual identity
- 🤖 [LLM Providers Guide](./LLM_PROVIDERS_GUIDE.md) - AI configuration

---

**Ready to test ArchiAgents CLI?**

```bash
python test_cli_scenarios.py
```

🚀 Let's go!
