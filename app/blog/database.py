import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = SessionLocal.query_property()


# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
#
# Base = declarative_base()
#
#

def get_db():
    db = SessionLocal.session_factory()
    try:
        yield db
    finally:
        db.close()
