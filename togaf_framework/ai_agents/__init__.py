"""
TOGAF AI Multi-Agent System

This module provides intelligent automation and collaborative AI agents
for the TOGAF 9.0/10 Architecture Development Method framework.

Features:
- LangGraph workflow orchestration for ADM phases
- CrewAI specialized agent teams for architecture tasks
- Multi-provider LLM support (OpenAI, Anthropic, Google, Ollama, etc.)
- Autonomous decision-making and analysis
- Collaborative workflows across all TOGAF aspects
- Intelligent recommendations and insights

Architecture:
- Agent Orchestration: LangGraph state machines
- Agent Teams: CrewAI collaborative agents
- LLM Providers: Multiple cloud and local providers
- Knowledge Management: Vector stores and memory
- Integration: Seamless TOGAF framework integration
"""

from typing import Optional

__version__ = "2.0.0"

# Check for optional AI dependencies
try:
    import langgraph
    LANGGRAPH_AVAILABLE = True
except ImportError:
    LANGGRAPH_AVAILABLE = False

try:
    import crewai
    CREWAI_AVAILABLE = True
except ImportError:
    CREWAI_AVAILABLE = False

try:
    import langchain
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False

# Import core classes
from .agent_base import (
    TOGAFAgent,
    AgentTeam,
    AgentTask,
    AgentMemory,
    AgentRole,
    AgentCapability,
    TaskPriority,
    TaskStatus
)

from .llm_providers import (
    LLMProvider,
    LLMConfig,
    LLMProviderManager,
    LLMProviderFactory,
    get_recommended_models,
    get_provider_info
)

from .ai_orchestrator import AIAgentOrchestrator


def check_ai_dependencies() -> dict:
    """Check which AI frameworks are available"""
    # Get available LLM providers
    try:
        llm_providers = LLMProviderManager.get_available_providers()
    except:
        llm_providers = []
    
    return {
        "langgraph": LANGGRAPH_AVAILABLE,
        "crewai": CREWAI_AVAILABLE,
        "langchain": LANGCHAIN_AVAILABLE,
        "llm_providers": llm_providers,
        "ai_enabled": LANGGRAPH_AVAILABLE or CREWAI_AVAILABLE,
        "has_cloud_llm": any(p in llm_providers for p in ["openai", "anthropic", "google"]),
        "has_local_llm": "ollama" in llm_providers
    }


def get_ai_status() -> str:
    """Get human-readable AI system status"""
    deps = check_ai_dependencies()
    
    if not deps["ai_enabled"]:
        return """❌ AI agents disabled
Install: pip install langgraph langchain-openai crewai
For local LLMs: pip install langchain-community + Ollama"""
    
    status = "✅ AI agents enabled:\n"
    if deps["langgraph"]:
        status += "  • LangGraph: Available for workflow orchestration\n"
    if deps["crewai"]:
        status += "  • CrewAI: Available for agent teams\n"
    if deps["llm_providers"]:
        status += f"  • LLM Providers: {', '.join(deps['llm_providers'])}\n"
    if deps["has_local_llm"]:
        status += "  • Local LLMs: Ollama available\n"
    
    return status


__all__ = [
    # Core classes
    "TOGAFAgent",
    "AgentTeam",
    "AgentTask",
    "AgentMemory",
    "AgentRole",
    "AgentCapability",
    "TaskPriority",
    "TaskStatus",
    
    # LLM Providers
    "LLMProvider",
    "LLMConfig",
    "LLMProviderManager",
    "LLMProviderFactory",
    "get_recommended_models",
    "get_provider_info",
    
    # Orchestrator
    "AIAgentOrchestrator",
    
    # Utility functions
    "check_ai_dependencies",
    "get_ai_status",
    
    # Flags
    "LANGGRAPH_AVAILABLE",
    "CREWAI_AVAILABLE",
    "LANGCHAIN_AVAILABLE",
]
