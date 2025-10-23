@echo off
REM Backend Setup and Run Script for Windows

echo ╔════════════════════════════════════════════════════════════════╗
echo ║          ArchiAgents Backend - Setup and Start                 ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+
    exit /b 1
)

echo ✅ Python found
python --version
echo.

REM Check if in correct directory
if not exist "web_app\backend\main.py" (
    echo ❌ Error: Please run this script from the project root directory
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -q fastapi uvicorn sqlalchemy passlib python-jose python-multipart bcrypt

REM Run database migration
echo.
echo 🗄️  Running database migration...
cd web_app\backend
python migrations\add_notifications_invitations.py

REM Start server
echo.
echo 🚀 Starting ArchiAgents Backend Server...
echo.
echo    API:  http://localhost:8000/api
echo    Docs: http://localhost:8000/api/docs
echo.
echo Press Ctrl+C to stop
echo.

python main.py
