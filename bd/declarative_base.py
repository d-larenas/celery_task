from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from celery_service.settings import Setting

engine = create_engine(Setting.DATABASE_URL)
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    """Get session."""
    Base.metadata.create_all(engine)
    return _SessionFactory()
