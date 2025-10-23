"""
Main CLI entry point for ArchiAgents

Provides command-line interface for enterprise architecture management using
TOGAF framework, AI agents, and Runtime Intelligence Layer.
"""
import click
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from cli.config import Config
from cli.utils import ConsoleColors, OutputFormatter


# Global configuration
config = Config()


@click.group()
@click.version_option(version="1.0.0", prog_name="archiagents")
@click.option('--config', type=click.Path(), help='Path to configuration file')
@click.option('--verbose', is_flag=True, help='Enable verbose output')
@click.pass_context
def cli(ctx, config_file, verbose):
    """
    ArchiAgents - Enterprise Architecture Management CLI
    
    A comprehensive tool for managing enterprise architecture using TOGAF framework,
    AI-powered agents, and intelligent runtime decision-making.
    
    \b
    Command Groups:
      project       - Project lifecycle management (init, list, status, delete)
      phase         - TOGAF ADM phase execution (run, list, status, reset)
      ai            - AI agent configuration and execution (configure, test, run, agents)
      intelligence  - Runtime intelligence & autonomous decisions (analyze, decide, health)
      model         - ArchiMate/UML model generation (generate, list, validate, export)
      report        - Architecture reports (generate, list, compare)
      scenario      - Pre-built scenarios (cloud-migration, digital-transformation, etc.)
      validate      - Quality & compliance validation (architecture, completeness, quality)
      import        - Import from external tools (Archi, EA, JSON)
      export        - Export to external tools (Archi, EA, Mermaid, batch)
      config        - CLI configuration (show, set, get, validate, export, import)
    
    \b
    Quick Examples:
      # Initialize a new project
      archiagents project init --name "Digital Transformation" --enterprise "TechCorp"
      
      # Configure AI provider
      archiagents ai configure --provider openai --model gpt-4
      
      # Execute Phase A with AI
      archiagents phase run phase-a --use-ai
      
      # Analyze architecture health
      archiagents intelligence health
      
      # Generate ArchiMate model
      archiagents model generate --type archimate-business --name "Business Layer"
      
      # Run cloud migration scenario
      archiagents scenario run cloud-migration --enterprise "TechCorp"
      
      # Validate architecture
      archiagents validate architecture --standard togaf
      
      # Export to Archi tool
      archiagents export to-archi --model-id my-model
    
    \b
    Features:
      ✓ 50+ CLI commands across 11 command groups
      ✓ Multi-provider AI support (OpenAI, Claude, Gemini, Ollama)
      ✓ 21 model types (ArchiMate, BPMN, UML)
      ✓ 6 export formats (Text, Mermaid, Kroki, Archi, GoJS, EA)
      ✓ Real-time intelligence and autonomous decision-making
      ✓ TOGAF 10, ArchiMate 3.2, Saudi NORA compliance
      ✓ Import/Export from Archi, Enterprise Architect
      ✓ Comprehensive validation and quality checks
    
    For detailed help on any command, use: archiagents COMMAND --help
    """
    ctx.ensure_object(dict)
    
    # Load configuration
    if config_file:
        ctx.obj['config'] = Config(config_file)
    else:
        ctx.obj['config'] = config
    
    ctx.obj['verbose'] = verbose or config.get('output.verbose', False)
    ctx.obj['output_format'] = config.get('output.format', 'table')
    ctx.obj['color'] = config.get('output.color', True)


@cli.group()
def project():
    """Manage architecture projects"""
    pass


@cli.group()
def phase():
    """Execute and manage TOGAF ADM phases"""
    pass


@cli.group()
def ai():
    """Configure and run AI agents"""
    pass


@cli.group()
def intelligence():
    """Runtime intelligence and autonomous decision-making"""
    pass


@cli.group()
def model():
    """ArchiMate model management"""
    pass


@cli.group()
def report():
    """Generate architecture reports"""
    pass


@cli.group()
def scenario():
    """Run predefined real-world scenarios"""
    pass


@cli.group()
def config_cmd():
    """Manage CLI configuration"""
    pass


@cli.group()
def validate():
    """Validate architecture quality and compliance"""
    pass


@cli.group(name='import')
def import_cmd():
    """Import architecture from external tools"""
    pass


@cli.group(name='export')
def export_cmd():
    """Export architecture to external tools"""
    pass


# Register as 'config' command
cli.add_command(config_cmd, name='config')


# Import and register all commands
from cli.commands import (
    init_project, list_projects, project_status, delete_project,
    run_phase, list_phases, phase_status, reset_phase,
    analyze_architecture, make_decision, check_health, intelligence_report,
    list_scenarios, describe_scenario, run_scenario,
    generate_model, list_models, validate_model, export_model, improve_model,
    configure_ai, test_ai, list_ai_models, list_agents, run_ai_task,
    generate_report, list_reports, compare_architectures,
    show_config, set_config, get_config, reset_config, validate_config, export_config, import_config,
    validate_architecture, validate_completeness, validate_quality,
    import_from_archi, import_from_ea, import_from_json,
    export_to_archi, export_to_ea, export_to_mermaid, batch_export
)

# Register project commands
project.add_command(init_project, name='init')
project.add_command(list_projects, name='list')
project.add_command(project_status, name='status')
project.add_command(delete_project, name='delete')

# Register phase commands
phase.add_command(run_phase, name='run')
phase.add_command(list_phases, name='list')
phase.add_command(phase_status, name='status')
phase.add_command(reset_phase, name='reset')

# Register intelligence commands
intelligence.add_command(analyze_architecture, name='analyze')
intelligence.add_command(make_decision, name='decide')
intelligence.add_command(check_health, name='health')
intelligence.add_command(intelligence_report, name='report')

# Register model commands
model.add_command(generate_model, name='generate')
model.add_command(list_models, name='list')
model.add_command(validate_model, name='validate')
model.add_command(export_model, name='export')
model.add_command(improve_model, name='improve')

# Register scenario commands
scenario.add_command(list_scenarios, name='list')
scenario.add_command(describe_scenario, name='describe')
scenario.add_command(run_scenario, name='run')

# Register AI commands
ai.add_command(configure_ai, name='configure')
ai.add_command(test_ai, name='test')
ai.add_command(list_ai_models, name='list-models')
ai.add_command(list_agents, name='agents')
ai.add_command(run_ai_task, name='run')

# Register report commands
report.add_command(generate_report, name='generate')
report.add_command(list_reports, name='list')
report.add_command(compare_architectures, name='compare')

# Register config commands
config_cmd.add_command(show_config, name='show')
config_cmd.add_command(set_config, name='set')
config_cmd.add_command(get_config, name='get')
config_cmd.add_command(reset_config, name='reset')
config_cmd.add_command(validate_config, name='validate')
config_cmd.add_command(export_config, name='export')
config_cmd.add_command(import_config, name='import')

# Register validate commands
validate.add_command(validate_architecture, name='architecture')
validate.add_command(validate_completeness, name='completeness')
validate.add_command(validate_quality, name='quality')

# Register import commands
import_cmd.add_command(import_from_archi, name='from-archi')
import_cmd.add_command(import_from_ea, name='from-ea')
import_cmd.add_command(import_from_json, name='from-json')

# Register export commands
export_cmd.add_command(export_to_archi, name='to-archi')
export_cmd.add_command(export_to_ea, name='to-ea')
export_cmd.add_command(export_to_mermaid, name='to-mermaid')
export_cmd.add_command(batch_export, name='batch')


if __name__ == '__main__':
    cli()
