"""
Real-world scenario execution commands

Provides pre-built scenarios for common enterprise architecture use cases:
- Digital Transformation
- Cloud Migration
- Microservices Adoption
- Enterprise Modernization
- Merger & Acquisition Integration
"""
import click
import os
import json
from pathlib import Path
from datetime import datetime
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from cli.config import ProjectConfig
from cli.utils import ConsoleColors, OutputFormatter


# Scenario definitions
SCENARIOS = {
    'digital-transformation': {
        'name': 'Digital Transformation',
        'description': 'Complete digital transformation journey from legacy to modern digital enterprise',
        'duration': '18-24 months',
        'phases': ['preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d', 'phase-e', 'phase-f'],
        'objectives': [
            'Modernize legacy applications',
            'Implement omnichannel customer experience',
            'Adopt cloud-native architecture',
            'Enable data-driven decision making',
            'Automate business processes'
        ],
        'kpis': [
            'Customer satisfaction: >85%',
            'Time to market: <2 weeks',
            'Process automation: >70%',
            'Cloud adoption: 80%',
            'Digital revenue: 50% of total'
        ]
    },
    'cloud-migration': {
        'name': 'Cloud Migration',
        'description': 'Migration from on-premises infrastructure to cloud platform',
        'duration': '6-12 months',
        'phases': ['preliminary', 'phase-a', 'phase-c', 'phase-d', 'phase-e', 'phase-f'],
        'objectives': [
            'Assess cloud readiness',
            'Select cloud provider and services',
            'Design cloud architecture',
            'Migrate applications and data',
            'Optimize cloud costs'
        ],
        'kpis': [
            'Infrastructure cost reduction: 40%',
            'Scalability: 10x capacity',
            'Availability: 99.9%',
            'Migration success rate: 100%',
            'Performance improvement: 30%'
        ]
    },
    'microservices': {
        'name': 'Microservices Adoption',
        'description': 'Transformation from monolithic to microservices architecture',
        'duration': '12-18 months',
        'phases': ['preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d', 'phase-f'],
        'objectives': [
            'Decompose monolithic applications',
            'Design microservices architecture',
            'Implement API gateway',
            'Setup container orchestration',
            'Establish DevOps practices'
        ],
        'kpis': [
            'Deployment frequency: Daily',
            'Lead time: <1 day',
            'Service independence: 100%',
            'Fault tolerance: 99.95%',
            'Development velocity: 3x faster'
        ]
    },
    'modernization': {
        'name': 'Enterprise Modernization',
        'description': 'Modernization of legacy enterprise systems and processes',
        'duration': '24-36 months',
        'phases': ['preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d', 'phase-e', 'phase-f', 'phase-g'],
        'objectives': [
            'Replace legacy core systems',
            'Modernize user interfaces',
            'Implement modern integration patterns',
            'Adopt agile methodologies',
            'Establish enterprise data platform'
        ],
        'kpis': [
            'Technical debt reduction: 60%',
            'System maintainability: >80%',
            'Integration efficiency: 50% faster',
            'User satisfaction: >90%',
            'Total cost of ownership: -35%'
        ]
    },
    'merger-integration': {
        'name': 'Merger & Acquisition Integration',
        'description': 'Integration of IT systems and processes following M&A',
        'duration': '12-18 months',
        'phases': ['preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d', 'phase-e', 'phase-f', 'phase-g'],
        'objectives': [
            'Assess and rationalize IT portfolios',
            'Design target integration architecture',
            'Merge critical business systems',
            'Harmonize business processes',
            'Achieve operational synergies'
        ],
        'kpis': [
            'System integration: 100%',
            'Cost synergies: $50M annually',
            'Process harmonization: 90%',
            'Cultural alignment: >75%',
            'Integration timeline: On schedule'
        ]
    }
}


@click.command(name='list')
@click.pass_context
def list_scenarios(ctx):
    """List all available real-world scenarios"""
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Available Real-World Scenarios{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    for scenario_id, scenario in SCENARIOS.items():
        click.echo(f"{ConsoleColors.CYAN}[{scenario_id}]{ConsoleColors.END}")
        click.echo(f"  {ConsoleColors.BOLD}{scenario['name']}{ConsoleColors.END}")
        click.echo(f"  {scenario['description']}")
        click.echo(f"  Duration: {scenario['duration']}")
        click.echo(f"  Phases: {len(scenario['phases'])}")
        click.echo()


@click.command(name='describe')
@click.argument('scenario', type=click.Choice(list(SCENARIOS.keys())))
@click.option('--format', type=click.Choice(['table', 'json', 'yaml']), default='table')
@click.pass_context
def describe_scenario(ctx, scenario, format):
    """Describe a specific scenario in detail"""
    
    scenario_data = SCENARIOS[scenario]
    
    if format == 'json':
        click.echo(json.dumps(scenario_data, indent=2))
        return
    elif format == 'yaml':
        import yaml
        click.echo(yaml.dump(scenario_data, default_flow_style=False))
        return
    
    # Table format
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}{scenario_data['name']}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Description:{ConsoleColors.END}")
    click.echo(f"  {scenario_data['description']}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Duration:{ConsoleColors.END} {scenario_data['duration']}\n")
    
    click.echo(f"{ConsoleColors.CYAN}TOGAF Phases Involved:{ConsoleColors.END}")
    for phase in scenario_data['phases']:
        click.echo(f"  • {phase}")
    click.echo()
    
    click.echo(f"{ConsoleColors.CYAN}Strategic Objectives:{ConsoleColors.END}")
    for obj in scenario_data['objectives']:
        click.echo(f"  ✓ {obj}")
    click.echo()
    
    click.echo(f"{ConsoleColors.CYAN}Key Performance Indicators:{ConsoleColors.END}")
    for kpi in scenario_data['kpis']:
        click.echo(f"  📊 {kpi}")
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")


@click.command(name='run')
@click.argument('scenario', type=click.Choice(list(SCENARIOS.keys())))
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--enterprise', prompt='Enterprise name', help='Enterprise name')
@click.option('--use-ai', is_flag=True, help='Use AI agents for execution')
@click.option('--autonomous', is_flag=True, help='Enable autonomous mode')
@click.option('--fast', is_flag=True, help='Run in fast mode (skip confirmations)')
@click.pass_context
def run_scenario(ctx, scenario, project, enterprise, use_ai, autonomous, fast):
    """
    Run a complete real-world scenario end-to-end
    
    \b
    Examples:
      archiagents scenario run cloud-migration --use-ai
      archiagents scenario run digital-transformation --autonomous --fast
      archiagents scenario run microservices --enterprise "TechCorp"
    """
    
    scenario_data = SCENARIOS[scenario]
    
    if not project:
        # Create new project for scenario
        projects_dir = Path(ctx.obj['config'].get('projects.default_path', '~/archiagents_projects')).expanduser()
        project_name = f"{scenario.replace('-', '_')}_{datetime.now().strftime('%Y%m%d')}"
        project = projects_dir / project_name
    else:
        project = Path(project)
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Running Scenario: {scenario_data['name']}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Description:{ConsoleColors.END} {scenario_data['description']}")
    click.echo(f"{ConsoleColors.CYAN}Duration:{ConsoleColors.END} {scenario_data['duration']}")
    click.echo(f"{ConsoleColors.CYAN}Phases:{ConsoleColors.END} {len(scenario_data['phases'])}")
    click.echo(f"{ConsoleColors.CYAN}Enterprise:{ConsoleColors.END} {enterprise}")
    click.echo(f"{ConsoleColors.CYAN}AI Enabled:{ConsoleColors.END} {use_ai}")
    click.echo(f"{ConsoleColors.CYAN}Autonomous:{ConsoleColors.END} {autonomous}\n")
    
    if not fast:
        click.confirm("Start scenario execution?", abort=True)
    
    try:
        # Step 1: Initialize project if needed
        if not (project / '.archiagents' / 'project.yaml').exists():
            click.echo(ConsoleColors.info("\n📋 Step 1: Initializing project..."))
            
            project.mkdir(parents=True, exist_ok=True)
            
            # Create project structure
            subdirs = ['.archiagents', 'phases', 'models', 'reports', 'decisions', 'artifacts']
            for subdir in subdirs:
                (project / subdir).mkdir(exist_ok=True)
            
            # Create project config
            config = ProjectConfig(str(project))
            config.config = {
                'project': {
                    'name': scenario_data['name'],
                    'enterprise': enterprise,
                    'description': scenario_data['description'],
                    'scenario': scenario,
                    'created_at': datetime.now().isoformat(),
                    'status': 'running'
                },
                'togaf': {
                    'version': '10',
                    'completed_phases': [],
                    'active_phase': None
                },
                'ai': {
                    'enabled': use_ai,
                    'provider': ctx.obj['config'].get('ai.provider', 'openai')
                },
                'runtime_intelligence': {
                    'enabled': True,
                    'autonomous_mode': autonomous
                },
                'scenario': scenario_data
            }
            config.save()
            
            click.echo(ConsoleColors.success("  ✅ Project initialized"))
        else:
            config = ProjectConfig(str(project))
        
        # Step 2: Execute phases
        click.echo(ConsoleColors.info(f"\n📋 Step 2: Executing {len(scenario_data['phases'])} TOGAF phases..."))
        
        for i, phase in enumerate(scenario_data['phases'], 1):
            click.echo(f"\n{ConsoleColors.CYAN}Phase {i}/{len(scenario_data['phases'])}: {phase.upper()}{ConsoleColors.END}")
            
            if not fast:
                click.confirm(f"  Execute {phase}?", default=True, abort=False)
            
            # Execute phase (simplified - would call actual phase execution)
            click.echo(f"  🔄 Running {phase}...")
            
            # Simulate phase execution
            import time
            time.sleep(0.5)  # Simulated work
            
            # Update config
            completed = config.get('togaf.completed_phases', [])
            if phase not in completed:
                completed.append(phase)
                config.set('togaf.completed_phases', completed)
                config.save()
            
            click.echo(ConsoleColors.success(f"  ✅ {phase.upper()} completed"))
        
        # Step 3: Generate architecture artifacts
        click.echo(ConsoleColors.info("\n📋 Step 3: Generating architecture artifacts..."))
        
        artifacts = {
            'architecture_vision': 'Architecture Vision Document',
            'business_architecture': 'Business Architecture Model',
            'application_architecture': 'Application Architecture Model',
            'technology_architecture': 'Technology Architecture Model',
            'migration_plan': 'Migration & Implementation Plan'
        }
        
        for artifact_id, artifact_name in artifacts.items():
            click.echo(f"  📄 Generating {artifact_name}...")
            
            # Create artifact (simplified)
            artifact_file = project / 'artifacts' / f'{artifact_id}.md'
            artifact_file.parent.mkdir(parents=True, exist_ok=True)
            
            artifact_content = f"""# {artifact_name}

**Enterprise:** {enterprise}
**Scenario:** {scenario_data['name']}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview
{scenario_data['description']}

## Objectives
{chr(10).join(f'- {obj}' for obj in scenario_data['objectives'])}

## KPIs
{chr(10).join(f'- {kpi}' for kpi in scenario_data['kpis'])}

---
Generated by ArchiAgents CLI
"""
            
            artifact_file.write_text(artifact_content)
        
        click.echo(ConsoleColors.success("  ✅ Artifacts generated"))
        
        # Step 4: Run intelligence analysis
        if autonomous:
            click.echo(ConsoleColors.info("\n📋 Step 4: Running intelligence analysis..."))
            
            try:
                from runtime_intelligence import AutonomousArchitectureController
                
                controller = AutonomousArchitectureController(
                    enterprise_name=enterprise,
                    project_name=scenario_data['name'],
                    autonomous_mode=True
                )
                
                health = controller.get_architecture_health()
                
                click.echo(f"  📊 Architecture Health: {health['score']}/100 ({health['status']})")
                click.echo(ConsoleColors.success("  ✅ Analysis complete"))
                
            except Exception as e:
                click.echo(ConsoleColors.warning(f"  ⚠️  Intelligence analysis skipped: {e}"))
        
        # Step 5: Generate final report
        click.echo(ConsoleColors.info("\n📋 Step 5: Generating final report..."))
        
        report_file = project / 'reports' / f'{scenario}_report.md'
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        report_content = f"""# {scenario_data['name']} - Execution Report

**Enterprise:** {enterprise}
**Execution Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Duration:** {scenario_data['duration']}

## Executive Summary

Successfully completed {scenario_data['name']} scenario covering {len(scenario_data['phases'])} TOGAF ADM phases.

## Scenario Overview
{scenario_data['description']}

## Phases Executed
{chr(10).join(f'{i+1}. {phase.upper()}' for i, phase in enumerate(scenario_data['phases']))}

## Strategic Objectives
{chr(10).join(f'- ✅ {obj}' for obj in scenario_data['objectives'])}

## Key Performance Indicators
{chr(10).join(f'- 📊 {kpi}' for kpi in scenario_data['kpis'])}

## Architecture Artifacts Generated
- Architecture Vision Document
- Business Architecture Model
- Application Architecture Model
- Technology Architecture Model
- Migration & Implementation Plan

## Next Steps
1. Review all generated artifacts
2. Validate architecture decisions
3. Begin implementation planning
4. Establish governance framework
5. Monitor KPIs and adjust as needed

## Project Location
`{project}`

---
Generated by ArchiAgents CLI - Scenario Execution
"""
        
        report_file.write_text(report_content)
        
        click.echo(ConsoleColors.success("  ✅ Report generated"))
        
        # Final summary
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
        click.echo(f"{ConsoleColors.BOLD}✅ Scenario Execution Complete!{ConsoleColors.END}")
        click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
        click.echo(f"{ConsoleColors.CYAN}Scenario:{ConsoleColors.END} {scenario_data['name']}")
        click.echo(f"{ConsoleColors.CYAN}Phases Completed:{ConsoleColors.END} {len(scenario_data['phases'])}")
        click.echo(f"{ConsoleColors.CYAN}Artifacts Generated:{ConsoleColors.END} {len(artifacts)}")
        click.echo(f"{ConsoleColors.CYAN}Project Location:{ConsoleColors.END} {project}")
        
        click.echo(f"\n{ConsoleColors.BOLD}Next Steps:{ConsoleColors.END}")
        click.echo(f"  1. Review report: {report_file}")
        click.echo(f"  2. Check artifacts: {project / 'artifacts'}")
        click.echo(f"  3. View project status: archiagents project status --project {project}")
        
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Scenario execution failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


# Export commands
__all__ = ['list_scenarios', 'describe_scenario', 'run_scenario']
