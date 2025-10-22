#!/bin/bash

# ArchiAgents Web Application - Quick Start Script
# This script helps you get started with the web application

echo "🚀 ArchiAgents Web Application - Quick Start"
echo "=============================================="
echo ""

# Check if we're in the right directory
if [ ! -d "web_app" ]; then
    echo "❌ Error: Please run this script from the ArchiAgents root directory"
    exit 1
fi

# Backend Setup
echo "📦 Setting up Backend..."
cd web_app/backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "  Creating Python virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "  Activating virtual environment..."
source venv/bin/activate || source venv/Scripts/activate

# Install dependencies
echo "  Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Backend setup complete!"
echo ""
echo "📋 Available Commands:"
echo "  Start backend server:"
echo "    cd web_app/backend"
echo "    source venv/bin/activate  # or venv\\Scripts\\activate on Windows"
echo "    python main.py"
echo ""
echo "  Access API documentation:"
echo "    http://localhost:8000/api/docs"
echo ""
echo "  Test API:"
echo "    # Register user"
echo "    curl -X POST http://localhost:8000/api/auth/register \\"
echo "      -H 'Content-Type: application/json' \\"
echo "      -d '{\"email\":\"architect@example.com\",\"username\":\"architect\",\"password\":\"secure123\",\"role\":\"architect\"}'"
echo ""
echo "    # Login"
echo "    curl -X POST http://localhost:8000/api/auth/login \\"
echo "      -d 'username=architect&password=secure123'"
echo ""
echo "🎨 Frontend setup coming in Phase 3!"
echo ""
echo "📖 For detailed instructions, see: WEB_APP_IMPLEMENTATION_GUIDE.md"
