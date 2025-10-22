"""
Model Management CLI Commands

Commands for generating and managing architecture models with multiple
output formats and AI-powered generation.
"""

import click
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from model_generation.engine import (
    ModelGenerationEngine,
    ModelType,
    ArchitectureLayer
)
from model_generation.formats import (
    TextExporter,
    MermaidExporter,
    KrokiExporter,
    ArchiExporter,
    GoJSExporter,
    EnterpriseArchitectExporter
)
from model_generation.ai_modeler import AIModelingAgent
from cli.utils.formatters import OutputFormatter, ConsoleColors


@click.group()
def model():
    """ArchiMate and UML model generation and management"""
    pass


@model.command()
@click.option('--project', type=click.Path(exists=True), default='.', 
              help='Project directory')
@click.option('--type', 'model_type', 
              type=click.Choice([
                  'archimate-strategy', 'archimate-business', 'archimate-application',
                  'archimate-technology', 'archimate-physical', 'archimate-implementation',
                  'archimate-multi-layer',
                  'bpmn-process',
                  'uml-class', 'uml-sequence', 'uml-use-case', 'uml-activity',
                  'uml-state', 'uml-component', 'uml-deployment'
              ]),
              required=True,
              help='Type of model to generate')
@click.option('--name', required=True, help='Model name')
@click.option('--format', 'output_format',
              type=click.Choice(['text', 'mermaid', 'kroki', 'archi', 'gojs', 'ea']),
              multiple=True,
              default=['text', 'mermaid'],
              help='Output formats (can specify multiple)')
@click.option('--use-ai/--no-ai', default=True, help='Use AI for intelligent generation')
@click.option('--output-dir', type=click.Path(), help='Custom output directory')
def generate(project, model_type, name, output_format, use_ai, output_dir):
    """
    Generate architecture model with multiple output formats.
    
    Examples:
    
        # Generate ArchiMate business layer model
        python archiagents.py model generate --type archimate-business --name "Business Architecture"
        
        # Generate UML class diagram with multiple formats
        python archiagents.py model generate --type uml-class --name "Domain Model" --format mermaid --format gojs
        
        # Generate BPMN process
        python archiagents.py model generate --type bpmn-process --name "Order Processing"
    """
    click.echo(ConsoleColors.header(f"\n{'='*60}"))
    click.echo(ConsoleColors.header(f"  ArchiAgents Model Generator"))
    click.echo(ConsoleColors.header(f"{'='*60}\n"))
    
    # Initialize engine
    engine = ModelGenerationEngine()
    ai_agent = AIModelingAgent() if use_ai else None
    
    # Load context from project
    context = _load_project_context(project)
    
    # Generate model based on type
    click.echo(f"Generating {model_type} model: {name}...")
    
    model = None
    
    if model_type.startswith('archimate'):
        if model_type == 'archimate-multi-layer':
            # Generate multi-layer model
            layers = [
                ArchitectureLayer.STRATEGY,
                ArchitectureLayer.BUSINESS,
                ArchitectureLayer.APPLICATION,
                ArchitectureLayer.TECHNOLOGY
            ]
            model = engine.generate_multi_layer_model(layers, context, use_ai)
        else:
            # Single layer
            layer_map = {
                'archimate-strategy': ArchitectureLayer.STRATEGY,
                'archimate-business': ArchitectureLayer.BUSINESS,
                'archimate-application': ArchitectureLayer.APPLICATION,
                'archimate-technology': ArchitectureLayer.TECHNOLOGY,
                'archimate-physical': ArchitectureLayer.PHYSICAL,
                'archimate-implementation': ArchitectureLayer.IMPLEMENTATION
            }
            layer = layer_map[model_type]
            model = engine.generate_archimate_model(layer, context, use_ai)
            model['name'] = name
    
    elif model_type == 'bpmn-process':
        model = engine.generate_bpmn_model(name, context, 'process', use_ai)
    
    elif model_type.startswith('uml'):
        # Map to ModelType enum
        type_map = {
            'uml-class': ModelType.UML_CLASS,
            'uml-sequence': ModelType.UML_SEQUENCE,
            'uml-use-case': ModelType.UML_USE_CASE,
            'uml-activity': ModelType.UML_ACTIVITY,
            'uml-state': ModelType.UML_STATE_MACHINE,
            'uml-component': ModelType.UML_COMPONENT,
            'uml-deployment': ModelType.UML_DEPLOYMENT
        }
        uml_type = type_map.get(model_type, ModelType.UML_CLASS)
        model = engine.generate_uml_model(uml_type, name, context, use_ai)
    
    if not model:
        click.echo(ConsoleColors.error("Failed to generate model"))
        return
    
    # Determine output directory
    if not output_dir:
        output_dir = os.path.join(project, 'models', model['id'])
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Save model JSON
    model_file = os.path.join(output_dir, 'model.json')
    with open(model_file, 'w') as f:
        json.dump(model, f, indent=2)
    
    click.echo(ConsoleColors.success(f"✅ Model generated: {model['id']}"))
    click.echo(f"   Model file: {model_file}")
    
    # Export to requested formats
    exporters = {
        'text': TextExporter(),
        'mermaid': MermaidExporter(),
        'kroki': KrokiExporter(),
        'archi': ArchiExporter(),
        'gojs': GoJSExporter(),
        'ea': EnterpriseArchitectExporter()
    }
    
    click.echo(f"\nExporting to {len(output_format)} format(s)...")
    
    for fmt in output_format:
        exporter = exporters.get(fmt)
        if not exporter:
            continue
        
        # Export
        try:
            content = exporter.export(model)
            
            # Determine file extension
            ext_map = {
                'text': 'md',
                'mermaid': 'mmd',
                'kroki': 'puml',
                'archi': 'xml',
                'gojs': 'json',
                'ea': 'xmi'
            }
            ext = ext_map.get(fmt, 'txt')
            
            # Save file
            output_file = os.path.join(output_dir, f'model.{ext}')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            click.echo(ConsoleColors.success(f"   ✅ {fmt.upper()}: {output_file}"))
        
        except Exception as e:
            click.echo(ConsoleColors.error(f"   ❌ {fmt.upper()}: {str(e)}"))
    
    # Display summary
    click.echo(f"\n{ConsoleColors.info('ℹ️  Model Summary:')}")
    click.echo(f"   Name: {model['name']}")
    click.echo(f"   Type: {model['type']}")
    click.echo(f"   Elements: {len(model.get('elements', []))}")
    click.echo(f"   Relationships: {len(model.get('relationships', []))}")
    click.echo(f"   Output Directory: {output_dir}")
    
    # Show next steps
    click.echo(f"\n{ConsoleColors.header('Next Steps:')}")
    click.echo("   1. Review generated model files")
    click.echo("   2. Import into Enterprise Architect or Archi tool")
    click.echo("   3. Refine and customize as needed")
    click.echo("   4. Use 'model validate' to check compliance")


@model.command()
@click.option('--project', type=click.Path(exists=True), default='.', help='Project directory')
@click.option('--format', 'output_format', 
              type=click.Choice(['table', 'json', 'tree']),
              default='table',
              help='Output format')
def list(project, output_format):
    """
    List all generated models in project.
    
    Example:
        python archiagents.py model list
    """
    models_dir = os.path.join(project, 'models')
    
    if not os.path.exists(models_dir):
        click.echo(ConsoleColors.warning("⚠️  No models directory found"))
        return
    
    # Find all model.json files
    models = []
    for root, dirs, files in os.walk(models_dir):
        if 'model.json' in files:
            try:
                with open(os.path.join(root, 'model.json'), 'r') as f:
                    model = json.load(f)
                    models.append({
                        'id': model.get('id', 'unknown'),
                        'name': model.get('name', 'Unnamed'),
                        'type': model.get('type', 'unknown'),
                        'created': model.get('created', 'unknown'),
                        'elements': len(model.get('elements', [])),
                        'path': root
                    })
            except:
                pass
    
    if not models:
        click.echo(ConsoleColors.info("ℹ️  No models found"))
        return
    
    if output_format == 'json':
        click.echo(json.dumps(models, indent=2))
    elif output_format == 'tree':
        formatter = OutputFormatter()
        tree_data = {
            'models': {
                m['id']: {
                    'name': m['name'],
                    'type': m['type'],
                    'elements': m['elements']
                }
                for m in models
            }
        }
        click.echo(formatter.format_tree(tree_data))
    else:
        # Table format
        formatter = OutputFormatter()
        headers = ['ID', 'Name', 'Type', 'Elements', 'Created']
        rows = [
            [
                m['id'][:20] + '...' if len(m['id']) > 20 else m['id'],
                m['name'][:30] + '...' if len(m['name']) > 30 else m['name'],
                m['type'],
                str(m['elements']),
                m['created'][:10]
            ]
            for m in models
        ]
        click.echo(formatter.format_table(headers, rows))
        click.echo(f"\n{ConsoleColors.info(f'Total: {len(models)} model(s)')}")


@model.command()
@click.argument('model_id')
@click.option('--project', type=click.Path(exists=True), default='.', help='Project directory')
@click.option('--standards', multiple=True, 
              default=['archimate', 'togaf'],
              help='Standards to validate against')
def validate(model_id, project, standards):
    """
    Validate model against architecture standards.
    
    Example:
        python archiagents.py model validate archimate_business_20250101
    """
    # Find model
    models_dir = os.path.join(project, 'models')
    model_file = None
    
    for root, dirs, files in os.walk(models_dir):
        if model_id in root and 'model.json' in files:
            model_file = os.path.join(root, 'model.json')
            break
    
    if not model_file:
        click.echo(ConsoleColors.error(f"❌ Model not found: {model_id}"))
        return
    
    # Load model
    with open(model_file, 'r') as f:
        model = json.load(f)
    
    click.echo(f"Validating model: {model.get('name', 'Unnamed')}")
    click.echo(f"Standards: {', '.join(standards)}\n")
    
    # Perform validation
    ai_agent = AIModelingAgent()
    results = ai_agent.validate_model_compliance(model, list(standards))
    
    # Display results
    score = results.get('compliance_score', 0)
    
    if score >= 80:
        score_color = ConsoleColors.success
    elif score >= 60:
        score_color = ConsoleColors.warning
    else:
        score_color = ConsoleColors.error
    
    click.echo(score_color(f"Compliance Score: {score}/100"))
    click.echo(f"\n{results.get('summary', 'No summary available')}\n")
    
    # Display issues
    issues = results.get('issues', [])
    
    if issues:
        click.echo(ConsoleColors.header("Issues Found:"))
        for i, issue in enumerate(issues, 1):
            severity = issue.get('severity', 'info')
            if severity == 'error':
                icon = '❌'
                color = ConsoleColors.error
            elif severity == 'warning':
                icon = '⚠️'
                color = ConsoleColors.warning
            else:
                icon = 'ℹ️'
                color = ConsoleColors.info
            
            click.echo(f"\n{icon} {color(f'{severity.upper()}')}: {issue.get('description', '')}")
            click.echo(f"   Standard: {issue.get('standard', 'general')}")
            click.echo(f"   Element: {issue.get('element', 'N/A')}")
            click.echo(f"   Fix: {issue.get('fix', 'No fix suggestion')}")
    else:
        click.echo(ConsoleColors.success("✅ No issues found!"))


@model.command()
@click.argument('model_id')
@click.option('--project', type=click.Path(exists=True), default='.', help='Project directory')
@click.option('--format', 'export_format',
              type=click.Choice(['text', 'mermaid', 'kroki', 'archi', 'gojs', 'ea']),
              required=True,
              help='Export format')
@click.option('--output', type=click.Path(), help='Output file path')
def export(model_id, project, export_format, output):
    """
    Export model to different format.
    
    Examples:
        python archiagents.py model export my_model --format mermaid --output diagram.mmd
        python archiagents.py model export my_model --format archi --output model.xml
    """
    # Find and load model
    models_dir = os.path.join(project, 'models')
    model_file = None
    
    for root, dirs, files in os.walk(models_dir):
        if model_id in root and 'model.json' in files:
            model_file = os.path.join(root, 'model.json')
            break
    
    if not model_file:
        click.echo(ConsoleColors.error(f"❌ Model not found: {model_id}"))
        return
    
    with open(model_file, 'r') as f:
        model = json.load(f)
    
    # Select exporter
    exporters = {
        'text': TextExporter(),
        'mermaid': MermaidExporter(),
        'kroki': KrokiExporter(),
        'archi': ArchiExporter(),
        'gojs': GoJSExporter(),
        'ea': EnterpriseArchitectExporter()
    }
    
    exporter = exporters.get(export_format)
    if not exporter:
        click.echo(ConsoleColors.error(f"❌ Unknown format: {export_format}"))
        return
    
    # Export
    click.echo(f"Exporting model to {export_format.upper()} format...")
    
    try:
        content = exporter.export(model)
        
        if output:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(content)
            click.echo(ConsoleColors.success(f"✅ Exported to: {output}"))
        else:
            click.echo("\n" + "="*60)
            click.echo(content)
            click.echo("="*60)
    
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Export failed: {str(e)}"))


@model.command()
@click.argument('model_id')
@click.option('--project', type=click.Path(exists=True), default='.', help='Project directory')
def improve(model_id, project):
    """
    Get AI-powered improvement suggestions for model.
    
    Example:
        python archiagents.py model improve my_model
    """
    # Find and load model
    models_dir = os.path.join(project, 'models')
    model_file = None
    
    for root, dirs, files in os.walk(models_dir):
        if model_id in root and 'model.json' in files:
            model_file = os.path.join(root, 'model.json')
            break
    
    if not model_file:
        click.echo(ConsoleColors.error(f"❌ Model not found: {model_id}"))
        return
    
    with open(model_file, 'r') as f:
        model = json.load(f)
    
    click.echo(f"Analyzing model: {model.get('name', 'Unnamed')}\n")
    
    # Get suggestions
    ai_agent = AIModelingAgent()
    suggestions = ai_agent.suggest_model_improvements(model)
    
    if not suggestions:
        click.echo(ConsoleColors.success("✅ No improvements needed!"))
        return
    
    click.echo(ConsoleColors.header(f"Found {len(suggestions)} improvement suggestion(s):\n"))
    
    for i, suggestion in enumerate(suggestions, 1):
        category = suggestion.get('category', 'general')
        severity = suggestion.get('severity', 'info')
        
        # Color by severity
        if severity == 'high':
            color = ConsoleColors.error
        elif severity == 'medium':
            color = ConsoleColors.warning
        else:
            color = ConsoleColors.info
        
        click.echo(color(f"{i}. [{severity.upper()}] {category.upper()}"))
        click.echo(f"   Issue: {suggestion.get('description', 'No description')}")
        click.echo(f"   Recommendation: {suggestion.get('recommendation', 'No recommendation')}\n")


def _load_project_context(project_path: str) -> Dict[str, Any]:
    """Load project context for model generation"""
    context = {
        "industry": "Technology",
        "organization_size": "Medium",
        "goals": ["Digital Transformation", "Cloud Migration", "Process Automation"],
        "challenges": ["Legacy Systems", "Integration Complexity", "Technical Debt"]
    }
    
    # Try to load from project config
    config_file = os.path.join(project_path, '.archiagents', 'project.yaml')
    if os.path.exists(config_file):
        try:
            import yaml
            with open(config_file, 'r') as f:
                project_config = yaml.safe_load(f)
                context.update(project_config.get('enterprise', {}))
        except:
            pass
    
    return context


if __name__ == '__main__':
    model()
