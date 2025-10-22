# ArchiAgents Web Application - Implementation Guide

## 🚀 Overview

The **ArchiAgents Web Application** is a comprehensive full-stack enterprise architecture platform that provides:

- **Visual Diagram Editor** for ArchiMate, BPMN, and UML models
- **AI-Powered Model Generation** using existing AI agents
- **Real-time Collaboration** with WebSocket support
- **Role-Based Access Control** for enterprise teams
- **CLI Integration** for power users
- **Multi-Format Export** (Mermaid, Archi, EA, GoJS, etc.)
- **TOGAF 10 Integration** for methodology compliance

## 📁 Project Structure

```
web_app/
├── backend/                    # FastAPI Backend
│   ├── main.py                # Main FastAPI application
│   ├── requirements.txt       # Python dependencies
│   ├── api/                   # API utilities
│   │   └── database_manager.py
│   ├── models/                # Data models
│   │   ├── database.py       # SQLAlchemy ORM models
│   │   └── schemas.py        # Pydantic validation schemas
│   └── services/             # Business logic
│       ├── auth_service.py   # Authentication & JWT
│       ├── model_service.py  # Model CRUD operations (TO IMPLEMENT)
│       ├── ai_service.py     # AI generation integration (TO IMPLEMENT)
│       └── collaboration_service.py # WebSocket collaboration (TO IMPLEMENT)
├── frontend/                  # React Frontend (TO IMPLEMENT)
│   ├── public/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API client
│   │   ├── hooks/           # Custom React hooks
│   │   └── utils/           # Utilities
│   ├── package.json
│   └── vite.config.ts
└── data/                     # Database files (auto-created)
    └── archiagents.db       # SQLite database
```

## 🎯 Features Implemented (Backend)

### ✅ Complete

1. **Database Schema** (`models/database.py`)
   - Users with role-based access
   - Projects for organizing models
   - Architecture Models (21 types)
   - Comments and collaboration
   - Model exports
   - Activity logs
   - Version control

2. **API Schemas** (`models/schemas.py`)
   - Pydantic models for validation
   - Request/Response schemas
   - Type safety throughout

3. **FastAPI Application** (`main.py`)
   - 40+ API endpoints
   - RESTful design
   - Auto-generated API documentation
   - CORS configuration
   - WebSocket support for collaboration

4. **Authentication Service** (`services/auth_service.py`)
   - JWT token-based auth
   - Password hashing with bcrypt
   - User registration/login
   - Role-based access control

### 🔨 To Implement

1. **Model Service** (`services/model_service.py`)
   - CRUD operations for projects and models
   - Integration with existing model_generation system
   - Export functionality
   - Dashboard statistics

2. **AI Service** (`services/ai_service.py`)
   - Integration with existing AI agents
   - Model generation
   - Validation and improvement suggestions
   - Context-aware generation

3. **Collaboration Service** (`services/collaboration_service.py`)
   - WebSocket handler
   - Real-time updates
   - Conflict resolution
   - Presence tracking

4. **Frontend Application** (React + GoJS)
   - Visual diagram editor
   - Model browser
   - AI generation wizard
   - Dashboard
   - Collaboration UI

## 🗄️ Database Schema

### Users Table
- Role-based access (Admin, Architect, Business Analyst, Developer, Viewer)
- JWT authentication
- Activity tracking

### Projects Table
- Hierarchical organization
- TOGAF phase tracking
- Team collaboration

### Architecture Models Table
- 21 model types (ArchiMate, BPMN, UML)
- JSON storage for elements and relationships
- Version control
- AI generation metadata
- Compliance scoring

### Supporting Tables
- Comments (model feedback)
- Model Exports (cached formats)
- Collaboration Sessions (real-time editing)
- Activity Logs (audit trail)

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get token
- `GET /api/auth/me` - Get current user
- `PUT /api/auth/me` - Update user profile

### Projects
- `GET /api/projects` - List projects
- `POST /api/projects` - Create project
- `GET /api/projects/{id}` - Get project details
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

### Models
- `GET /api/models` - List models (with filters)
- `POST /api/models` - Create model
- `GET /api/models/{id}` - Get model
- `PUT /api/models/{id}` - Update model
- `DELETE /api/models/{id}` - Delete model

### AI Generation
- `POST /api/ai/generate` - Generate model with AI
- `POST /api/ai/improve/{id}` - Get improvement suggestions
- `POST /api/ai/validate/{id}` - Validate against standards

### Export
- `POST /api/export` - Export model to format
- `GET /api/export/{id}/formats` - Get available formats

### Collaboration
- `POST /api/collaboration/sessions` - Create session
- `GET /api/collaboration/sessions/{token}` - Get session
- `WS /ws/collaboration/{token}` - WebSocket connection

### Dashboard
- `GET /api/dashboard/stats` - Get statistics
- `GET /api/dashboard/recent-activity` - Recent activity

### Comments
- `GET /api/models/{id}/comments` - Get comments
- `POST /api/comments` - Create comment

### Search
- `POST /api/search` - Search across projects/models

## 🚀 Getting Started

### Backend Setup

1. **Install Dependencies**
```bash
cd web_app/backend
pip install -r requirements.txt
```

2. **Run Backend Server**
```bash
python main.py
```

Server starts at `http://localhost:8000`

3. **Access API Documentation**
- Swagger UI: `http://localhost:8000/api/docs`
- ReDoc: `http://localhost:8000/api/redoc`

### Frontend Setup (To Be Implemented)

```bash
cd web_app/frontend
npm install
npm run dev
```

Frontend will run at `http://localhost:3000`

## 🎨 Frontend Architecture (Planned)

### Technology Stack
- **React 18** with TypeScript
- **Vite** for build tooling
- **GoJS** for visual diagram editing
- **TailwindCSS** for styling
- **React Query** for data fetching
- **Zustand** for state management
- **React Router** for navigation

### Key Components

1. **Dashboard**
   - Project overview
   - Recent activity
   - Quick actions
   - Statistics

2. **Visual Diagram Editor**
   - GoJS integration
   - Drag-and-drop interface
   - Context menus
   - Properties panel
   - Toolbar with tools

3. **Model Browser**
   - Tree view of models
   - Filter and search
   - Quick preview
   - Bulk operations

4. **AI Generation Wizard**
   - Step-by-step wizard
   - Model type selection
   - AI prompting
   - Preview before save

5. **Collaboration View**
   - Real-time cursors
   - Change highlights
   - Chat integration
   - Conflict resolution

## 🔧 Integration with Existing Systems

### Model Generation System
```python
# In ai_service.py
from model_generation import ModelGenerationEngine, AIModelingAgent

engine = ModelGenerationEngine()
ai_agent = AIModelingAgent()

# Generate model using existing system
model = await ai_agent.generate_archimate_model_with_ai(...)
```

### CLI Integration
```python
# CLI can call web API
import requests

response = requests.post(
    "http://localhost:8000/api/ai/generate",
    headers={"Authorization": f"Bearer {token}"},
    json={
        "project_id": 1,
        "model_type": "archimate-business",
        "name": "Customer Management"
    }
)
```

## 🔐 Security Features

1. **JWT Authentication**
   - Secure token-based auth
   - 30-minute expiration
   - Refresh token support (to implement)

2. **Password Hashing**
   - Bcrypt algorithm
   - Salt per user

3. **Role-Based Access Control**
   - Admin, Architect, Business Analyst, Developer, Viewer
   - Permission checks on all endpoints

4. **CORS Configuration**
   - Whitelist allowed origins
   - Secure cookie handling

5. **SQL Injection Protection**
   - SQLAlchemy ORM
   - Parameterized queries

## 📊 Visual Editor Capabilities (Planned)

### ArchiMate Diagrams
- Strategy layer (capabilities, value streams)
- Business layer (processes, actors, services)
- Application layer (components, interfaces)
- Technology layer (nodes, devices)
- Multi-layer views
- Drag-and-drop elements
- Relationship creation
- Element properties editing

### BPMN Diagrams
- Pools and lanes
- Tasks (user, service, script)
- Events (start, intermediate, end)
- Gateways (exclusive, parallel, inclusive)
- Sequence flows
- Message flows

### UML Diagrams
- Class diagrams with attributes/methods
- Sequence diagrams with lifelines
- Use case diagrams
- Activity diagrams
- State machine diagrams

### Editor Features
- Zoom and pan
- Minimap navigator
- Undo/redo
- Copy/paste
- Align and distribute tools
- Auto-layout algorithms
- Export to image
- Print support

## 🤝 Collaboration Features (Planned)

1. **Real-Time Editing**
   - WebSocket connections
   - Operational transformation
   - Conflict resolution

2. **Presence Awareness**
   - See who's online
   - User cursors
   - Active element indicators

3. **Comments & Discussions**
   - Comment on specific elements
   - Reply threads
   - Resolve discussions

4. **Version Control**
   - Save versions
   - Compare versions
   - Restore previous versions
   - Branch and merge

## 📈 Dashboard Analytics (Planned)

- Total projects/models
- Models by type (pie chart)
- Models by status (bar chart)
- Recent activity timeline
- Team member activity
- Compliance scores trend
- Usage statistics

## 🎯 User Roles & Permissions

### Admin
- Full system access
- User management
- System configuration

### Architect
- Create/edit all models
- Project management
- AI generation
- Export all formats
- Collaboration

### Business Analyst
- Create/edit business models
- Comment on all models
- View all models
- Export business formats

### Developer
- Create/edit UML models
- View all models
- Export technical formats

### Viewer
- View all models
- Comment on models
- Export read-only formats

## 🚧 Implementation Roadmap

### Phase 1: Backend Foundation ✅ (CURRENT)
- [x] Database schema
- [x] API schemas
- [x] FastAPI application
- [x] Authentication service
- [ ] Model service
- [ ] AI service
- [ ] Collaboration service

### Phase 2: Core Services (NEXT)
- [ ] Complete model_service.py
- [ ] Complete ai_service.py
- [ ] Complete collaboration_service.py
- [ ] Testing suite
- [ ] API documentation

### Phase 3: Frontend Foundation
- [ ] React project setup
- [ ] Component library
- [ ] API client
- [ ] Authentication flow
- [ ] Routing

### Phase 4: Visual Editor
- [ ] GoJS integration
- [ ] ArchiMate palette
- [ ] BPMN palette
- [ ] UML palettes
- [ ] Properties panel

### Phase 5: Collaboration
- [ ] WebSocket client
- [ ] Real-time updates
- [ ] Presence tracking
- [ ] Comments UI

### Phase 6: Polish & Production
- [ ] Performance optimization
- [ ] Security audit
- [ ] User testing
- [ ] Documentation
- [ ] Deployment guide

## 📚 Next Steps

1. **Complete Backend Services**
   ```bash
   # Create these files:
   web_app/backend/services/model_service.py
   web_app/backend/services/ai_service.py
   web_app/backend/services/collaboration_service.py
   ```

2. **Frontend Scaffolding**
   ```bash
   npm create vite@latest frontend -- --template react-ts
   cd frontend
   npm install
   npm install gojs react-router-dom @tanstack/react-query zustand
   npm install -D tailwindcss postcss autoprefixer
   ```

3. **Test Backend API**
   ```bash
   # Install httpie or use curl
   http POST http://localhost:8000/api/auth/register \
     email=architect@example.com \
     username=architect \
     password=securepass123 \
     role=architect
   ```

4. **Integration Testing**
   - Test CLI → Web API integration
   - Test AI generation through API
   - Test model export formats

## 🎉 Benefits

- **10x Faster Modeling** with visual drag-and-drop
- **AI-Powered** intelligent model generation
- **Real-Time Collaboration** for distributed teams
- **Standards Compliant** ArchiMate 3.0, TOGAF 10, UML 2.0
- **Multi-Format Export** for tool interoperability
- **Enterprise Ready** with RBAC and audit logs
- **CLI Integration** for power users and automation
- **Cloud-Ready** architecture for scalability

---

**ArchiAgents Web Platform - Enterprise Architecture Made Visual and Collaborative** 🚀
