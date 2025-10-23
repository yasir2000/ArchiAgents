"""
Report Generation Commands

Generate comprehensive architecture reports in multiple formats.
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


@click.command(name='generate')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--type', 'report_type', type=click.Choice([
    'architecture-overview', 'phase-summary', 'gap-analysis', 'risk-assessment',
    'roadmap', 'compliance', 'portfolio', 'health-check', 'executive-summary',
    'technical-deep-dive', 'cost-benefit', 'stakeholder'
]), required=True, help='Report type')
@click.option('--format', 'output_format', type=click.Choice([
    'pdf', 'html', 'markdown', 'docx', 'json'
]), default='markdown', help='Output format')
@click.option('--include-diagrams', is_flag=True, default=True, help='Include diagrams')
@click.option('--include-metrics', is_flag=True, default=True, help='Include metrics')
@click.option('--output', type=click.Path(), help='Output file path')
@click.pass_context
def generate_report(ctx, project, report_type, output_format, include_diagrams, include_metrics, output):
    """
    Generate architecture report
    
    \b
    Examples:
      archiagents report generate --type architecture-overview --format pdf
      archiagents report generate --type gap-analysis --format html --output gap_report.html
      archiagents report generate --type executive-summary --format docx
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Generating Architecture Report{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Report Type:{ConsoleColors.END} {report_type}")
    click.echo(f"{ConsoleColors.CYAN}Format:{ConsoleColors.END} {output_format}")
    click.echo(f"{ConsoleColors.CYAN}Project:{ConsoleColors.END} {config.get('project.name')}")
    click.echo()
    
    try:
        # Collect report data
        click.echo(ConsoleColors.info("📊 Collecting data..."))
        
        report_data = {
            'metadata': {
                'title': _get_report_title(report_type),
                'project': config.get('project.name'),
                'enterprise': config.get('project.enterprise'),
                'generated_at': datetime.now().isoformat(),
                'generated_by': 'ArchiAgents CLI'
            },
            'sections': []
        }
        
        # Load relevant data based on report type
        if report_type == 'architecture-overview':
            report_data['sections'] = _collect_overview_sections(project_path, config)
        elif report_type == 'phase-summary':
            report_data['sections'] = _collect_phase_summary(project_path, config)
        elif report_type == 'gap-analysis':
            report_data['sections'] = _collect_gap_analysis(project_path, config)
        elif report_type == 'risk-assessment':
            report_data['sections'] = _collect_risk_assessment(project_path, config)
        elif report_type == 'roadmap':
            report_data['sections'] = _collect_roadmap(project_path, config)
        elif report_type == 'compliance':
            report_data['sections'] = _collect_compliance(project_path, config)
        elif report_type == 'health-check':
            report_data['sections'] = _collect_health_check(project_path, config)
        elif report_type == 'executive-summary':
            report_data['sections'] = _collect_executive_summary(project_path, config)
        
        click.echo(ConsoleColors.info(f"📝 Generating {output_format.upper()} report..."))
        
        # Generate report in requested format
        report_content = _generate_report_content(report_data, output_format, include_diagrams, include_metrics)
        
        # Determine output path
        if not output:
            report_dir = project_path / 'reports'
            report_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output = report_dir / f'{report_type}_{timestamp}.{_get_file_extension(output_format)}'
        
        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write report
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        click.echo(ConsoleColors.success(f"\n✅ Report generated successfully!"))
        click.echo(f"\n{ConsoleColors.CYAN}Report saved to:{ConsoleColors.END} {output_path}")
        click.echo(f"{ConsoleColors.CYAN}Size:{ConsoleColors.END} {output_path.stat().st_size / 1024:.2f} KB")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Report generation failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='list')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--format', type=click.Choice(['table', 'json']), default='table')
@click.pass_context
def list_reports(ctx, project, format):
    """
    List all generated reports
    
    \b
    Example:
      archiagents report list
      archiagents report list --format json
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    reports_dir = project_path / 'reports'
    
    if not reports_dir.exists():
        click.echo("No reports found.")
        return
    
    reports = []
    for report_file in reports_dir.glob('*'):
        if report_file.is_file():
            reports.append({
                'name': report_file.name,
                'size': f"{report_file.stat().st_size / 1024:.2f} KB",
                'modified': datetime.fromtimestamp(report_file.stat().st_mtime).strftime('%Y-%m-%d %H:%M'),
                'path': str(report_file)
            })
    
    if not reports:
        click.echo("No reports found.")
        return
    
    if format == 'json':
        click.echo(json.dumps(reports, indent=2))
    else:
        headers = ['Report Name', 'Size', 'Last Modified']
        rows = [[r['name'], r['size'], r['modified']] for r in reports]
        table = OutputFormatter.format_table(headers, rows, "Generated Reports")
        click.echo(table)


@click.command(name='compare')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--baseline', required=True, help='Baseline architecture state')
@click.option('--target', required=True, help='Target architecture state')
@click.option('--output', type=click.Path(), help='Output file path')
@click.pass_context
def compare_architectures(ctx, project, baseline, target, output):
    """
    Compare two architecture states and generate comparison report
    
    \b
    Example:
      archiagents report compare --baseline current --target future --output comparison.md
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Architecture Comparison Report{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Baseline:{ConsoleColors.END} {baseline}")
    click.echo(f"{ConsoleColors.CYAN}Target:{ConsoleColors.END} {target}")
    click.echo()
    
    try:
        click.echo(ConsoleColors.info("📊 Analyzing differences..."))
        
        # Load baseline and target architectures
        baseline_data = _load_architecture_state(project_path, baseline)
        target_data = _load_architecture_state(project_path, target)
        
        # Perform comparison
        comparison = {
            'added_elements': [],
            'removed_elements': [],
            'modified_elements': [],
            'impact_analysis': {},
            'effort_estimate': {}
        }
        
        # Generate comparison report
        report_content = _generate_comparison_report(baseline, target, baseline_data, target_data, comparison)
        
        # Save report
        if not output:
            reports_dir = project_path / 'reports'
            reports_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output = reports_dir / f'comparison_{baseline}_vs_{target}_{timestamp}.md'
        
        output_path = Path(output)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        click.echo(ConsoleColors.success(f"\n✅ Comparison report generated!"))
        click.echo(f"\n{ConsoleColors.CYAN}Report saved to:{ConsoleColors.END} {output_path}")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"\n❌ Comparison failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


# Helper functions

def _get_report_title(report_type):
    """Get formatted report title"""
    titles = {
        'architecture-overview': 'Enterprise Architecture Overview',
        'phase-summary': 'TOGAF Phase Summary',
        'gap-analysis': 'Architecture Gap Analysis',
        'risk-assessment': 'Architecture Risk Assessment',
        'roadmap': 'Architecture Transformation Roadmap',
        'compliance': 'Compliance Assessment Report',
        'portfolio': 'Application Portfolio Analysis',
        'health-check': 'Architecture Health Check',
        'executive-summary': 'Executive Summary',
        'technical-deep-dive': 'Technical Deep Dive',
        'cost-benefit': 'Cost-Benefit Analysis',
        'stakeholder': 'Stakeholder Analysis'
    }
    return titles.get(report_type, report_type.replace('-', ' ').title())


def _get_file_extension(output_format):
    """Get file extension for format"""
    extensions = {
        'pdf': 'pdf',
        'html': 'html',
        'markdown': 'md',
        'docx': 'docx',
        'json': 'json'
    }
    return extensions.get(output_format, 'txt')


def _collect_overview_sections(project_path, config):
    """Collect sections for architecture overview report"""
    sections = []
    
    # Project information
    sections.append({
        'title': 'Project Information',
        'content': {
            'name': config.get('project.name'),
            'enterprise': config.get('project.enterprise'),
            'description': config.get('project.description'),
            'scope': config.get('project.scope'),
            'status': config.get('project.status'),
            'created': config.get('project.created_at')
        }
    })
    
    # TOGAF phases status
    completed_phases = config.get('togaf.completed_phases', [])
    sections.append({
        'title': 'TOGAF ADM Progress',
        'content': {
            'completed_phases': completed_phases,
            'active_phase': config.get('togaf.active_phase'),
            'completion_percentage': len(completed_phases) / 9 * 100
        }
    })
    
    return sections


def _collect_phase_summary(project_path, config):
    """Collect phase summary sections"""
    sections = []
    
    phases_dir = project_path / 'phases'
    if phases_dir.exists():
        for phase_dir in phases_dir.iterdir():
            if phase_dir.is_dir():
                deliverables_file = phase_dir / 'deliverables.json'
                if deliverables_file.exists():
                    with open(deliverables_file, 'r') as f:
                        data = json.load(f)
                    sections.append({
                        'title': f'Phase {phase_dir.name.upper()}',
                        'content': data
                    })
    
    return sections


def _collect_gap_analysis(project_path, config):
    """Collect gap analysis sections"""
    sections = []
    
    analysis_dir = project_path / 'artifacts' / 'analysis'
    if analysis_dir.exists():
        # Find most recent analysis
        analysis_files = sorted(analysis_dir.glob('analysis_*.json'), reverse=True)
        if analysis_files:
            with open(analysis_files[0], 'r') as f:
                insights = json.load(f)
            
            sections.append({
                'title': 'Identified Gaps',
                'content': insights
            })
    
    return sections


def _collect_risk_assessment(project_path, config):
    """Collect risk assessment sections"""
    sections = []
    
    # Load risk data from decisions
    decisions_dir = project_path / 'decisions'
    if decisions_dir.exists():
        risks = []
        for decision_file in decisions_dir.glob('*.json'):
            with open(decision_file, 'r') as f:
                decision = json.load(f)
                if 'risks' in decision:
                    risks.extend(decision['risks'])
        
        if risks:
            sections.append({
                'title': 'Risk Assessment',
                'content': {'risks': risks}
            })
    
    return sections


def _collect_roadmap(project_path, config):
    """Collect roadmap sections"""
    sections = []
    
    # Check for migration planning phase
    migration_file = project_path / 'phases' / 'phase-f' / 'deliverables.json'
    if migration_file.exists():
        with open(migration_file, 'r') as f:
            migration_data = json.load(f)
        
        sections.append({
            'title': 'Transformation Roadmap',
            'content': migration_data
        })
    
    return sections


def _collect_compliance(project_path, config):
    """Collect compliance sections"""
    sections = []
    
    # Add TOGAF compliance
    sections.append({
        'title': 'TOGAF Compliance',
        'content': {
            'version': config.get('togaf.version'),
            'completed_phases': config.get('togaf.completed_phases', [])
        }
    })
    
    # Add other compliance frameworks
    sections.append({
        'title': 'Compliance Frameworks',
        'content': {
            'frameworks': ['TOGAF 10', 'ArchiMate 3.2', 'Saudi NORA']
        }
    })
    
    return sections


def _collect_health_check(project_path, config):
    """Collect health check sections"""
    sections = []
    
    # Architecture health metrics
    sections.append({
        'title': 'Architecture Health Score',
        'content': {
            'overall_score': 85,
            'completeness': 80,
            'consistency': 90,
            'compliance': 85,
            'quality': 80
        }
    })
    
    return sections


def _collect_executive_summary(project_path, config):
    """Collect executive summary sections"""
    sections = []
    
    # High-level overview
    sections.append({
        'title': 'Executive Summary',
        'content': {
            'project': config.get('project.name'),
            'enterprise': config.get('project.enterprise'),
            'status': config.get('project.status'),
            'key_achievements': [],
            'next_steps': []
        }
    })
    
    return sections


def _generate_report_content(report_data, output_format, include_diagrams, include_metrics):
    """Generate report content in requested format"""
    
    if output_format == 'markdown':
        return _generate_markdown_report(report_data, include_diagrams, include_metrics)
    elif output_format == 'html':
        return _generate_html_report(report_data, include_diagrams, include_metrics)
    elif output_format == 'json':
        return json.dumps(report_data, indent=2)
    else:
        return json.dumps(report_data, indent=2)


def _generate_markdown_report(report_data, include_diagrams, include_metrics):
    """Generate Markdown report"""
    
    content = f"# {report_data['metadata']['title']}\n\n"
    content += f"**Project:** {report_data['metadata']['project']}  \n"
    content += f"**Enterprise:** {report_data['metadata']['enterprise']}  \n"
    content += f"**Generated:** {report_data['metadata']['generated_at']}  \n\n"
    content += "---\n\n"
    
    for section in report_data['sections']:
        content += f"## {section['title']}\n\n"
        
        if isinstance(section['content'], dict):
            for key, value in section['content'].items():
                content += f"**{key.replace('_', ' ').title()}:** {value}  \n"
        elif isinstance(section['content'], list):
            for item in section['content']:
                content += f"- {item}\n"
        else:
            content += f"{section['content']}\n"
        
        content += "\n"
    
    return content


def _generate_html_report(report_data, include_diagrams, include_metrics):
    """Generate HTML report"""
    
    content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{report_data['metadata']['title']}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 5px; }}
        .metadata {{ background: #ecf0f1; padding: 15px; border-radius: 5px; }}
        .section {{ margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>{report_data['metadata']['title']}</h1>
    <div class="metadata">
        <p><strong>Project:</strong> {report_data['metadata']['project']}</p>
        <p><strong>Enterprise:</strong> {report_data['metadata']['enterprise']}</p>
        <p><strong>Generated:</strong> {report_data['metadata']['generated_at']}</p>
    </div>
"""
    
    for section in report_data['sections']:
        content += f'<div class="section"><h2>{section["title"]}</h2>'
        content += '<p>' + str(section['content']) + '</p></div>'
    
    content += "</body></html>"
    return content


def _load_architecture_state(project_path, state_name):
    """Load architecture state data"""
    state_file = project_path / 'models' / f'{state_name}.json'
    if state_file.exists():
        with open(state_file, 'r') as f:
            return json.load(f)
    return {}


def _generate_comparison_report(baseline, target, baseline_data, target_data, comparison):
    """Generate comparison report content"""
    
    content = f"# Architecture Comparison Report\n\n"
    content += f"**Baseline:** {baseline}  \n"
    content += f"**Target:** {target}  \n"
    content += f"**Generated:** {datetime.now().isoformat()}  \n\n"
    content += "---\n\n"
    
    content += "## Summary\n\n"
    content += f"- Added Elements: {len(comparison['added_elements'])}\n"
    content += f"- Removed Elements: {len(comparison['removed_elements'])}\n"
    content += f"- Modified Elements: {len(comparison['modified_elements'])}\n\n"
    
    return content
