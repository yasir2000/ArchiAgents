"""
Database Migration - Add Notifications and User Invitations
Run this script to update the database schema with new tables
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from web_app.backend.api.database_manager import engine
from web_app.backend.models.database import Base, Notification, UserInvitation

def run_migration():
    """Create new tables in the database"""
    print("🔄 Running database migration...")
    print("   Creating tables: notifications, user_invitations")
    
    try:
        # Create only the new tables
        Base.metadata.create_all(bind=engine, tables=[
            Notification.__table__,
            UserInvitation.__table__
        ])
        print("✅ Migration completed successfully!")
        print("   - notifications table created")
        print("   - user_invitations table created")
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        raise

if __name__ == "__main__":
    run_migration()
