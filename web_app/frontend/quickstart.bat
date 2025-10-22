@echo off
REM ArchiAgents Frontend - Quick Start Script (Windows)

echo ==========================================
echo ArchiAgents Frontend - Quick Start
echo ==========================================
echo.

REM Check if Node.js is installed
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Node.js is not installed. Please install Node.js 18+ from https://nodejs.org/
    exit /b 1
)

echo ✅ Node.js version:
node --version
echo ✅ npm version:
npm --version
echo.

REM Navigate to frontend directory
cd /d %~dp0

REM Install dependencies
echo 📦 Installing dependencies...
echo.
call npm install

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Failed to install dependencies
    exit /b 1
)

echo.
echo ==========================================
echo ✅ Setup Complete!
echo ==========================================
echo.
echo To start the development server:
echo   npm run dev
echo.
echo The app will be available at:
echo   http://localhost:3000
echo.
echo Make sure the backend is running at:
echo   http://localhost:8000
echo.
echo To build for production:
echo   npm run build
echo.
echo ==========================================
pause
