"""
ArchiAgents Web Application - Database Models
SQLAlchemy ORM models for the enterprise architecture web platform
"""

from datetime import datetime
from typing import Optional, List
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, JSON, Boolean, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()


class UserRole(str, enum.Enum):
    """User roles in the system"""
    ADMIN = "admin"
    ARCHITECT = "architect"
    BUSINESS_ANALYST = "business_analyst"
    DEVELOPER = "developer"
    VIEWER = "viewer"


class ModelType(str, enum.Enum):
    """Architecture model types"""
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


class ModelStatus(str, enum.Enum):
    """Model lifecycle status"""
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class User(Base):
    """User model with role-based access"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(SQLEnum(UserRole), default=UserRole.VIEWER)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Relationships
    projects = relationship("Project", back_populates="owner", cascade="all, delete-orphan")
    models = relationship("ArchitectureModel", back_populates="created_by_user")
    comments = relationship("Comment", back_populates="user")
    sessions = relationship("CollaborationSession", back_populates="owner")


class Project(Base):
    """Enterprise architecture project"""
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    togaf_phase = Column(String(50))  # Phase A-H
    status = Column(String(50), default="active")
    project_metadata = Column(JSON)  # Additional project metadata (renamed from metadata to avoid SQLAlchemy conflict)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    owner = relationship("User", back_populates="projects")
    models = relationship("ArchitectureModel", back_populates="project", cascade="all, delete-orphan")
    team_members = relationship("ProjectMember", back_populates="project", cascade="all, delete-orphan")


class ProjectMember(Base):
    """Project team members with roles"""
    __tablename__ = "project_members"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String(50))  # Lead Architect, Business Analyst, etc.
    permissions = Column(JSON)  # Custom permissions
    joined_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("Project", back_populates="team_members")
    user = relationship("User")


class ArchitectureModel(Base):
    """Architecture model (ArchiMate, BPMN, UML)"""
    __tablename__ = "architecture_models"
    
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    model_type = Column(SQLEnum(ModelType), nullable=False)
    status = Column(SQLEnum(ModelStatus), default=ModelStatus.DRAFT)
    
    # Model content
    elements = Column(JSON, nullable=False)  # Model elements (nodes)
    relationships = Column(JSON, nullable=False)  # Relationships (edges)
    model_metadata = Column(JSON)  # Additional model metadata (renamed from metadata to avoid SQLAlchemy conflict)
    
    # Versioning
    version = Column(String(50), default="1.0.0")
    parent_version_id = Column(Integer, ForeignKey("architecture_models.id"), nullable=True)
    
    # AI Generation
    generated_by_ai = Column(Boolean, default=False)
    ai_generation_prompt = Column(Text, nullable=True)
    compliance_score = Column(Integer, nullable=True)  # 0-100
    
    # Audit
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime, nullable=True)
    
    # Relationships
    project = relationship("Project", back_populates="models")
    created_by_user = relationship("User", back_populates="models")
    versions = relationship("ArchitectureModel", remote_side=[parent_version_id])
    comments = relationship("Comment", back_populates="model", cascade="all, delete-orphan")
    exports = relationship("ModelExport", back_populates="model", cascade="all, delete-orphan")


class Comment(Base):
    """Comments on architecture models"""
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("architecture_models.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    element_id = Column(String(100), nullable=True)  # Specific element being commented on
    resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    model = relationship("ArchitectureModel", back_populates="comments")
    user = relationship("User", back_populates="comments")


class ModelExport(Base):
    """Exported model formats"""
    __tablename__ = "model_exports"
    
    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("architecture_models.id"), nullable=False)
    format = Column(String(50), nullable=False)  # mermaid, archi, ea, gojs, etc.
    content = Column(Text, nullable=False)
    file_path = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    model = relationship("ArchitectureModel", back_populates="exports")


class CollaborationSession(Base):
    """Real-time collaboration sessions"""
    __tablename__ = "collaboration_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(Integer, ForeignKey("architecture_models.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_token = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    participants = Column(JSON)  # List of user IDs
    created_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    
    # Relationships
    model = relationship("ArchitectureModel")
    owner = relationship("User", back_populates="sessions")


class ActivityLog(Base):
    """Audit log for all activities"""
    __tablename__ = "activity_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String(100), nullable=False)  # create, update, delete, export, etc.
    resource_type = Column(String(50))  # model, project, user, etc.
    resource_id = Column(Integer)
    details = Column(JSON)
    ip_address = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User")


class NotificationType(str, enum.Enum):
    """Notification types"""
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


class Notification(Base):
    """User notifications"""
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(SQLEnum(NotificationType), default=NotificationType.INFO)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    read = Column(Boolean, default=False)
    link = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User")


class UserInvitation(Base):
    """Pending user invitations"""
    __tablename__ = "user_invitations"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    role = Column(SQLEnum(UserRole), default=UserRole.VIEWER)
    invited_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String(255), unique=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    accepted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    inviter = relationship("User")
