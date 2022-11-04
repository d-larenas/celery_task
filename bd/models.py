from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .declarative_base import Base


class ReportError(Base):
    """Model of register of error."""
    __tablename__ = "report_error"

    id = Column("id", Integer(), primary_key=True)
    status = Column("status", Integer(), nullable=False)
    message = Column("message", Text, nullable=False)
    created_at = Column("created_at", DateTime(), default=datetime.now())
    url_id = Column("url_id", Integer, ForeignKey("url.id", ondelete="CASCADE"), nullable=False)
    is_notification = Column("is_notification", Boolean(), default=False, nullable=False)

    def __str__(self):  # noqa
        return str(self.id)


class Url(Base):
    """Model register url."""
    __tablename__ = "url"

    id = Column("id", Integer(), primary_key=True)
    url = Column("url", Text, unique=True)
    reports = relationship("ReportError", lazy='dynamic', cascade="all, delete, delete-orphan")

    def __str__(self):  # noqa
        return self.url
