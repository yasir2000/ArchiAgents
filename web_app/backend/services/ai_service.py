"""
ArchiAgents Web Application - AI Service
Integration with AI agents for model generation, validation, and improvement
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

import time
from datetime import datetime
from typing import List, Dict, Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from web_app.backend.models import database, schemas
from web_app.backend.services import model_service

# Import existing model generation system
from model_generation.engine import ModelGenerationEngine, ModelType as EngineModelType, ArchitectureLayer
from model_generation.ai_modeler import AIModelingAgent


# Initialize AI components
model_engine = ModelGenerationEngine()
ai_agent = AIModelingAgent()


# Map web schema types to engine types
MODEL_TYPE_MAPPING = {
    schemas.ModelType.ARCHIMATE_STRATEGY: (EngineModelType.ARCHIMATE, ArchitectureLayer.STRATEGY),
    schemas.ModelType.ARCHIMATE_BUSINESS: (EngineModelType.ARCHIMATE, ArchitectureLayer.BUSINESS),
    schemas.ModelType.ARCHIMATE_APPLICATION: (EngineModelType.ARCHIMATE, ArchitectureLayer.APPLICATION),
    schemas.ModelType.ARCHIMATE_TECHNOLOGY: (EngineModelType.ARCHIMATE, ArchitectureLayer.TECHNOLOGY),
    schemas.ModelType.ARCHIMATE_PHYSICAL: (EngineModelType.ARCHIMATE, ArchitectureLayer.PHYSICAL),
    schemas.ModelType.ARCHIMATE_IMPLEMENTATION: (EngineModelType.ARCHIMATE, ArchitectureLayer.IMPLEMENTATION),
    schemas.ModelType.ARCHIMATE_MULTI_LAYER: (EngineModelType.ARCHIMATE_MULTI_LAYER, None),
    schemas.ModelType.BPMN_PROCESS: (EngineModelType.BPMN_PROCESS, None),
    schemas.ModelType.BPMN_COLLABORATION: (EngineModelType.BPMN_COLLABORATION, None),
    schemas.ModelType.BPMN_CHOREOGRAPHY: (EngineModelType.BPMN_CHOREOGRAPHY, None),
    schemas.ModelType.UML_CLASS: (EngineModelType.UML_CLASS, None),
    schemas.ModelType.UML_SEQUENCE: (EngineModelType.UML_SEQUENCE, None),
    schemas.ModelType.UML_USE_CASE: (EngineModelType.UML_USE_CASE, None),
    schemas.ModelType.UML_ACTIVITY: (EngineModelType.UML_ACTIVITY, None),
    schemas.ModelType.UML_STATE_MACHINE: (EngineModelType.UML_STATE_MACHINE, None),
    schemas.ModelType.UML_COMPONENT: (EngineModelType.UML_COMPONENT, None),
    schemas.ModelType.UML_DEPLOYMENT: (EngineModelType.UML_DEPLOYMENT, None),
}


async def generate_model(
    request: schemas.AIGenerationRequest,
    user_id: int,
    db: Session
) -> schemas.AIGenerationResponse:
    """Generate architecture model using AI"""
    
    # Verify project access
    await model_service.get_project(request.project_id, user_id, db)
    
    # Get project context if requested
    context = {}
    if request.use_project_context:
        project = db.query(database.Project).filter(database.Project.id == request.project_id).first()
        context = {
            "project_name": project.name,
            "project_description": project.description,
            "togaf_phase": request.togaf_phase or project.togaf_phase,
            "existing_models": len(project.models) if project.models else 0
        }
    
    # Map model type
    engine_type_info = MODEL_TYPE_MAPPING.get(request.model_type)
    if not engine_type_info:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported model type: {request.model_type}"
        )
    
    engine_type, layer = engine_type_info
    
    # Start generation
    start_time = time.time()
    
    try:
        # Generate using AI agent
        if engine_type == EngineModelType.ARCHIMATE:
            if layer == ArchitectureLayer.STRATEGY:
                generated_model = await ai_agent.generate_archimate_model_with_ai(
                    layer="strategy",
                    name=request.name,
                    description=request.description,
                    context=context
                )
            elif layer == ArchitectureLayer.BUSINESS:
                generated_model = await ai_agent.generate_archimate_model_with_ai(
                    layer="business",
                    name=request.name,
                    description=request.description,
                    context=context
                )
            elif layer == ArchitectureLayer.APPLICATION:
                generated_model = await ai_agent.generate_archimate_model_with_ai(
                    layer="application",
                    name=request.name,
                    description=request.description,
                    context=context
                )
            elif layer == ArchitectureLayer.TECHNOLOGY:
                generated_model = await ai_agent.generate_archimate_model_with_ai(
                    layer="technology",
                    name=request.name,
                    description=request.description,
                    context=context
                )
            elif layer == ArchitectureLayer.PHYSICAL:
                generated_model = await ai_agent.generate_archimate_model_with_ai(
                    layer="physical",
                    name=request.name,
                    description=request.description,
                    context=context
                )
            elif layer == ArchitectureLayer.IMPLEMENTATION:
                generated_model = await ai_agent.generate_archimate_model_with_ai(
                    layer="implementation",
                    name=request.name,
                    description=request.description,
                    context=context
                )
        elif engine_type == EngineModelType.ARCHIMATE_MULTI_LAYER:
            generated_model = model_engine.generate_multi_layer_model(
                name=request.name,
                description=request.description or "Multi-layer enterprise architecture"
            )
        elif engine_type == EngineModelType.BPMN_PROCESS:
            generated_model = await ai_agent.generate_bpmn_process_with_ai(
                name=request.name,
                description=request.description,
                context=context
            )
        elif engine_type == EngineModelType.BPMN_COLLABORATION:
            generated_model = model_engine.generate_bpmn_model(
                bpmn_type="collaboration",
                name=request.name,
                description=request.description or "BPMN Collaboration Model"
            )
        elif engine_type == EngineModelType.BPMN_CHOREOGRAPHY:
            generated_model = model_engine.generate_bpmn_model(
                bpmn_type="choreography",
                name=request.name,
                description=request.description or "BPMN Choreography Model"
            )
        else:
            # UML models
            uml_type = engine_type.value.replace("uml-", "")
            generated_model = await ai_agent.generate_uml_diagram_with_ai(
                diagram_type=uml_type,
                name=request.name,
                purpose=request.description or f"UML {uml_type} diagram",
                context=context
            )
        
        generation_time = time.time() - start_time
        
        # Convert generated model to web format
        elements = []
        for elem in generated_model.get("elements", []):
            elements.append(schemas.ModelElement(
                id=elem["id"],
                type=elem["type"],
                name=elem["name"],
                description=elem.get("description"),
                properties=elem.get("properties", {}),
                position=elem.get("position")
            ))
        
        relationships = []
        for rel in generated_model.get("relationships", []):
            relationships.append(schemas.ModelRelationship(
                id=rel["id"],
                type=rel["type"],
                name=rel.get("name"),
                source=rel["source"],
                target=rel["target"],
                properties=rel.get("properties", {})
            ))
        
        # Create model in database
        model_create = schemas.ArchitectureModelCreate(
            project_id=request.project_id,
            name=request.name,
            description=request.description or generated_model.get("description", ""),
            model_type=request.model_type,
            status=schemas.ModelStatus.DRAFT,
            elements=elements,
            relationships=relationships,
            metadata=generated_model.get("metadata", {})
        )
        
        db_model = database.ArchitectureModel(
            project_id=model_create.project_id,
            name=model_create.name,
            description=model_create.description,
            model_type=model_create.model_type,
            status=model_create.status,
            elements=[elem.dict() for elem in model_create.elements],
            relationships=[rel.dict() for rel in model_create.relationships],
            metadata=model_create.metadata,
            version="1.0.0",
            generated_by_ai=True,
            ai_generation_prompt=request.prompt,
            created_by=user_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        
        # Log activity
        await model_service.log_activity(
            user_id=user_id,
            action="ai_generate",
            resource_type="model",
            resource_id=db_model.id,
            details={
                "model_type": request.model_type.value,
                "elements_generated": len(elements),
                "relationships_generated": len(relationships),
                "generation_time": generation_time
            },
            db=db
        )
        
        # Get suggestions
        suggestions = [
            "Review and validate all generated elements",
            "Customize element properties as needed",
            "Add additional relationships for completeness",
            "Run compliance validation before publishing"
        ]
        
        return schemas.AIGenerationResponse(
            model=schemas.ArchitectureModel.from_orm(db_model),
            generation_time=generation_time,
            elements_generated=len(elements),
            relationships_generated=len(relationships),
            suggestions=suggestions
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI generation failed: {str(e)}"
        )


async def suggest_improvements(
    model_id: int,
    user_id: int,
    db: Session
) -> Dict[str, Any]:
    """Get AI-powered improvement suggestions for a model"""
    
    # Get model
    model = await model_service.get_model(model_id, user_id, db)
    
    # Convert to format for AI agent
    model_data = {
        "id": str(model.id),
        "name": model.name,
        "description": model.description,
        "type": model.model_type.value,
        "elements": model.elements,
        "relationships": model.relationships,
        "metadata": model.metadata
    }
    
    try:
        # Get suggestions from AI agent
        suggestions = await ai_agent.suggest_model_improvements(model_data)
        
        # Log activity
        await model_service.log_activity(
            user_id=user_id,
            action="ai_improve",
            resource_type="model",
            resource_id=model_id,
            details={"suggestion_count": len(suggestions.get("suggestions", []))},
            db=db
        )
        
        return suggestions
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate improvement suggestions: {str(e)}"
        )


async def validate_model(
    model_id: int,
    standards: List[str],
    user_id: int,
    db: Session
) -> schemas.ValidationResult:
    """Validate model against standards"""
    
    # Get model
    model = await model_service.get_model(model_id, user_id, db)
    
    # Convert to format for AI agent
    model_data = {
        "id": str(model.id),
        "name": model.name,
        "description": model.description,
        "type": model.model_type.value,
        "elements": model.elements,
        "relationships": model.relationships,
        "metadata": model.metadata
    }
    
    try:
        # Validate using AI agent
        validation_result = await ai_agent.validate_model_compliance(model_data, standards)
        
        # Convert to schema format
        issues = []
        for issue in validation_result.get("issues", []):
            issues.append(schemas.ValidationIssue(
                severity=issue["severity"],
                message=issue["message"],
                element_id=issue.get("element_id"),
                suggestion=issue.get("suggestion")
            ))
        
        compliance_score = validation_result.get("compliance_score", 0)
        
        # Update model compliance score
        model.compliance_score = compliance_score
        db.commit()
        
        # Log activity
        await model_service.log_activity(
            user_id=user_id,
            action="ai_validate",
            resource_type="model",
            resource_id=model_id,
            details={
                "standards": standards,
                "compliance_score": compliance_score,
                "issues_found": len(issues)
            },
            db=db
        )
        
        return schemas.ValidationResult(
            model_id=model_id,
            compliance_score=compliance_score,
            standards=standards,
            issues=issues,
            summary=validation_result.get("summary", "Validation complete")
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Validation failed: {str(e)}"
        )
