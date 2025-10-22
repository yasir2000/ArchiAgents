#!/bin/bash

# ArchiAgents Web Application Backend - Quick Test Guide
# This script provides example commands to test the backend API

echo "=========================================="
echo "ArchiAgents Backend API - Test Guide"
echo "=========================================="
echo ""

# Server should be running at http://localhost:8000
API_URL="http://localhost:8000"

echo "Step 1: Start the Backend Server"
echo "=========================================="
echo "cd web_app/backend"
echo "source venv/bin/activate  # Windows: venv\\Scripts\\activate"
echo "python main.py"
echo ""
echo "Server will start at: $API_URL"
echo "API Documentation: $API_URL/api/docs"
echo "ReDoc: $API_URL/api/redoc"
echo ""

echo "Step 2: Register a New User"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "architect@archiagents.com",
    "username": "chief_architect",
    "password": "SecurePass123!",
    "full_name": "Chief Enterprise Architect",
    "role": "architect"
  }'
EOF
echo ""

echo "Step 3: Login to Get Access Token"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=chief_architect&password=SecurePass123!"

# Save the access_token from the response
# export TOKEN="your_access_token_here"
EOF
echo ""

echo "Step 4: Create a Project"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/projects \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Digital Transformation Initiative",
    "description": "Enterprise-wide digital transformation program",
    "togaf_phase": "Phase B",
    "metadata": {
      "budget": "5M USD",
      "timeline": "18 months",
      "strategic_goal": "Vision 2030 alignment"
    }
  }'

# Save the project ID from the response
# PROJECT_ID=1
EOF
echo ""

echo "Step 5: Generate AI-Powered Model"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/ai/generate \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": 1,
    "model_type": "archimate-business",
    "name": "Customer Management Capability",
    "description": "End-to-end customer lifecycle management",
    "use_project_context": true,
    "ai_parameters": {
      "complexity": "medium",
      "detail_level": "comprehensive"
    }
  }'

# Save the model ID from the response
# MODEL_ID=1
EOF
echo ""

echo "Step 6: Validate Model Against Standards"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/ai/validate/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"

# Response includes:
# - Compliance score (0-100)
# - Issues by severity (error, warning, info)
# - Fix suggestions
EOF
echo ""

echo "Step 7: Get AI Improvement Suggestions"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/ai/improve/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"

# Response includes suggestions for:
# - Completeness
# - Relationships
# - Best practices
# - Naming conventions
# - Structure optimization
EOF
echo ""

echo "Step 8: Export Model to Different Formats"
echo "=========================================="
cat << 'EOF'
# Export to Mermaid (GitHub/GitLab compatible)
curl -X POST http://localhost:8000/api/export \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": 1,
    "format": "mermaid"
  }'

# Export to Archi tool format
curl -X POST http://localhost:8000/api/export \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": 1,
    "format": "archi"
  }'

# Export to GoJS (web visualization)
curl -X POST http://localhost:8000/api/export \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": 1,
    "format": "gojs"
  }'

# Export to Enterprise Architect (XMI)
curl -X POST http://localhost:8000/api/export \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": 1,
    "format": "ea"
  }'
EOF
echo ""

echo "Step 9: Create Collaboration Session"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/collaboration/sessions \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": 1
  }'

# Save the session token from the response
# SESSION_TOKEN="unique_session_token"
# Connect via WebSocket: ws://localhost:8000/ws/collaboration/{SESSION_TOKEN}
EOF
echo ""

echo "Step 10: Add Comments to Model"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/comments \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": 1,
    "content": "This capability model needs additional validation steps",
    "element_id": "element_123",
    "metadata": {
      "priority": "high",
      "category": "review"
    }
  }'
EOF
echo ""

echo "Step 11: View Dashboard Statistics"
echo "=========================================="
cat << 'EOF'
curl -X GET http://localhost:8000/api/dashboard/stats \
  -H "Authorization: Bearer $TOKEN"

# Response includes:
# - Total projects and models
# - Models by type (distribution)
# - Models by status (workflow)
# - Recent activity
# - Team size
EOF
echo ""

echo "Step 12: Search Projects and Models"
echo "=========================================="
cat << 'EOF'
curl -X POST http://localhost:8000/api/search \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "customer management",
    "filters": {
      "type": "model",
      "model_type": "archimate-business"
    },
    "limit": 20,
    "offset": 0
  }'
EOF
echo ""

echo "Step 13: List All Projects"
echo "=========================================="
cat << 'EOF'
curl -X GET "http://localhost:8000/api/projects?skip=0&limit=10" \
  -H "Authorization: Bearer $TOKEN"
EOF
echo ""

echo "Step 14: List Models with Filters"
echo "=========================================="
cat << 'EOF'
# All models
curl -X GET "http://localhost:8000/api/models" \
  -H "Authorization: Bearer $TOKEN"

# Filter by project
curl -X GET "http://localhost:8000/api/models?project_id=1" \
  -H "Authorization: Bearer $TOKEN"

# Filter by type
curl -X GET "http://localhost:8000/api/models?model_type=archimate-business" \
  -H "Authorization: Bearer $TOKEN"

# Filter by status
curl -X GET "http://localhost:8000/api/models?status=approved" \
  -H "Authorization: Bearer $TOKEN"
EOF
echo ""

echo "Step 15: Get Recent Activity"
echo "=========================================="
cat << 'EOF'
curl -X GET "http://localhost:8000/api/dashboard/recent-activity?limit=20" \
  -H "Authorization: Bearer $TOKEN"
EOF
echo ""

echo "=========================================="
echo "Additional Testing Options"
echo "=========================================="
echo ""

echo "Test with Python Requests:"
cat << 'EOF'
import requests

# Login
response = requests.post(
    "http://localhost:8000/api/auth/login",
    data={"username": "chief_architect", "password": "SecurePass123!"}
)
token = response.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Generate model
response = requests.post(
    "http://localhost:8000/api/ai/generate",
    headers=headers,
    json={
        "project_id": 1,
        "model_type": "archimate-business",
        "name": "Customer Management",
        "use_project_context": True
    }
)
model = response.json()
print(f"Generated model: {model['name']}")
print(f"Elements: {len(model['elements'])}")
print(f"Relationships: {len(model['relationships'])}")
EOF
echo ""

echo "Test WebSocket Collaboration:"
cat << 'EOF'
# Install websocket client
pip install websockets

# Python WebSocket client example
import asyncio
import websockets
import json

async def test_collaboration():
    uri = "ws://localhost:8000/ws/collaboration/{session_token}"
    async with websockets.connect(uri) as websocket:
        # Wait for initial state
        initial = await websocket.recv()
        print(f"Initial state: {json.loads(initial)}")
        
        # Send cursor update
        await websocket.send(json.dumps({
            "type": "cursor_move",
            "data": {"x": 100, "y": 200}
        }))
        
        # Receive updates
        while True:
            message = await websocket.recv()
            print(f"Received: {json.loads(message)}")

asyncio.run(test_collaboration())
EOF
echo ""

echo "=========================================="
echo "Available User Roles"
echo "=========================================="
echo "1. admin         - Full system access"
echo "2. architect     - Full architecture modeling access"
echo "3. business_analyst - Business model focus"
echo "4. developer     - Technical model focus"
echo "5. viewer        - Read-only access"
echo ""

echo "=========================================="
echo "Available Model Types (21)"
echo "=========================================="
echo "ArchiMate (7):"
echo "  - archimate-strategy"
echo "  - archimate-business"
echo "  - archimate-application"
echo "  - archimate-technology"
echo "  - archimate-physical"
echo "  - archimate-implementation"
echo "  - archimate-multi-layer"
echo ""
echo "BPMN (3):"
echo "  - bpmn-process"
echo "  - bpmn-collaboration"
echo "  - bpmn-choreography"
echo ""
echo "UML (11):"
echo "  - uml-class"
echo "  - uml-sequence"
echo "  - uml-use-case"
echo "  - uml-activity"
echo "  - uml-state-machine"
echo "  - uml-component"
echo "  - uml-deployment"
echo "  - uml-object"
echo "  - uml-package"
echo "  - uml-timing"
echo "  - uml-communication"
echo ""

echo "=========================================="
echo "Available Export Formats (6)"
echo "=========================================="
echo "1. text     - Markdown documentation"
echo "2. mermaid  - GitHub/GitLab diagrams"
echo "3. kroki    - PlantUML format"
echo "4. archi    - Archi tool XML"
echo "5. gojs     - GoJS web visualization"
echo "6. ea       - Enterprise Architect XMI"
echo ""

echo "=========================================="
echo "API Documentation"
echo "=========================================="
echo "Swagger UI: http://localhost:8000/api/docs"
echo "ReDoc:      http://localhost:8000/api/redoc"
echo "Health:     http://localhost:8000/api/health"
echo ""

echo "=========================================="
echo "Happy Testing! 🚀"
echo "=========================================="
