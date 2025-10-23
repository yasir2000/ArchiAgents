"""
ArchiAgents Web Application - Notification Service
Handles user notifications and alerts
"""

from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from models import database, schemas


class NotificationService:
    """Service for managing user notifications"""
    
    @staticmethod
    def create_notification(
        db: Session,
        user_id: int,
        notification_type: database.NotificationType,
        title: str,
        message: str,
        link: Optional[str] = None
    ) -> database.Notification:
        """Create a new notification"""
        notification = database.Notification(
            user_id=user_id,
            type=notification_type,
            title=title,
            message=message,
            link=link
        )
        db.add(notification)
        db.commit()
        db.refresh(notification)
        return notification
    
    @staticmethod
    def get_user_notifications(
        db: Session,
        user_id: int,
        unread_only: bool = False,
        limit: int = 50,
        offset: int = 0
    ) -> List[database.Notification]:
        """Get notifications for a user"""
        query = db.query(database.Notification).filter(
            database.Notification.user_id == user_id
        )
        
        if unread_only:
            query = query.filter(database.Notification.read == False)
        
        notifications = query.order_by(
            database.Notification.created_at.desc()
        ).offset(offset).limit(limit).all()
        
        return notifications
    
    @staticmethod
    def get_unread_count(db: Session, user_id: int) -> int:
        """Get count of unread notifications"""
        count = db.query(database.Notification).filter(
            database.Notification.user_id == user_id,
            database.Notification.read == False
        ).count()
        return count
    
    @staticmethod
    def mark_as_read(
        db: Session,
        notification_id: int,
        user_id: int
    ) -> database.Notification:
        """Mark a notification as read"""
        notification = db.query(database.Notification).filter(
            database.Notification.id == notification_id,
            database.Notification.user_id == user_id
        ).first()
        
        if not notification:
            raise HTTPException(status_code=404, detail="Notification not found")
        
        notification.read = True
        db.commit()
        db.refresh(notification)
        return notification
    
    @staticmethod
    def mark_all_as_read(db: Session, user_id: int) -> int:
        """Mark all notifications as read for a user"""
        result = db.query(database.Notification).filter(
            database.Notification.user_id == user_id,
            database.Notification.read == False
        ).update({"read": True})
        db.commit()
        return result
    
    @staticmethod
    def delete_notification(
        db: Session,
        notification_id: int,
        user_id: int
    ) -> bool:
        """Delete a notification"""
        notification = db.query(database.Notification).filter(
            database.Notification.id == notification_id,
            database.Notification.user_id == user_id
        ).first()
        
        if not notification:
            raise HTTPException(status_code=404, detail="Notification not found")
        
        db.delete(notification)
        db.commit()
        return True
    
    @staticmethod
    def clear_all_notifications(db: Session, user_id: int) -> int:
        """Delete all notifications for a user"""
        result = db.query(database.Notification).filter(
            database.Notification.user_id == user_id
        ).delete()
        db.commit()
        return result
    
    @staticmethod
    def notify_model_created(
        db: Session,
        model: database.ArchitectureModel,
        created_by: database.User
    ):
        """Notify relevant users about new model"""
        # Notify project owner if different from creator
        project = model.project
        if project.owner_id != created_by.id:
            NotificationService.create_notification(
                db=db,
                user_id=project.owner_id,
                notification_type=database.NotificationType.INFO,
                title="New Model Created",
                message=f"{created_by.name} created model '{model.name}' in project '{project.name}'",
                link=f"/projects/{project.id}/models/{model.id}"
            )
    
    @staticmethod
    def notify_model_updated(
        db: Session,
        model: database.ArchitectureModel,
        updated_by: database.User
    ):
        """Notify relevant users about model update"""
        project = model.project
        if project.owner_id != updated_by.id:
            NotificationService.create_notification(
                db=db,
                user_id=project.owner_id,
                notification_type=database.NotificationType.INFO,
                title="Model Updated",
                message=f"{updated_by.name} updated model '{model.name}'",
                link=f"/projects/{project.id}/models/{model.id}"
            )
    
    @staticmethod
    def notify_comment_added(
        db: Session,
        comment: database.Comment,
        model: database.ArchitectureModel,
        commenter: database.User
    ):
        """Notify relevant users about new comment"""
        # Notify model creator if different from commenter
        if model.created_by != commenter.id:
            NotificationService.create_notification(
                db=db,
                user_id=model.created_by,
                notification_type=database.NotificationType.INFO,
                title="New Comment",
                message=f"{commenter.name} commented on '{model.name}'",
                link=f"/projects/{model.project_id}/models/{model.id}#comment-{comment.id}"
            )
    
    @staticmethod
    def notify_user_invited(
        db: Session,
        invitation: database.UserInvitation
    ):
        """Notify admin about new invitation sent"""
        inviter = db.query(database.User).filter(
            database.User.id == invitation.invited_by
        ).first()
        
        # For now, just log. In production, send email
        print(f"Invitation sent to {invitation.email} by {inviter.name}")


def get_notification_service():
    """Dependency injection for notification service"""
    return NotificationService()
