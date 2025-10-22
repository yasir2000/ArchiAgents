"""
Format Exporters for Model Generation

Supports multiple output formats:
- Text (Markdown)
- Mermaid
- Kroki
- Archi (XML)
- GoJS (JSON)
- Enterprise Architect (XML)
"""

import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Any
from abc import ABC, abstractmethod


class BaseExporter(ABC):
    """Base class for format exporters"""
    
    @abstractmethod
    def export(self, model: Dict[str, Any]) -> str:
        """Export model to specific format"""
        pass


class TextExporter(BaseExporter):
    """Export models as Markdown text"""
    
    def export(self, model: Dict[str, Any]) -> str:
        """Export model as Markdown"""
        lines = []
        
        lines.append(f"# {model['name']}\n")
        lines.append(f"**Type:** {model['type']}")
        lines.append(f"**Created:** {model['created']}\n")
        
        # Elements
        if "elements" in model and model["elements"]:
            lines.append("## Elements\n")
            for elem in model["elements"]:
                lines.append(f"### {elem['name']}")
                lines.append(f"- **Type:** {elem['type']}")
                lines.append(f"- **ID:** {elem['id']}")
                if "description" in elem:
                    lines.append(f"- **Description:** {elem['description']}")
                if "attributes" in elem:
                    lines.append(f"- **Attributes:** {', '.join(elem['attributes'])}")
                if "methods" in elem:
                    lines.append(f"- **Methods:** {', '.join(elem['methods'])}")
                lines.append("")
        
        # Relationships
        if "relationships" in model and model["relationships"]:
            lines.append("## Relationships\n")
            for rel in model["relationships"]:
                lines.append(f"- `{rel['source']}` --[{rel['type']}]--> `{rel['target']}`")
        
        # BPMN specific
        if "tasks" in model:
            lines.append("\n## BPMN Process\n")
            lines.append("### Tasks")
            for task in model["tasks"]:
                lines.append(f"- **{task['name']}** ({task['type']})")
        
        if "gateways" in model and model["gateways"]:
            lines.append("\n### Gateways")
            for gateway in model["gateways"]:
                lines.append(f"- **{gateway['name']}** ({gateway['type']})")
        
        return "\n".join(lines)


class MermaidExporter(BaseExporter):
    """Export models as Mermaid diagrams"""
    
    def export(self, model: Dict[str, Any]) -> str:
        """Export model as Mermaid diagram"""
        model_type = model.get("type", "")
        
        if "archimate" in model_type:
            return self._export_archimate_mermaid(model)
        elif "bpmn" in model_type:
            return self._export_bpmn_mermaid(model)
        elif "uml_class" in model_type:
            return self._export_class_diagram_mermaid(model)
        elif "uml_sequence" in model_type:
            return self._export_sequence_diagram_mermaid(model)
        elif "uml_state" in model_type:
            return self._export_state_machine_mermaid(model)
        elif "uml_activity" in model_type:
            return self._export_activity_diagram_mermaid(model)
        else:
            return self._export_generic_mermaid(model)
    
    def _export_archimate_mermaid(self, model: Dict[str, Any]) -> str:
        """Export ArchiMate model as Mermaid flowchart"""
        lines = ["graph TB"]
        
        # Add elements
        for elem in model.get("elements", []):
            elem_id = elem["id"].replace("-", "_")
            elem_name = elem["name"].replace('"', '\\"')
            elem_type = elem["type"]
            
            # Different shapes for different element types
            if "actor" in elem_type:
                lines.append(f'    {elem_id}["{elem_name}"]')
            elif "process" in elem_type or "function" in elem_type:
                lines.append(f'    {elem_id}["{elem_name}"]')
            elif "service" in elem_type:
                lines.append(f'    {elem_id}("{elem_name}")')
            elif "data" in elem_type:
                lines.append(f'    {elem_id}[("{elem_name}")]')
            else:
                lines.append(f'    {elem_id}["{elem_name}"]')
        
        # Add relationships
        for rel in model.get("relationships", []):
            source = rel["source"].replace("-", "_")
            target = rel["target"].replace("-", "_")
            rel_type = rel["type"]
            lines.append(f'    {source} -->|{rel_type}| {target}')
        
        # Add styling
        lines.append("\n    classDef business fill:#FFE4B5")
        lines.append("    classDef application fill:#87CEEB")
        lines.append("    classDef technology fill:#90EE90")
        
        return "\n".join(lines)
    
    def _export_bpmn_mermaid(self, model: Dict[str, Any]) -> str:
        """Export BPMN model as Mermaid flowchart"""
        lines = ["graph LR"]
        
        # Events
        for event in model.get("events", []):
            event_id = event["id"]
            event_name = event["name"]
            if event["type"] == "start":
                lines.append(f'    {event_id}(("{event_name}"))')
            elif event["type"] == "end":
                lines.append(f'    {event_id}((("{event_name}")))')
        
        # Tasks
        for task in model.get("tasks", []):
            task_id = task["id"]
            task_name = task["name"]
            lines.append(f'    {task_id}["{task_name}"]')
        
        # Gateways
        for gateway in model.get("gateways", []):
            gw_id = gateway["id"]
            gw_name = gateway["name"]
            lines.append(f'    {gw_id}{{{{{gw_name}}}}}')
        
        # Flows
        for flow in model.get("flows", []):
            source = flow["source"]
            target = flow["target"]
            condition = flow.get("condition", "")
            if condition:
                lines.append(f'    {source} -->|{condition}| {target}')
            else:
                lines.append(f'    {source} --> {target}')
        
        return "\n".join(lines)
    
    def _export_class_diagram_mermaid(self, model: Dict[str, Any]) -> str:
        """Export UML class diagram as Mermaid"""
        lines = ["classDiagram"]
        
        for elem in model.get("elements", []):
            if elem["type"] == "class":
                class_name = elem["name"]
                lines.append(f'    class {class_name} {{')
                
                # Attributes
                for attr in elem.get("attributes", []):
                    lines.append(f'        {attr}')
                
                # Methods
                for method in elem.get("methods", []):
                    lines.append(f'        {method}')
                
                lines.append('    }')
        
        # Relationships (simplified)
        for rel in model.get("relationships", []):
            source = rel.get("source", "").replace("class_", "")
            target = rel.get("target", "").replace("class_", "")
            if source and target:
                lines.append(f'    {source} --> {target}')
        
        return "\n".join(lines)
    
    def _export_sequence_diagram_mermaid(self, model: Dict[str, Any]) -> str:
        """Export UML sequence diagram as Mermaid"""
        lines = ["sequenceDiagram"]
        
        # Participants
        participants = set()
        for elem in model.get("elements", []):
            if elem["type"] in ["actor", "object"]:
                participants.add(elem["id"])
        
        for participant in participants:
            lines.append(f'    participant {participant}')
        
        # Messages
        for elem in model.get("elements", []):
            if elem["type"] == "message":
                from_id = elem["from"]
                to_id = elem["to"]
                message = elem["message"]
                lines.append(f'    {from_id}->>+{to_id}: {message}')
            elif elem["type"] == "return":
                from_id = elem["from"]
                to_id = elem["to"]
                message = elem["message"]
                lines.append(f'    {from_id}-->>-{to_id}: {message}')
        
        return "\n".join(lines)
    
    def _export_state_machine_mermaid(self, model: Dict[str, Any]) -> str:
        """Export UML state machine as Mermaid"""
        lines = ["stateDiagram-v2"]
        
        # States
        for elem in model.get("elements", []):
            if elem["type"] == "state":
                state_id = elem["id"]
                state_name = elem["name"]
                lines.append(f'    {state_id}: {state_name}')
        
        # Transitions
        for elem in model.get("elements", []):
            if elem["type"] == "transition":
                from_state = elem["from"]
                to_state = elem["to"]
                trigger = elem.get("trigger", "")
                lines.append(f'    {from_state} --> {to_state}: {trigger}')
        
        return "\n".join(lines)
    
    def _export_activity_diagram_mermaid(self, model: Dict[str, Any]) -> str:
        """Export UML activity diagram as Mermaid flowchart"""
        lines = ["flowchart TD"]
        
        for elem in model.get("elements", []):
            elem_id = elem["id"]
            elem_name = elem["name"]
            elem_type = elem["type"]
            
            if elem_type == "initial_node":
                lines.append(f'    {elem_id}((Start))')
            elif elem_type == "final_node":
                lines.append(f'    {elem_id}((End))')
            elif elem_type == "activity":
                lines.append(f'    {elem_id}["{elem_name}"]')
            elif elem_type == "decision_node":
                lines.append(f'    {elem_id}{{{{{elem_name}}}}}')
        
        return "\n".join(lines)
    
    def _export_generic_mermaid(self, model: Dict[str, Any]) -> str:
        """Export generic model as Mermaid flowchart"""
        lines = ["graph TD"]
        
        for elem in model.get("elements", []):
            elem_id = elem["id"].replace("-", "_")
            elem_name = elem["name"].replace('"', '\\"')
            lines.append(f'    {elem_id}["{elem_name}"]')
        
        for rel in model.get("relationships", []):
            source = rel["source"].replace("-", "_")
            target = rel["target"].replace("-", "_")
            lines.append(f'    {source} --> {target}')
        
        return "\n".join(lines)


class KrokiExporter(BaseExporter):
    """Export models for Kroki diagram service"""
    
    def export(self, model: Dict[str, Any]) -> str:
        """Export model in Kroki-compatible format (PlantUML)"""
        model_type = model.get("type", "")
        
        if "archimate" in model_type:
            return self._export_archimate_plantuml(model)
        elif "bpmn" in model_type:
            return self._export_bpmn_plantuml(model)
        elif "uml" in model_type:
            return self._export_uml_plantuml(model)
        else:
            return self._export_generic_plantuml(model)
    
    def _export_archimate_plantuml(self, model: Dict[str, Any]) -> str:
        """Export ArchiMate as PlantUML"""
        lines = ["@startuml", "!include <archimate/Archimate>", ""]
        
        for elem in model.get("elements", []):
            elem_type = elem["type"]
            elem_id = elem["id"]
            elem_name = elem["name"]
            
            # Map ArchiMate element types to PlantUML
            if "actor" in elem_type:
                lines.append(f'Business_Actor({elem_id}, "{elem_name}")')
            elif "process" in elem_type:
                lines.append(f'Business_Process({elem_id}, "{elem_name}")')
            elif "service" in elem_type:
                lines.append(f'Business_Service({elem_id}, "{elem_name}")')
            elif "application" in elem_type:
                lines.append(f'Application_Component({elem_id}, "{elem_name}")')
            elif "node" in elem_type:
                lines.append(f'Node({elem_id}, "{elem_name}")')
            else:
                lines.append(f'rectangle "{elem_name}" as {elem_id}')
        
        lines.append("")
        
        for rel in model.get("relationships", []):
            source = rel["source"]
            target = rel["target"]
            rel_type = rel["type"]
            lines.append(f'{source} --> {target}: {rel_type}')
        
        lines.append("@enduml")
        return "\n".join(lines)
    
    def _export_bpmn_plantuml(self, model: Dict[str, Any]) -> str:
        """Export BPMN as PlantUML activity diagram"""
        lines = ["@startuml", "start"]
        
        for task in model.get("tasks", []):
            lines.append(f':{task["name"]};')
        
        lines.append("stop")
        lines.append("@enduml")
        return "\n".join(lines)
    
    def _export_uml_plantuml(self, model: Dict[str, Any]) -> str:
        """Export UML diagram as PlantUML"""
        model_type = model.get("type", "")
        
        if "class" in model_type:
            return self._export_class_plantuml(model)
        elif "sequence" in model_type:
            return self._export_sequence_plantuml(model)
        else:
            return self._export_generic_plantuml(model)
    
    def _export_class_plantuml(self, model: Dict[str, Any]) -> str:
        """Export class diagram as PlantUML"""
        lines = ["@startuml"]
        
        for elem in model.get("elements", []):
            if elem["type"] == "class":
                class_name = elem["name"]
                lines.append(f'class {class_name} {{')
                
                for attr in elem.get("attributes", []):
                    lines.append(f'  {attr}')
                
                for method in elem.get("methods", []):
                    lines.append(f'  {method}')
                
                lines.append('}')
        
        lines.append("@enduml")
        return "\n".join(lines)
    
    def _export_sequence_plantuml(self, model: Dict[str, Any]) -> str:
        """Export sequence diagram as PlantUML"""
        lines = ["@startuml"]
        
        for elem in model.get("elements", []):
            if elem["type"] in ["actor", "object"]:
                lines.append(f'participant {elem["id"]} as "{elem["name"]}"')
        
        for elem in model.get("elements", []):
            if elem["type"] == "message":
                lines.append(f'{elem["from"]} -> {elem["to"]}: {elem["message"]}')
            elif elem["type"] == "return":
                lines.append(f'{elem["from"]} --> {elem["to"]}: {elem["message"]}')
        
        lines.append("@enduml")
        return "\n".join(lines)
    
    def _export_generic_plantuml(self, model: Dict[str, Any]) -> str:
        """Export generic model as PlantUML component diagram"""
        lines = ["@startuml"]
        
        for elem in model.get("elements", []):
            elem_id = elem["id"]
            elem_name = elem["name"]
            lines.append(f'component "{elem_name}" as {elem_id}')
        
        for rel in model.get("relationships", []):
            lines.append(f'{rel["source"]} --> {rel["target"]}')
        
        lines.append("@enduml")
        return "\n".join(lines)


class ArchiExporter(BaseExporter):
    """Export models as Archi XML format"""
    
    def export(self, model: Dict[str, Any]) -> str:
        """Export model as Archi XML"""
        root = ET.Element("archimate:model")
        root.set("xmlns:archimate", "http://www.archimatetool.com/archimate")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("name", model.get("name", "Model"))
        root.set("id", model.get("id", "model-1"))
        
        # Create folders
        folders = ET.SubElement(root, "folders")
        
        # Business folder
        business_folder = ET.SubElement(folders, "folder")
        business_folder.set("name", "Business")
        business_folder.set("id", "business-folder")
        business_folder.set("type", "business")
        
        # Application folder
        app_folder = ET.SubElement(folders, "folder")
        app_folder.set("name", "Application")
        app_folder.set("id", "application-folder")
        app_folder.set("type", "application")
        
        # Technology folder
        tech_folder = ET.SubElement(folders, "folder")
        tech_folder.set("name", "Technology")
        tech_folder.set("id", "technology-folder")
        tech_folder.set("type", "technology")
        
        # Add elements
        for elem in model.get("elements", []):
            elem_type = elem["type"]
            
            if "business" in elem_type:
                parent = business_folder
            elif "application" in elem_type:
                parent = app_folder
            elif "technology" in elem_type or "node" in elem_type:
                parent = tech_folder
            else:
                parent = business_folder
            
            element = ET.SubElement(parent, "element")
            element.set("xsi:type", f"archimate:{elem_type}")
            element.set("name", elem.get("name", ""))
            element.set("id", elem.get("id", ""))
            
            if "description" in elem:
                element.set("documentation", elem["description"])
        
        # Add relationships folder
        rel_folder = ET.SubElement(folders, "folder")
        rel_folder.set("name", "Relations")
        rel_folder.set("id", "relations-folder")
        rel_folder.set("type", "relations")
        
        for rel in model.get("relationships", []):
            relationship = ET.SubElement(rel_folder, "element")
            relationship.set("xsi:type", f"archimate:{rel.get('type', 'association')}-relationship")
            relationship.set("id", rel.get("id", ""))
            relationship.set("source", rel.get("source", ""))
            relationship.set("target", rel.get("target", ""))
        
        # Convert to string
        return ET.tostring(root, encoding="unicode", method="xml")


class GoJSExporter(BaseExporter):
    """Export models as GoJS JSON format"""
    
    def export(self, model: Dict[str, Any]) -> str:
        """Export model as GoJS JSON"""
        gojs_model = {
            "class": "GraphLinksModel",
            "modelData": {
                "name": model.get("name", ""),
                "type": model.get("type", ""),
                "created": model.get("created", "")
            },
            "nodeDataArray": [],
            "linkDataArray": []
        }
        
        # Add nodes
        for elem in model.get("elements", []):
            node = {
                "key": elem.get("id", ""),
                "text": elem.get("name", ""),
                "category": elem.get("type", ""),
                "description": elem.get("description", "")
            }
            
            # Add UML-specific properties
            if "attributes" in elem:
                node["attributes"] = elem["attributes"]
            if "methods" in elem:
                node["methods"] = elem["methods"]
            
            gojs_model["nodeDataArray"].append(node)
        
        # Add links
        for rel in model.get("relationships", []):
            link = {
                "from": rel.get("source", ""),
                "to": rel.get("target", ""),
                "text": rel.get("type", ""),
                "category": rel.get("type", "")
            }
            gojs_model["linkDataArray"].append(link)
        
        # Handle BPMN-specific elements
        if "tasks" in model:
            for task in model.get("tasks", []):
                gojs_model["nodeDataArray"].append({
                    "key": task["id"],
                    "text": task["name"],
                    "category": task["type"]
                })
        
        if "flows" in model:
            for flow in model.get("flows", []):
                gojs_model["linkDataArray"].append({
                    "from": flow["source"],
                    "to": flow["target"],
                    "text": flow.get("condition", "")
                })
        
        return json.dumps(gojs_model, indent=2)


class EnterpriseArchitectExporter(BaseExporter):
    """Export models for Enterprise Architect (XMI format)"""
    
    def export(self, model: Dict[str, Any]) -> str:
        """Export model as Enterprise Architect XMI"""
        root = ET.Element("XMI")
        root.set("xmi.version", "1.1")
        root.set("xmlns:UML", "omg.org/UML1.3")
        
        # XMI Header
        header = ET.SubElement(root, "XMI.header")
        doc = ET.SubElement(header, "XMI.documentation")
        exporter = ET.SubElement(doc, "XMI.exporter")
        exporter.text = "ArchiAgents Model Generator"
        
        # XMI Content
        content = ET.SubElement(root, "XMI.content")
        
        # Model
        uml_model = ET.SubElement(content, "UML:Model")
        uml_model.set("xmi.id", model.get("id", "model-1"))
        uml_model.set("name", model.get("name", "Model"))
        
        # Namespace
        namespace = ET.SubElement(uml_model, "UML:Namespace.ownedElement")
        
        # Package
        package = ET.SubElement(namespace, "UML:Package")
        package.set("xmi.id", f"{model.get('id', 'model')}_package")
        package.set("name", model.get("type", "Package"))
        
        package_namespace = ET.SubElement(package, "UML:Namespace.ownedElement")
        
        # Add elements as classes/components
        for elem in model.get("elements", []):
            if elem.get("type") == "class":
                uml_class = ET.SubElement(package_namespace, "UML:Class")
                uml_class.set("xmi.id", elem.get("id", ""))
                uml_class.set("name", elem.get("name", ""))
                
                # Add attributes
                if "attributes" in elem:
                    classifier = ET.SubElement(uml_class, "UML:Classifier.feature")
                    for attr in elem["attributes"]:
                        attribute = ET.SubElement(classifier, "UML:Attribute")
                        attribute.set("name", attr)
            else:
                # Generic component
                component = ET.SubElement(package_namespace, "UML:Component")
                component.set("xmi.id", elem.get("id", ""))
                component.set("name", elem.get("name", ""))
        
        # Add relationships
        for rel in model.get("relationships", []):
            association = ET.SubElement(package_namespace, "UML:Association")
            association.set("xmi.id", rel.get("id", ""))
            
            connection = ET.SubElement(association, "UML:Association.connection")
            
            end1 = ET.SubElement(connection, "UML:AssociationEnd")
            end1.set("type", rel.get("source", ""))
            
            end2 = ET.SubElement(connection, "UML:AssociationEnd")
            end2.set("type", rel.get("target", ""))
        
        return ET.tostring(root, encoding="unicode", method="xml")
