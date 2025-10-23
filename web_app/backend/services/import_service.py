"""
ArchiAgents Web Application - Model Import Service
Handles importing architecture models from various formats
"""

import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Any, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile

from models import database, schemas


class ModelImportService:
    """Service for importing architecture models"""
    
    @staticmethod
    def parse_text_format(content: str) -> Dict[str, Any]:
        """Parse plain text format (simple list of elements)"""
        lines = content.strip().split('\n')
        elements = []
        relationships = []
        
        element_counter = 0
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Check if it's a relationship (contains -> or --)
            if '->' in line or '--' in line:
                parts = line.replace('->', '->').split('->')
                if len(parts) >= 2:
                    source_name = parts[0].strip()
                    target_name = parts[1].strip()
                    
                    # Find or create elements
                    source_id = f"element_{len(elements)}"
                    target_id = f"element_{len(elements) + 1}"
                    
                    elements.append({
                        "id": source_id,
                        "type": "component",
                        "name": source_name,
                        "properties": {}
                    })
                    
                    elements.append({
                        "id": target_id,
                        "type": "component",
                        "name": target_name,
                        "properties": {}
                    })
                    
                    relationships.append({
                        "id": f"rel_{len(relationships)}",
                        "type": "association",
                        "source": source_id,
                        "target": target_id,
                        "properties": {}
                    })
            else:
                # It's an element
                element_counter += 1
                elements.append({
                    "id": f"element_{element_counter}",
                    "type": "component",
                    "name": line,
                    "properties": {}
                })
        
        return {
            "elements": elements,
            "relationships": relationships
        }
    
    @staticmethod
    def parse_mermaid_format(content: str) -> Dict[str, Any]:
        """Parse Mermaid diagram format"""
        lines = content.strip().split('\n')
        elements = []
        relationships = []
        element_map = {}
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('%%') or line.startswith('graph') or line.startswith('flowchart'):
                continue
            
            # Parse Mermaid syntax: A[Label] or A --> B
            if '-->' in line or '---' in line or '-..->' in line:
                # Relationship
                parts = line.replace('-->', '|').replace('---', '|').replace('-..->', '|').split('|')
                if len(parts) >= 2:
                    source = parts[0].strip().split('[')[0].strip()
                    target = parts[-1].strip().split('[')[0].strip()
                    
                    if source not in element_map:
                        elem_id = f"element_{len(elements)}"
                        element_map[source] = elem_id
                        elements.append({
                            "id": elem_id,
                            "type": "component",
                            "name": source,
                            "properties": {}
                        })
                    
                    if target not in element_map:
                        elem_id = f"element_{len(elements)}"
                        element_map[target] = elem_id
                        elements.append({
                            "id": elem_id,
                            "type": "component",
                            "name": target,
                            "properties": {}
                        })
                    
                    relationships.append({
                        "id": f"rel_{len(relationships)}",
                        "type": "flow",
                        "source": element_map[source],
                        "target": element_map[target],
                        "properties": {}
                    })
            elif '[' in line and ']' in line:
                # Element definition: A[Label]
                parts = line.split('[')
                if len(parts) >= 2:
                    node_id = parts[0].strip()
                    label = parts[1].split(']')[0].strip()
                    
                    if node_id not in element_map:
                        elem_id = f"element_{len(elements)}"
                        element_map[node_id] = elem_id
                        elements.append({
                            "id": elem_id,
                            "type": "component",
                            "name": label,
                            "properties": {}
                        })
        
        return {
            "elements": elements,
            "relationships": relationships
        }
    
    @staticmethod
    def parse_json_format(content: str) -> Dict[str, Any]:
        """Parse JSON format (GoJS-like or custom)"""
        try:
            data = json.loads(content)
            
            # Check if it's GoJS format
            if "nodeDataArray" in data:
                elements = []
                relationships = []
                
                # Parse nodes
                for node in data.get("nodeDataArray", []):
                    elements.append({
                        "id": str(node.get("key", node.get("id", f"element_{len(elements)}"))),
                        "type": node.get("category", "component"),
                        "name": node.get("text", node.get("name", "Unnamed")),
                        "description": node.get("description"),
                        "properties": {k: v for k, v in node.items() if k not in ["key", "id", "text", "name", "category"]}
                    })
                
                # Parse links
                for link in data.get("linkDataArray", []):
                    relationships.append({
                        "id": str(link.get("key", f"rel_{len(relationships)}")),
                        "type": link.get("category", "association"),
                        "source": str(link.get("from", link.get("source"))),
                        "target": str(link.get("to", link.get("target"))),
                        "name": link.get("text"),
                        "properties": {k: v for k, v in link.items() if k not in ["key", "from", "to", "source", "target", "category"]}
                    })
                
                return {
                    "elements": elements,
                    "relationships": relationships
                }
            
            # Check if it's our custom format
            elif "elements" in data and "relationships" in data:
                return data
            
            else:
                raise ValueError("Unsupported JSON format")
        
        except json.JSONDecodeError as e:
            raise HTTPException(status_code=400, detail=f"Invalid JSON format: {str(e)}")
    
    @staticmethod
    def parse_archi_format(content: bytes) -> Dict[str, Any]:
        """Parse Archi XML format"""
        try:
            root = ET.fromstring(content)
            elements = []
            relationships = []
            
            # Parse elements (simplified - Archi XML is complex)
            for elem in root.findall('.//{http://www.archimatetool.com/archimate}element'):
                elem_id = elem.get('id', f"element_{len(elements)}")
                elem_type = elem.get('{http://www.w3.org/2001/XMLSchema-instance}type', 'component')
                elem_name = elem.get('name', 'Unnamed')
                
                elements.append({
                    "id": elem_id,
                    "type": elem_type.split(':')[-1] if ':' in elem_type else elem_type,
                    "name": elem_name,
                    "properties": {}
                })
            
            # Parse relationships
            for rel in root.findall('.//{http://www.archimatetool.com/archimate}relationship'):
                rel_id = rel.get('id', f"rel_{len(relationships)}")
                rel_type = rel.get('{http://www.w3.org/2001/XMLSchema-instance}type', 'association')
                source = rel.get('source')
                target = rel.get('target')
                
                if source and target:
                    relationships.append({
                        "id": rel_id,
                        "type": rel_type.split(':')[-1] if ':' in rel_type else rel_type,
                        "source": source,
                        "target": target,
                        "properties": {}
                    })
            
            return {
                "elements": elements,
                "relationships": relationships
            }
        
        except ET.ParseError as e:
            raise HTTPException(status_code=400, detail=f"Invalid Archi XML format: {str(e)}")
    
    @staticmethod
    def parse_ea_format(content: bytes) -> Dict[str, Any]:
        """Parse Enterprise Architect XMI format"""
        try:
            root = ET.fromstring(content)
            elements = []
            relationships = []
            
            # Parse UML elements (simplified - XMI is complex)
            for elem in root.findall('.//{http://schema.omg.org/spec/UML/2.1}packagedElement'):
                elem_id = elem.get('{http://schema.omg.org/spec/XMI/2.1}id', f"element_{len(elements)}")
                elem_type = elem.get('{http://www.w3.org/2001/XMLSchema-instance}type', 'Class')
                elem_name = elem.get('name', 'Unnamed')
                
                elements.append({
                    "id": elem_id,
                    "type": elem_type.split(':')[-1] if ':' in elem_type else elem_type,
                    "name": elem_name,
                    "properties": {}
                })
            
            # Parse associations
            for assoc in root.findall('.//{http://schema.omg.org/spec/UML/2.1}association'):
                rel_id = assoc.get('{http://schema.omg.org/spec/XMI/2.1}id', f"rel_{len(relationships)}")
                
                # Find source and target
                owned_ends = assoc.findall('.//{http://schema.omg.org/spec/UML/2.1}ownedEnd')
                if len(owned_ends) >= 2:
                    source = owned_ends[0].get('type')
                    target = owned_ends[1].get('type')
                    
                    if source and target:
                        relationships.append({
                            "id": rel_id,
                            "type": "association",
                            "source": source,
                            "target": target,
                            "properties": {}
                        })
            
            return {
                "elements": elements,
                "relationships": relationships
            }
        
        except ET.ParseError as e:
            raise HTTPException(status_code=400, detail=f"Invalid EA XMI format: {str(e)}")
    
    @staticmethod
    async def import_model(
        db: Session,
        file: UploadFile,
        project_id: int,
        name: str,
        format: str,
        description: Optional[str],
        user: database.User
    ) -> schemas.ModelImportResponse:
        """Import a model from file"""
        # Verify project exists and user has access
        project = db.query(database.Project).filter(database.Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        
        # Check permissions (must be owner or team member)
        if project.owner_id != user.id:
            # TODO: Check if user is team member
            pass
        
        # Read file content
        content = await file.read()
        
        # Parse based on format
        warnings = []
        parsed_data = None
        
        try:
            if format == "text":
                parsed_data = ModelImportService.parse_text_format(content.decode('utf-8'))
            elif format == "mermaid":
                parsed_data = ModelImportService.parse_mermaid_format(content.decode('utf-8'))
            elif format == "gojs" or format == "json":
                parsed_data = ModelImportService.parse_json_format(content.decode('utf-8'))
            elif format == "archi":
                parsed_data = ModelImportService.parse_archi_format(content)
            elif format == "ea":
                parsed_data = ModelImportService.parse_ea_format(content)
            else:
                raise HTTPException(status_code=400, detail=f"Unsupported format: {format}")
        
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to parse file: {str(e)}")
        
        if not parsed_data or not parsed_data.get("elements"):
            raise HTTPException(status_code=400, detail="No valid elements found in file")
        
        # Determine model type based on content
        model_type = database.ModelType.ARCHIMATE_APPLICATION  # Default
        
        # Create model
        model = database.ArchitectureModel(
            project_id=project_id,
            name=name,
            description=description,
            model_type=model_type,
            status=database.ModelStatus.DRAFT,
            elements=parsed_data.get("elements", []),
            relationships=parsed_data.get("relationships", []),
            model_metadata={"imported_from": format, "original_filename": file.filename},
            created_by=user.id,
            generated_by_ai=False
        )
        
        db.add(model)
        db.commit()
        db.refresh(model)
        
        # Log activity
        activity = database.ActivityLog(
            user_id=user.id,
            action="import_model",
            resource_type="model",
            resource_id=model.id,
            details={
                "format": format,
                "filename": file.filename,
                "elements_count": len(parsed_data.get("elements", [])),
                "relationships_count": len(parsed_data.get("relationships", []))
            }
        )
        db.add(activity)
        db.commit()
        
        return schemas.ModelImportResponse(
            model_id=model.id,
            name=model.name,
            elements_imported=len(parsed_data.get("elements", [])),
            relationships_imported=len(parsed_data.get("relationships", [])),
            warnings=warnings,
            success=True
        )


def get_model_import_service():
    """Dependency injection for model import service"""
    return ModelImportService()
