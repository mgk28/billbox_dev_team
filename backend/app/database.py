import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Chemin absolu vers la base de données dans le dossier backend
BASE_DIR = Path(__file__).parent.parent
SQLALCHEMY_DATABASE_URL = f"sqlite:///{BASE_DIR}/billbox.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
