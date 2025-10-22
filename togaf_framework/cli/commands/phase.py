"""
TOGAF ADM phase execution commands
"""
import click
import os
import json
from pathlib import Path
from datetime import datetime
import sys

# Add parent paths for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from cli.config import ProjectConfig
from cli.utils import ConsoleColors, OutputFormatter


@click.command(name='run')
@click.argument('phase', type=click.Choice([
    'preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d',
    'phase-e', 'phase-f', 'phase-g', 'phase-h'
]))
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--use-ai', is_flag=True, help='Use AI agents for execution')
@click.option('--autonomous', is_flag=True, help='Enable autonomous mode for runtime intelligence')
@click.option('--output', type=click.Path(), help='Output file for phase results')
@click.pass_context
def run_phase(ctx, phase, project, use_ai, autonomous, output):
    """
    Execute a TOGAF ADM phase
    
    \b
    Examples:
      archiagents phase run phase-a
      archiagents phase run phase-a --use-ai
      archiagents phase run phase-b --autonomous --output results.json
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config_file = project_path / '.archiagents' / 'project.yaml'
    
    if not config_file.exists():
        click.echo(ConsoleColors.error("❌ Not an ArchiAgents project directory"), err=True)
        raise click.Abort()
    
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Executing TOGAF {phase.upper()}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Project:{ConsoleColors.END} {config.get('project.name')}")
    click.echo(f"{ConsoleColors.CYAN}Enterprise:{ConsoleColors.END} {config.get('project.enterprise')}")
    click.echo(f"{ConsoleColors.CYAN}AI Enabled:{ConsoleColors.END} {use_ai}")
    click.echo(f"{ConsoleColors.CYAN}Autonomous:{ConsoleColors.END} {autonomous}\n")
    
    # Phase mapping
    phase_modules = {
        'preliminary': ('adm.preliminary_phase', 'PreliminaryPhase'),
        'phase-a': ('adm.phase_a_vision', 'PhaseAVision'),
        'phase-b': ('adm.phase_b_business', 'PhaseBBusiness'),
        'phase-c': ('adm.phase_c_information', 'PhaseCInformation'),
        'phase-d': ('adm.phase_d_technology', 'PhaseDTechnology'),
        'phase-e': ('adm.phase_e_opportunities', 'PhaseEOpportunities'),
        'phase-f': ('adm.phase_f_migration', 'PhaseFMigration'),
        'phase-g': ('adm.phase_g_governance', 'PhaseGGovernance'),
        'phase-h': ('adm.phase_h_change', 'PhaseHChange'),
    }
    
    try:
        # Import required modules
        if use_ai:
            from ai_agents import AIAgentOrchestrator
            
            click.echo(ConsoleColors.info("🤖 Initializing AI agents..."))
            
            orchestrator = AIAgentOrchestrator(
                enterprise_name=config.get('project.enterprise'),
                project_name=config.get('project.name'),
                architecture_scope=config.get('project.scope')
            )
            
            # Execute phase with AI
            click.echo(ConsoleColors.info(f"🔄 Running {phase} with AI agents..."))
            
            context = {
                "project": config.get('project.name'),
                "enterprise": config.get('project.enterprise'),
                "scope": config.get('project.scope'),
                "use_langgraph": True,
                "use_crewai": True
            }
            
            result = orchestrator.execute_phase_with_ai(
                phase_name=phase.replace('-', '_'),
                use_langgraph=True,
                use_crewai=True,
                context=context
            )
            
            click.echo(ConsoleColors.success(f"\n✅ {phase.upper()} completed with AI!"))
            click.echo(f"\n{ConsoleColors.CYAN}Duration:{ConsoleColors.END} {result.get('duration_seconds', 0):.2f}s")
            click.echo(f"{ConsoleColors.CYAN}Recommendations:{ConsoleColors.END} {len(result.get('recommendations', []))}")
            
            # Show top recommendations
            if result.get('recommendations'):
                click.echo(f"\n{ConsoleColors.BOLD}Top Recommendations:{ConsoleColors.END}")
                for i, rec in enumerate(result['recommendations'][:5], 1):
                    click.echo(f"  {i}. {rec}")
            
        else:
            # Manual TOGAF execution
            module_name, class_name = phase_modules[phase]
            module = __import__(f'togaf_framework.{module_name}', fromlist=[class_name])
            PhaseClass = getattr(module, class_name)
            
            click.echo(ConsoleColors.info(f"🔄 Running {phase}..."))
            
            phase_instance = PhaseClass(
                enterprise_name=config.get('project.enterprise'),
                project_name=config.get('project.name')
            )
            
            # Execute phase
            result = phase_instance.execute({})
            
            click.echo(ConsoleColors.success(f"\n✅ {phase.upper()} completed!"))
        
        # Update project configuration
        config.set('togaf.active_phase', None)
        completed = config.get('togaf.completed_phases', [])
        if phase not in completed:
            completed.append(phase)
            config.set('togaf.completed_phases', completed)
        config.set('project.status', 'in-progress')
        config.save()
        
        # Save results if output specified
        if output:
            output_path = Path(output)
            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2, default=str)
            click.echo(f"\n{ConsoleColors.CYAN}Results saved to:{ConsoleColors.END} {output_path}")
        
        # Save phase deliverables
        phase_dir = project_path / 'phases' / phase
        phase_dir.mkdir(parents=True, exist_ok=True)
        
        deliverables_file = phase_dir / 'deliverables.json'
        with open(deliverables_file, 'w') as f:
            json.dump(result, f, indent=2, default=str)
        
        click.echo(f"{ConsoleColors.CYAN}Deliverables saved to:{ConsoleColors.END} {phase_dir}")
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Phase execution failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='list')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.pass_context
def list_phases(ctx, project):
    """List all TOGAF ADM phases and their status"""
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    phases_info = [
        ('preliminary', 'Preliminary Phase', 'Foundation and Principles'),
        ('phase-a', 'Phase A', 'Architecture Vision'),
        ('phase-b', 'Phase B', 'Business Architecture'),
        ('phase-c', 'Phase C', 'Information Systems Architecture'),
        ('phase-d', 'Phase D', 'Technology Architecture'),
        ('phase-e', 'Phase E', 'Opportunities and Solutions'),
        ('phase-f', 'Phase F', 'Migration Planning'),
        ('phase-g', 'Phase G', 'Implementation Governance'),
        ('phase-h', 'Phase H', 'Architecture Change Management')
    ]
    
    completed = config.get('togaf.completed_phases', [])
    active = config.get('togaf.active_phase')
    
    headers = ['Phase', 'Name', 'Description', 'Status']
    rows = []
    
    for phase_id, phase_name, description in phases_info:
        if phase_id in completed:
            status = ConsoleColors.success('✅ Complete')
        elif phase_id == active:
            status = ConsoleColors.warning('🔄 In Progress')
        else:
            status = '⏳ Pending'
        
        rows.append([phase_id, phase_name, description, status])
    
    table = OutputFormatter.format_table(headers, rows, "TOGAF ADM Phases")
    click.echo(table)


@click.command(name='status')
@click.argument('phase', type=click.Choice([
    'preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d',
    'phase-e', 'phase-f', 'phase-g', 'phase-h'
]))
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--format', type=click.Choice(['table', 'json', 'yaml']), default='table')
@click.pass_context
def phase_status(ctx, phase, project, format):
    """Show status and deliverables for a specific phase"""
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    phase_dir = project_path / 'phases' / phase
    
    if not phase_dir.exists():
        click.echo(ConsoleColors.warning(f"⚠️  Phase {phase} has not been executed yet"))
        return
    
    deliverables_file = phase_dir / 'deliverables.json'
    
    if not deliverables_file.exists():
        click.echo(ConsoleColors.warning(f"⚠️  No deliverables found for {phase}"))
        return
    
    with open(deliverables_file, 'r') as f:
        deliverables = json.load(f)
    
    if format == 'json':
        click.echo(json.dumps(deliverables, indent=2))
    elif format == 'yaml':
        import yaml
        click.echo(yaml.dump(deliverables, default_flow_style=False))
    else:
        click.echo(f"\n{ConsoleColors.HEADER}{phase.upper()} - Deliverables{ConsoleColors.END}\n")
        
        for key, value in deliverables.items():
            if isinstance(value, (list, dict)):
                click.echo(f"{ConsoleColors.CYAN}{key}:{ConsoleColors.END}")
                if isinstance(value, list):
                    for item in value[:5]:  # Show first 5
                        click.echo(f"  • {item}")
                    if len(value) > 5:
                        click.echo(f"  ... and {len(value) - 5} more")
                else:
                    click.echo(f"  {json.dumps(value, indent=2)}")
            else:
                click.echo(f"{ConsoleColors.CYAN}{key}:{ConsoleColors.END} {value}")
        
        click.echo()


@click.command(name='reset')
@click.argument('phase', type=click.Choice([
    'preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d',
    'phase-e', 'phase-f', 'phase-g', 'phase-h', 'all'
]))
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--force', is_flag=True, help='Force reset without confirmation')
@click.pass_context
def reset_phase(ctx, phase, project, force):
    """Reset a phase (or all phases) to restart"""
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    if not force:
        msg = f"Reset {phase}?" if phase != 'all' else "Reset ALL phases?"
        click.confirm(msg, abort=True)
    
    if phase == 'all':
        phases = ['preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d',
                  'phase-e', 'phase-f', 'phase-g', 'phase-h']
    else:
        phases = [phase]
    
    for p in phases:
        # Remove from completed
        completed = config.get('togaf.completed_phases', [])
        if p in completed:
            completed.remove(p)
            config.set('togaf.completed_phases', completed)
        
        # Clear active if it's the active phase
        if config.get('togaf.active_phase') == p:
            config.set('togaf.active_phase', None)
        
        # Delete phase deliverables
        phase_dir = project_path / 'phases' / p
        if phase_dir.exists():
            import shutil
            shutil.rmtree(phase_dir)
    
    config.save()
    
    click.echo(ConsoleColors.success(f"✅ Phase(s) reset successfully"))


# Export commands
__all__ = ['run_phase', 'list_phases', 'phase_status', 'reset_phase']
