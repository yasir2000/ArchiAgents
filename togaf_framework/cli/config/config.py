"""
Configuration management for ArchiAgents CLI
"""
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional
import yaml


class Config:
    """Configuration manager for CLI"""
    
    DEFAULT_CONFIG = {
        "enterprise": {
            "name": "My Organization",
            "domain": "myorg.com"
        },
        "ai": {
            "provider": "openai",
            "model": "gpt-4",
            "api_key": None,
            "temperature": 0.7,
            "max_tokens": 4000
        },
        "runtime_intelligence": {
            "autonomous_mode": False,
            "auto_approve_low_risk": False,
            "health_check_interval": 300
        },
        "output": {
            "format": "table",
            "color": True,
            "verbose": False
        },
        "projects": {
            "default_path": "~/archiagents_projects"
        }
    }
    
    def __init__(self, config_file: Optional[str] = None):
        """Initialize configuration"""
        self.config_file = config_file or self._get_default_config_path()
        self.config = self._load_config()
    
    def _get_default_config_path(self) -> str:
        """Get default config file path"""
        config_dir = Path.home() / ".archiagents"
        config_dir.mkdir(exist_ok=True)
        return str(config_dir / "config.yaml")
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    if self.config_file.endswith('.yaml') or self.config_file.endswith('.yml'):
                        config = yaml.safe_load(f)
                    else:
                        config = json.load(f)
                
                # Merge with defaults
                return self._merge_config(self.DEFAULT_CONFIG, config)
            except Exception as e:
                print(f"Warning: Could not load config file: {e}")
                return self.DEFAULT_CONFIG.copy()
        else:
            return self.DEFAULT_CONFIG.copy()
    
    def _merge_config(self, default: Dict, custom: Dict) -> Dict:
        """Recursively merge custom config with defaults"""
        result = default.copy()
        for key, value in custom.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_config(result[key], value)
            else:
                result[key] = value
        return result
    
    def save(self):
        """Save configuration to file"""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        
        with open(self.config_file, 'w') as f:
            if self.config_file.endswith('.yaml') or self.config_file.endswith('.yml'):
                yaml.dump(self.config, f, default_flow_style=False)
            else:
                json.dump(self.config, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value using dot notation"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value using dot notation"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def reset(self):
        """Reset configuration to defaults"""
        self.config = self.DEFAULT_CONFIG.copy()
    
    def show(self) -> Dict[str, Any]:
        """Get all configuration"""
        return self.config.copy()


class ProjectConfig:
    """Project-specific configuration"""
    
    def __init__(self, project_path: str):
        """Initialize project configuration"""
        self.project_path = Path(project_path)
        self.config_file = self.project_path / ".archiagents" / "project.yaml"
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load project configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return yaml.safe_load(f) or {}
        return {}
    
    def save(self):
        """Save project configuration"""
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_file, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
