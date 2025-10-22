@echo off
REM ArchiAgents Web Application Backend - Quick Test Guide (Windows)
REM This script provides example commands to test the backend API

echo ==========================================
echo ArchiAgents Backend API - Test Guide
echo ==========================================
echo.

REM Server should be running at http://localhost:8000
set API_URL=http://localhost:8000

echo Step 1: Start the Backend Server
echo ==========================================
echo cd web_app\backend
echo venv\Scripts\activate
echo python main.py
echo.
echo Server will start at: %API_URL%
echo API Documentation: %API_URL%/api/docs
echo ReDoc: %API_URL%/api/redoc
echo.

echo Step 2: Register a New User
echo ==========================================
echo curl -X POST http://localhost:8000/api/auth/register ^
echo   -H "Content-Type: application/json" ^
echo   -d "{\"email\": \"architect@archiagents.com\", \"username\": \"chief_architect\", \"password\": \"SecurePass123!\", \"full_name\": \"Chief Enterprise Architect\", \"role\": \"architect\"}"
echo.

echo Step 3: Login to Get Access Token
echo ==========================================
echo curl -X POST http://localhost:8000/api/auth/login ^
echo   -H "Content-Type: application/x-www-form-urlencoded" ^
echo   -d "username=chief_architect&password=SecurePass123!"
echo.
echo Save the access_token from the response
echo set TOKEN=your_access_token_here
echo.

echo For more examples, see test_backend.sh or visit:
echo http://localhost:8000/api/docs
echo.

echo ==========================================
echo Available User Roles
echo ==========================================
echo 1. admin         - Full system access
echo 2. architect     - Full architecture modeling access
echo 3. business_analyst - Business model focus
echo 4. developer     - Technical model focus
echo 5. viewer        - Read-only access
echo.

echo ==========================================
echo Available Model Types (21)
echo ==========================================
echo ArchiMate: archimate-strategy, archimate-business, archimate-application,
echo            archimate-technology, archimate-physical, archimate-implementation,
echo            archimate-multi-layer
echo.
echo BPMN: bpmn-process, bpmn-collaboration, bpmn-choreography
echo.
echo UML: uml-class, uml-sequence, uml-use-case, uml-activity,
echo      uml-state-machine, uml-component, uml-deployment,
echo      uml-object, uml-package, uml-timing, uml-communication
echo.

echo ==========================================
echo Available Export Formats (6)
echo ==========================================
echo 1. text     - Markdown documentation
echo 2. mermaid  - GitHub/GitLab diagrams
echo 3. kroki    - PlantUML format
echo 4. archi    - Archi tool XML
echo 5. gojs     - GoJS web visualization
echo 6. ea       - Enterprise Architect XMI
echo.

echo ==========================================
echo API Documentation
echo ==========================================
echo Swagger UI: http://localhost:8000/api/docs
echo ReDoc:      http://localhost:8000/api/redoc
echo Health:     http://localhost:8000/api/health
echo.

echo ==========================================
echo Happy Testing! 🚀
echo ==========================================
pause
