"""
Configuration Management Commands

Manage CLI configuration settings.
"""
import click
import os
import json
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from cli.config import Config, ProjectConfig
from cli.utils import ConsoleColors, OutputFormatter


@click.command(name='show')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--global-config', is_flag=True, help='Show global configuration')
@click.option('--format', type=click.Choice(['table', 'json', 'yaml']), default='table')
@click.pass_context
def show_config(ctx, project, global_config, format):
    """
    Show current configuration
    
    \b
    Examples:
      archiagents config show
      archiagents config show --global-config
      archiagents config show --format json
    """
    
    if global_config:
        config = ctx.obj['config']
        config_data = config.config
    else:
        if not project:
            project = os.getcwd()
        
        project_path = Path(project)
        config_file = project_path / '.archiagents' / 'project.yaml'
        
        if not config_file.exists():
            click.echo(ConsoleColors.error("❌ Not an ArchiAgents project directory"), err=True)
            raise click.Abort()
        
        config = ProjectConfig(str(project_path))
        config_data = config.config
    
    if format == 'json':
        click.echo(json.dumps(config_data, indent=2, default=str))
    elif format == 'yaml':
        import yaml
        click.echo(yaml.dump(config_data, default_flow_style=False))
    else:
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
        click.echo(f"{ConsoleColors.BOLD}Configuration{ConsoleColors.END}")
        click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
        _print_config_section(config_data, 0)


@click.command(name='set')
@click.argument('key')
@click.argument('value')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--global-config', is_flag=True, help='Set global configuration')
@click.pass_context
def set_config(ctx, key, value, project, global_config):
    """
    Set configuration value
    
    \b
    Examples:
      archiagents config set output.format json
      archiagents config set ai.provider openai
      archiagents config set --global-config projects.default_path /path/to/projects
    """
    
    # Parse value (try to convert to appropriate type)
    try:
        if value.lower() == 'true':
            value = True
        elif value.lower() == 'false':
            value = False
        elif value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit():
            value = float(value)
    except:
        pass  # Keep as string
    
    if global_config:
        config = ctx.obj['config']
        config.set(key, value)
        config.save()
        click.echo(ConsoleColors.success(f"✅ Global configuration updated: {key} = {value}"))
    else:
        if not project:
            project = os.getcwd()
        
        project_path = Path(project)
        config = ProjectConfig(str(project_path))
        config.set(key, value)
        config.save()
        click.echo(ConsoleColors.success(f"✅ Project configuration updated: {key} = {value}"))


@click.command(name='get')
@click.argument('key')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--global-config', is_flag=True, help='Get from global configuration')
@click.pass_context
def get_config(ctx, key, project, global_config):
    """
    Get configuration value
    
    \b
    Examples:
      archiagents config get ai.provider
      archiagents config get output.format
      archiagents config get --global-config projects.default_path
    """
    
    if global_config:
        config = ctx.obj['config']
    else:
        if not project:
            project = os.getcwd()
        
        project_path = Path(project)
        config = ProjectConfig(str(project_path))
    
    value = config.get(key)
    
    if value is None:
        click.echo(ConsoleColors.error(f"❌ Configuration key not found: {key}"), err=True)
    else:
        click.echo(f"{ConsoleColors.CYAN}{key}:{ConsoleColors.END} {value}")


@click.command(name='reset')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--global-config', is_flag=True, help='Reset global configuration')
@click.option('--confirm', is_flag=True, help='Skip confirmation')
@click.pass_context
def reset_config(ctx, project, global_config, confirm):
    """
    Reset configuration to defaults
    
    \b
    Example:
      archiagents config reset --confirm
      archiagents config reset --global-config --confirm
    """
    
    if not confirm:
        if not click.confirm('Are you sure you want to reset configuration to defaults?'):
            click.echo("Cancelled.")
            return
    
    if global_config:
        config = ctx.obj['config']
        config.config = Config.get_default_config()
        config.save()
        click.echo(ConsoleColors.success("✅ Global configuration reset to defaults"))
    else:
        if not project:
            project = os.getcwd()
        
        project_path = Path(project)
        config = ProjectConfig(str(project_path))
        # Reset specific sections while keeping project info
        config.set('ai', Config.get_default_config()['ai'])
        config.set('runtime_intelligence', Config.get_default_config()['runtime_intelligence'])
        config.save()
        click.echo(ConsoleColors.success("✅ Project configuration reset to defaults"))


@click.command(name='validate')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.pass_context
def validate_config(ctx, project):
    """
    Validate configuration
    
    \b
    Example:
      archiagents config validate
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}Validating Configuration{ConsoleColors.END}\n")
    
    issues = []
    warnings = []
    
    # Validate required fields
    required_fields = [
        'project.name',
        'project.enterprise',
        'togaf.version'
    ]
    
    for field in required_fields:
        value = config.get(field)
        if not value:
            issues.append(f"Missing required field: {field}")
    
    # Validate AI configuration
    if config.get('ai.enabled'):
        provider = config.get('ai.provider')
        if provider not in ['openai', 'anthropic', 'google', 'azure', 'mistral', 'ollama']:
            issues.append(f"Invalid AI provider: {provider}")
        
        if provider != 'ollama' and not config.get('ai.api_key'):
            warnings.append(f"AI provider '{provider}' requires API key")
    
    # Display results
    if issues:
        click.echo(ConsoleColors.error(f"❌ Found {len(issues)} issue(s):"))
        for issue in issues:
            click.echo(f"  • {issue}")
        click.echo()
    
    if warnings:
        click.echo(ConsoleColors.warning(f"⚠️  Found {len(warnings)} warning(s):"))
        for warning in warnings:
            click.echo(f"  • {warning}")
        click.echo()
    
    if not issues and not warnings:
        click.echo(ConsoleColors.success("✅ Configuration is valid!"))
    
    click.echo()


@click.command(name='export')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--output', type=click.Path(), required=True, help='Output file path')
@click.option('--format', type=click.Choice(['json', 'yaml']), default='yaml')
@click.pass_context
def export_config(ctx, project, output, format):
    """
    Export configuration to file
    
    \b
    Examples:
      archiagents config export --output config.yaml
      archiagents config export --output config.json --format json
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    output_path = Path(output)
    
    try:
        if format == 'json':
            with open(output_path, 'w') as f:
                json.dump(config.config, f, indent=2, default=str)
        else:  # yaml
            import yaml
            with open(output_path, 'w') as f:
                yaml.dump(config.config, f, default_flow_style=False)
        
        click.echo(ConsoleColors.success(f"✅ Configuration exported to: {output_path}"))
    
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Export failed: {e}"), err=True)
        raise click.Abort()


@click.command(name='import')
@click.argument('config_file', type=click.Path(exists=True))
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--merge', is_flag=True, help='Merge with existing configuration')
@click.pass_context
def import_config(ctx, config_file, project, merge):
    """
    Import configuration from file
    
    \b
    Examples:
      archiagents config import config.yaml
      archiagents config import config.json --merge
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    config_path = Path(config_file)
    
    try:
        if config_path.suffix == '.json':
            with open(config_path, 'r') as f:
                new_config = json.load(f)
        else:  # yaml
            import yaml
            with open(config_path, 'r') as f:
                new_config = yaml.safe_load(f)
        
        if merge:
            # Merge configurations
            config.config.update(new_config)
        else:
            # Replace configuration
            config.config = new_config
        
        config.save()
        
        click.echo(ConsoleColors.success(f"✅ Configuration imported from: {config_path}"))
    
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Import failed: {e}"), err=True)
        raise click.Abort()


def _print_config_section(data, indent=0):
    """Recursively print configuration sections"""
    prefix = "  " * indent
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                click.echo(f"{prefix}{ConsoleColors.CYAN}{key}:{ConsoleColors.END}")
                _print_config_section(value, indent + 1)
            else:
                click.echo(f"{prefix}{ConsoleColors.CYAN}{key}:{ConsoleColors.END} {value}")
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                _print_config_section(item, indent)
            else:
                click.echo(f"{prefix}• {item}")
