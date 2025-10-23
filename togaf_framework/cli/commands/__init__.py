"""
CLI commands package
"""

from .project import init_project, list_projects, project_status, delete_project
from .phase import run_phase, list_phases, phase_status, reset_phase
from .intelligence import analyze_architecture, make_decision, check_health, generate_report as intelligence_report
from .scenario import list_scenarios, describe_scenario, run_scenario
from .model import generate_model, list_models, validate_model, export_model, improve_model
from .ai import configure_ai, test_ai, list_models as list_ai_models, list_agents, run_ai_task
from .report import generate_report, list_reports, compare_architectures
from .config import show_config, set_config, get_config, reset_config, validate_config, export_config, import_config
from .validate import validate_architecture, validate_completeness, validate_quality
from .interop import (
    import_from_archi, import_from_ea, import_from_json,
    export_to_archi, export_to_ea, export_to_mermaid, batch_export
)

__all__ = [
    # Project commands
    'init_project',
    'list_projects',
    'project_status',
    'delete_project',
    
    # Phase commands
    'run_phase',
    'list_phases',
    'phase_status',
    'reset_phase',
    
    # Intelligence commands
    'analyze_architecture',
    'make_decision',
    'check_health',
    'intelligence_report',
    
    # Scenario commands
    'list_scenarios',
    'describe_scenario',
    'run_scenario',
    
    # Model commands
    'generate_model',
    'list_models',
    'validate_model',
    'export_model',
    'improve_model',
    
    # AI commands
    'configure_ai',
    'test_ai',
    'list_ai_models',
    'list_agents',
    'run_ai_task',
    
    # Report commands
    'generate_report',
    'list_reports',
    'compare_architectures',
    
    # Config commands
    'show_config',
    'set_config',
    'get_config',
    'reset_config',
    'validate_config',
    'export_config',
    'import_config',
    
    # Validate commands
    'validate_architecture',
    'validate_completeness',
    'validate_quality',
    
    # Import/Export commands
    'import_from_archi',
    'import_from_ea',
    'import_from_json',
    'export_to_archi',
    'export_to_ea',
    'export_to_mermaid',
    'batch_export'
]
