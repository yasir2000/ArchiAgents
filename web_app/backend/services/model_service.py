"""
ArchiAgents Web Application - Model Service
CRUD operations for projects, models, exports, and dashboard statistics
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from datetime import datetime
from typing import List, Optional, Dict, Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

from web_app.backend.models import database, schemas
from model_generation.engine import ModelGenerationEngine, ModelType as EngineModelType
from model_generation.formats import (
    TextExporter, MermaidExporter, KrokiExporter,
    ArchiExporter, GoJSExporter, EnterpriseArchitectExporter
)


# Initialize model generation engine
model_engine = ModelGenerationEngine()


# ============================================================================
# PROJECT OPERATIONS
# ============================================================================

async def get_user_projects(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = None
) -> List[database.Project]:
    """Get all projects for a user"""
    return db.query(database.Project)\
        .filter(database.Project.owner_id == user_id)\
        .offset(skip)\
        .limit(limit)\
        .all()


async def create_project(
    project: schemas.ProjectCreate,
    user_id: int,
    db: Session
) -> database.Project:
    """Create a new project"""
    db_project = database.Project(
        name=project.name,
        description=project.description,
        owner_id=user_id,
        togaf_phase=project.togaf_phase,
        status=project.status,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    
    # Log activity
    await log_activity(
        user_id=user_id,
        action="create",
        resource_type="project",
        resource_id=db_project.id,
        details={"name": project.name},
        db=db
    )
    
    return db_project


async def get_project(
    project_id: int,
    user_id: int,
    db: Session
) -> database.Project:
    """Get project by ID with access check"""
    project = db.query(database.Project)\
        .filter(database.Project.id == project_id)\
        .first()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    # Check access
    if project.owner_id != user_id:
        # Check if user is a team member
        member = db.query(database.ProjectMember)\
            .filter(
                and_(
                    database.ProjectMember.project_id == project_id,
                    database.ProjectMember.user_id == user_id
                )
            ).first()
        
        if not member:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied to this project"
            )
    
    return project


async def update_project(
    project_id: int,
    project_update: schemas.ProjectUpdate,
    user_id: int,
    db: Session
) -> database.Project:
    """Update project"""
    project = await get_project(project_id, user_id, db)
    
    # Update fields
    if project_update.name is not None:
        project.name = project_update.name
    if project_update.description is not None:
        project.description = project_update.description
    if project_update.togaf_phase is not None:
        project.togaf_phase = project_update.togaf_phase
    if project_update.status is not None:
        project.status = project_update.status
    
    project.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(project)
    
    # Log activity
    await log_activity(
        user_id=user_id,
        action="update",
        resource_type="project",
        resource_id=project_id,
        details=project_update.dict(exclude_unset=True),
        db=db
    )
    
    return project


async def delete_project(
    project_id: int,
    user_id: int,
    db: Session
) -> None:
    """Delete project"""
    project = await get_project(project_id, user_id, db)
    
    # Only owner can delete
    if project.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only project owner can delete the project"
        )
    
    # Log before delete
    await log_activity(
        user_id=user_id,
        action="delete",
        resource_type="project",
        resource_id=project_id,
        details={"name": project.name},
        db=db
    )
    
    db.delete(project)
    db.commit()


# ============================================================================
# MODEL OPERATIONS
# ============================================================================

async def get_models(
    user_id: int,
    project_id: Optional[int] = None,
    model_type: Optional[schemas.ModelType] = None,
    status: Optional[schemas.ModelStatus] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = None
) -> List[database.ArchitectureModel]:
    """Get models with filters"""
    query = db.query(database.ArchitectureModel)\
        .join(database.Project)\
        .filter(database.Project.owner_id == user_id)
    
    if project_id:
        query = query.filter(database.ArchitectureModel.project_id == project_id)
    
    if model_type:
        query = query.filter(database.ArchitectureModel.model_type == model_type)
    
    if status:
        query = query.filter(database.ArchitectureModel.status == status)
    
    return query.offset(skip).limit(limit).all()


async def create_model(
    model: schemas.ArchitectureModelCreate,
    user_id: int,
    db: Session
) -> database.ArchitectureModel:
    """Create a new architecture model"""
    # Verify project access
    await get_project(model.project_id, user_id, db)
    
    db_model = database.ArchitectureModel(
        project_id=model.project_id,
        name=model.name,
        description=model.description,
        model_type=model.model_type,
        status=model.status,
        elements=[elem.dict() for elem in model.elements],
        relationships=[rel.dict() for rel in model.relationships],
        metadata=model.metadata,
        version="1.0.0",
        generated_by_ai=False,
        created_by=user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    
    # Log activity
    await log_activity(
        user_id=user_id,
        action="create",
        resource_type="model",
        resource_id=db_model.id,
        details={
            "name": model.name,
            "type": model.model_type.value,
            "elements": len(model.elements),
            "relationships": len(model.relationships)
        },
        db=db
    )
    
    return db_model


async def get_model(
    model_id: int,
    user_id: int,
    db: Session
) -> database.ArchitectureModel:
    """Get model by ID with access check"""
    model = db.query(database.ArchitectureModel)\
        .filter(database.ArchitectureModel.id == model_id)\
        .first()
    
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model not found"
        )
    
    # Check project access
    await get_project(model.project_id, user_id, db)
    
    return model


async def update_model(
    model_id: int,
    model_update: schemas.ArchitectureModelUpdate,
    user_id: int,
    db: Session
) -> database.ArchitectureModel:
    """Update architecture model"""
    model = await get_model(model_id, user_id, db)
    
    # Update fields
    if model_update.name is not None:
        model.name = model_update.name
    if model_update.description is not None:
        model.description = model_update.description
    if model_update.status is not None:
        model.status = model_update.status
    if model_update.elements is not None:
        model.elements = [elem.dict() for elem in model_update.elements]
    if model_update.relationships is not None:
        model.relationships = [rel.dict() for rel in model_update.relationships]
    if model_update.metadata is not None:
        model.metadata = model_update.metadata
    
    model.updated_at = datetime.utcnow()
    
    # Update version if elements or relationships changed
    if model_update.elements is not None or model_update.relationships is not None:
        version_parts = model.version.split('.')
        version_parts[2] = str(int(version_parts[2]) + 1)  # Increment patch version
        model.version = '.'.join(version_parts)
    
    db.commit()
    db.refresh(model)
    
    # Log activity
    await log_activity(
        user_id=user_id,
        action="update",
        resource_type="model",
        resource_id=model_id,
        details=model_update.dict(exclude_unset=True),
        db=db
    )
    
    return model


async def delete_model(
    model_id: int,
    user_id: int,
    db: Session
) -> None:
    """Delete architecture model"""
    model = await get_model(model_id, user_id, db)
    
    # Log before delete
    await log_activity(
        user_id=user_id,
        action="delete",
        resource_type="model",
        resource_id=model_id,
        details={"name": model.name, "type": model.model_type.value},
        db=db
    )
    
    db.delete(model)
    db.commit()


# ============================================================================
# EXPORT OPERATIONS
# ============================================================================

async def export_model(
    request: schemas.ModelExportRequest,
    user_id: int,
    db: Session
) -> schemas.ModelExportResponse:
    """Export model to different format"""
    model = await get_model(request.model_id, user_id, db)
    
    # Convert to model_generation format
    model_data = {
        "id": str(model.id),
        "name": model.name,
        "description": model.description,
        "type": model.model_type.value,
        "elements": model.elements,
        "relationships": model.relationships,
        "metadata": model.metadata
    }
    
    # Select exporter
    exporters = {
        "text": TextExporter(),
        "mermaid": MermaidExporter(),
        "kroki": KrokiExporter(),
        "archi": ArchiExporter(),
        "gojs": GoJSExporter(),
        "ea": EnterpriseArchitectExporter()
    }
    
    exporter = exporters.get(request.format)
    if not exporter:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported export format: {request.format}"
        )
    
    # Export
    content = exporter.export(model_data)
    
    # Save export record
    db_export = database.ModelExport(
        model_id=model.id,
        format=request.format,
        content=content,
        created_at=datetime.utcnow()
    )
    db.add(db_export)
    db.commit()
    
    # Log activity
    await log_activity(
        user_id=user_id,
        action="export",
        resource_type="model",
        resource_id=model.id,
        details={"format": request.format},
        db=db
    )
    
    return schemas.ModelExportResponse(
        model_id=model.id,
        format=request.format,
        content=content,
        created_at=db_export.created_at
    )


async def get_export_formats(
    model_id: int,
    user_id: int,
    db: Session
) -> List[Dict[str, str]]:
    """Get available export formats"""
    model = await get_model(model_id, user_id, db)
    
    formats = [
        {"format": "text", "name": "Markdown Documentation", "extension": ".md"},
        {"format": "mermaid", "name": "Mermaid Diagram", "extension": ".mermaid"},
        {"format": "kroki", "name": "PlantUML (Kroki)", "extension": ".puml"},
        {"format": "archi", "name": "Archi Tool XML", "extension": ".archi"},
        {"format": "gojs", "name": "GoJS JSON", "extension": ".json"},
        {"format": "ea", "name": "Enterprise Architect XMI", "extension": ".xmi"}
    ]
    
    return formats


# ============================================================================
# COMMENTS
# ============================================================================

async def get_comments(
    model_id: int,
    user_id: int,
    db: Session
) -> List[database.Comment]:
    """Get all comments for a model"""
    # Verify access
    await get_model(model_id, user_id, db)
    
    return db.query(database.Comment)\
        .filter(database.Comment.model_id == model_id)\
        .order_by(database.Comment.created_at.desc())\
        .all()


async def create_comment(
    comment: schemas.CommentCreate,
    user_id: int,
    db: Session
) -> database.Comment:
    """Create a comment on a model"""
    # Verify access
    await get_model(comment.model_id, user_id, db)
    
    db_comment = database.Comment(
        model_id=comment.model_id,
        user_id=user_id,
        content=comment.content,
        element_id=comment.element_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    
    return db_comment


# ============================================================================
# DASHBOARD & STATISTICS
# ============================================================================

async def get_dashboard_stats(
    user_id: int,
    db: Session
) -> schemas.DashboardStats:
    """Get dashboard statistics"""
    # Get all user's projects
    projects = await get_user_projects(user_id, db=db)
    project_ids = [p.id for p in projects]
    
    # Count models
    total_models = db.query(database.ArchitectureModel)\
        .filter(database.ArchitectureModel.project_id.in_(project_ids))\
        .count()
    
    # Models by type
    models_by_type = {}
    for model_type in schemas.ModelType:
        count = db.query(database.ArchitectureModel)\
            .filter(
                and_(
                    database.ArchitectureModel.project_id.in_(project_ids),
                    database.ArchitectureModel.model_type == model_type
                )
            ).count()
        if count > 0:
            models_by_type[model_type.value] = count
    
    # Models by status
    models_by_status = {}
    for status_val in schemas.ModelStatus:
        count = db.query(database.ArchitectureModel)\
            .filter(
                and_(
                    database.ArchitectureModel.project_id.in_(project_ids),
                    database.ArchitectureModel.status == status_val
                )
            ).count()
        if count > 0:
            models_by_status[status_val.value] = count
    
    # Recent activity
    recent_activity = db.query(database.ActivityLog)\
        .filter(database.ActivityLog.user_id == user_id)\
        .order_by(database.ActivityLog.created_at.desc())\
        .limit(10)\
        .all()
    
    activity_list = [
        {
            "action": log.action,
            "resource_type": log.resource_type,
            "resource_id": log.resource_id,
            "details": log.details,
            "created_at": log.created_at.isoformat()
        }
        for log in recent_activity
    ]
    
    # Team members (count unique members across all projects)
    team_members = db.query(database.ProjectMember)\
        .filter(database.ProjectMember.project_id.in_(project_ids))\
        .distinct(database.ProjectMember.user_id)\
        .count()
    
    return schemas.DashboardStats(
        total_projects=len(projects),
        total_models=total_models,
        models_by_type=models_by_type,
        models_by_status=models_by_status,
        recent_activity=activity_list,
        team_members=team_members
    )


async def get_recent_activity(
    user_id: int,
    limit: int,
    db: Session
) -> List[database.ActivityLog]:
    """Get recent activity logs"""
    return db.query(database.ActivityLog)\
        .filter(database.ActivityLog.user_id == user_id)\
        .order_by(database.ActivityLog.created_at.desc())\
        .limit(limit)\
        .all()


# ============================================================================
# SEARCH
# ============================================================================

async def search(
    search_request: schemas.SearchRequest,
    user_id: int,
    db: Session
) -> schemas.SearchResult:
    """Search across projects and models"""
    query = search_request.query.lower()
    results = []
    
    # Search projects
    projects = db.query(database.Project)\
        .filter(
            and_(
                database.Project.owner_id == user_id,
                or_(
                    database.Project.name.ilike(f"%{query}%"),
                    database.Project.description.ilike(f"%{query}%")
                )
            )
        ).all()
    
    for project in projects:
        results.append({
            "type": "project",
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "created_at": project.created_at.isoformat()
        })
    
    # Search models
    project_ids = [p.id for p in db.query(database.Project).filter(database.Project.owner_id == user_id).all()]
    models = db.query(database.ArchitectureModel)\
        .filter(
            and_(
                database.ArchitectureModel.project_id.in_(project_ids),
                or_(
                    database.ArchitectureModel.name.ilike(f"%{query}%"),
                    database.ArchitectureModel.description.ilike(f"%{query}%")
                )
            )
        ).all()
    
    for model in models:
        results.append({
            "type": "model",
            "id": model.id,
            "name": model.name,
            "description": model.description,
            "model_type": model.model_type.value,
            "status": model.status.value,
            "created_at": model.created_at.isoformat()
        })
    
    # Paginate
    total = len(results)
    start = (search_request.page - 1) * search_request.page_size
    end = start + search_request.page_size
    paginated_results = results[start:end]
    
    return schemas.SearchResult(
        total=total,
        page=search_request.page,
        page_size=search_request.page_size,
        results=paginated_results
    )


# ============================================================================
# UTILITIES
# ============================================================================

async def log_activity(
    user_id: int,
    action: str,
    resource_type: str,
    resource_id: int,
    details: Dict[str, Any],
    db: Session
) -> None:
    """Log user activity"""
    log = database.ActivityLog(
        user_id=user_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        details=details,
        created_at=datetime.utcnow()
    )
    db.add(log)
    db.commit()
