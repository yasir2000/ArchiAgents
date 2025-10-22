#!/bin/bash

# ArchiAgents Frontend - Quick Start Script

echo "=========================================="
echo "ArchiAgents Frontend - Quick Start"
echo "=========================================="
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ from https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"
echo ""

# Navigate to frontend directory
cd "$(dirname "$0")"

# Install dependencies
echo "📦 Installing dependencies..."
echo ""
npm install

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "To start the development server:"
echo "  npm run dev"
echo ""
echo "The app will be available at:"
echo "  http://localhost:3000"
echo ""
echo "Make sure the backend is running at:"
echo "  http://localhost:8000"
echo ""
echo "To build for production:"
echo "  npm run build"
echo ""
echo "=========================================="
