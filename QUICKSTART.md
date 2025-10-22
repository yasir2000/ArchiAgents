# Quick Start Guide - AI Multi-Agent System

## 🚀 Get Started in 5 Minutes

The TOGAF AI Multi-Agent System supports **multiple LLM providers** including both cloud-based (OpenAI, Claude, Gemini) and **FREE local models via Ollama**.

---

## Prerequisites

```bash
# Python 3.8 or higher
python --version

# Clone repository
git clone <repository-url>
cd ArchiAgents

# Install TOGAF framework
pip install -e .
```

---

## Option 1: Cloud LLM (High Quality) ☁️

Perfect for production use with highest quality results.

### Setup

```bash
# Install OpenAI provider
pip install langchain-openai

# Set API key
export OPENAI_API_KEY=sk-your-api-key-here

# Run demo
python togaf_framework/examples/llm_providers_demo.py
```

### Usage

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# Create orchestrator with GPT-4
orchestrator = AIAgentOrchestrator(
    enterprise_name="TechCorp Global",
    project_name="Cloud Migration",
    architecture_scope="Enterprise cloud transformation",
    llm_provider="gpt-4"  # Highest quality
)

# Run TOGAF Phase A - Architecture Vision
vision = orchestrator.run_phase_a()
print(vision)

# Run TOGAF Phase B - Business Architecture  
business = orchestrator.run_phase_b()
print(business)
```

**Cost:** Pay-per-use ($0.03/1K tokens for GPT-4)  
**Quality:** Highest available  
**Privacy:** Cloud-based

---

## Option 2: Local LLM (FREE & PRIVATE) 🏠 ⭐ **RECOMMENDED FOR LEARNING**

Perfect for development, learning, and sensitive data. **Completely FREE with NO API costs!**

### Setup

```bash
# 1. Install Ollama
# Download from: https://ollama.ai
# Windows: Download installer and run
# Mac: brew install ollama
# Linux: curl -fsSL https://ollama.ai/install.sh | sh

# 2. Pull model (one-time, ~4GB download)
ollama pull llama3.1

# 3. Install Python provider
pip install langchain-community

# 4. Run demo (NO API KEY NEEDED!)
python togaf_framework/examples/llm_providers_demo.py
```

### Usage

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# Create orchestrator with local Llama 3.1
orchestrator = AIAgentOrchestrator(
    enterprise_name="StartupCo",
    project_name="MVP Architecture",
    architecture_scope="Minimum viable product",
    llm_provider="llama3.1"  # FREE, runs locally!
)

# Run TOGAF Phase A - Architecture Vision
vision = orchestrator.run_phase_a()
print(vision)

# Run TOGAF Phase B - Business Architecture
business = orchestrator.run_phase_b()
print(business)
```

**Cost:** 🎉 **100% FREE** - No API costs, no usage limits!  
**Quality:** High (comparable to GPT-3.5)  
**Privacy:** 🔒 **100% LOCAL** - Data never leaves your machine!  
**Internet:** Not required after model download

### Available Local Models

```bash
# Fast and capable (recommended)
ollama pull llama3.1     # Meta Llama 3.1 (8B)
ollama pull mistral      # Mistral 7B

# Most powerful local model
ollama pull mixtral      # Mixtral 8x7B

# Ultra-fast and small
ollama pull phi-2        # Microsoft Phi-2

# Code-specialized
ollama pull codellama    # Code generation
ollama pull deepseek-coder # Advanced coding
```

---

## Option 3: Dynamic Provider Switching 🔄

Use different models for different tasks - start cheap/local, upgrade for complex analysis.

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# Start with FREE local model for initial analysis
orchestrator = AIAgentOrchestrator(
    enterprise_name="FlexibleCorp",
    project_name="Adaptive Architecture",
    architecture_scope="Multi-scenario analysis",
    llm_provider="mistral"  # FREE, fast
)

print("Phase A: Using free local model")
orchestrator.run_phase_a()

# Switch to high-quality GPT-4 for complex business analysis
print("\nPhase B: Switching to GPT-4 for detailed analysis")
orchestrator.switch_llm_provider("gpt-4")
orchestrator.run_phase_b()

# Switch back to local for cost savings
print("\nPhase C: Back to local model")
orchestrator.switch_llm_provider("llama3.1")
orchestrator.run_phase_c()
```

**Benefits:**
- 💰 Save money: Use free local models when possible
- 🎯 High quality: Upgrade to GPT-4 for critical decisions
- 🔒 Privacy: Keep sensitive data on local models
- ⚡ Speed: Use faster models for simple tasks

---

## Other Cloud Providers

### Anthropic Claude (High Quality)

```bash
pip install langchain-anthropic
export ANTHROPIC_API_KEY=sk-ant-your-key
```

```python
orchestrator = AIAgentOrchestrator(...,
    llm_provider="claude-3-opus-20240229"  # Highest quality
)
```

### Google Gemini

```bash
pip install langchain-google-genai
export GOOGLE_API_KEY=your-key
```

```python
orchestrator = AIAgentOrchestrator(...,
    llm_provider="gemini-pro"
)
```

### Azure OpenAI (Enterprise)

```bash
pip install langchain-openai
export AZURE_OPENAI_API_KEY=your-key
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
```

```python
orchestrator = AIAgentOrchestrator(...,
    llm_provider="azure/gpt-4",
    llm_config={
        "api_base": "https://your-resource.openai.azure.com/",
        "api_version": "2024-02-15-preview"
    }
)
```

---

## Checking Your Setup

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# List available providers
providers = AIAgentOrchestrator.list_available_providers()
print(f"Available providers: {providers}")

# Get recommended models by use case
models = AIAgentOrchestrator.get_recommended_models_by_use_case()
print(f"\nLocal models (FREE): {models['local']}")
print(f"Coding models: {models['coding']}")
print(f"Cost-effective: {models['cost_effective']}")

# Print comprehensive provider guide
AIAgentOrchestrator.print_provider_guide()
```

---

## Complete Example Workflow

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# Create orchestrator (using FREE local model)
orchestrator = AIAgentOrchestrator(
    enterprise_name="InnovateCorp",
    project_name="Digital Transformation",
    architecture_scope="Complete enterprise modernization",
    llm_provider="llama3.1"  # FREE!
)

# Run complete TOGAF ADM cycle
print("Phase A: Architecture Vision")
vision = orchestrator.run_phase_a()

print("\nPhase B: Business Architecture")
business = orchestrator.run_phase_b()

# Upgrade to GPT-4 for detailed technical analysis
orchestrator.switch_llm_provider("gpt-4")

print("\nPhase C: Information Systems Architecture")
systems = orchestrator.run_phase_c()

print("\nPhase D: Technology Architecture")
technology = orchestrator.run_phase_d()

# Back to local for standard planning
orchestrator.switch_llm_provider("llama3.1")

print("\nPhase E: Opportunities & Solutions")
solutions = orchestrator.run_phase_e()

print("\nPhase F: Migration Planning")
migration = orchestrator.run_phase_f()

print("\nPhase G: Implementation Governance")
governance = orchestrator.run_phase_g()

print("\nPhase H: Architecture Change Management")
change = orchestrator.run_phase_h()

# Get LLM configuration
llm_info = orchestrator.get_llm_info()
print(f"\nUsed LLM: {llm_info}")
```

---

## Troubleshooting

### "Ollama connection failed"

```bash
# Check Ollama is running
ollama list

# Start Ollama service
ollama serve

# Test connection
curl http://localhost:11434/api/generate -d '{"model": "llama3.1", "prompt": "test"}'
```

### "API key not found"

```bash
# Check environment variable
echo $OPENAI_API_KEY

# Set temporarily
export OPENAI_API_KEY=sk-your-key

# Or pass in config
orchestrator = AIAgentOrchestrator(...,
    llm_config={"api_key": "sk-your-key"}
)
```

### "Provider not available"

```bash
# Check installed providers
python -c "from togaf_framework.ai_agents import LLMProviderManager; print(LLMProviderManager.get_available_providers())"

# Install missing provider
pip install langchain-openai      # OpenAI
pip install langchain-anthropic   # Claude
pip install langchain-google-genai # Gemini
pip install langchain-community   # Ollama
```

---

## Next Steps

1. **Run Examples:**
   ```bash
   python togaf_framework/examples/llm_providers_demo.py
   python togaf_framework/examples/ai_agent_demo.py
   ```

2. **Read Documentation:**
   - [LLM Providers Guide](LLM_PROVIDERS_GUIDE.md) - Complete provider documentation
   - [AI Multi-Agent System](togaf_framework/AI_MULTIAGENT_SYSTEM.md) - AI system details
   - [Implementation Status](togaf_framework/COMPLETE_IMPLEMENTATION_STATUS.md) - Current status

3. **Explore Features:**
   - Try different LLM providers
   - Test provider switching
   - Run complete TOGAF ADM cycles
   - Experiment with local models

---

## Comparison: Cloud vs Local

| Feature | Cloud (OpenAI GPT-4) | Local (Ollama Llama 3.1) |
|---------|---------------------|-------------------------|
| **Cost** | $$$ pay-per-use | 🎉 **FREE** |
| **Privacy** | Cloud-based | 🔒 **100% LOCAL** |
| **Quality** | Highest | High (GPT-3.5 level) |
| **Speed** | Fast | Very fast (on GPU) |
| **Setup** | API key only | Install Ollama |
| **Internet** | Required | Not required (after download) |
| **Best For** | Production, critical decisions | Development, learning, sensitive data |

---

## Recommended Workflow

### Development Phase
- **Use:** Ollama (llama3.1, mistral)
- **Why:** FREE, fast iteration, no API costs
- **Perfect for:** Prototyping, testing, development

### Testing Phase
- **Use:** GPT-3.5-turbo or Claude Haiku
- **Why:** Affordable, good quality
- **Perfect for:** Integration testing, validation

### Production Phase
- **Use:** GPT-4, Claude Opus, or Gemini Pro
- **Why:** Highest quality for critical decisions
- **Perfect for:** Production architecture, client deliverables

### Sensitive Data
- **Use:** Ollama (any model)
- **Why:** 100% local, data never leaves your machine
- **Perfect for:** Confidential architectures, compliance requirements

---

**🎉 You're ready to build intelligent enterprise architectures with AI!**

Choose your provider and start architecting! 🚀
