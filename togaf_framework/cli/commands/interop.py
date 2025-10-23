"""
Import/Export Commands for Architecture Interoperability

Import and export architecture artifacts from/to various tools and formats.
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


@click.command(name='from-archi')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.argument('archi_file', type=click.Path(exists=True))
@click.option('--merge', is_flag=True, help='Merge with existing models')
@click.pass_context
def import_from_archi(ctx, project, archi_file, merge):
    """
    Import from Archi tool (XML format)
    
    \b
    Example:
      archiagents import from-archi model.archimate
      archiagents import from-archi model.xml --merge
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    config = ProjectConfig(str(project_path))
    
    click.echo(f"\n{ConsoleColors.info('📥 Importing from Archi tool...')}\n")
    
    try:
        import xml.etree.ElementTree as ET
        
        tree = ET.parse(archi_file)
        root = tree.getroot()
        
        # Parse ArchiMate XML
        elements = []
        relationships = []
        
        for elem in root.findall('.//{*}element'):
            elements.append({
                'id': elem.get('id'),
                'name': elem.get('name'),
                'type': elem.get('{http://www.w3.org/2001/XMLSchema-instance}type'),
                'documentation': elem.findtext('.//{*}documentation', '')
            })
        
        for rel in root.findall('.//{*}relationship'):
            relationships.append({
                'id': rel.get('id'),
                'source': rel.get('source'),
                'target': rel.get('target'),
                'type': rel.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            })
        
        # Save to project
        models_dir = project_path / 'models'
        models_dir.mkdir(exist_ok=True)
        
        imported_model = {
            'id': f'imported_archi_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
            'name': 'Imported from Archi',
            'source': 'Archi Tool',
            'imported_at': datetime.now().isoformat(),
            'elements': elements,
            'relationships': relationships
        }
        
        output_file = models_dir / f'{imported_model["id"]}.json'
        with open(output_file, 'w') as f:
            json.dump(imported_model, f, indent=2)
        
        click.echo(ConsoleColors.success(f"✅ Imported successfully!"))
        click.echo(f"  Elements: {len(elements)}")
        click.echo(f"  Relationships: {len(relationships)}")
        click.echo(f"  Saved to: {output_file}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Import failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='from-ea')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.argument('ea_file', type=click.Path(exists=True))
@click.pass_context
def import_from_ea(ctx, project, ea_file):
    """
    Import from Sparx Enterprise Architect (XMI format)
    
    \b
    Example:
      archiagents import from-ea model.xmi
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    
    click.echo(f"\n{ConsoleColors.info('📥 Importing from Enterprise Architect...')}\n")
    
    try:
        import xml.etree.ElementTree as ET
        
        tree = ET.parse(ea_file)
        root = tree.getroot()
        
        # Parse XMI structure
        packages = []
        classes = []
        
        for package in root.findall('.//{*}Package'):
            packages.append({
                'id': package.get('id'),
                'name': package.get('name')
            })
        
        for class_elem in root.findall('.//{*}Class'):
            classes.append({
                'id': class_elem.get('id'),
                'name': class_elem.get('name'),
                'type': 'class'
            })
        
        # Save to project
        models_dir = project_path / 'models'
        models_dir.mkdir(exist_ok=True)
        
        imported_model = {
            'id': f'imported_ea_{datetime.now().strftime("%Y%m%d_%H%M%S")}',
            'name': 'Imported from Enterprise Architect',
            'source': 'Sparx EA',
            'imported_at': datetime.now().isoformat(),
            'packages': packages,
            'classes': classes
        }
        
        output_file = models_dir / f'{imported_model["id"]}.json'
        with open(output_file, 'w') as f:
            json.dump(imported_model, f, indent=2)
        
        click.echo(ConsoleColors.success(f"✅ Imported successfully!"))
        click.echo(f"  Packages: {len(packages)}")
        click.echo(f"  Classes: {len(classes)}")
        click.echo(f"  Saved to: {output_file}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Import failed: {e}"), err=True)
        raise click.Abort()


@click.command(name='from-json')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.argument('json_file', type=click.Path(exists=True))
@click.option('--model-type', type=click.Choice([
    'archimate', 'uml', 'bpmn', 'generic'
]), default='generic', help='Model type')
@click.pass_context
def import_from_json(ctx, project, json_file, model_type):
    """
    Import from JSON file
    
    \b
    Example:
      archiagents import from-json model.json --model-type archimate
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    
    click.echo(f"\n{ConsoleColors.info('📥 Importing from JSON...')}\n")
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        models_dir = project_path / 'models'
        models_dir.mkdir(exist_ok=True)
        
        # Add metadata
        data['imported_at'] = datetime.now().isoformat()
        data['model_type'] = model_type
        
        output_file = models_dir / Path(json_file).name
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        click.echo(ConsoleColors.success(f"✅ Imported successfully!"))
        click.echo(f"  Saved to: {output_file}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Import failed: {e}"), err=True)
        raise click.Abort()


@click.command(name='to-archi')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--model-id', required=True, help='Model ID to export')
@click.option('--output', type=click.Path(), help='Output file path')
@click.pass_context
def export_to_archi(ctx, project, model_id, output):
    """
    Export to Archi tool format (XML)
    
    \b
    Example:
      archiagents export to-archi --model-id my-model --output model.archimate
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    
    click.echo(f"\n{ConsoleColors.info('📤 Exporting to Archi format...')}\n")
    
    try:
        # Load model
        model_file = project_path / 'models' / f'{model_id}.json'
        if not model_file.exists():
            click.echo(ConsoleColors.error(f"❌ Model not found: {model_id}"), err=True)
            raise click.Abort()
        
        with open(model_file, 'r') as f:
            model = json.load(f)
        
        # Generate Archi XML
        from model_generation.formats import ArchiExporter
        exporter = ArchiExporter()
        xml_content = exporter.export(model)
        
        # Determine output path
        if not output:
            output = project_path / 'exports' / f'{model_id}.archimate'
        
        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        click.echo(ConsoleColors.success(f"✅ Exported successfully!"))
        click.echo(f"  Output: {output_path}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Export failed: {e}"), err=True)
        if ctx.obj.get('verbose'):
            import traceback
            traceback.print_exc()
        raise click.Abort()


@click.command(name='to-ea')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--model-id', required=True, help='Model ID to export')
@click.option('--output', type=click.Path(), help='Output file path')
@click.pass_context
def export_to_ea(ctx, project, model_id, output):
    """
    Export to Enterprise Architect format (XMI)
    
    \b
    Example:
      archiagents export to-ea --model-id my-model --output model.xmi
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    
    click.echo(f"\n{ConsoleColors.info('📤 Exporting to EA format...')}\n")
    
    try:
        # Load model
        model_file = project_path / 'models' / f'{model_id}.json'
        if not model_file.exists():
            click.echo(ConsoleColors.error(f"❌ Model not found: {model_id}"), err=True)
            raise click.Abort()
        
        with open(model_file, 'r') as f:
            model = json.load(f)
        
        # Generate EA XMI
        from model_generation.formats import EnterpriseArchitectExporter
        exporter = EnterpriseArchitectExporter()
        xmi_content = exporter.export(model)
        
        # Determine output path
        if not output:
            output = project_path / 'exports' / f'{model_id}.xmi'
        
        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xmi_content)
        
        click.echo(ConsoleColors.success(f"✅ Exported successfully!"))
        click.echo(f"  Output: {output_path}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Export failed: {e}"), err=True)
        raise click.Abort()


@click.command(name='to-mermaid')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--model-id', required=True, help='Model ID to export')
@click.option('--output', type=click.Path(), help='Output file path')
@click.pass_context
def export_to_mermaid(ctx, project, model_id, output):
    """
    Export to Mermaid diagram format
    
    \b
    Example:
      archiagents export to-mermaid --model-id my-model --output diagram.mmd
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    
    click.echo(f"\n{ConsoleColors.info('📤 Exporting to Mermaid format...')}\n")
    
    try:
        # Load model
        model_file = project_path / 'models' / f'{model_id}.json'
        if not model_file.exists():
            click.echo(ConsoleColors.error(f"❌ Model not found: {model_id}"), err=True)
            raise click.Abort()
        
        with open(model_file, 'r') as f:
            model = json.load(f)
        
        # Generate Mermaid
        from model_generation.formats import MermaidExporter
        exporter = MermaidExporter()
        mermaid_content = exporter.export(model)
        
        # Determine output path
        if not output:
            output = project_path / 'exports' / f'{model_id}.mmd'
        
        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(mermaid_content)
        
        click.echo(ConsoleColors.success(f"✅ Exported successfully!"))
        click.echo(f"  Output: {output_path}\n")
        
    except Exception as e:
        click.echo(ConsoleColors.error(f"❌ Export failed: {e}"), err=True)
        raise click.Abort()


@click.command(name='batch')
@click.option('--project', type=click.Path(exists=True), help='Project directory')
@click.option('--format', type=click.Choice([
    'archi', 'ea', 'mermaid', 'gojs', 'all'
]), default='all', help='Export format')
@click.option('--output-dir', type=click.Path(), help='Output directory')
@click.pass_context
def batch_export(ctx, project, format, output_dir):
    """
    Batch export all models to specified format(s)
    
    \b
    Example:
      archiagents export batch --format all
      archiagents export batch --format mermaid --output-dir ./exports
    """
    
    if not project:
        project = os.getcwd()
    
    project_path = Path(project)
    
    click.echo(f"\n{ConsoleColors.info('📤 Batch exporting models...')}\n")
    
    # Find all models
    models_dir = project_path / 'models'
    if not models_dir.exists():
        click.echo(ConsoleColors.error("❌ No models directory found"), err=True)
        raise click.Abort()
    
    model_files = list(models_dir.glob('**/*.json'))
    
    if not model_files:
        click.echo("No models found to export.")
        return
    
    click.echo(f"Found {len(model_files)} model(s) to export")
    click.echo()
    
    formats_to_export = []
    if format == 'all':
        formats_to_export = ['archi', 'ea', 'mermaid', 'gojs']
    else:
        formats_to_export = [format]
    
    # Determine output directory
    if not output_dir:
        output_dir = project_path / 'exports'
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    fail_count = 0
    
    for model_file in model_files:
        model_id = model_file.stem
        click.echo(f"Exporting {model_id}...")
        
        try:
            with open(model_file, 'r') as f:
                model = json.load(f)
            
            for fmt in formats_to_export:
                try:
                    if fmt == 'archi':
                        from model_generation.formats import ArchiExporter
                        exporter = ArchiExporter()
                        ext = 'archimate'
                    elif fmt == 'ea':
                        from model_generation.formats import EnterpriseArchitectExporter
                        exporter = EnterpriseArchitectExporter()
                        ext = 'xmi'
                    elif fmt == 'mermaid':
                        from model_generation.formats import MermaidExporter
                        exporter = MermaidExporter()
                        ext = 'mmd'
                    elif fmt == 'gojs':
                        from model_generation.formats import GoJSExporter
                        exporter = GoJSExporter()
                        ext = 'json'
                    
                    content = exporter.export(model)
                    
                    output_file = output_path / f'{model_id}.{ext}'
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    click.echo(f"  ✅ {fmt}: {output_file}")
                    success_count += 1
                
                except Exception as e:
                    click.echo(f"  ❌ {fmt}: {e}")
                    fail_count += 1
        
        except Exception as e:
            click.echo(f"  ❌ Failed to load model: {e}")
            fail_count += 1
        
        click.echo()
    
    click.echo(ConsoleColors.success(f"✅ Batch export complete!"))
    click.echo(f"  Successful: {success_count}")
    if fail_count > 0:
        click.echo(f"  Failed: {fail_count}")
    click.echo()
