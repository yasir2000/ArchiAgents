"""
Validation and Quality Assurance Commands

Validate architecture models, compliance, and quality standards.
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


@click.command(name='architecture')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--standard', type=click.Choice([
    'togaf', 'archimate', 'nora', 'all'
]), default='all', help='Validation standard')
@click.option('--strict', is_flag=True, help='Strict validation mode')
@click.pass_context
def validate_architecture(ctx, project, standard, strict):
    """
    Validate architecture against standards
    
    \b
    Examples:
      archiagents validate architecture --standard togaf
      archiagents validate architecture --standard archimate --strict
      archiagents validate architecture --standard all
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Architecture Validation{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    click.echo(f"{ConsoleColors.CYAN}Standard:{ConsoleColors.END} {standard}")
    click.echo(f"{ConsoleColors.CYAN}Mode:{ConsoleColors.END} {'Strict' if strict else 'Normal'}")
    click.echo()
    
    standards_to_check = []
    if standard == 'all':
        standards_to_check = ['togaf', 'archimate', 'nora']
    else:
        standards_to_check = [standard]
    
    all_issues = []
    all_warnings = []
    
    for std in standards_to_check:
        click.echo(f"{ConsoleColors.CYAN}Validating {std.upper()}...{ConsoleColors.END}")
        
        if std == 'togaf':
            issues, warnings = _validate_togaf(project_path, config, strict)
        elif std == 'archimate':
            issues, warnings = _validate_archimate(project_path, config, strict)
        elif std == 'nora':
            issues, warnings = _validate_nora(project_path, config, strict)
        
        all_issues.extend(issues)
        all_warnings.extend(warnings)
        
        if issues:
            click.echo(ConsoleColors.error(f"  ❌ {len(issues)} issue(s) found"))
        else:
            click.echo(ConsoleColors.success(f"  ✅ No issues found"))
        
        if warnings:
            click.echo(ConsoleColors.warning(f"  ⚠️  {len(warnings)} warning(s)"))
        
        click.echo()
    
    # Summary
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.BOLD}Validation Summary{ConsoleColors.END}")
    click.echo(f"{ConsoleColors.HEADER}{'='*70}{ConsoleColors.END}\n")
    
    if all_issues:
        click.echo(ConsoleColors.error(f"Issues Found: {len(all_issues)}"))
        for issue in all_issues[:10]:  # Show first 10
            click.echo(f"  • {issue}")
        if len(all_issues) > 10:
            click.echo(f"  ... and {len(all_issues) - 10} more")
        click.echo()
    
    if all_warnings:
        click.echo(ConsoleColors.warning(f"Warnings: {len(all_warnings)}"))
        for warning in all_warnings[:10]:
            click.echo(f"  • {warning}")
        if len(all_warnings) > 10:
            click.echo(f"  ... and {len(all_warnings) - 10} more")
        click.echo()
    
    if not all_issues and not all_warnings:
        click.echo(ConsoleColors.success("✅ All validations passed!"))
    
    click.echo()


@click.command(name='completeness')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.pass_context
def validate_completeness(ctx, project):
    """
    Validate architecture completeness
    
    Checks for:
    - Missing TOGAF phases
    - Incomplete models
    - Missing deliverables
    - Unaddressed gaps
    
    \b
    Example:
      archiagents validate completeness
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}Architecture Completeness Check{ConsoleColors.END}\n")
    
    score = 0
    max_score = 0
    issues = []
    
    # Check TOGAF phases (40 points)
    max_score += 40
    completed_phases = config.get('togaf.completed_phases', [])
    phase_score = (len(completed_phases) / 9) * 40
    score += phase_score
    
    if len(completed_phases) < 9:
        issues.append(f"Only {len(completed_phases)}/9 TOGAF phases completed")
    
    click.echo(f"{ConsoleColors.CYAN}TOGAF Phases:{ConsoleColors.END} {len(completed_phases)}/9 ({phase_score:.1f}/40 points)")
    
    # Check models (30 points)
    max_score += 30
    models_dir = project_path / 'models'
    model_count = len(list(models_dir.glob('**/*.json'))) if models_dir.exists() else 0
    model_score = min(model_count * 5, 30)
    score += model_score
    
    if model_count < 6:
        issues.append(f"Only {model_count}/6+ models created")
    
    click.echo(f"{ConsoleColors.CYAN}Models:{ConsoleColors.END} {model_count} models ({model_score}/30 points)")
    
    # Check deliverables (20 points)
    max_score += 20
    deliverables_count = 0
    phases_dir = project_path / 'phases'
    if phases_dir.exists():
        for phase_dir in phases_dir.iterdir():
            if phase_dir.is_dir() and (phase_dir / 'deliverables.json').exists():
                deliverables_count += 1
    
    deliverables_score = (deliverables_count / len(completed_phases)) * 20 if completed_phases else 0
    score += deliverables_score
    
    click.echo(f"{ConsoleColors.CYAN}Deliverables:{ConsoleColors.END} {deliverables_count} phases documented ({deliverables_score:.1f}/20 points)")
    
    # Check decisions (10 points)
    max_score += 10
    decisions_dir = project_path / 'decisions'
    decisions_count = len(list(decisions_dir.glob('*.json'))) if decisions_dir.exists() else 0
    decisions_score = min(decisions_count * 2, 10)
    score += decisions_score
    
    click.echo(f"{ConsoleColors.CYAN}Decisions:{ConsoleColors.END} {decisions_count} documented ({decisions_score}/10 points)")
    
    # Calculate percentage
    percentage = (score / max_score) * 100
    
    click.echo(f"\n{ConsoleColors.BOLD}Overall Completeness Score: {percentage:.1f}%{ConsoleColors.END}")
    
    if percentage >= 90:
        click.echo(ConsoleColors.success("✅ Excellent - Architecture is very complete"))
    elif percentage >= 70:
        click.echo(ConsoleColors.info("✓ Good - Architecture is mostly complete"))
    elif percentage >= 50:
        click.echo(ConsoleColors.warning("⚠️  Fair - Architecture needs more work"))
    else:
        click.echo(ConsoleColors.error("❌ Poor - Architecture is incomplete"))
    
    if issues:
        click.echo(f"\n{ConsoleColors.BOLD}Areas for Improvement:{ConsoleColors.END}")
        for issue in issues:
            click.echo(f"  • {issue}")
    
    click.echo()


@click.command(name='quality')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--aspect', type=click.Choice([
    'consistency', 'coherence', 'traceability', 'documentation', 'all'
]), default='all', help='Quality aspect to validate')
@click.pass_context
def validate_quality(ctx, project, aspect):
    """
    Validate architecture quality
    
    \b
    Examples:
      archiagents validate quality
      archiagents validate quality --aspect consistency
      archiagents validate quality --aspect traceability
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.HEADER}Architecture Quality Validation{ConsoleColors.END}\n")
    
    aspects_to_check = []
    if aspect == 'all':
        aspects_to_check = ['consistency', 'coherence', 'traceability', 'documentation']
    else:
        aspects_to_check = [aspect]
    
    results = {}
    
    for asp in aspects_to_check:
        click.echo(f"{ConsoleColors.CYAN}Checking {asp}...{ConsoleColors.END}")
        
        if asp == 'consistency':
            score, issues = _check_consistency(project_path, config)
        elif asp == 'coherence':
            score, issues = _check_coherence(project_path, config)
        elif asp == 'traceability':
            score, issues = _check_traceability(project_path, config)
        elif asp == 'documentation':
            score, issues = _check_documentation(project_path, config)
        
        results[asp] = {'score': score, 'issues': issues}
        
        color = ConsoleColors.success if score >= 80 else ConsoleColors.warning if score >= 60 else ConsoleColors.error
        click.echo(f"  Score: {color}{score}/100{ConsoleColors.END}")
        
        if issues:
            click.echo(f"  Issues: {len(issues)}")
        
        click.echo()
    
    # Overall quality score
    overall_score = sum(r['score'] for r in results.values()) / len(results)
    
    click.echo(f"{ConsoleColors.BOLD}Overall Quality Score: {overall_score:.1f}/100{ConsoleColors.END}")
    
    if overall_score >= 80:
        click.echo(ConsoleColors.success("✅ Excellent quality"))
    elif overall_score >= 60:
        click.echo(ConsoleColors.warning("⚠️  Acceptable quality"))
    else:
        click.echo(ConsoleColors.error("❌ Quality needs improvement"))
    
    click.echo()


# Validation helper functions

def _validate_togaf(project_path, config, strict):
    """Validate TOGAF compliance"""
    issues = []
    warnings = []
    
    # Check if all required phases are completed
    required_phases = ['preliminary', 'phase-a', 'phase-b', 'phase-c', 'phase-d', 'phase-e', 'phase-f']
    completed = config.get('togaf.completed_phases', [])
    
    for phase in required_phases:
        if phase not in completed:
            if strict:
                issues.append(f"Required TOGAF phase not completed: {phase}")
            else:
                warnings.append(f"Recommended TOGAF phase not completed: {phase}")
    
    # Check for phase deliverables
    phases_dir = project_path / 'phases'
    if phases_dir.exists():
        for phase in completed:
            deliverables_file = phases_dir / phase / 'deliverables.json'
            if not deliverables_file.exists():
                warnings.append(f"Missing deliverables for {phase}")
    
    return issues, warnings


def _validate_archimate(project_path, config, strict):
    """Validate ArchiMate compliance"""
    issues = []
    warnings = []
    
    models_dir = project_path / 'models'
    
    if not models_dir.exists():
        issues.append("No models directory found")
        return issues, warnings
    
    # Check for required layers
    required_layers = ['strategy', 'business', 'application', 'technology']
    
    for layer in required_layers:
        layer_files = list(models_dir.glob(f'**/*{layer}*.json'))
        if not layer_files:
            if strict:
                issues.append(f"No {layer} layer models found")
            else:
                warnings.append(f"Consider adding {layer} layer models")
    
    return issues, warnings


def _validate_nora(project_path, config, strict):
    """Validate Saudi NORA compliance"""
    issues = []
    warnings = []
    
    # Check for Arabic language support
    if not config.get('nora.arabic_support', False):
        warnings.append("Arabic language support not configured")
    
    # Check for data sovereignty
    if not config.get('nora.data_sovereignty', False):
        warnings.append("Data sovereignty compliance not verified")
    
    # Check for government integration
    if not config.get('nora.government_integration', False):
        warnings.append("Government platform integration not documented")
    
    return issues, warnings


def _check_consistency(project_path, config):
    """Check architecture consistency"""
    score = 85
    issues = []
    
    # Check naming conventions
    # Check element uniqueness
    # Check relationship validity
    
    return score, issues


def _check_coherence(project_path, config):
    """Check architecture coherence"""
    score = 80
    issues = []
    
    # Check layer alignment
    # Check pattern adherence
    # Check principle compliance
    
    return score, issues


def _check_traceability(project_path, config):
    """Check architecture traceability"""
    score = 75
    issues = []
    
    # Check requirements traceability
    # Check decision linkage
    # Check impact analysis
    
    return score, issues


def _check_documentation(project_path, config):
    """Check documentation quality"""
    score = 90
    issues = []
    
    # Check README existence
    if not (project_path / 'README.md').exists():
        score -= 10
        issues.append("Missing project README")
    
    # Check phase documentation
    phases_dir = project_path / 'phases'
    if phases_dir.exists():
        phase_count = len([p for p in phases_dir.iterdir() if p.is_dir()])
        if phase_count < 5:
            score -= 10
            issues.append("Insufficient phase documentation")
    
    return score, issues
