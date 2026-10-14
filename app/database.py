from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./taskflow.db"
# Baad mein Postgres: "postgresql://user:password@localhost/taskflow"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # sirf SQLite ke liye
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()