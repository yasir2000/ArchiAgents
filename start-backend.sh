#!/bin/bash
# Backend Setup and Run Script

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          ArchiAgents Backend - Setup and Start                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check Python
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python found: $(python --version)"
echo ""

# Check if in correct directory
if [ ! -f "web_app/backend/main.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q fastapi uvicorn sqlalchemy passlib python-jose python-multipart bcrypt

# Run database migration
echo ""
echo "🗄️  Running database migration..."
cd web_app/backend
python migrations/add_notifications_invitations.py

# Start server
echo ""
echo "🚀 Starting ArchiAgents Backend Server..."
echo ""
echo "   API:  http://localhost:8000/api"
echo "   Docs: http://localhost:8000/api/docs"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python main.py
