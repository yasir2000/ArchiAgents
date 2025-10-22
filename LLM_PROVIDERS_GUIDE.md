# LLM Providers Guide - TOGAF AI Multi-Agent System

## Overview

The TOGAF AI Multi-Agent System supports multiple LLM providers, including both cloud-based and **local models via Ollama**. This gives you flexibility to choose based on quality, cost, privacy, and performance needs.

## Supported Providers

### Cloud Providers
- **OpenAI** - GPT-4, GPT-3.5-turbo
- **Azure OpenAI** - Enterprise GPT models
- **Anthropic** - Claude 3 (Opus, Sonnet, Haiku)
- **Google** - Gemini (Pro, 1.5 Pro, Ultra)
- **Hugging Face** - Any model via API

### Local Provider (Privacy & Cost-Free)
- **Ollama** - Run LLMs locally on your machine
  - Llama 3.1 (Meta)
  - Mistral (Mistral AI)
  - Mixtral (Mistral AI)
  - Phi-2 (Microsoft)
  - Gemma (Google)
  - CodeLlama (Meta)
  - DeepSeek Coder
  - And many more...

---

## Quick Start

### Cloud LLM (OpenAI GPT-4)

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# 1. Set environment variable
# export OPENAI_API_KEY=sk-...

# 2. Create orchestrator
orchestrator = AIAgentOrchestrator(
    enterprise_name="TechCorp Global",
    project_name="Cloud Migration",
    architecture_scope="Enterprise transformation",
    llm_provider="gpt-4"  # or "gpt-3.5-turbo"
)

# 3. Use as normal
orchestrator.run_phase_a()
```

### Local LLM (Ollama - FREE & PRIVATE)

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# 1. Install Ollama (one-time)
# Download from: https://ollama.ai
# ollama pull llama3.1

# 2. Create orchestrator (NO API KEY NEEDED!)
orchestrator = AIAgentOrchestrator(
    enterprise_name="PrivateCorp",
    project_name="Secure Architecture",
    architecture_scope="On-premises architecture",
    llm_provider="llama3.1"  # Runs locally!
)

# 3. Use as normal - completely private!
orchestrator.run_phase_a()
```

---

## Provider Setup Instructions

### 1. OpenAI (GPT-4, GPT-3.5-turbo)

**Installation:**
```bash
pip install langchain-openai
```

**Configuration:**
```bash
export OPENAI_API_KEY=sk-your-api-key-here
```

**Usage:**
```python
# GPT-4 (highest quality)
orchestrator = AIAgentOrchestrator(..., llm_provider="gpt-4")

# GPT-3.5-turbo (faster, cheaper)
orchestrator = AIAgentOrchestrator(..., llm_provider="gpt-3.5-turbo")
```

**Cost:** Pay-per-use ($0.03/1K tokens for GPT-4)

---

### 2. Anthropic Claude

**Installation:**
```bash
pip install langchain-anthropic
```

**Configuration:**
```bash
export ANTHROPIC_API_KEY=sk-ant-your-api-key-here
```

**Usage:**
```python
# Claude 3 Opus (highest quality)
orchestrator = AIAgentOrchestrator(..., 
    llm_provider="claude-3-opus-20240229")

# Claude 3 Sonnet (balanced)
orchestrator = AIAgentOrchestrator(..., 
    llm_provider="claude-3-sonnet-20240229")

# Claude 3 Haiku (fastest)
orchestrator = AIAgentOrchestrator(..., 
    llm_provider="claude-3-haiku-20240307")
```

**Cost:** Pay-per-use ($15/1M tokens for Opus)

---

### 3. Google Gemini

**Installation:**
```bash
pip install langchain-google-genai
```

**Configuration:**
```bash
export GOOGLE_API_KEY=your-api-key-here
```

**Usage:**
```python
# Gemini Pro
orchestrator = AIAgentOrchestrator(..., llm_provider="gemini-pro")

# Gemini 1.5 Pro (longer context)
orchestrator = AIAgentOrchestrator(..., llm_provider="gemini-1.5-pro")
```

**Cost:** Pay-per-use ($0.50/1M tokens for Pro)

---

### 4. Azure OpenAI (Enterprise)

**Installation:**
```bash
pip install langchain-openai
```

**Configuration:**
```bash
export AZURE_OPENAI_API_KEY=your-api-key-here
export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
```

**Usage:**
```python
orchestrator = AIAgentOrchestrator(..., 
    llm_provider="azure/gpt-4",
    llm_config={
        "api_base": "https://your-resource.openai.azure.com/",
        "api_version": "2024-02-15-preview"
    }
)
```

**Cost:** Enterprise pricing

---

### 5. Ollama (Local - FREE & PRIVATE) ⭐

**Installation:**
```bash
# 1. Install Ollama
# Download from: https://ollama.ai
# Windows: Download installer
# Mac: brew install ollama
# Linux: curl -fsSL https://ollama.ai/install.sh | sh

# 2. Install Python package
pip install langchain-community

# 3. Pull models (one-time per model)
ollama pull llama3.1        # Meta Llama 3.1 (8B)
ollama pull mistral         # Mistral 7B
ollama pull mixtral         # Mixtral 8x7B
ollama pull phi-2           # Microsoft Phi-2
ollama pull gemma           # Google Gemma
ollama pull codellama       # Code-specialized
ollama pull deepseek-coder  # Advanced coding
```

**Configuration:**
NO API KEY NEEDED! Runs 100% locally.

**Usage:**
```python
# Using Llama 3.1
orchestrator = AIAgentOrchestrator(..., llm_provider="llama3.1")

# Using Mistral (faster)
orchestrator = AIAgentOrchestrator(..., llm_provider="mistral")

# Using Mixtral (most powerful local model)
orchestrator = AIAgentOrchestrator(..., llm_provider="mixtral")

# Custom Ollama server
orchestrator = AIAgentOrchestrator(..., 
    llm_provider="llama3.1",
    llm_config={"base_url": "http://custom-server:11434"}
)
```

**Available Models:**
- `llama3.1` - Meta's Llama 3.1 (excellent balance)
- `mistral` - Mistral 7B (very fast)
- `mixtral` - Mixtral 8x7B (highest quality local)
- `phi-2` - Microsoft Phi-2 (ultra fast, small)
- `gemma` - Google Gemma (efficient)
- `codellama` - Code generation
- `deepseek-coder` - Advanced coding
- `qwen` - Alibaba Qwen

**Cost:** 100% FREE! No API costs, no usage limits.

**Privacy:** 100% LOCAL! Data never leaves your machine.

**Requirements:**
- 8GB+ RAM (16GB recommended for larger models)
- 10-20GB disk space per model
- No internet required (after initial download)

---

### 6. Hugging Face

**Installation:**
```bash
pip install langchain-huggingface
```

**Configuration:**
```bash
export HUGGINGFACEHUB_API_TOKEN=hf_your-token-here
```

**Usage:**
```python
orchestrator = AIAgentOrchestrator(..., 
    llm_provider="mistralai/Mistral-7B-v0.1")
```

---

## Provider Comparison

| Provider | Privacy | Cost | Quality | Speed | Context |
|----------|---------|------|---------|-------|---------|
| **OpenAI GPT-4** | Cloud | $$$$ | Highest | Medium | 128K |
| **GPT-3.5-turbo** | Cloud | $ | Good | Fast | 16K |
| **Claude 3 Opus** | Cloud | $$$$ | Highest | Medium | 200K |
| **Claude 3 Sonnet** | Cloud | $$ | High | Fast | 200K |
| **Claude 3 Haiku** | Cloud | $ | Good | Fastest | 200K |
| **Gemini Pro** | Cloud | $$ | High | Fast | 32K |
| **Gemini 1.5 Pro** | Cloud | $$$ | Highest | Medium | 1M |
| **Llama 3.1 (Ollama)** | 100% Local | FREE | High | Fast | 128K |
| **Mistral (Ollama)** | 100% Local | FREE | Good | Very Fast | 32K |
| **Mixtral (Ollama)** | 100% Local | FREE | Highest | Medium | 32K |
| **Phi-2 (Ollama)** | 100% Local | FREE | Good | Ultra Fast | 2K |

---

## Use Case Recommendations

### 🎯 High Quality (Complex Architecture)
**Best for:** Critical decisions, complex reasoning, detailed analysis

**Recommended:**
- GPT-4
- Claude 3 Opus
- Gemini 1.5 Pro
- Mixtral (local)

```python
orchestrator = AIAgentOrchestrator(..., llm_provider="gpt-4")
```

---

### ⚡ Fast & Cost-Effective (Rapid Prototyping)
**Best for:** Quick iterations, development, testing

**Recommended:**
- GPT-3.5-turbo ($)
- Claude 3 Haiku ($)
- Llama 3.1 (FREE, local)
- Mistral (FREE, local)
- Phi-2 (FREE, local)

```python
orchestrator = AIAgentOrchestrator(..., llm_provider="llama3.1")
```

---

### 🏠 Privacy & Security (Sensitive Data)
**Best for:** Confidential architecture, compliance requirements, air-gapped environments

**Recommended (100% Local):**
- Llama 3.1 via Ollama
- Mistral via Ollama
- Mixtral via Ollama

```python
orchestrator = AIAgentOrchestrator(..., llm_provider="llama3.1")
# Data NEVER leaves your machine!
```

---

### 💻 Coding & Technical (Technical Architecture)
**Best for:** Application architecture, API design, code generation

**Recommended:**
- GPT-4
- Claude 3 Opus
- CodeLlama (FREE, local)
- DeepSeek Coder (FREE, local)

```python
orchestrator = AIAgentOrchestrator(..., llm_provider="codellama")
```

---

### 💰 Zero Budget (Students, Startups)
**Best for:** Learning, experimentation, proof-of-concept

**Recommended (100% FREE):**
- Llama 3.1 via Ollama
- Mistral via Ollama
- Phi-2 via Ollama

```python
orchestrator = AIAgentOrchestrator(..., llm_provider="mistral")
# Completely free, no API keys, no limits!
```

---

## Dynamic Provider Switching

Switch between providers at runtime:

```python
# Start with fast model for initial analysis
orchestrator = AIAgentOrchestrator(..., llm_provider="mistral")
orchestrator.run_phase_a()

# Switch to high-quality for detailed review
orchestrator.switch_llm_provider("gpt-4")
orchestrator.run_phase_b()

# Switch to local model for private data
orchestrator.switch_llm_provider("llama3.1")
orchestrator.run_phase_c()
```

---

## Advanced Configuration

### Custom Temperature & Tokens

```python
orchestrator = AIAgentOrchestrator(...,
    llm_provider="gpt-4",
    llm_config={
        "temperature": 0.3,      # More focused (0-1)
        "max_tokens": 4000,      # Response length
        "timeout": 60,           # Request timeout
        "retry_attempts": 3      # Retry on failure
    }
)
```

### Streaming Responses

```python
orchestrator = AIAgentOrchestrator(...,
    llm_provider="gpt-4",
    llm_config={"streaming": True}
)
```

### Custom Ollama Server

```python
# Connect to remote Ollama instance
orchestrator = AIAgentOrchestrator(...,
    llm_provider="llama3.1",
    llm_config={
        "base_url": "http://192.168.1.100:11434"
    }
)
```

---

## Checking Available Providers

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# List installed providers
providers = AIAgentOrchestrator.list_available_providers()
print(f"Available: {providers}")

# Get recommended models
models = AIAgentOrchestrator.get_recommended_models_by_use_case()
print(f"Local models: {models['local']}")
print(f"Coding models: {models['coding']}")

# Print full guide
AIAgentOrchestrator.print_provider_guide()
```

---

## Troubleshooting

### Issue: "Provider not available"

**Solution:**
```bash
# Check which providers are installed
python -c "from togaf_framework.ai_agents import LLMProviderManager; print(LLMProviderManager.get_available_providers())"

# Install missing provider
pip install langchain-openai      # OpenAI
pip install langchain-anthropic   # Claude
pip install langchain-google-genai # Gemini
pip install langchain-community   # Ollama
```

### Issue: "Ollama connection failed"

**Solution:**
```bash
# Check if Ollama is running
ollama list

# Start Ollama (if not running)
ollama serve

# Verify model is downloaded
ollama pull llama3.1

# Test connection
curl http://localhost:11434/api/generate -d '{"model": "llama3.1", "prompt": "Hello"}'
```

### Issue: "API key not found"

**Solution:**
```bash
# Set environment variable
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
export GOOGLE_API_KEY=...

# Or pass in config
orchestrator = AIAgentOrchestrator(...,
    llm_provider="gpt-4",
    llm_config={"api_key": "sk-..."}
)
```

---

## Best Practices

### 1. **Start Local, Scale to Cloud**
- Develop with Ollama (free, fast iteration)
- Deploy with GPT-4 (production quality)

### 2. **Match Provider to Use Case**
- Complex analysis → GPT-4, Claude Opus
- Rapid prototyping → Mistral, GPT-3.5
- Sensitive data → Ollama (local)
- Coding tasks → CodeLlama, DeepSeek

### 3. **Use Provider Switching**
- Different phases may need different models
- Switch based on task complexity
- Balance cost vs. quality

### 4. **Monitor Costs**
- Track cloud API usage
- Use local models for development
- Reserve GPT-4 for critical decisions

### 5. **Privacy Considerations**
- Use Ollama for confidential architectures
- Never send sensitive data to cloud LLMs
- Local models for air-gapped environments

---

## Example Workflow

```python
from togaf_framework.ai_agents import AIAgentOrchestrator

# 1. Initial analysis with free local model
orchestrator = AIAgentOrchestrator(
    enterprise_name="TechCorp",
    project_name="Cloud Migration",
    architecture_scope="Enterprise transformation",
    llm_provider="llama3.1"  # FREE, local
)

# Phase A: Vision (local is fine)
vision = orchestrator.run_phase_a()

# Phase B: Business (switch to high-quality)
orchestrator.switch_llm_provider("gpt-4")
business = orchestrator.run_phase_b()

# Phase C: Systems (use coding model)
orchestrator.switch_llm_provider("codellama")
systems = orchestrator.run_phase_c()

# Final review (best quality)
orchestrator.switch_llm_provider("claude-3-opus-20240229")
review = orchestrator.run_phase_h()
```

---

## Resources

### Provider Documentation
- **OpenAI:** https://platform.openai.com/docs
- **Anthropic:** https://docs.anthropic.com/claude/docs
- **Google:** https://ai.google.dev/docs
- **Ollama:** https://ollama.ai
- **Hugging Face:** https://huggingface.co/docs

### Ollama Resources
- **Installation:** https://ollama.ai
- **Model Library:** https://ollama.ai/library
- **GitHub:** https://github.com/ollama/ollama
- **Discord:** https://discord.gg/ollama

### LangChain Integration
- **OpenAI:** https://python.langchain.com/docs/integrations/llms/openai
- **Anthropic:** https://python.langchain.com/docs/integrations/llms/anthropic
- **Ollama:** https://python.langchain.com/docs/integrations/llms/ollama

---

## Summary

✅ **6 LLM Providers Supported**
- Cloud: OpenAI, Azure, Anthropic, Google, Hugging Face
- Local: Ollama (FREE & PRIVATE)

✅ **20+ Models Available**
- High-quality: GPT-4, Claude Opus, Gemini Pro
- Cost-effective: GPT-3.5, Mistral, Phi-2
- Coding: CodeLlama, DeepSeek Coder

✅ **Flexible Configuration**
- Auto-detection from model name
- Runtime provider switching
- Custom parameters per provider

✅ **Zero-Cost Option**
- Ollama provides FREE local LLMs
- No API keys, no usage limits
- 100% privacy - data never leaves your machine

**Get Started:**
```bash
# Cloud (OpenAI)
export OPENAI_API_KEY=sk-...
python -c "from togaf_framework.ai_agents import AIAgentOrchestrator; AIAgentOrchestrator(..., llm_provider='gpt-4')"

# Local (Ollama - FREE!)
ollama pull llama3.1
python -c "from togaf_framework.ai_agents import AIAgentOrchestrator; AIAgentOrchestrator(..., llm_provider='llama3.1')"
```

---

**Choose the right provider for your needs and start building intelligent enterprise architectures!** 🚀
