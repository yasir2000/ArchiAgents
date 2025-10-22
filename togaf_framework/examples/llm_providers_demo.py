"""
Multi-Provider LLM Support Demonstration

Shows how to use different LLM providers with the AI Agent system:
- OpenAI (GPT-4, GPT-3.5-turbo)
- Anthropic Claude
- Google Gemini  
- Ollama (local models like Llama3, Mistral)
- Azure OpenAI
- Hugging Face

Demonstrates provider switching and configuration.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from togaf_framework.ai_agents import (
    AIAgentOrchestrator,
    LLMProviderManager,
    LLMProvider,
    get_recommended_models,
    get_provider_info,
    check_ai_dependencies
)


def print_section(title: str):
    """Print formatted section header"""
    print(f"\n{'=' * 80}")
    print(f"{title.upper()}")
    print(f"{'=' * 80}\n")


def main():
    """Demonstrate multi-provider LLM support"""
    
    print_section("TOGAF AI Multi-Agent System - Multi-Provider LLM Support")
    
    # Check available providers
    print_section("Available LLM Providers")
    
    available = LLMProviderManager.get_available_providers()
    if available:
        print("✅ Available providers:")
        for provider in available:
            print(f"   • {provider}")
    else:
        print("⚠️  No LLM providers installed")
        print("\nInstall providers:")
        print("  Cloud: pip install langchain-openai langchain-anthropic langchain-google-genai")
        print("  Local: pip install langchain-community")
        print("         Install Ollama from https://ollama.ai")
        print("         ollama pull llama3.1")
    
    # Show provider information
    print_section("Provider Information")
    
    AIAgentOrchestrator.print_provider_guide()
    
    # Example 1: OpenAI GPT-4 (default)
    print_section("Example 1: OpenAI GPT-4 (Default)")
    
    print("Creating orchestrator with GPT-4...")
    try:
        orchestrator = AIAgentOrchestrator(
            enterprise_name="TechCorp Global",
            project_name="Cloud Migration",
            architecture_scope="Enterprise cloud transformation",
            llm_provider="gpt-4"  # Default
        )
        
        llm_info = orchestrator.get_llm_info()
        print(f"\n✅ Configured:")
        print(f"   Model: {llm_info['model']}")
        print(f"   Provider: {llm_info['provider']}")
        print(f"   Ready: {llm_info['configured']}")
        
    except Exception as e:
        print(f"⚠️  Could not configure GPT-4: {e}")
        print("   Set OPENAI_API_KEY environment variable")
    
    # Example 2: GPT-3.5-turbo (faster/cheaper)
    print_section("Example 2: OpenAI GPT-3.5-turbo (Fast & Cost-Effective)")
    
    print("Creating orchestrator with GPT-3.5-turbo...")
    try:
        orchestrator_35 = AIAgentOrchestrator(
            enterprise_name="StartupCo",
            project_name="MVP Architecture",
            architecture_scope="Minimum viable product",
            llm_provider="gpt-3.5-turbo",
            llm_config={
                "temperature": 0.5,  # More focused
                "max_tokens": 2000
            }
        )
        
        print(f"✅ Using GPT-3.5-turbo for faster, cost-effective analysis")
        
    except Exception as e:
        print(f"⚠️  Could not configure: {e}")
    
    # Example 3: Anthropic Claude
    print_section("Example 3: Anthropic Claude 3 Opus (High Quality)")
    
    print("Creating orchestrator with Claude 3 Opus...")
    try:
        orchestrator_claude = AIAgentOrchestrator(
            enterprise_name="Enterprise Inc",
            project_name="Complex Architecture",
            architecture_scope="Multi-cloud enterprise architecture",
            llm_provider="claude-3-opus-20240229"
        )
        
        print(f"✅ Using Claude 3 Opus for detailed analysis")
        print("   Set ANTHROPIC_API_KEY environment variable")
        
    except Exception as e:
        print(f"⚠️  Could not configure: {e}")
    
    # Example 4: Google Gemini
    print_section("Example 4: Google Gemini Pro")
    
    print("Creating orchestrator with Gemini Pro...")
    try:
        orchestrator_gemini = AIAgentOrchestrator(
            enterprise_name="Innovation Labs",
            project_name="AI-First Architecture",
            architecture_scope="AI-powered applications",
            llm_provider="gemini-pro"
        )
        
        print(f"✅ Using Gemini Pro")
        print("   Set GOOGLE_API_KEY environment variable")
        
    except Exception as e:
        print(f"⚠️  Could not configure: {e}")
    
    # Example 5: Ollama (Local Models)
    print_section("Example 5: Ollama - Local LLM (Privacy & Cost-Free)")
    
    print("🏠 Using LOCAL LLM - No API keys needed!")
    print("\nAvailable local models:")
    local_models = [
        "llama3.1 (Meta's Llama 3.1 - 8B, 70B)",
        "mistral (Mistral 7B - Fast and capable)",
        "mixtral (Mixtral 8x7B - Very powerful)",
        "phi-2 (Microsoft Phi-2 - Small and fast)",
        "gemma (Google Gemma - Lightweight)",
        "codellama (Code-specialized)",
        "deepseek-coder (Advanced coding)"
    ]
    for model in local_models:
        print(f"   • {model}")
    
    print("\nSetup:")
    print("   1. Install Ollama: https://ollama.ai")
    print("   2. Pull model: ollama pull llama3.1")
    print("   3. Use with TOGAF: llm_provider='llama3.1'")
    
    try:
        print("\nCreating orchestrator with local Llama 3.1...")
        orchestrator_local = AIAgentOrchestrator(
            enterprise_name="DataSensitive Corp",
            project_name="Private Architecture",
            architecture_scope="On-premises secure architecture",
            llm_provider="llama3.1",  # Local model via Ollama
            llm_config={
                "temperature": 0.7,
                "base_url": "http://localhost:11434"  # Default Ollama URL
            }
        )
        
        llm_info = orchestrator_local.get_llm_info()
        print(f"\n✅ Using LOCAL LLM:")
        print(f"   Model: {llm_info['model']}")
        print(f"   Provider: {llm_info['provider']}")
        print(f"   Privacy: 100% - runs on your machine")
        print(f"   Cost: $0 - completely free")
        print(f"   Internet: Not required (after download)")
        
    except Exception as e:
        print(f"\n⚠️  Ollama not available: {e}")
        print("   Install from: https://ollama.ai")
        print("   Then run: ollama pull llama3.1")
    
    # Example 6: Azure OpenAI
    print_section("Example 6: Azure OpenAI (Enterprise)")
    
    print("Creating orchestrator with Azure OpenAI...")
    try:
        orchestrator_azure = AIAgentOrchestrator(
            enterprise_name="Enterprise Global",
            project_name="Corporate Architecture",
            architecture_scope="Global enterprise transformation",
            llm_provider="azure/gpt-4",  # Azure prefix
            llm_config={
                "api_base": "https://your-resource.openai.azure.com/",
                "api_version": "2024-02-15-preview"
            }
        )
        
        print(f"✅ Using Azure OpenAI (enterprise-grade)")
        print("   Set AZURE_OPENAI_API_KEY environment variable")
        print("   Set AZURE_OPENAI_ENDPOINT environment variable")
        
    except Exception as e:
        print(f"⚠️  Could not configure: {e}")
    
    # Example 7: Switching Providers Dynamically
    print_section("Example 7: Dynamic Provider Switching")
    
    print("Switching between providers at runtime...")
    
    try:
        # Create with one provider
        orch = AIAgentOrchestrator(
            enterprise_name="FlexibleCorp",
            project_name="Adaptive Architecture",
            architecture_scope="Multi-scenario analysis",
            llm_provider="gpt-3.5-turbo"
        )
        
        print(f"Initial: {orch.get_llm_info()['model']}")
        
        # Switch to local model for cost savings
        if "ollama" in LLMProviderManager.get_available_providers():
            print("\nSwitching to local Llama 3.1 for cost-free analysis...")
            success = orch.switch_llm_provider("llama3.1")
            if success:
                print(f"Current: {orch.get_llm_info()['model']}")
        
        # Switch to Claude for complex analysis
        print("\nSwitching to Claude 3 for detailed review...")
        success = orch.switch_llm_provider("claude-3-sonnet-20240229")
        print(f"Current: {orch.get_llm_info()['model']}")
        
    except Exception as e:
        print(f"⚠️  Switching demo skipped: {e}")
    
    # Use case recommendations
    print_section("Recommended Models by Use Case")
    
    recommendations = get_recommended_models()
    
    print("🎯 High Quality (complex architecture):")
    for model in recommendations["high_quality"]:
        print(f"   • {model}")
    
    print("\n⚡ Fast & Cost-Effective (rapid prototyping):")
    for model in recommendations["cost_effective"]:
        print(f"   • {model}")
    
    print("\n🏠 Local & Private (sensitive data):")
    for model in recommendations["local"]:
        print(f"   • {model}")
    
    print("\n💻 Coding & Technical (technical architecture):")
    for model in recommendations["coding"]:
        print(f"   • {model}")
    
    # Comparison table
    print_section("Provider Comparison")
    
    print(f"{'Provider':<20} {'Privacy':<12} {'Cost':<15} {'Quality':<10} {'Speed':<10}")
    print("-" * 80)
    print(f"{'OpenAI GPT-4':<20} {'Cloud':<12} {'$$$$':<15} {'Highest':<10} {'Medium':<10}")
    print(f"{'GPT-3.5-turbo':<20} {'Cloud':<12} {'$':<15} {'Good':<10} {'Fast':<10}")
    print(f"{'Claude 3 Opus':<20} {'Cloud':<12} {'$$$$':<15} {'Highest':<10} {'Medium':<10}")
    print(f"{'Claude 3 Haiku':<20} {'Cloud':<12} {'$':<15} {'Good':<10} {'Fastest':<10}")
    print(f"{'Gemini Pro':<20} {'Cloud':<12} {'$$':<15} {'High':<10} {'Fast':<10}")
    print(f"{'Llama 3.1 (local)':<20} {'100% Local':<12} {'FREE':<15} {'High':<10} {'Fast':<10}")
    print(f"{'Mistral (local)':<20} {'100% Local':<12} {'FREE':<15} {'Good':<10} {'Very Fast':<10}")
    print(f"{'Phi-2 (local)':<20} {'100% Local':<12} {'FREE':<15} {'Good':<10} {'Ultra Fast':<10}")
    
    # Summary
    print_section("Summary")
    
    print("✅ Multi-Provider Support Enabled!")
    print("\n📦 Install providers as needed:")
    print("   Cloud:")
    print("     pip install langchain-openai        # OpenAI + Azure")
    print("     pip install langchain-anthropic     # Claude")
    print("     pip install langchain-google-genai  # Gemini")
    print("\n   Local (Free & Private):")
    print("     pip install langchain-community")
    print("     Install Ollama from https://ollama.ai")
    print("     ollama pull llama3.1")
    print("     ollama pull mistral")
    
    print("\n💡 Usage:")
    print("   # Cloud LLM")
    print("   orchestrator = AIAgentOrchestrator(..., llm_provider='gpt-4')")
    print("\n   # Local LLM (FREE)")
    print("   orchestrator = AIAgentOrchestrator(..., llm_provider='llama3.1')")
    print("\n   # Switch dynamically")
    print("   orchestrator.switch_llm_provider('mistral')")
    
    print("\n🎯 Choose based on your needs:")
    print("   • Best Quality: GPT-4, Claude 3 Opus")
    print("   • Best Value: GPT-3.5-turbo, Claude 3 Haiku")
    print("   • Best Privacy: Llama 3.1, Mistral (local)")
    print("   • Best Speed: Mistral, Phi-2 (local)")
    print("   • Best Free: Any Ollama model (local)")
    
    print("\n" + "=" * 80)
    print("MULTI-PROVIDER LLM SYSTEM - READY")
    print("=" * 80)


if __name__ == "__main__":
    main()
