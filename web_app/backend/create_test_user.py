"""
Quick script to create a test user for Visual Editor testing
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from web_app.backend.models import database
from web_app.backend.api.database_manager import SessionLocal, engine

# Create tables
database.Base.metadata.create_all(bind=engine)

# Create session
db = SessionLocal()

try:
    # Check if user already exists
    existing_user = db.query(database.User).filter(database.User.email == "test@demo.com").first()
    
    if existing_user:
        print(f"✅ User already exists: {existing_user.email}")
        print(f"   ID: {existing_user.id}")
        print(f"   Name: {existing_user.name}")
        print(f"   Role: {existing_user.role}")
    else:
        # Create new user with plain password (for testing only!)
        new_user = database.User(
            username="testuser",
            email="test@demo.com",
            name="Test User",
            hashed_password="$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYk3H.uh6a2",  # "password123"
            role="architect",
            is_active=True
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        print(f"✅ User created successfully!")
        print(f"   Email: {new_user.email}")
        print(f"   Password: password123")
        print(f"   Name: {new_user.name}")
        print(f"   Role: {new_user.role}")
        
    # Create a test model for the visual editor
    existing_model = db.query(database.Model).filter(database.Model.name == "Test Architecture Diagram").first()
    
    if not existing_model:
        user = db.query(database.User).filter(database.User.email == "test@demo.com").first()
        if user:
            test_model = database.Model(
                name="Test Architecture Diagram",
                description="A sample ArchiMate diagram for testing the Visual Editor",
                model_type="archimate",
                project_id=None,
                created_by_id=user.id,
                content='{"nodeDataArray":[],"linkDataArray":[]}',
                status="draft"
            )
            db.add(test_model)
            db.commit()
            db.refresh(test_model)
            print(f"\n✅ Test model created!")
            print(f"   ID: {test_model.id}")
            print(f"   Name: {test_model.name}")
    
    print("\n🎉 Database setup complete!")
    print("\n📝 Login credentials:")
    print("   Email: test@demo.com")
    print("   Password: password123")
    print("\n🌐 Access the app at: http://localhost:3000")
    
finally:
    db.close()
