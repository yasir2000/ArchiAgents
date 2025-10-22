"""
TOGAF AI Multi-Agent System

This module provides intelligent automation and collaborative AI agents
for the TOGAF 9.0/10 Architecture Development Method framework.

Features:
- LangGraph workflow orchestration for ADM phases
- CrewAI specialized agent teams for architecture tasks
- Autonomous decision-making and analysis
- Collaborative workflows across all TOGAF aspects
- Intelligent recommendations and insights

Architecture:
- Agent Orchestration: LangGraph state machines
- Agent Teams: CrewAI collaborative agents
- Knowledge Management: Vector stores and memory
- Integration: Seamless TOGAF framework integration
"""

from typing import Optional

__version__ = "1.0.0"
__all__ = [
    "TOGAFAgentOrchestrator",
    "ArchitectureAgentTeam",
    "PhaseWorkflowGraph",
    "AgentKnowledgeBase",
]

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
    from langchain_openai import ChatOpenAI
    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False


def check_ai_dependencies() -> dict:
    """Check which AI frameworks are available"""
    return {
        "langgraph": LANGGRAPH_AVAILABLE,
        "crewai": CREWAI_AVAILABLE,
        "langchain": LANGCHAIN_AVAILABLE,
        "ai_enabled": LANGGRAPH_AVAILABLE or CREWAI_AVAILABLE
    }


def get_ai_status() -> str:
    """Get human-readable AI system status"""
    deps = check_ai_dependencies()
    
    if not deps["ai_enabled"]:
        return "❌ AI agents disabled - Install langgraph and crewai"
    
    status = "✅ AI agents enabled:\n"
    if deps["langgraph"]:
        status += "  • LangGraph: Available for workflow orchestration\n"
    if deps["crewai"]:
        status += "  • CrewAI: Available for agent teams\n"
    if deps["langchain"]:
        status += "  • LangChain: Available for LLM integration\n"
    
    return status
