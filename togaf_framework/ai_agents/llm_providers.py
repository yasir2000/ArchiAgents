"""
LLM Provider Abstraction Layer

Supports multiple LLM providers:
- OpenAI (GPT-4, GPT-3.5-turbo)
- Azure OpenAI
- Anthropic Claude
- Google Gemini
- Local models via Ollama
- Hugging Face models

Provides unified interface for all providers.
"""

import os
from typing import Optional, Dict, Any, List
from enum import Enum
from dataclasses import dataclass


class LLMProvider(Enum):
    """Supported LLM providers"""
    OPENAI = "openai"
    AZURE_OPENAI = "azure_openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    OLLAMA = "ollama"
    HUGGINGFACE = "huggingface"
    CUSTOM = "custom"


class LLMCapability(Enum):
    """LLM capabilities"""
    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"
    FUNCTION_CALLING = "function_calling"
    VISION = "vision"
    STREAMING = "streaming"


@dataclass
class LLMConfig:
    """LLM configuration"""
    provider: LLMProvider
    model_name: str
    api_key: Optional[str] = None
    api_base: Optional[str] = None
    api_version: Optional[str] = None
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    timeout: int = 60
    retry_attempts: int = 3
    streaming: bool = False
    extra_params: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.extra_params is None:
            self.extra_params = {}


class LLMProviderFactory:
    """
    Factory for creating LLM provider instances
    
    Handles provider-specific initialization and configuration.
    """
    
    @staticmethod
    def create_provider(config: LLMConfig) -> Any:
        """
        Create LLM provider instance based on configuration
        
        Args:
            config: LLM configuration
            
        Returns:
            Configured LLM provider instance
        """
        if config.provider == LLMProvider.OPENAI:
            return LLMProviderFactory._create_openai(config)
        elif config.provider == LLMProvider.AZURE_OPENAI:
            return LLMProviderFactory._create_azure_openai(config)
        elif config.provider == LLMProvider.ANTHROPIC:
            return LLMProviderFactory._create_anthropic(config)
        elif config.provider == LLMProvider.GOOGLE:
            return LLMProviderFactory._create_google(config)
        elif config.provider == LLMProvider.OLLAMA:
            return LLMProviderFactory._create_ollama(config)
        elif config.provider == LLMProvider.HUGGINGFACE:
            return LLMProviderFactory._create_huggingface(config)
        else:
            raise ValueError(f"Unsupported provider: {config.provider}")
    
    @staticmethod
    def _create_openai(config: LLMConfig) -> Any:
        """Create OpenAI provider"""
        try:
            from langchain_openai import ChatOpenAI
            
            return ChatOpenAI(
                model=config.model_name,
                api_key=config.api_key or os.getenv("OPENAI_API_KEY"),
                temperature=config.temperature,
                max_tokens=config.max_tokens,
                timeout=config.timeout,
                max_retries=config.retry_attempts,
                streaming=config.streaming,
                **config.extra_params
            )
        except ImportError:
            raise ImportError(
                "OpenAI provider requires: pip install langchain-openai"
            )
    
    @staticmethod
    def _create_azure_openai(config: LLMConfig) -> Any:
        """Create Azure OpenAI provider"""
        try:
            from langchain_openai import AzureChatOpenAI
            
            return AzureChatOpenAI(
                azure_deployment=config.model_name,
                api_key=config.api_key or os.getenv("AZURE_OPENAI_API_KEY"),
                azure_endpoint=config.api_base or os.getenv("AZURE_OPENAI_ENDPOINT"),
                api_version=config.api_version or os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
                temperature=config.temperature,
                max_tokens=config.max_tokens,
                timeout=config.timeout,
                max_retries=config.retry_attempts,
                streaming=config.streaming,
                **config.extra_params
            )
        except ImportError:
            raise ImportError(
                "Azure OpenAI provider requires: pip install langchain-openai"
            )
    
    @staticmethod
    def _create_anthropic(config: LLMConfig) -> Any:
        """Create Anthropic Claude provider"""
        try:
            from langchain_anthropic import ChatAnthropic
            
            return ChatAnthropic(
                model=config.model_name,
                anthropic_api_key=config.api_key or os.getenv("ANTHROPIC_API_KEY"),
                temperature=config.temperature,
                max_tokens=config.max_tokens or 4096,
                timeout=config.timeout,
                max_retries=config.retry_attempts,
                streaming=config.streaming,
                **config.extra_params
            )
        except ImportError:
            raise ImportError(
                "Anthropic provider requires: pip install langchain-anthropic"
            )
    
    @staticmethod
    def _create_google(config: LLMConfig) -> Any:
        """Create Google Gemini provider"""
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            
            return ChatGoogleGenerativeAI(
                model=config.model_name,
                google_api_key=config.api_key or os.getenv("GOOGLE_API_KEY"),
                temperature=config.temperature,
                max_output_tokens=config.max_tokens,
                timeout=config.timeout,
                max_retries=config.retry_attempts,
                streaming=config.streaming,
                **config.extra_params
            )
        except ImportError:
            raise ImportError(
                "Google provider requires: pip install langchain-google-genai"
            )
    
    @staticmethod
    def _create_ollama(config: LLMConfig) -> Any:
        """
        Create Ollama provider for local LLMs
        
        Supports any model available in Ollama:
        - llama2, llama3
        - mistral, mixtral
        - codellama
        - phi, phi-2
        - gemma
        - etc.
        """
        try:
            from langchain_community.chat_models import ChatOllama
            
            return ChatOllama(
                model=config.model_name,
                base_url=config.api_base or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                temperature=config.temperature,
                num_predict=config.max_tokens,
                timeout=config.timeout,
                **config.extra_params
            )
        except ImportError:
            raise ImportError(
                "Ollama provider requires: pip install langchain-community"
            )
    
    @staticmethod
    def _create_huggingface(config: LLMConfig) -> Any:
        """Create Hugging Face provider"""
        try:
            from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
            
            # Create endpoint
            endpoint = HuggingFaceEndpoint(
                repo_id=config.model_name,
                huggingfacehub_api_token=config.api_key or os.getenv("HUGGINGFACE_API_KEY"),
                temperature=config.temperature,
                max_new_tokens=config.max_tokens,
                timeout=config.timeout,
                **config.extra_params
            )
            
            # Wrap in chat model
            return ChatHuggingFace(llm=endpoint)
        except ImportError:
            raise ImportError(
                "Hugging Face provider requires: pip install langchain-huggingface"
            )


class LLMProviderManager:
    """
    Manager for LLM providers
    
    Provides unified interface and automatic provider selection.
    """
    
    # Popular model mappings
    MODEL_PROVIDERS = {
        # OpenAI
        "gpt-4": LLMProvider.OPENAI,
        "gpt-4-turbo": LLMProvider.OPENAI,
        "gpt-4-turbo-preview": LLMProvider.OPENAI,
        "gpt-3.5-turbo": LLMProvider.OPENAI,
        "gpt-3.5-turbo-16k": LLMProvider.OPENAI,
        
        # Anthropic
        "claude-3-opus-20240229": LLMProvider.ANTHROPIC,
        "claude-3-sonnet-20240229": LLMProvider.ANTHROPIC,
        "claude-3-haiku-20240307": LLMProvider.ANTHROPIC,
        "claude-2.1": LLMProvider.ANTHROPIC,
        "claude-2": LLMProvider.ANTHROPIC,
        
        # Google
        "gemini-pro": LLMProvider.GOOGLE,
        "gemini-1.5-pro": LLMProvider.GOOGLE,
        "gemini-ultra": LLMProvider.GOOGLE,
        
        # Ollama (local models)
        "llama2": LLMProvider.OLLAMA,
        "llama3": LLMProvider.OLLAMA,
        "llama3.1": LLMProvider.OLLAMA,
        "mistral": LLMProvider.OLLAMA,
        "mixtral": LLMProvider.OLLAMA,
        "codellama": LLMProvider.OLLAMA,
        "phi": LLMProvider.OLLAMA,
        "phi-2": LLMProvider.OLLAMA,
        "gemma": LLMProvider.OLLAMA,
        "qwen": LLMProvider.OLLAMA,
        "deepseek-coder": LLMProvider.OLLAMA,
    }
    
    @classmethod
    def auto_detect_provider(cls, model_name: str) -> LLMProvider:
        """
        Auto-detect provider from model name
        
        Args:
            model_name: Name of the model
            
        Returns:
            Detected provider
        """
        # Exact match
        if model_name in cls.MODEL_PROVIDERS:
            return cls.MODEL_PROVIDERS[model_name]
        
        # Check prefixes
        model_lower = model_name.lower()
        
        if model_lower.startswith("gpt"):
            return LLMProvider.OPENAI
        elif model_lower.startswith("claude"):
            return LLMProvider.ANTHROPIC
        elif model_lower.startswith("gemini"):
            return LLMProvider.GOOGLE
        elif model_lower.startswith("azure/"):
            return LLMProvider.AZURE_OPENAI
        elif "/" in model_name:  # Hugging Face format: org/model
            return LLMProvider.HUGGINGFACE
        else:
            # Default to Ollama for unknown models (likely local)
            return LLMProvider.OLLAMA
    
    @classmethod
    def create_llm(
        cls,
        model_name: str,
        provider: Optional[LLMProvider] = None,
        **kwargs
    ) -> Any:
        """
        Create LLM instance with automatic provider detection
        
        Args:
            model_name: Name of the model
            provider: Optional provider (auto-detected if not specified)
            **kwargs: Additional configuration
            
        Returns:
            Configured LLM instance
        """
        # Auto-detect provider if not specified
        if provider is None:
            provider = cls.auto_detect_provider(model_name)
        
        # Handle Azure special format
        if model_name.startswith("azure/"):
            model_name = model_name.replace("azure/", "")
            provider = LLMProvider.AZURE_OPENAI
        
        # Create configuration
        config = LLMConfig(
            provider=provider,
            model_name=model_name,
            **kwargs
        )
        
        # Create and return provider
        return LLMProviderFactory.create_provider(config)
    
    @classmethod
    def get_available_providers(cls) -> List[str]:
        """
        Get list of available providers (installed packages)
        
        Returns:
            List of available provider names
        """
        available = []
        
        # Check OpenAI
        try:
            import langchain_openai
            available.append("openai")
            available.append("azure_openai")
        except ImportError:
            pass
        
        # Check Anthropic
        try:
            import langchain_anthropic
            available.append("anthropic")
        except ImportError:
            pass
        
        # Check Google
        try:
            import langchain_google_genai
            available.append("google")
        except ImportError:
            pass
        
        # Check Ollama (via community)
        try:
            import langchain_community.chat_models
            available.append("ollama")
        except ImportError:
            pass
        
        # Check Hugging Face
        try:
            import langchain_huggingface
            available.append("huggingface")
        except ImportError:
            pass
        
        return available
    
    @classmethod
    def check_provider_available(cls, provider: LLMProvider) -> bool:
        """
        Check if a provider is available
        
        Args:
            provider: Provider to check
            
        Returns:
            True if available, False otherwise
        """
        return provider.value in cls.get_available_providers()


def get_recommended_models() -> Dict[str, List[str]]:
    """
    Get recommended models by use case
    
    Returns:
        Dictionary of use case to recommended models
    """
    return {
        "high_quality": [
            "gpt-4-turbo",
            "claude-3-opus-20240229",
            "gemini-1.5-pro"
        ],
        "balanced": [
            "gpt-3.5-turbo",
            "claude-3-sonnet-20240229",
            "gemini-pro"
        ],
        "fast": [
            "gpt-3.5-turbo",
            "claude-3-haiku-20240307",
            "gemini-pro"
        ],
        "local": [
            "llama3.1",
            "mistral",
            "mixtral",
            "phi-2",
            "gemma"
        ],
        "coding": [
            "gpt-4-turbo",
            "claude-3-opus-20240229",
            "codellama",
            "deepseek-coder"
        ],
        "cost_effective": [
            "gpt-3.5-turbo",
            "llama3.1",  # Local
            "mistral",   # Local
            "phi-2"      # Local
        ]
    }


def get_provider_info() -> Dict[str, Dict[str, Any]]:
    """
    Get information about all providers
    
    Returns:
        Dictionary with provider information
    """
    return {
        "openai": {
            "name": "OpenAI",
            "models": ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
            "requires": "pip install langchain-openai",
            "api_key": "OPENAI_API_KEY",
            "pricing": "Paid",
            "features": ["chat", "completion", "function_calling", "vision"]
        },
        "azure_openai": {
            "name": "Azure OpenAI",
            "models": ["gpt-4", "gpt-35-turbo"],
            "requires": "pip install langchain-openai",
            "api_key": "AZURE_OPENAI_API_KEY",
            "pricing": "Paid",
            "features": ["chat", "completion", "function_calling"]
        },
        "anthropic": {
            "name": "Anthropic Claude",
            "models": ["claude-3-opus", "claude-3-sonnet", "claude-3-haiku"],
            "requires": "pip install langchain-anthropic",
            "api_key": "ANTHROPIC_API_KEY",
            "pricing": "Paid",
            "features": ["chat", "completion", "vision"]
        },
        "google": {
            "name": "Google Gemini",
            "models": ["gemini-pro", "gemini-1.5-pro", "gemini-ultra"],
            "requires": "pip install langchain-google-genai",
            "api_key": "GOOGLE_API_KEY",
            "pricing": "Paid/Free tier",
            "features": ["chat", "completion", "vision"]
        },
        "ollama": {
            "name": "Ollama (Local)",
            "models": ["llama3.1", "mistral", "mixtral", "phi-2", "gemma", "codellama"],
            "requires": "pip install langchain-community + Ollama installed",
            "api_key": "None (local)",
            "pricing": "Free (runs locally)",
            "features": ["chat", "completion"],
            "setup": "Install Ollama from https://ollama.ai then: ollama pull <model>"
        },
        "huggingface": {
            "name": "Hugging Face",
            "models": ["meta-llama/Llama-2-7b-chat-hf", "mistralai/Mistral-7B-Instruct-v0.2"],
            "requires": "pip install langchain-huggingface",
            "api_key": "HUGGINGFACE_API_KEY",
            "pricing": "Free/Paid",
            "features": ["chat", "completion"]
        }
    }
