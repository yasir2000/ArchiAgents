"""
CLI commands package
"""

from .project import init_project, list_projects, project_status, delete_project
from .phase import run_phase, list_phases, phase_status, reset_phase
from .intelligence import analyze_architecture, make_decision, check_health, generate_report as intelligence_report
from .scenario import list_scenarios, describe_scenario, run_scenario
from .model import generate_model, list_models, validate_model, export_model, improve_model

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
    'improve_model'
]
