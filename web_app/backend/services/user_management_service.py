"""
ArchiAgents Web Application - User Management Service
Handles user administration, invitations, and role management
"""

import secrets
from datetime import datetime, timedelta
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import database, schemas
from services.auth_service import AuthService


class UserManagementService:
    """Service for user administration"""
    
    @staticmethod
    def list_users(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        role_filter: Optional[database.UserRole] = None,
        search: Optional[str] = None
    ) -> List[database.User]:
        """List all users with optional filters"""
        query = db.query(database.User)
        
        if role_filter:
            query = query.filter(database.User.role == role_filter)
        
        if search:
            search_pattern = f"%{search}%"
            query = query.filter(
                (database.User.name.ilike(search_pattern)) |
                (database.User.email.ilike(search_pattern))
            )
        
        users = query.order_by(database.User.created_at.desc()).offset(skip).limit(limit).all()
        return users
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[database.User]:
        """Get user by ID"""
        return db.query(database.User).filter(database.User.id == user_id).first()
    
    @staticmethod
    def update_user_role(
        db: Session,
        user_id: int,
        new_role: database.UserRole,
        updated_by: database.User
    ) -> database.User:
        """Update user role (admin only)"""
        # Check if updater is admin
        if updated_by.role != database.UserRole.ADMIN:
            raise HTTPException(status_code=403, detail="Admin access required")
        
        user = UserManagementService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Don't allow changing own role
        if user.id == updated_by.id:
            raise HTTPException(status_code=400, detail="Cannot change your own role")
        
        old_role = user.role
        user.role = new_role
        user.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(user)
        
        # Log activity
        activity = database.ActivityLog(
            user_id=updated_by.id,
            action="update_user_role",
            resource_type="user",
            resource_id=user_id,
            details={
                "old_role": old_role.value,
                "new_role": new_role.value,
                "target_user": user.email
            }
        )
        db.add(activity)
        db.commit()
        
        return user
    
    @staticmethod
    def deactivate_user(
        db: Session,
        user_id: int,
        deactivated_by: database.User
    ) -> database.User:
        """Deactivate user account"""
        if deactivated_by.role != database.UserRole.ADMIN:
            raise HTTPException(status_code=403, detail="Admin access required")
        
        user = UserManagementService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if user.id == deactivated_by.id:
            raise HTTPException(status_code=400, detail="Cannot deactivate your own account")
        
        user.is_active = False
        user.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(user)
        
        return user
    
    @staticmethod
    def delete_user(
        db: Session,
        user_id: int,
        deleted_by: database.User
    ) -> bool:
        """Permanently delete user (admin only)"""
        if deleted_by.role != database.UserRole.ADMIN:
            raise HTTPException(status_code=403, detail="Admin access required")
        
        user = UserManagementService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if user.id == deleted_by.id:
            raise HTTPException(status_code=400, detail="Cannot delete your own account")
        
        # Log before deletion
        activity = database.ActivityLog(
            user_id=deleted_by.id,
            action="delete_user",
            resource_type="user",
            resource_id=user_id,
            details={
                "deleted_user": user.email,
                "deleted_user_name": user.name
            }
        )
        db.add(activity)
        
        # Delete user
        db.delete(user)
        db.commit()
        
        return True
    
    @staticmethod
    def create_invitation(
        db: Session,
        email: str,
        role: database.UserRole,
        invited_by: database.User
    ) -> database.UserInvitation:
        """Create user invitation"""
        if invited_by.role != database.UserRole.ADMIN:
            raise HTTPException(status_code=403, detail="Admin access required")
        
        # Check if user already exists
        existing_user = db.query(database.User).filter(database.User.email == email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User with this email already exists")
        
        # Check if invitation already exists and is not expired
        existing_invitation = db.query(database.UserInvitation).filter(
            database.UserInvitation.email == email,
            database.UserInvitation.accepted == False,
            database.UserInvitation.expires_at > datetime.utcnow()
        ).first()
        
        if existing_invitation:
            raise HTTPException(status_code=400, detail="Active invitation already exists for this email")
        
        # Generate secure token
        token = secrets.token_urlsafe(32)
        
        # Create invitation (expires in 7 days)
        invitation = database.UserInvitation(
            email=email,
            role=role,
            invited_by=invited_by.id,
            token=token,
            expires_at=datetime.utcnow() + timedelta(days=7)
        )
        
        db.add(invitation)
        db.commit()
        db.refresh(invitation)
        
        # Log activity
        activity = database.ActivityLog(
            user_id=invited_by.id,
            action="invite_user",
            resource_type="invitation",
            resource_id=invitation.id,
            details={
                "email": email,
                "role": role.value
            }
        )
        db.add(activity)
        db.commit()
        
        # TODO: Send email invitation
        print(f"Invitation created for {email} with token: {token}")
        print(f"Invitation link: /accept-invitation?token={token}")
        
        return invitation
    
    @staticmethod
    def get_invitation_by_token(db: Session, token: str) -> Optional[database.UserInvitation]:
        """Get invitation by token"""
        invitation = db.query(database.UserInvitation).filter(
            database.UserInvitation.token == token,
            database.UserInvitation.accepted == False,
            database.UserInvitation.expires_at > datetime.utcnow()
        ).first()
        return invitation
    
    @staticmethod
    def accept_invitation(
        db: Session,
        token: str,
        name: str,
        password: str
    ) -> database.User:
        """Accept invitation and create user account"""
        invitation = UserManagementService.get_invitation_by_token(db, token)
        
        if not invitation:
            raise HTTPException(status_code=400, detail="Invalid or expired invitation")
        
        # Create user
        hashed_password = AuthService.get_password_hash(password)
        user = database.User(
            email=invitation.email,
            name=name,
            hashed_password=hashed_password,
            role=invitation.role,
            is_active=True
        )
        
        db.add(user)
        
        # Mark invitation as accepted
        invitation.accepted = True
        
        db.commit()
        db.refresh(user)
        
        # Log activity
        activity = database.ActivityLog(
            user_id=user.id,
            action="accept_invitation",
            resource_type="user",
            resource_id=user.id,
            details={
                "email": user.email,
                "role": user.role.value
            }
        )
        db.add(activity)
        db.commit()
        
        return user
    
    @staticmethod
    def list_pending_invitations(
        db: Session,
        invited_by: Optional[database.User] = None
    ) -> List[database.UserInvitation]:
        """List pending invitations"""
        query = db.query(database.UserInvitation).filter(
            database.UserInvitation.accepted == False,
            database.UserInvitation.expires_at > datetime.utcnow()
        )
        
        if invited_by and invited_by.role != database.UserRole.ADMIN:
            # Non-admins can only see their own invitations
            query = query.filter(database.UserInvitation.invited_by == invited_by.id)
        
        invitations = query.order_by(database.UserInvitation.created_at.desc()).all()
        return invitations
    
    @staticmethod
    def cancel_invitation(
        db: Session,
        invitation_id: int,
        cancelled_by: database.User
    ) -> bool:
        """Cancel a pending invitation"""
        invitation = db.query(database.UserInvitation).filter(
            database.UserInvitation.id == invitation_id
        ).first()
        
        if not invitation:
            raise HTTPException(status_code=404, detail="Invitation not found")
        
        # Check permissions
        if cancelled_by.role != database.UserRole.ADMIN and invitation.invited_by != cancelled_by.id:
            raise HTTPException(status_code=403, detail="Can only cancel your own invitations")
        
        db.delete(invitation)
        db.commit()
        
        return True


def get_user_management_service():
    """Dependency injection for user management service"""
    return UserManagementService()
