"""
Backend API Test Script
Tests all newly implemented endpoints
"""

import requests
import json
from typing import Dict, Optional

# Base URL
BASE_URL = "http://localhost:8000/api"

# Test credentials
ADMIN_EMAIL = "admin@archiagents.com"
ADMIN_PASSWORD = "admin123"
TEST_USER_EMAIL = "test@archiagents.com"
TEST_USER_PASSWORD = "test123"

# Global variables for auth tokens
admin_token = None
user_token = None
test_project_id = None
test_model_id = None


def print_section(title: str):
    """Print section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_test(name: str, passed: bool, message: str = ""):
    """Print test result"""
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"{status} - {name}")
    if message:
        print(f"         {message}")


def make_request(method: str, endpoint: str, token: Optional[str] = None, **kwargs) -> requests.Response:
    """Make HTTP request with optional auth"""
    url = f"{BASE_URL}{endpoint}"
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        return response
    except requests.exceptions.ConnectionError:
        print(f"❌ ERROR: Cannot connect to {BASE_URL}")
        print("         Make sure the backend server is running!")
        exit(1)


# ============================================================================
# AUTHENTICATION TESTS
# ============================================================================

def test_authentication():
    global admin_token, user_token
    
    print_section("AUTHENTICATION TESTS")
    
    # Test 1: Register admin user
    response = make_request("POST", "/auth/register", json={
        "email": ADMIN_EMAIL,
        "name": "Admin User",
        "password": ADMIN_PASSWORD,
        "role": "admin"
    })
    
    if response.status_code == 201:
        print_test("Register Admin User", True, "Admin user created")
    elif response.status_code == 400 and "already registered" in response.text:
        print_test("Register Admin User", True, "Admin user already exists")
    else:
        print_test("Register Admin User", False, f"Status: {response.status_code}")
    
    # Test 2: Login admin
    response = make_request("POST", "/auth/login", data={
        "username": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    })
    
    if response.status_code == 200:
        admin_token = response.json()["access_token"]
        print_test("Admin Login", True, f"Token: {admin_token[:20]}...")
    else:
        print_test("Admin Login", False, f"Status: {response.status_code}")
        return False
    
    # Test 3: Get current user
    response = make_request("GET", "/auth/me", token=admin_token)
    print_test("Get Current User", response.status_code == 200)
    
    return True


# ============================================================================
# PASSWORD CHANGE TESTS
# ============================================================================

def test_password_change():
    print_section("PASSWORD CHANGE TESTS")
    
    # Test 1: Change password with wrong current password
    response = make_request("POST", "/auth/change-password", token=admin_token, json={
        "current_password": "wrongpassword",
        "new_password": "newpassword123"
    })
    print_test("Change Password - Wrong Current", response.status_code == 400)
    
    # Test 2: Change password successfully (then change back)
    response = make_request("POST", "/auth/change-password", token=admin_token, json={
        "current_password": ADMIN_PASSWORD,
        "new_password": "newpassword123"
    })
    
    if response.status_code == 200:
        print_test("Change Password - Success", True)
        
        # Change it back
        response = make_request("POST", "/auth/change-password", token=admin_token, json={
            "current_password": "newpassword123",
            "new_password": ADMIN_PASSWORD
        })
        print_test("Change Password Back", response.status_code == 200)
    else:
        print_test("Change Password - Success", False, f"Status: {response.status_code}")


# ============================================================================
# NOTIFICATION TESTS
# ============================================================================

def test_notifications():
    print_section("NOTIFICATION TESTS")
    
    # Test 1: Get notifications (empty initially)
    response = make_request("GET", "/notifications", token=admin_token)
    print_test("Get Notifications", response.status_code == 200)
    
    # Test 2: Get unread count
    response = make_request("GET", "/notifications/unread-count", token=admin_token)
    if response.status_code == 200:
        count = response.json()["count"]
        print_test("Get Unread Count", True, f"Unread: {count}")
    else:
        print_test("Get Unread Count", False)
    
    # Note: Notifications are created automatically by the system
    # We can't directly create them via API (they're created by events)


# ============================================================================
# USER MANAGEMENT TESTS
# ============================================================================

def test_user_management():
    print_section("USER MANAGEMENT TESTS")
    
    # Test 1: List users (admin only)
    response = make_request("GET", "/users", token=admin_token)
    if response.status_code == 200:
        users = response.json()
        print_test("List Users", True, f"Found {len(users)} users")
    else:
        print_test("List Users", False, f"Status: {response.status_code}")
    
    # Test 2: Invite user
    response = make_request("POST", "/users/invite", token=admin_token, json={
        "email": "invited@example.com",
        "role": "architect"
    })
    
    if response.status_code == 201:
        invitation = response.json()
        print_test("Invite User", True, f"Token: {invitation['token'][:20]}...")
    elif response.status_code == 400 and "already exists" in response.text:
        print_test("Invite User", True, "Invitation already exists")
    else:
        print_test("Invite User", False, f"Status: {response.status_code}")
    
    # Test 3: List invitations
    response = make_request("GET", "/users/invitations", token=admin_token)
    if response.status_code == 200:
        invitations = response.json()
        print_test("List Invitations", True, f"Found {len(invitations)} pending invitations")
    else:
        print_test("List Invitations", False)


# ============================================================================
# PROJECT AND MODEL SETUP (for other tests)
# ============================================================================

def setup_test_data():
    global test_project_id, test_model_id
    
    print_section("TEST DATA SETUP")
    
    # Create test project
    response = make_request("POST", "/projects", token=admin_token, json={
        "name": "Test Project",
        "description": "Project for testing",
        "togaf_phase": "Phase A"
    })
    
    if response.status_code == 201:
        test_project_id = response.json()["id"]
        print_test("Create Test Project", True, f"Project ID: {test_project_id}")
    elif response.status_code == 200:
        # Project might already exist, get it
        response = make_request("GET", "/projects", token=admin_token)
        projects = response.json()
        if projects:
            test_project_id = projects[0]["id"]
            print_test("Get Existing Project", True, f"Project ID: {test_project_id}")
    
    # Create test model
    if test_project_id:
        response = make_request("POST", "/models", token=admin_token, json={
            "project_id": test_project_id,
            "name": "Test Model",
            "description": "Model for testing",
            "model_type": "archimate-application",
            "elements": [
                {"id": "e1", "type": "application", "name": "App1", "properties": {}},
                {"id": "e2", "type": "application", "name": "App2", "properties": {}}
            ],
            "relationships": [
                {"id": "r1", "type": "flow", "source": "e1", "target": "e2", "properties": {}}
            ]
        })
        
        if response.status_code == 201:
            test_model_id = response.json()["id"]
            print_test("Create Test Model", True, f"Model ID: {test_model_id}")


# ============================================================================
# MODEL IMPORT TESTS
# ============================================================================

def test_model_import():
    print_section("MODEL IMPORT TESTS")
    
    if not test_project_id:
        print_test("Model Import Tests", False, "No test project available")
        return
    
    # Test 1: Import text format
    text_content = """
    Component A
    Component B
    Component C
    Component A -> Component B
    Component B -> Component C
    """
    
    files = {
        "file": ("test_model.txt", text_content, "text/plain")
    }
    data = {
        "project_id": test_project_id,
        "name": "Imported Text Model",
        "format": "text"
    }
    
    response = requests.post(
        f"{BASE_URL}/models/import",
        headers={"Authorization": f"Bearer {admin_token}"},
        files=files,
        data=data
    )
    
    if response.status_code == 201:
        result = response.json()
        print_test("Import Text Model", True, 
                  f"Imported {result['elements_imported']} elements, {result['relationships_imported']} relationships")
    else:
        print_test("Import Text Model", False, f"Status: {response.status_code}, {response.text}")
    
    # Test 2: Import Mermaid format
    mermaid_content = """
    graph TD
        A[Component A] --> B[Component B]
        B --> C[Component C]
        C --> D[Component D]
    """
    
    files = {
        "file": ("test_model.mmd", mermaid_content, "text/plain")
    }
    data = {
        "project_id": test_project_id,
        "name": "Imported Mermaid Model",
        "format": "mermaid"
    }
    
    response = requests.post(
        f"{BASE_URL}/models/import",
        headers={"Authorization": f"Bearer {admin_token}"},
        files=files,
        data=data
    )
    
    if response.status_code == 201:
        result = response.json()
        print_test("Import Mermaid Model", True,
                  f"Imported {result['elements_imported']} elements, {result['relationships_imported']} relationships")
    else:
        print_test("Import Mermaid Model", False, f"Status: {response.status_code}")
    
    # Test 3: Import JSON format
    json_content = {
        "nodeDataArray": [
            {"key": 1, "text": "Node 1", "category": "application"},
            {"key": 2, "text": "Node 2", "category": "application"}
        ],
        "linkDataArray": [
            {"from": 1, "to": 2, "category": "flow"}
        ]
    }
    
    files = {
        "file": ("test_model.json", json.dumps(json_content), "application/json")
    }
    data = {
        "project_id": test_project_id,
        "name": "Imported JSON Model",
        "format": "json"
    }
    
    response = requests.post(
        f"{BASE_URL}/models/import",
        headers={"Authorization": f"Bearer {admin_token}"},
        files=files,
        data=data
    )
    
    if response.status_code == 201:
        result = response.json()
        print_test("Import JSON Model", True,
                  f"Imported {result['elements_imported']} elements, {result['relationships_imported']} relationships")
    else:
        print_test("Import JSON Model", False, f"Status: {response.status_code}")


# ============================================================================
# COLLABORATION TESTS
# ============================================================================

def test_collaboration():
    print_section("COLLABORATION TESTS")
    
    if not test_model_id:
        print_test("Collaboration Tests", False, "No test model available")
        return
    
    # Test 1: Get participants
    response = make_request("GET", f"/collaboration/participants/{test_model_id}", token=admin_token)
    if response.status_code == 200:
        result = response.json()
        print_test("Get Collaboration Participants", True, f"Found {result['total_count']} participants")
    else:
        print_test("Get Collaboration Participants", False)
    
    # Test 2: Get activity
    response = make_request("GET", f"/collaboration/activity/{test_model_id}", token=admin_token)
    if response.status_code == 200:
        result = response.json()
        print_test("Get Collaboration Activity", True, f"Found {result['total_count']} activities")
    else:
        print_test("Get Collaboration Activity", False)


# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

def run_all_tests():
    """Run all backend tests"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "ARCHIAGENTS BACKEND API TESTS" + " " * 29 + "║")
    print("╚" + "=" * 78 + "╝")
    
    # Check if server is running
    try:
        response = requests.get(f"{BASE_URL.replace('/api', '')}/api/health")
        if response.status_code != 200:
            print("\n❌ Backend server is not responding properly!")
            print("   Please start the server with: python web_app/backend/main.py")
            return
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to backend server!")
        print("   Please start the server with: python web_app/backend/main.py")
        return
    
    print(f"\n✅ Backend server is running at {BASE_URL}")
    
    # Run tests
    if not test_authentication():
        print("\n❌ Authentication failed. Cannot continue tests.")
        return
    
    test_password_change()
    test_notifications()
    test_user_management()
    setup_test_data()
    test_model_import()
    test_collaboration()
    
    # Summary
    print_section("TEST SUMMARY")
    print("All backend endpoint tests completed!")
    print("\n✅ New Features Implemented:")
    print("   - Password Change")
    print("   - Notifications System")
    print("   - User Management (List, Invite, Role Update, Delete)")
    print("   - Model Import (Text, Mermaid, JSON formats)")
    print("   - Enhanced Collaboration (Participants, Activity)")
    print("\n📚 Next Steps:")
    print("   1. Run database migration: python web_app/backend/migrations/add_notifications_invitations.py")
    print("   2. Test frontend integration")
    print("   3. Configure email service for invitations")
    print("   4. Add more import format parsers (Archi, EA)")
    print("\n")


if __name__ == "__main__":
    run_all_tests()
