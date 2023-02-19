from datetime import datetime
import pytz
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, Boolean, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .declarative_base import Base
from uuid import uuid4
from celery_service import Setting

from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
class ModelBase:
    """Model base"""

    id = Column("id", Integer(), primary_key=True)
    created = Column("created", DateTime(), default=func.now())
    modified = Column("modified", DateTime(), onupdate=func.now(), default=func.now())
    uuid = Column("uuid", UUID(as_uuid=True), default=uuid4)

    @hybrid_property
    def created_date(self):
        return self.created.strftime("%d-%m-%Y")

    @hybrid_property
    def created_time(self):
        return self.created.strftime("%H:%M:%S")


class MessageType(ModelBase, Base):
    """Alert."""
    __tablename__ = "logs_page_messagetype"

    id = Column("id", Integer(), primary_key=True)
    email = Column("email", Text, nullable=False)
    type_alert = Column("type_alert", Integer(), default=1)
    sites = relationship("SiteAlert", back_populates="message_type")


    def __str__(self):  # noqa
        return str(self.email)


class SiteAlert(ModelBase, Base):
    __tablename__ = "logs_page_sitealert"

    url_site = Column("url_site", Text, nullable=False)
    enable = Column("enable", Boolean, default=True)
    message_type_id = Column("message_type_id", Integer,
                             ForeignKey("logs_page_messagetype.id"))
    message_type = relationship("MessageType", back_populates="sites")
    site_register = relationship("SiteRegister", back_populates="page")

    def __str__(self):  # noqa
        return str(self.url_site)


class SiteRegister(ModelBase, Base):
    __tablename__ = "logs_page_siteregister"

    message_error = Column("message_error", Text, nullable=False)
    is_alerted = Column("is_alerted", Boolean, default=False)
    status_code = Column("status_code", Text, nullable=False)
    page = relationship("SiteAlert", back_populates="site_register")
    page_id = Column("page_id", Integer,
                     ForeignKey("logs_page_sitealert.id", ondelete="CASCADE"),
                     nullable=False)

    def __str__(self):  # noqa
        return f"{self.status_code} - {self.page}"
