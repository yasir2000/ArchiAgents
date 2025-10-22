"""
Runtime Intelligence Layer commands
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


@click.command(name='analyze')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--autonomous', is_flag=True, help='Enable autonomous mode')
@click.option('--format', type=click.Choice(['table', 'json', 'tree']), default='table')
@click.pass_context
def analyze_architecture(ctx, project, autonomous, format):
    """
    Analyze architecture using Runtime Intelligence Layer
    
    Performs comprehensive analysis including:
    - Gap analysis (missing layers, orphaned elements)
    - Dependency analysis (coupling, circular dependencies)
    - Pattern recognition (layered architecture, microservices)
    - Optimization detection (redundancy)
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Architecture Analysis - Runtime Intelligence{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    try:
        from runtime_intelligence import AutonomousArchitectureController
        
        controller = AutonomousArchitectureController(
            enterprise_name=config.get('project.enterprise'),
            project_name=config.get('project.name'),
            autonomous_mode=autonomous
        )
        
        click.echo(ConsoleColors.info("🔍 Analyzing architecture..."))
        
        # Load existing ArchiMate model if available
        model_file = project_path / 'models' / 'archimate_model.json'
        if model_file.exists():
            with open(model_file, 'r') as f:
                model_data = json.load(f)
            
            # Load elements and relationships
            from runtime_intelligence import ArchiMateElement, ArchiMateRelationship
            
            for element in model_data.get('elements', []):
                controller.archimate_analyzer.add_element(ArchiMateElement(**element))
            
            for rel in model_data.get('relationships', []):
                controller.archimate_analyzer.add_relationship(ArchiMateRelationship(**rel))
        
        # Perform analysis
        insights = controller.analyze_architecture()
        
        click.echo(ConsoleColors.success(f"\n✅ Analysis complete! Found {len(insights)} insights\n"))
        
        # Group insights by severity
        by_severity = {'critical': [], 'high': [], 'medium': [], 'low': []}
        for insight in insights:
            by_severity[insight.severity].append(insight)
        
        # Display insights
        for severity in ['critical', 'high', 'medium', 'low']:
            insights_list = by_severity[severity]
            if not insights_list:
                continue
            
            severity_color = {
                'critical': ConsoleColors.RED,
                'high': ConsoleColors.YELLOW,
                'medium': ConsoleColors.CYAN,
                'low': ConsoleColors.BLUE
            }[severity]
            
            click.echo(f"{severity_color}{severity.upper()} ({len(insights_list)}){ConsoleColors.END}")
            
            for insight in insights_list:
                click.echo(f"  • {insight.type}: {insight.description}")
                if insight.recommendations:
                    for rec in insight.recommendations[:2]:
                        click.echo(f"    → {rec}")
                click.echo()
        
        # Save analysis results
        analysis_dir = project_path / 'artifacts' / 'analysis'
        analysis_dir.mkdir(parents=True, exist_ok=True)
        
        analysis_file = analysis_dir / f'analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        with open(analysis_file, 'w') as f:
            json.dump([{
                'type': i.type,
                'severity': i.severity,
                'description': i.description,
                'affected_elements': i.affected_elements,
                'affected_layers': i.affected_layers,
                'recommendations': i.recommendations,
                'estimated_impact': i.estimated_impact,
                'estimated_effort': i.estimated_effort,
                'confidence': i.confidence
            } for i in insights], f, indent=2)
        
        click.echo(f"{ConsoleColors.CYAN}Analysis saved to:{ConsoleColors.END} {analysis_file}")
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Analysis failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='decide')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--title', prompt='Decision title', help='Decision title')
@click.option('--type', 'decision_type', 
              type=click.Choice(['strategic', 'tactical', 'technical', 'organizational', 
                                'governance', 'risk', 'compliance', 'optimization']),
              default='strategic', help='Decision type')
@click.option('--priority', type=click.Choice(['critical', 'high', 'medium', 'low']), 
              default='high', help='Decision priority')
@click.option('--autonomous', is_flag=True, help='Enable autonomous decision-making')
@click.pass_context
def make_decision(ctx, project, title, decision_type, priority, autonomous):
    """
    Make an architecture decision using AI-driven decision engine
    
    \b
    Example:
      archiagents intelligence decide \\
        --title "Cloud Migration Strategy" \\
        --type strategic \\
        --priority high \\
        --autonomous
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Architecture Decision - Runtime Intelligence{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Decision:{ConsoleColors.END} {title}")
    click.echo(f"{ConsoleColors.CYAN}Type:{ConsoleColors.END} {decision_type}")
    click.echo(f"{ConsoleColors.CYAN}Priority:{ConsoleColors.END} {priority}")
    click.echo(f"{ConsoleColors.CYAN}Autonomous:{ConsoleColors.END} {autonomous}\n")
    
    # Collect decision options
    click.echo(ConsoleColors.info("📋 Please provide decision options (minimum 2)"))
    click.echo("Enter option details. Press Ctrl+C when done.\n")
    
    options = []
    option_num = 1
    
    try:
        while True:
            click.echo(f"{ConsoleColors.BOLD}Option {option_num}:{ConsoleColors.END}")
            
            name = click.prompt("  Name", default=f"Option {option_num}")
            description = click.prompt("  Description")
            feasibility = click.prompt("  Feasibility (0-1)", type=float, default=0.8)
            cost = click.prompt("  Cost ($)", type=int, default=0)
            time_days = click.prompt("  Time (days)", type=int, default=90)
            complexity = click.prompt("  Complexity (0-1)", type=float, default=0.5)
            risk = click.prompt("  Risk (0-1)", type=float, default=0.3)
            
            options.append({
                "name": name,
                "description": description,
                "feasibility": feasibility,
                "cost": cost,
                "time_days": time_days,
                "complexity": complexity,
                "risk": risk
            })
            
            option_num += 1
            
            if len(options) >= 2:
                if not click.confirm("\nAdd another option?", default=False):
                    break
            
            click.echo()
            
    except (KeyboardInterrupt, click.Abort):
        if len(options) < 2:
            click.echo(ConsoleColors.error("\n❌ At least 2 options required"), err=True)
            raise click.Abort()
    
    try:
        from runtime_intelligence import AutonomousArchitectureController
        
        controller = AutonomousArchitectureController(
            enterprise_name=config.get('project.enterprise'),
            project_name=config.get('project.name'),
            autonomous_mode=autonomous
        )
        
        click.echo(f"\n{ConsoleColors.info('🤖 Making decision...')}")
        
        decision = controller.make_autonomous_decision(
            decision_title=title,
            decision_context={
                "scope": title,
                "type": decision_type,
                "priority": priority,
                "phase": config.get('togaf.active_phase', 'phase-a')
            },
            options=options
        )
        
        click.echo(ConsoleColors.success(f"\n✅ Decision made!\n"))
        
        # Display decision
        click.echo(f"{ConsoleColors.BOLD}Recommended:{ConsoleColors.END} {decision['recommended']}")
        click.echo(f"{ConsoleColors.BOLD}Confidence:{ConsoleColors.END} {decision['confidence']}")
        click.echo(f"{ConsoleColors.BOLD}Cost:{ConsoleColors.END} ${decision.get('cost', 0):,}")
        click.echo(f"{ConsoleColors.BOLD}Timeline:{ConsoleColors.END} {decision.get('timeline', 0)} days")
        
        if decision.get('reasoning'):
            click.echo(f"\n{ConsoleColors.CYAN}Reasoning:{ConsoleColors.END}")
            reasoning_lines = decision['reasoning'].split('\n')
            for line in reasoning_lines[:10]:  # Show first 10 lines
                click.echo(f"  {line}")
            if len(reasoning_lines) > 10:
                click.echo(f"  ... ({len(reasoning_lines) - 10} more lines)")
        
        # Save decision
        decisions_dir = project_path / 'decisions'
        decisions_dir.mkdir(parents=True, exist_ok=True)
        
        decision_file = decisions_dir / f'{title.replace(" ", "_").lower()}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        with open(decision_file, 'w') as f:
            json.dump(decision, f, indent=2, default=str)
        
        click.echo(f"\n{ConsoleColors.CYAN}Decision saved to:{ConsoleColors.END} {decision_file}")
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Decision failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='health')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--format', type=click.Choice(['table', 'json']), default='table')
@click.pass_context
def check_health(ctx, project, format):
    """
    Check architecture health score
    
    Health score is calculated based on insights severity:
    - Critical issues: -20 points each
    - High issues: -10 points each
    - Medium issues: -5 points each
    
    Scores:
    - 80-100: Healthy
    - 60-79: Fair
    - 40-59: At Risk
    - <40: Critical
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    try:
        from runtime_intelligence import AutonomousArchitectureController
        
        controller = AutonomousArchitectureController(
            enterprise_name=config.get('project.enterprise'),
            project_name=config.get('project.name'),
            autonomous_mode=False
        )
        
        # Load existing model and perform analysis
        model_file = project_path / 'models' / 'archimate_model.json'
        if model_file.exists():
            with open(model_file, 'r') as f:
                model_data = json.load(f)
            
            from runtime_intelligence import ArchiMateElement, ArchiMateRelationship
            
            for element in model_data.get('elements', []):
                controller.archimate_analyzer.add_element(ArchiMateElement(**element))
            
            for rel in model_data.get('relationships', []):
                controller.archimate_analyzer.add_relationship(ArchiMateRelationship(**rel))
            
            # Analyze to get insights
            controller.analyze_architecture()
        
        health = controller.get_architecture_health()
        
        if format == 'json':
            click.echo(json.dumps(health, indent=2))
            return
        
        # Display health
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
        click.echo(f"{ConsoleColors.BOLD}Architecture Health Check{ConsoleColors.END}")
        click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
        # Health score with color
        score = health['score']
        status = health['status'].upper()
        
        if score >= 80:
            score_display = ConsoleColors.success(f"{score}/100")
            status_display = ConsoleColors.success(status)
        elif score >= 60:
            score_display = ConsoleColors.warning(f"{score}/100")
            status_display = ConsoleColors.warning(status)
        else:
            score_display = ConsoleColors.error(f"{score}/100")
            status_display = ConsoleColors.error(status)
        
        click.echo(f"{ConsoleColors.BOLD}Health Score:{ConsoleColors.END} {score_display}")
        click.echo(f"{ConsoleColors.BOLD}Status:{ConsoleColors.END} {status_display}\n")
        
        # Issue counts
        click.echo(f"{ConsoleColors.BOLD}Issues:{ConsoleColors.END}")
        click.echo(f"  Critical: {ConsoleColors.error(str(health['critical_count']))}")
        click.echo(f"  High: {ConsoleColors.warning(str(health['high_count']))}")
        click.echo(f"  Medium: {ConsoleColors.info(str(health['medium_count']))}\n")
        
        # Recommendations
        if health.get('recommendations'):
            click.echo(f"{ConsoleColors.BOLD}Recommendations:{ConsoleColors.END}")
            for rec in health['recommendations']:
                click.echo(f"  • {rec}")
        
        click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Health check failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='report')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--output', type=click.Path(), help='Output file')
@click.pass_context
def generate_report(ctx, project, output):
    """Generate comprehensive intelligence report"""
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    try:
        from runtime_intelligence import AutonomousArchitectureController
        
        controller = AutonomousArchitectureController(
            enterprise_name=config.get('project.enterprise'),
            project_name=config.get('project.name'),
            autonomous_mode=False
        )
        
        # Load model and perform analysis
        model_file = project_path / 'models' / 'archimate_model.json'
        if model_file.exists():
            with open(model_file, 'r') as f:
                model_data = json.load(f)
            
            from runtime_intelligence import ArchiMateElement, ArchiMateRelationship
            
            for element in model_data.get('elements', []):
                controller.archimate_analyzer.add_element(ArchiMateElement(**element))
            
            for rel in model_data.get('relationships', []):
                controller.archimate_analyzer.add_relationship(ArchiMateRelationship(**rel))
            
            controller.analyze_architecture()
        
        # Generate report
        report = controller.generate_report()
        
        click.echo(report)
        
        if output:
            output_path = Path(output)
            output_path.write_text(report)
            click.echo(f"\n{ConsoleColors.CYAN}Report saved to:{ConsoleColors.END} {output_path}")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Report generation failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


# Export commands
__all__ = ['analyze_architecture', 'make_decision', 'check_health', 'generate_report']
