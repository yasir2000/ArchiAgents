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
    Commands:
      project     - Manage architecture projects
      phase       - Execute TOGAF ADM phases
      ai          - Configure and run AI agents
      intelligence - Runtime intelligence and autonomous decision-making
      model       - ArchiMate model management
      report      - Generate architecture reports
      scenario    - Run predefined real-world scenarios
      config      - Manage CLI configuration
    
    \b
    Examples:
      # Initialize a new project
      archiagents project init --name "Digital Transformation"
      
      # Execute Phase A with AI
      archiagents phase run phase-a --use-ai
      
      # Analyze architecture health
      archiagents intelligence health
      
      # Run cloud migration scenario
      archiagents scenario run cloud-migration
    
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


# Register as 'config' command
cli.add_command(config_cmd, name='config')


if __name__ == '__main__':
    cli()
