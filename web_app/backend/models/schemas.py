"""
ArchiAgents Web Application - Pydantic Schemas
Data validation and serialization schemas
"""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, EmailStr, Field, validator
from enum import Enum


# Enums
class UserRole(str, Enum):
    ADMIN = "admin"
    ARCHITECT = "architect"
    BUSINESS_ANALYST = "business_analyst"
    DEVELOPER = "developer"
    VIEWER = "viewer"


class ModelType(str, Enum):
    ARCHIMATE_STRATEGY = "archimate-strategy"
    ARCHIMATE_BUSINESS = "archimate-business"
    ARCHIMATE_APPLICATION = "archimate-application"
    ARCHIMATE_TECHNOLOGY = "archimate-technology"
    ARCHIMATE_PHYSICAL = "archimate-physical"
    ARCHIMATE_IMPLEMENTATION = "archimate-implementation"
    ARCHIMATE_MULTI_LAYER = "archimate-multi-layer"
    BPMN_PROCESS = "bpmn-process"
    BPMN_COLLABORATION = "bpmn-collaboration"
    BPMN_CHOREOGRAPHY = "bpmn-choreography"
    UML_CLASS = "uml-class"
    UML_SEQUENCE = "uml-sequence"
    UML_USE_CASE = "uml-use-case"
    UML_ACTIVITY = "uml-activity"
    UML_STATE_MACHINE = "uml-state-machine"
    UML_COMPONENT = "uml-component"
    UML_DEPLOYMENT = "uml-deployment"


class ModelStatus(str, Enum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    PUBLISHED = "published"
    ARCHIVED = "archived"


# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=255)
    role: UserRole = UserRole.VIEWER


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=72)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    last_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str


# Authentication Schemas
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: User


class TokenData(BaseModel):
    username: Optional[str] = None


class LoginRequest(BaseModel):
    username: str
    password: str


# Project Schemas
class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    togaf_phase: Optional[str] = None
    status: str = "active"


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    togaf_phase: Optional[str] = None
    status: Optional[str] = None


class Project(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ProjectWithModels(Project):
    models: List['ArchitectureModel'] = []


# Architecture Model Schemas
class ModelElement(BaseModel):
    id: str
    type: str
    name: str
    description: Optional[str] = None
    properties: Dict[str, Any] = {}
    position: Optional[Dict[str, float]] = None  # x, y coordinates


class ModelRelationship(BaseModel):
    id: str
    type: str
    name: Optional[str] = None
    source: str  # Element ID
    target: str  # Element ID
    properties: Dict[str, Any] = {}


class ArchitectureModelBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    model_type: ModelType
    status: ModelStatus = ModelStatus.DRAFT
    elements: List[ModelElement] = []
    relationships: List[ModelRelationship] = []
    metadata: Dict[str, Any] = {}


class ArchitectureModelCreate(ArchitectureModelBase):
    project_id: int


class ArchitectureModelUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ModelStatus] = None
    elements: Optional[List[ModelElement]] = None
    relationships: Optional[List[ModelRelationship]] = None
    metadata: Optional[Dict[str, Any]] = None


class ArchitectureModel(ArchitectureModelBase):
    id: int
    project_id: int
    version: str
    generated_by_ai: bool
    compliance_score: Optional[int] = None
    created_by: int
    created_at: datetime
    updated_at: datetime
    published_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ArchitectureModelWithDetails(ArchitectureModel):
    created_by_user: User
    project: Project


# AI Generation Schemas
class AIGenerationRequest(BaseModel):
    project_id: int
    model_type: ModelType
    name: str
    description: Optional[str] = None
    prompt: Optional[str] = None
    use_project_context: bool = True
    togaf_phase: Optional[str] = None


class AIGenerationResponse(BaseModel):
    model: ArchitectureModel
    generation_time: float
    elements_generated: int
    relationships_generated: int
    suggestions: List[str] = []


# Model Validation Schemas
class ValidationIssue(BaseModel):
    severity: str  # error, warning, info
    message: str
    element_id: Optional[str] = None
    suggestion: Optional[str] = None


class ValidationResult(BaseModel):
    model_id: int
    compliance_score: int = Field(..., ge=0, le=100)
    standards: List[str]
    issues: List[ValidationIssue]
    summary: str


# Export Schemas
class ModelExportRequest(BaseModel):
    model_id: int
    format: str  # mermaid, archi, ea, gojs, kroki, text


class ModelExportResponse(BaseModel):
    model_id: int
    format: str
    content: str
    file_path: Optional[str] = None
    created_at: datetime


# Collaboration Schemas
class CollaborationSessionCreate(BaseModel):
    model_id: int


class CollaborationSession(BaseModel):
    id: int
    model_id: int
    owner_id: int
    session_token: str
    is_active: bool
    participants: List[int] = []
    created_at: datetime
    
    class Config:
        from_attributes = True


class CollaborationUpdate(BaseModel):
    action: str  # add_element, update_element, delete_element, add_relationship, etc.
    data: Dict[str, Any]
    user_id: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# Comment Schemas
class CommentBase(BaseModel):
    content: str
    element_id: Optional[str] = None


class CommentCreate(CommentBase):
    model_id: int


class Comment(CommentBase):
    id: int
    model_id: int
    user_id: int
    resolved: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class CommentWithUser(Comment):
    user: User


# Dashboard Schemas
class DashboardStats(BaseModel):
    total_projects: int
    total_models: int
    models_by_type: Dict[str, int]
    models_by_status: Dict[str, int]
    recent_activity: List[Dict[str, Any]]
    team_members: int


# Search Schemas
class SearchRequest(BaseModel):
    query: str
    filters: Optional[Dict[str, Any]] = None
    page: int = 1
    page_size: int = 20


class SearchResult(BaseModel):
    total: int
    page: int
    page_size: int
    results: List[Dict[str, Any]]


# Activity Log Schema
class ActivityLog(BaseModel):
    id: int
    user_id: Optional[int]
    action: str
    resource_type: str
    resource_id: Optional[int]
    details: Dict[str, Any]
    created_at: datetime
    
    class Config:
        from_attributes = True


# Update forward references
ProjectWithModels.model_rebuild()
ArchitectureModelWithDetails.model_rebuild()
CommentWithUser.model_rebuild()
