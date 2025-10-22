# ArchiAgents Platform - Quick Reference Guide

**Last Updated:** January 2025

---

## 🚀 Quick Start (3 Minutes)

### Start Backend
```bash
cd web_app/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
✅ Backend running at **http://localhost:8000**

### Start Frontend
```bash
cd web_app/frontend
npm install
npm run dev
```
✅ Frontend running at **http://localhost:3000**

### First Login
1. Visit http://localhost:3000
2. Click "Create Account"
3. Fill in registration form
4. Select role (Architect recommended)
5. Login with credentials
6. Start creating projects!

---

## 📚 Documentation Quick Links

### Main Documentation
- **[WEB_PLATFORM_COMPLETE.md](WEB_PLATFORM_COMPLETE.md)** - Complete platform overview
- **[README.md](README.md)** - Project navigation
- **[PROJECT_STATUS.md](PROJECT_STATUS.md)** - Current status

### Backend Documentation
- **[WEB_APP_IMPLEMENTATION_GUIDE.md](WEB_APP_IMPLEMENTATION_GUIDE.md)** - Backend architecture
- **[BACKEND_SERVICES_COMPLETE.md](BACKEND_SERVICES_COMPLETE.md)** - Services details
- **[web_app/README.md](web_app/README.md)** - Backend setup
- **[web_app/test_backend.sh](web_app/test_backend.sh)** - API testing

### Frontend Documentation
- **[FRONTEND_COMPLETE_SUMMARY.md](FRONTEND_COMPLETE_SUMMARY.md)** - Complete frontend summary
- **[web_app/frontend/README.md](web_app/frontend/README.md)** - Frontend setup
- **[web_app/frontend/FRONTEND_IMPLEMENTATION.md](web_app/frontend/FRONTEND_IMPLEMENTATION.md)** - Component code

### Framework Documentation
- **[TOGAF_GUIDE.md](Docs/TOGAF_Guide.md)** - TOGAF methodology
- **[NORA-Compliance/](NORA-Compliance/)** - Saudi NORA compliance

---

## 🎯 Platform Features

### Backend (100% Complete) ✅
- 30+ REST API endpoints
- JWT authentication (5 roles)
- 21 model types (ArchiMate, BPMN, UML)
- AI-powered model generation
- Standards validation
- 6 export formats
- WebSocket real-time collaboration
- Dashboard analytics
- Full-text search
- Comments and discussions

### Frontend (60% Complete) 🚀
- React + TypeScript foundation
- Authentication pages (login, register)
- Responsive layout (desktop + mobile)
- API integration (Axios + React Query)
- State management (Zustand)
- WebSocket client
- Dashboard (code ready)
- Projects UI (code ready)
- Visual editor (planned)

---

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login (returns JWT)
- `GET /api/auth/me` - Get current user
- `PUT /api/auth/me` - Update profile

### Projects
- `GET /api/projects` - List all projects
- `POST /api/projects` - Create project
- `GET /api/projects/{id}` - Get project details
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

### Models
- `GET /api/models` - List all models
- `POST /api/models` - Create model
- `GET /api/models/{id}` - Get model details
- `PUT /api/models/{id}` - Update model
- `DELETE /api/models/{id}` - Delete model

### AI Generation
- `POST /api/ai/generate` - Generate model
- `POST /api/ai/improve` - Improve model
- `POST /api/ai/validate` - Validate model

### Export
- `POST /api/export/{model_id}` - Export model
- `GET /api/export/{export_id}/download` - Download export

### Collaboration
- `POST /api/collaboration/sessions` - Create session
- `GET /api/collaboration/sessions/{id}` - Get session
- `WS /ws/collaborate/{token}` - WebSocket connection

### Dashboard
- `GET /api/dashboard/stats` - Get statistics
- `GET /api/dashboard/activity` - Get recent activity

### Comments
- `GET /api/comments/{model_id}` - Get comments
- `POST /api/comments` - Create comment

### Search
- `GET /api/search?q={query}` - Full-text search

### Health
- `GET /` - Root endpoint
- `GET /health` - Health check

**Full API documentation:** http://localhost:8000/api/docs

---

## 👥 User Roles

### Admin
- Full system access
- User management
- All operations

### Architect
- Create/edit all models
- Full CRUD on projects
- AI generation
- Export models

### Business Analyst
- Create/edit business models
- View technical models
- Comment on all models

### Developer
- Create/edit technical models
- View business models
- Implementation focus

### Viewer
- Read-only access
- View all models
- Add comments

---

## 🎨 Frontend Stack

### Core
- **React** 18.2.0 - UI library
- **TypeScript** 5.2.2 - Type safety
- **Vite** 5.0.8 - Build tool

### Routing & State
- **React Router** 6.20.0 - Navigation
- **Zustand** 4.4.7 - State management
- **React Query** 5.12.0 - Data fetching

### UI & Styling
- **TailwindCSS** 3.3.6 - Styling
- **Lucide React** - Icons
- **Recharts** - Charts
- **React Hot Toast** - Notifications

### Visual Modeling
- **GoJS** 3.0.0 - Diagram library

### HTTP
- **Axios** 1.6.2 - API client

---

## 🛠️ Backend Stack

### Core
- **FastAPI** 0.104.1 - Web framework
- **Python** 3.11+ - Programming language
- **Uvicorn** - ASGI server

### Database
- **SQLAlchemy** 2.0.23 - ORM
- **SQLite** - Database (dev)

### Authentication
- **JWT** - Token authentication
- **Bcrypt** - Password hashing

### WebSocket
- **Starlette** - WebSocket support

---

## 📁 Project Structure

```
ArchiAgents/
├── web_app/                    # 🌐 Web Platform (70% Complete)
│   ├── backend/                # ✅ FastAPI Backend (100%)
│   │   ├── main.py             # 30+ endpoints
│   │   ├── models/             # Database & schemas
│   │   ├── services/           # Business logic
│   │   └── api/                # API utilities
│   └── frontend/               # 🚀 React Frontend (60%)
│       ├── src/
│       │   ├── pages/          # ✅ Auth, 📝 Dashboard, Projects
│       │   ├── components/     # ✅ Layout
│       │   ├── stores/         # ✅ Auth, Collaboration
│       │   ├── lib/            # ✅ API client
│       │   └── types/          # ✅ TypeScript types
│       ├── package.json        # Dependencies
│       └── README.md           # Setup guide
├── togaf_framework/            # 🤖 AI Agents (70%)
│   ├── ai_agents/              # Multi-LLM agents
│   ├── runtime_intelligence/   # AI intelligence
│   └── phases/                 # TOGAF phases
├── model_generation/           # 📊 Model Generation (100%)
│   ├── engine.py               # 21 model types
│   └── formats.py              # 6 export formats
├── cli/                        # 🎨 CLI (95%)
│   └── commands/               # 20+ commands
├── Phase-A-Architecture-Vision/ # TOGAF Documentation
├── Phase-B-Business-Architecture/
├── Phase-C-Information-Systems/
├── Phase-D-Technology-Architecture/
├── Phase-E-Opportunities-Solutions/
├── Phase-F-Migration-Planning/
├── Phase-G-Implementation-Governance/
├── Phase-H-Architecture-Change-Management/
├── ArchiMate-Models/           # ArchiMate models
├── Cross-Cutting-Concerns/     # Enterprise patterns
├── NORA-Compliance/            # Saudi NORA compliance
└── Templates/                  # Document templates
```

---

## 🎓 Development Workflow

### 1. Start Development Environment
```bash
# Terminal 1 - Backend
cd web_app/backend
source venv/bin/activate
python main.py

# Terminal 2 - Frontend
cd web_app/frontend
npm run dev
```

### 2. Make Changes
- Edit files in `web_app/frontend/src/`
- Hot reload happens automatically
- Check console for errors

### 3. Test Changes
- Backend: http://localhost:8000/api/docs
- Frontend: http://localhost:3000
- Use React DevTools for debugging

### 4. Common Tasks

**Add New Page:**
1. Create file in `src/pages/`
2. Add route in `src/App.tsx`
3. Add navigation link in `src/components/layout/Layout.tsx`

**Add New API Call:**
1. Add function in `src/lib/api-client.ts`
2. Use React Query hook in component
3. Handle loading/error states

**Add New Component:**
1. Create file in `src/components/`
2. Import and use in pages
3. Add TypeScript types if needed

---

## 🚨 Common Issues

### Backend Won't Start
- Check Python version (3.11+)
- Activate virtual environment
- Install requirements: `pip install -r requirements.txt`
- Check port 8000 is free

### Frontend Won't Start
- Check Node.js version (18+)
- Install dependencies: `npm install`
- Check port 3000 is free
- Clear cache: `npm run build` then `npm run dev`

### Authentication Fails
- Check backend is running
- Check API proxy in `vite.config.ts`
- Clear browser localStorage
- Check JWT token in devtools

### WebSocket Not Connecting
- Check backend WebSocket endpoint
- Check proxy configuration
- Check browser console for errors
- Verify token is valid

---

## 📊 Project Statistics

### Total Lines of Code
- **TOGAF Framework:** ~12,000 lines
- **AI Agents:** ~5,940 lines
- **Runtime Intelligence:** ~2,640 lines
- **CLI System:** ~2,600 lines
- **Model Generation:** ~3,650 lines
- **Backend:** ~2,750 lines
- **Frontend:** ~1,100 lines
- **Documentation:** ~5,000 lines
- **Total:** ~35,680 lines

### Implementation Progress
- **Backend:** 100% ✅
- **Frontend Foundation:** 100% ✅
- **Frontend Pages:** 60% 📝
- **Visual Editor:** 0% (designed)
- **Collaboration UI:** 0% (designed)
- **Overall Platform:** ~70% 🚀

---

## 🎯 Next Priorities

### Immediate (This Week)
1. ✅ Complete frontend foundation
2. 📝 Implement dashboard page
3. 📝 Implement projects page
4. Test end-to-end workflow

### Short-Term (This Month)
1. Implement models page
2. Build GoJS visual editor
3. Add real-time collaboration UI
4. Add unit tests

### Long-Term (Next Quarter)
1. Performance optimization
2. Accessibility improvements
3. Mobile app (React Native)
4. Desktop app (Electron)

---

## 💡 Tips & Tricks

### Frontend Development
- Use React DevTools for debugging
- Check Network tab for API calls
- Use React Query Devtools for cache inspection
- Hot reload saves time

### Backend Development
- Use FastAPI docs for testing: `/api/docs`
- Check SQLite database with DB Browser
- Use Postman for API testing
- Enable debug mode for detailed errors

### General
- Read the documentation first
- Check existing code for patterns
- Ask for help in issues
- Contribute improvements

---

## 🎉 Success Checklist

### Backend Setup ✅
- [ ] Python 3.11+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Backend starts without errors
- [ ] API docs accessible at /api/docs

### Frontend Setup ✅
- [ ] Node.js 18+ installed
- [ ] Dependencies installed with npm
- [ ] Frontend starts without errors
- [ ] Can access at http://localhost:3000

### First Use ✅
- [ ] Register new account
- [ ] Login successfully
- [ ] Navigate to dashboard
- [ ] Create first project
- [ ] Create first model

---

## 📞 Getting Help

### Documentation
- Read `WEB_PLATFORM_COMPLETE.md` for overview
- Check `FRONTEND_IMPLEMENTATION.md` for component code
- Review API docs at http://localhost:8000/api/docs

### Debugging
- Check browser console for frontend errors
- Check terminal for backend errors
- Use React DevTools
- Use Network tab for API calls

### Issues
- Check existing issues in repository
- Create new issue with details
- Include error messages
- Provide reproduction steps

---

## 🚀 You're Ready!

Start the platform:
```bash
# Terminal 1
cd web_app/backend && python main.py

# Terminal 2
cd web_app/frontend && npm run dev
```

Then visit **http://localhost:3000** and start building enterprise architectures! 🎉

---

**Happy Architecting!** 🏗️
