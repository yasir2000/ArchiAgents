"""
ArchiAgents Web Application - Main FastAPI Application
Enterprise Architecture Modeling Platform with Visual Design and AI Generation
"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from fastapi import FastAPI, HTTPException, Depends, status, WebSocket, WebSocketDisconnect, UploadFile, File, Form
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
    try:
        return await auth_service.create_user(user, db)
    except HTTPException:
        # Re-raise known HTTP exceptions
        raise
    except Exception as e:
        # Surface unexpected errors during development
        print(f"[/api/auth/register] Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/auth/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login and get access token (username field should contain email)"""
    # OAuth2PasswordRequestForm uses 'username' field, but we treat it as email
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


# ============================================================================
# PASSWORD CHANGE
# ============================================================================

@app.post("/api/auth/change-password")
async def change_password(
    password_change: schemas.PasswordChangeRequest,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Change user password"""
    # Verify current password
    if not auth_service.verify_password(password_change.current_password, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="Current password is incorrect")
    
    # Update password
    current_user.hashed_password = auth_service.get_password_hash(password_change.new_password)
    current_user.updated_at = database.datetime.utcnow()
    db.commit()
    
    return {"success": True, "message": "Password changed successfully"}


# ============================================================================
# NOTIFICATIONS
# ============================================================================

@app.get("/api/notifications", response_model=List[schemas.Notification])
async def get_notifications(
    unread_only: bool = False,
    limit: int = 50,
    offset: int = 0,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user notifications"""
    from services.notification_service import NotificationService
    return NotificationService.get_user_notifications(db, current_user.id, unread_only, limit, offset)


@app.get("/api/notifications/unread-count")
async def get_unread_count(
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get count of unread notifications"""
    from services.notification_service import NotificationService
    count = NotificationService.get_unread_count(db, current_user.id)
    return {"count": count}


@app.put("/api/notifications/{notification_id}/read", response_model=schemas.Notification)
async def mark_notification_read(
    notification_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Mark notification as read"""
    from services.notification_service import NotificationService
    return NotificationService.mark_as_read(db, notification_id, current_user.id)


@app.put("/api/notifications/read-all")
async def mark_all_notifications_read(
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Mark all notifications as read"""
    from services.notification_service import NotificationService
    count = NotificationService.mark_all_as_read(db, current_user.id)
    return {"success": True, "count": count}


@app.delete("/api/notifications/{notification_id}")
async def delete_notification(
    notification_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a notification"""
    from services.notification_service import NotificationService
    NotificationService.delete_notification(db, notification_id, current_user.id)
    return {"success": True}


@app.delete("/api/notifications/clear-all")
async def clear_all_notifications(
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Clear all notifications"""
    from services.notification_service import NotificationService
    count = NotificationService.clear_all_notifications(db, current_user.id)
    return {"success": True, "count": count}


# ============================================================================
# USER MANAGEMENT
# ============================================================================

@app.get("/api/users", response_model=List[schemas.UserListItem])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    role: Optional[database.UserRole] = None,
    search: Optional[str] = None,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List all users (admin only)"""
    if current_user.role != database.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Admin access required")
    
    from services.user_management_service import UserManagementService
    return UserManagementService.list_users(db, skip, limit, role, search)


@app.put("/api/users/{user_id}/role", response_model=schemas.User)
async def update_user_role(
    user_id: int,
    role_update: schemas.RoleUpdateRequest,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update user role (admin only)"""
    from services.user_management_service import UserManagementService
    return UserManagementService.update_user_role(db, user_id, role_update.role, current_user)


@app.delete("/api/users/{user_id}")
async def delete_user(
    user_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete user (admin only)"""
    from services.user_management_service import UserManagementService
    UserManagementService.delete_user(db, user_id, current_user)
    return {"success": True, "message": "User deleted successfully"}


@app.post("/api/users/invite", response_model=schemas.UserInvitation, status_code=status.HTTP_201_CREATED)
async def invite_user(
    invitation: schemas.UserInviteRequest,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Invite a new user (admin only)"""
    from services.user_management_service import UserManagementService
    return UserManagementService.create_invitation(db, invitation.email, invitation.role, current_user)


@app.get("/api/users/invitations", response_model=List[schemas.UserInvitation])
async def list_invitations(
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List pending invitations"""
    from services.user_management_service import UserManagementService
    return UserManagementService.list_pending_invitations(db, current_user)


@app.post("/api/users/accept-invitation", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
async def accept_invitation(
    accept_request: schemas.AcceptInvitationRequest,
    db: Session = Depends(get_db)
):
    """Accept user invitation and create account"""
    from services.user_management_service import UserManagementService
    return UserManagementService.accept_invitation(
        db, accept_request.token, accept_request.name, accept_request.password
    )


# ============================================================================
# MODEL IMPORT
# ============================================================================

@app.post("/api/models/import", response_model=schemas.ModelImportResponse, status_code=status.HTTP_201_CREATED)
async def import_model(
    file: UploadFile = File(...),
    project_id: int = Form(...),
    name: str = Form(...),
    format: str = Form(...),
    description: Optional[str] = Form(None),
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Import model from file"""
    from services.import_service import ModelImportService
    return await ModelImportService.import_model(
        db, file, project_id, name, format, description, current_user
    )


# ============================================================================
# COLLABORATION ENHANCEMENTS
# ============================================================================

@app.get("/api/collaboration/participants/{model_id}", response_model=schemas.CollaborationParticipantsResponse)
async def get_collaboration_participants(
    model_id: int,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get participants in a collaboration session"""
    # Get active session for model
    session = db.query(database.CollaborationSession).filter(
        database.CollaborationSession.model_id == model_id,
        database.CollaborationSession.is_active == True
    ).first()
    
    if not session:
        return schemas.CollaborationParticipantsResponse(
            model_id=model_id,
            session_id=0,
            participants=[],
            total_count=0
        )
    
    # Get participant details
    participants = []
    for user_id in session.participants or []:
        user = db.query(database.User).filter(database.User.id == user_id).first()
        if user:
            participants.append(schemas.CollaborationParticipant(
                user_id=user.id,
                name=user.name,
                email=user.email,
                status="active",
                joined_at=session.created_at
            ))
    
    return schemas.CollaborationParticipantsResponse(
        model_id=model_id,
        session_id=session.id,
        participants=participants,
        total_count=len(participants)
    )


@app.get("/api/collaboration/activity/{model_id}", response_model=schemas.CollaborationActivityResponse)
async def get_collaboration_activity(
    model_id: int,
    limit: int = 20,
    current_user: database.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get recent collaboration activity for a model"""
    # Get activity logs for the model
    activities = db.query(database.ActivityLog).filter(
        database.ActivityLog.resource_type == "model",
        database.ActivityLog.resource_id == model_id
    ).order_by(database.ActivityLog.created_at.desc()).limit(limit).all()
    
    # Convert to collaboration activity format
    activity_list = []
    for activity in activities:
        user = db.query(database.User).filter(database.User.id == activity.user_id).first()
        if user:
            activity_list.append(schemas.CollaborationActivity(
                id=str(activity.id),
                user_id=user.id,
                user_name=user.name,
                action=activity.action,
                description=f"{user.name} {activity.action.replace('_', ' ')}",
                timestamp=activity.created_at,
                element_id=activity.details.get("element_id") if activity.details else None
            ))
    
    return schemas.CollaborationActivityResponse(
        model_id=model_id,
        activities=activity_list,
        total_count=len(activity_list)
    )


# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """Initialize database and create tables"""
    database_manager.init_db()
    try:
        import inspect
        print(f"[startup] database module: {inspect.getfile(database)}")
    except Exception:
        pass
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
