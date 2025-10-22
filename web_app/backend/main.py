"""
ArchiAgents Web Application - Main FastAPI Application
Enterprise Architecture Modeling Platform with Visual Design and AI Generation
"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fastapi import FastAPI, HTTPException, Depends, status, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn

from web_app.backend.models import database, schemas
from web_app.backend.services import auth_service, model_service, ai_service, collaboration_service
from web_app.backend.api import database_manager

# Initialize FastAPI app
app = FastAPI(
    title="ArchiAgents Web Platform",
    description="Enterprise Architecture Modeling Platform with AI-Powered Visual Design",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# Database dependency
def get_db():
    db = database_manager.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Current user dependency
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> database.User:
    """Get current authenticated user"""
    return await auth_service.get_current_user(token, db)


# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "ArchiAgents Web Platform API",
        "version": "1.0.0",
        "docs": "/api/docs",
        "features": [
            "AI-Powered Model Generation",
            "Visual Diagram Editor",
            "Real-time Collaboration",
            "21 Model Types (ArchiMate, BPMN, UML)",
            "6 Export Formats",
            "TOGAF 10 Integration",
            "CLI Integration"
        ]
    }


# Health check
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}


# ============================================================================
# AUTHENTICATION ENDPOINTS
# ============================================================================

@app.post("/api/auth/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    return await auth_service.create_user(user, db)


@app.post("/api/auth/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login and get access token"""
    return await auth_service.authenticate_user(form_data.username, form_data.password, db)


@app.get("/api/auth/me", response_model=schemas.User)
async def get_current_user_info(current_user: database.User = Depends(get_current_user)):
    """Get current user information"""
    return current_user


@app.put("/api/auth/me", response_model=schemas.User)
async def update_current_user(
    user_update: schemas.UserUpdate,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update current user information"""
    return await auth_service.update_user(current_user.id, user_update, db)


# ============================================================================
# PROJECT ENDPOINTS
# ============================================================================

@app.get("/api/projects", response_model=List[schemas.Project])
async def get_projects(
    skip: int = 0,
    limit: int = 100,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all projects for current user"""
    return await model_service.get_user_projects(current_user.id, skip, limit, db)


@app.post("/api/projects", response_model=schemas.Project, status_code=status.HTTP_201_CREATED)
async def create_project(
    project: schemas.ProjectCreate,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new project"""
    return await model_service.create_project(project, current_user.id, db)


@app.get("/api/projects/{project_id}", response_model=schemas.ProjectWithModels)
async def get_project(
    project_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get project by ID with all models"""
    return await model_service.get_project(project_id, current_user.id, db)


@app.put("/api/projects/{project_id}", response_model=schemas.Project)
async def update_project(
    project_id: int,
    project_update: schemas.ProjectUpdate,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update project"""
    return await model_service.update_project(project_id, project_update, current_user.id, db)


@app.delete("/api/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete project"""
    await model_service.delete_project(project_id, current_user.id, db)
    return None


# ============================================================================
# MODEL ENDPOINTS
# ============================================================================

@app.get("/api/models", response_model=List[schemas.ArchitectureModel])
async def get_models(
    project_id: Optional[int] = None,
    model_type: Optional[schemas.ModelType] = None,
    status: Optional[schemas.ModelStatus] = None,
    skip: int = 0,
    limit: int = 100,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get architecture models with filters"""
    return await model_service.get_models(
        user_id=current_user.id,
        project_id=project_id,
        model_type=model_type,
        status=status,
        skip=skip,
        limit=limit,
        db=db
    )


@app.post("/api/models", response_model=schemas.ArchitectureModel, status_code=status.HTTP_201_CREATED)
async def create_model(
    model: schemas.ArchitectureModelCreate,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new architecture model"""
    return await model_service.create_model(model, current_user.id, db)


@app.get("/api/models/{model_id}", response_model=schemas.ArchitectureModelWithDetails)
async def get_model(
    model_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get model by ID with full details"""
    return await model_service.get_model(model_id, current_user.id, db)


@app.put("/api/models/{model_id}", response_model=schemas.ArchitectureModel)
async def update_model(
    model_id: int,
    model_update: schemas.ArchitectureModelUpdate,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update architecture model"""
    return await model_service.update_model(model_id, model_update, current_user.id, db)


@app.delete("/api/models/{model_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_model(
    model_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete architecture model"""
    await model_service.delete_model(model_id, current_user.id, db)
    return None


# ============================================================================
# AI GENERATION ENDPOINTS
# ============================================================================

@app.post("/api/ai/generate", response_model=schemas.AIGenerationResponse)
async def generate_model_with_ai(
    request: schemas.AIGenerationRequest,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Generate architecture model using AI"""
    return await ai_service.generate_model(request, current_user.id, db)


@app.post("/api/ai/improve/{model_id}", response_model=dict)
async def get_improvement_suggestions(
    model_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get AI-powered improvement suggestions for a model"""
    return await ai_service.suggest_improvements(model_id, current_user.id, db)


@app.post("/api/ai/validate/{model_id}", response_model=schemas.ValidationResult)
async def validate_model(
    model_id: int,
    standards: List[str] = ["archimate", "togaf"],
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Validate model against standards"""
    return await ai_service.validate_model(model_id, standards, current_user.id, db)


# ============================================================================
# EXPORT ENDPOINTS
# ============================================================================

@app.post("/api/export", response_model=schemas.ModelExportResponse)
async def export_model(
    request: schemas.ModelExportRequest,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Export model to different format"""
    return await model_service.export_model(request, current_user.id, db)


@app.get("/api/export/{model_id}/formats", response_model=List[dict])
async def get_available_formats(
    model_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get available export formats for a model"""
    return await model_service.get_export_formats(model_id, current_user.id, db)


# ============================================================================
# COLLABORATION ENDPOINTS
# ============================================================================

@app.post("/api/collaboration/sessions", response_model=schemas.CollaborationSession)
async def create_collaboration_session(
    session_request: schemas.CollaborationSessionCreate,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new collaboration session"""
    return await collaboration_service.create_session(session_request, current_user.id, db)


@app.get("/api/collaboration/sessions/{session_token}", response_model=schemas.CollaborationSession)
async def get_collaboration_session(
    session_token: str,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get collaboration session by token"""
    return await collaboration_service.get_session(session_token, db)


# WebSocket for real-time collaboration
@app.websocket("/ws/collaboration/{session_token}")
async def collaboration_websocket(
    websocket: WebSocket,
    session_token: str,
    db: Session = Depends(get_db)
):
    """WebSocket endpoint for real-time collaboration"""
    await collaboration_service.handle_websocket(websocket, session_token, db)


# ============================================================================
# DASHBOARD & STATISTICS
# ============================================================================

@app.get("/api/dashboard/stats", response_model=schemas.DashboardStats)
async def get_dashboard_stats(
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get dashboard statistics"""
    return await model_service.get_dashboard_stats(current_user.id, db)


@app.get("/api/dashboard/recent-activity", response_model=List[schemas.ActivityLog])
async def get_recent_activity(
    limit: int = 20,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get recent activity logs"""
    return await model_service.get_recent_activity(current_user.id, limit, db)


# ============================================================================
# COMMENTS
# ============================================================================

@app.get("/api/models/{model_id}/comments", response_model=List[schemas.CommentWithUser])
async def get_model_comments(
    model_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all comments for a model"""
    return await model_service.get_comments(model_id, current_user.id, db)


@app.post("/api/comments", response_model=schemas.Comment, status_code=status.HTTP_201_CREATED)
async def create_comment(
    comment: schemas.CommentCreate,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a comment on a model"""
    return await model_service.create_comment(comment, current_user.id, db)


# ============================================================================
# SEARCH
# ============================================================================

@app.post("/api/search", response_model=schemas.SearchResult)
async def search(
    search_request: schemas.SearchRequest,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Search across projects and models"""
    return await model_service.search(search_request, current_user.id, db)


# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database and create tables"""
    database_manager.init_db()
    print("✓ Database initialized")
    print("✓ ArchiAgents Web Platform started")
    print("📊 API Documentation: http://localhost:8000/api/docs")
    print("🎨 Frontend: http://localhost:3000")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
