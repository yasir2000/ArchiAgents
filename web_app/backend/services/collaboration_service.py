"""
ArchiAgents Web Application - Collaboration Service
Real-time collaboration with WebSocket support
"""

import json
import secrets
from datetime import datetime
from typing import Dict, Set, Optional
from fastapi import WebSocket, WebSocketDisconnect, HTTPException, status
from sqlalchemy.orm import Session

from web_app.backend.models import database, schemas
from web_app.backend.services import model_service


# Connection manager for WebSocket connections
class ConnectionManager:
    """Manage WebSocket connections for real-time collaboration"""
    
    def __init__(self):
        # session_token -> set of WebSocket connections
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        # websocket -> user_id mapping
        self.user_mapping: Dict[WebSocket, int] = {}
        # session_token -> model_id mapping
        self.session_models: Dict[str, int] = {}
    
    async def connect(self, websocket: WebSocket, session_token: str, user_id: int, model_id: int):
        """Connect a new WebSocket to a collaboration session"""
        await websocket.accept()
        
        if session_token not in self.active_connections:
            self.active_connections[session_token] = set()
        
        self.active_connections[session_token].add(websocket)
        self.user_mapping[websocket] = user_id
        self.session_models[session_token] = model_id
        
        # Notify others about new participant
        await self.broadcast_to_session(
            session_token,
            {
                "type": "user_joined",
                "user_id": user_id,
                "timestamp": datetime.utcnow().isoformat(),
                "participants": len(self.active_connections[session_token])
            },
            exclude=websocket
        )
    
    def disconnect(self, websocket: WebSocket, session_token: str):
        """Disconnect a WebSocket from a collaboration session"""
        if session_token in self.active_connections:
            self.active_connections[session_token].discard(websocket)
            
            if len(self.active_connections[session_token]) == 0:
                del self.active_connections[session_token]
                if session_token in self.session_models:
                    del self.session_models[session_token]
        
        user_id = self.user_mapping.pop(websocket, None)
        
        # Notify others about participant leaving
        if session_token in self.active_connections and user_id:
            import asyncio
            asyncio.create_task(self.broadcast_to_session(
                session_token,
                {
                    "type": "user_left",
                    "user_id": user_id,
                    "timestamp": datetime.utcnow().isoformat(),
                    "participants": len(self.active_connections[session_token])
                }
            ))
    
    async def send_to_connection(self, websocket: WebSocket, message: dict):
        """Send message to specific WebSocket connection"""
        await websocket.send_json(message)
    
    async def broadcast_to_session(self, session_token: str, message: dict, exclude: Optional[WebSocket] = None):
        """Broadcast message to all connections in a session"""
        if session_token not in self.active_connections:
            return
        
        for connection in self.active_connections[session_token]:
            if connection != exclude:
                try:
                    await connection.send_json(message)
                except:
                    pass  # Connection might be closed
    
    def get_participants(self, session_token: str) -> int:
        """Get number of active participants in a session"""
        if session_token not in self.active_connections:
            return 0
        return len(self.active_connections[session_token])


# Global connection manager
connection_manager = ConnectionManager()


async def create_session(
    session_request: schemas.CollaborationSessionCreate,
    user_id: int,
    db: Session
) -> database.CollaborationSession:
    """Create a new collaboration session"""
    
    # Verify model access
    model = await model_service.get_model(session_request.model_id, user_id, db)
    
    # Generate unique session token
    session_token = secrets.token_urlsafe(32)
    
    # Create session
    db_session = database.CollaborationSession(
        model_id=session_request.model_id,
        owner_id=user_id,
        session_token=session_token,
        is_active=True,
        participants=[user_id],
        created_at=datetime.utcnow()
    )
    
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    
    # Log activity
    await model_service.log_activity(
        user_id=user_id,
        action="create_collaboration",
        resource_type="session",
        resource_id=db_session.id,
        details={"model_id": session_request.model_id, "session_token": session_token},
        db=db
    )
    
    return db_session


async def get_session(
    session_token: str,
    db: Session
) -> database.CollaborationSession:
    """Get collaboration session by token"""
    
    session = db.query(database.CollaborationSession)\
        .filter(database.CollaborationSession.session_token == session_token)\
        .first()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Collaboration session not found"
        )
    
    if not session.is_active:
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail="Collaboration session has ended"
        )
    
    return session


async def end_session(
    session_token: str,
    user_id: int,
    db: Session
) -> None:
    """End a collaboration session"""
    
    session = await get_session(session_token, db)
    
    # Only owner can end session
    if session.owner_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only session owner can end the session"
        )
    
    session.is_active = False
    session.ended_at = datetime.utcnow()
    db.commit()
    
    # Notify all participants
    await connection_manager.broadcast_to_session(
        session_token,
        {
            "type": "session_ended",
            "timestamp": datetime.utcnow().isoformat()
        }
    )


async def handle_websocket(
    websocket: WebSocket,
    session_token: str,
    db: Session
):
    """Handle WebSocket connection for real-time collaboration"""
    
    # Verify session exists and is active
    try:
        session = await get_session(session_token, db)
    except HTTPException:
        await websocket.close(code=1008, reason="Invalid or inactive session")
        return
    
    # For now, we'll use a placeholder user_id
    # In production, you would extract this from the WebSocket connection/auth
    # For example, from a JWT token passed in the WebSocket connection
    user_id = session.owner_id  # Placeholder
    
    # Connect to session
    await connection_manager.connect(websocket, session_token, user_id, session.model_id)
    
    try:
        # Send initial state
        model = db.query(database.ArchitectureModel)\
            .filter(database.ArchitectureModel.id == session.model_id)\
            .first()
        
        await connection_manager.send_to_connection(websocket, {
            "type": "initial_state",
            "model": {
                "id": model.id,
                "name": model.name,
                "elements": model.elements,
                "relationships": model.relationships,
                "version": model.version
            },
            "participants": connection_manager.get_participants(session_token),
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Listen for updates
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Process different message types
            if message.get("type") == "update_element":
                # Update element in model
                element_id = message.get("element_id")
                updates = message.get("updates", {})
                
                # Find and update element
                for elem in model.elements:
                    if elem.get("id") == element_id:
                        elem.update(updates)
                        break
                
                model.updated_at = datetime.utcnow()
                db.commit()
                
                # Broadcast to other participants
                await connection_manager.broadcast_to_session(
                    session_token,
                    {
                        "type": "element_updated",
                        "element_id": element_id,
                        "updates": updates,
                        "user_id": user_id,
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    exclude=websocket
                )
            
            elif message.get("type") == "add_element":
                # Add new element
                element = message.get("element")
                model.elements.append(element)
                model.updated_at = datetime.utcnow()
                db.commit()
                
                # Broadcast to other participants
                await connection_manager.broadcast_to_session(
                    session_token,
                    {
                        "type": "element_added",
                        "element": element,
                        "user_id": user_id,
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    exclude=websocket
                )
            
            elif message.get("type") == "delete_element":
                # Delete element
                element_id = message.get("element_id")
                model.elements = [e for e in model.elements if e.get("id") != element_id]
                model.updated_at = datetime.utcnow()
                db.commit()
                
                # Broadcast to other participants
                await connection_manager.broadcast_to_session(
                    session_token,
                    {
                        "type": "element_deleted",
                        "element_id": element_id,
                        "user_id": user_id,
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    exclude=websocket
                )
            
            elif message.get("type") == "add_relationship":
                # Add new relationship
                relationship = message.get("relationship")
                model.relationships.append(relationship)
                model.updated_at = datetime.utcnow()
                db.commit()
                
                # Broadcast to other participants
                await connection_manager.broadcast_to_session(
                    session_token,
                    {
                        "type": "relationship_added",
                        "relationship": relationship,
                        "user_id": user_id,
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    exclude=websocket
                )
            
            elif message.get("type") == "delete_relationship":
                # Delete relationship
                relationship_id = message.get("relationship_id")
                model.relationships = [r for r in model.relationships if r.get("id") != relationship_id]
                model.updated_at = datetime.utcnow()
                db.commit()
                
                # Broadcast to other participants
                await connection_manager.broadcast_to_session(
                    session_token,
                    {
                        "type": "relationship_deleted",
                        "relationship_id": relationship_id,
                        "user_id": user_id,
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    exclude=websocket
                )
            
            elif message.get("type") == "cursor_move":
                # Broadcast cursor position to others
                await connection_manager.broadcast_to_session(
                    session_token,
                    {
                        "type": "cursor_move",
                        "user_id": user_id,
                        "position": message.get("position"),
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    exclude=websocket
                )
            
            elif message.get("type") == "ping":
                # Respond to ping
                await connection_manager.send_to_connection(websocket, {
                    "type": "pong",
                    "timestamp": datetime.utcnow().isoformat()
                })
    
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket, session_token)
    except Exception as e:
        print(f"WebSocket error: {str(e)}")
        connection_manager.disconnect(websocket, session_token)
        await websocket.close(code=1011, reason="Internal error")
