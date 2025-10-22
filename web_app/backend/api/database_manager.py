"""
ArchiAgents Web Application - Database Manager
Database connection and initialization
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

from web_app.backend.models.database import Base
from sqlalchemy import text

# Database configuration
DATABASE_DIR = Path(__file__).parent.parent.parent / "data"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_DIR}/archiagents.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=False  # Set to True for SQL logging
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Initialize database and create all tables"""
    print(f"[database_manager] DATABASE_URL: {DATABASE_URL}")
    print(f"[database_manager] Using DB file: {DATABASE_DIR / 'archiagents.db'}")
    # Lightweight sqlite migration: ensure expected columns exist
    try:
        with engine.connect() as conn:
            # Check users table columns
            result = conn.execute(text("PRAGMA table_info(users)"))
            cols = [row[1] for row in result.fetchall()]
            if cols:
                if 'name' not in cols:
                    print("[database_manager] Migrating: adding missing column users.name")
                    conn.execute(text("ALTER TABLE users ADD COLUMN name VARCHAR(255)"))
                    # Backfill from legacy columns if present
                    if 'full_name' in cols:
                        conn.execute(text("UPDATE users SET name = COALESCE(full_name, name)"))
                    elif 'username' in cols:
                        conn.execute(text("UPDATE users SET name = COALESCE(username, name)"))
                    conn.commit()
            # Check architecture_models metadata column rename
            result = conn.execute(text("PRAGMA table_info(architecture_models)"))
            cols = [row[1] for row in result.fetchall()]
            if cols and 'model_metadata' not in cols:
                print("[database_manager] Migrating: adding missing column architecture_models.model_metadata")
                # SQLite: JSON maps to TEXT; add the column then backfill from legacy 'metadata' if present
                conn.execute(text("ALTER TABLE architecture_models ADD COLUMN model_metadata TEXT"))
                if 'metadata' in cols:
                    conn.execute(text("UPDATE architecture_models SET model_metadata = metadata WHERE model_metadata IS NULL"))
                conn.commit()
    except Exception as e:
        print(f"[database_manager] Migration check error (safe to ignore on first run): {e}")
    Base.metadata.create_all(bind=engine)


def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
