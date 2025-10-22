# ArchiAgents Web Application 🚀

**Enterprise Architecture Modeling Platform with Visual Design & AI-Powered Generation**

## Overview

The ArchiAgents Web Application is a full-stack enterprise architecture platform that brings together:

- 🎨 **Visual Diagram Editor** - Drag-and-drop interface for ArchiMate, BPMN, and UML models
- 🤖 **AI-Powered Generation** - Intelligent model creation using LLM agents
- 👥 **Real-Time Collaboration** - Work together with your team in real-time
- 🔐 **Role-Based Access** - Enterprise-grade security and permissions
- 💻 **CLI Integration** - Seamless integration with ArchiAgents CLI
- 📊 **Dashboard Analytics** - Track progress and compliance
- 📤 **Multi-Format Export** - Export to Mermaid, Archi, Enterprise Architect, GoJS, and more

## Features

### ✅ Implemented (Phase 1 - Backend Foundation)

- **Backend API** - FastAPI with 40+ endpoints
- **Database Schema** - SQLAlchemy ORM with 9 tables
- **Authentication** - JWT token-based with bcrypt password hashing
- **API Documentation** - Auto-generated Swagger UI and ReDoc
- **CORS Support** - Configured for frontend integration
- **WebSocket Ready** - Infrastructure for real-time collaboration

### 🔨 In Progress

- **Model Service** - CRUD operations and integration
- **AI Service** - Integration with existing AI agents
- **Collaboration Service** - Real-time WebSocket handlers

### 📋 Planned (Phase 2-6)

- **Frontend Application** - React + TypeScript + GoJS
- **Visual Diagram Editor** - Full-featured modeling interface
- **Dashboard** - Analytics and project management
- **Real-Time Collaboration** - Multi-user editing
- **Export System** - All supported formats
- **Mobile Support** - Responsive design

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (React)                     │
│  ┌─────────────┬──────────────┬────────────────────┐  │
│  │  Dashboard  │ Visual Editor│  AI Generation     │  │
│  │             │   (GoJS)     │     Wizard         │  │
│  └─────────────┴──────────────┴────────────────────┘  │
│                         ↕                               │
│                    REST API / WebSocket                 │
│                         ↕                               │
│                  Backend (FastAPI)                      │
│  ┌─────────────┬──────────────┬────────────────────┐  │
│  │Auth Service │Model Service │ AI Service         │  │
│  └─────────────┴──────────────┴────────────────────┘  │
│                         ↕                               │
│  ┌─────────────┬──────────────┬────────────────────┐  │
│  │  Database   │Model Engine  │ AI Agents          │  │
│  │  (SQLite)   │(Existing)    │(Existing)          │  │
│  └─────────────┴──────────────┴────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+ (for frontend when implemented)
- pip (Python package manager)

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd web_app/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python main.py
   ```

   The server will start at `http://localhost:8000`

5. **Access API Documentation**
   - Swagger UI: http://localhost:8000/api/docs
   - ReDoc: http://localhost:8000/api/redoc

### Test the API

**Register a User:**
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "architect@example.com",
    "username": "architect",
    "password": "secure123",
    "full_name": "Enterprise Architect",
    "role": "architect"
  }'
```

**Login:**
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -d "username=architect&password=secure123"
```

**Create a Project:**
```bash
curl -X POST http://localhost:8000/api/projects \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Digital Transformation",
    "description": "Enterprise-wide digital transformation initiative",
    "togaf_phase": "Phase B"
  }'
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token
- `GET /api/auth/me` - Get current user profile
- `PUT /api/auth/me` - Update user profile

### Projects
- `GET /api/projects` - List all projects
- `POST /api/projects` - Create new project
- `GET /api/projects/{id}` - Get project with models
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

### Models
- `GET /api/models` - List models (filterable)
- `POST /api/models` - Create model
- `GET /api/models/{id}` - Get model details
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
- `POST /api/collaboration/sessions` - Create collaboration session
- `GET /api/collaboration/sessions/{token}` - Get session info
- `WS /ws/collaboration/{token}` - WebSocket for real-time editing

### Dashboard
- `GET /api/dashboard/stats` - Get dashboard statistics
- `GET /api/dashboard/recent-activity` - Recent activity logs

## Database Schema

### Users
- Authentication and authorization
- Role-based access control (Admin, Architect, Business Analyst, Developer, Viewer)

### Projects
- Organize models by initiative
- TOGAF phase tracking
- Team collaboration

### Architecture Models
- 21 model types (ArchiMate, BPMN, UML)
- Elements and relationships as JSON
- Version control
- AI generation metadata
- Compliance scoring

### Supporting Tables
- Comments (model feedback)
- Model Exports (cached formats)
- Collaboration Sessions (real-time editing)
- Activity Logs (audit trail)

## User Roles & Permissions

| Role | Permissions |
|------|------------|
| **Admin** | Full system access, user management |
| **Architect** | Create/edit all models, project management, AI generation |
| **Business Analyst** | Create/edit business models, comment on all models |
| **Developer** | Create/edit UML models, view all models |
| **Viewer** | View and comment on models, read-only exports |

## Supported Model Types

### ArchiMate 3.0 (7 types)
- Strategy Layer - Capabilities, goals, value streams
- Business Layer - Processes, actors, services
- Application Layer - Components, interfaces, data
- Technology Layer - Nodes, devices, networks
- Physical Layer - Equipment, facilities
- Implementation Layer - Work packages, deliverables
- Multi-Layer - Complete enterprise architecture

### BPMN 2.0 (3 types)
- Process - Business process flows
- Collaboration - Multi-participant processes
- Choreography - Message choreography

### UML 2.0 (12 types)
- Class, Sequence, Use Case, Activity
- State Machine, Component, Deployment
- Object, Package, Timing, Communication
- Interaction Overview

## Export Formats

- **Text** - Markdown documentation
- **Mermaid** - GitHub/GitLab diagrams
- **Kroki** - PlantUML for rendering services
- **Archi** - Archi tool XML import
- **GoJS** - Interactive web visualization
- **Enterprise Architect** - Sparx EA XMI format

## Integration with ArchiAgents CLI

The web application provides full API access for CLI integration:

```bash
# Generate model via web API
archiagents web generate \
  --project-id 1 \
  --type archimate-business \
  --name "Customer Management" \
  --use-ai

# List models from web platform
archiagents web list --format table

# Export model from web
archiagents web export <model-id> --format ea
```

## Development

### Project Structure

```
web_app/
├── backend/
│   ├── main.py                    # FastAPI application
│   ├── requirements.txt           # Python dependencies
│   ├── api/
│   │   └── database_manager.py    # Database connection
│   ├── models/
│   │   ├── database.py            # SQLAlchemy models
│   │   └── schemas.py             # Pydantic schemas
│   └── services/
│       ├── auth_service.py        # Authentication
│       ├── model_service.py       # Model operations
│       ├── ai_service.py          # AI integration
│       └── collaboration_service.py # Real-time collaboration
├── frontend/                       # React app (to implement)
│   ├── src/
│   │   ├── components/            # React components
│   │   ├── pages/                 # Page components
│   │   ├── services/              # API client
│   │   └── utils/                 # Utilities
│   └── package.json
└── data/
    └── archiagents.db             # SQLite database
```

### Adding New Endpoints

1. Define Pydantic schema in `models/schemas.py`
2. Add database model in `models/database.py`
3. Implement service logic in appropriate service file
4. Add endpoint in `main.py`

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

## Security

- **JWT Authentication** - Secure token-based authentication
- **Password Hashing** - Bcrypt with individual salts
- **CORS Protection** - Configured allowed origins
- **SQL Injection Prevention** - SQLAlchemy ORM
- **Role-Based Access Control** - Fine-grained permissions
- **Activity Logging** - Complete audit trail

## Performance

- **Async/Await** - Non-blocking I/O with FastAPI
- **Connection Pooling** - Efficient database connections
- **JSON Storage** - Fast model data retrieval
- **Caching** - Export format caching
- **WebSocket** - Efficient real-time updates

## Deployment

### Development
```bash
python main.py
```

### Production
```bash
# Using Gunicorn with Uvicorn workers
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000

# Using Docker
docker build -t archiagents-web .
docker run -p 8000:8000 archiagents-web
```

## Roadmap

### Phase 1: Backend Foundation ✅ (Current)
- [x] Database schema
- [x] API structure
- [x] Authentication
- [ ] Core services
- [ ] Testing

### Phase 2: Core Services
- [ ] Model CRUD operations
- [ ] AI integration
- [ ] Collaboration handlers
- [ ] Export system

### Phase 3: Frontend Foundation
- [ ] React project setup
- [ ] Component library
- [ ] API client
- [ ] Authentication flow

### Phase 4: Visual Editor
- [ ] GoJS integration
- [ ] Diagram palettes
- [ ] Properties panel
- [ ] Toolbar

### Phase 5: Collaboration
- [ ] Real-time editing
- [ ] Presence tracking
- [ ] Comments UI
- [ ] Version control

### Phase 6: Production
- [ ] Performance optimization
- [ ] Security audit
- [ ] Documentation
- [ ] Deployment guide

## Contributing

This is part of the ArchiAgents project. See main project README for contribution guidelines.

## License

Same as ArchiAgents main project.

## Support

- **Documentation**: See `WEB_APP_IMPLEMENTATION_GUIDE.md`
- **API Docs**: http://localhost:8000/api/docs
- **Issues**: Use ArchiAgents main repository

---

**ArchiAgents Web Platform - Making Enterprise Architecture Visual, Collaborative, and Intelligent** 🚀
