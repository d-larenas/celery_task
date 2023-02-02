from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .declarative_base import Base
from uuid import uuid4


class MessageType(Base):
    """Alert."""
    __tablename__ = "logs_page_messagetype"

    id = Column("id", Integer(), primary_key=True)
    email = Column("email", Text, nullable=False)
    created = Column("created", DateTime(), default=datetime.now())
    modified = Column("modified", DateTime(), default=datetime.now())
    uuid = Column("uuid", UUID(as_uuid=True), default=uuid4)
    type_alert = Column("type_alert", Integer(), default=1)
    sites = relationship("SiteAlert", back_populates="message_type")

    def __str__(self):  # noqa
        return str(self.email)


class SiteAlert(Base):
    __tablename__ = "logs_page_sitealert"

    id = Column("id", Integer(), primary_key=True)
    uuid = Column("uuid", UUID(as_uuid=True), default=uuid4)
    created = Column("created", DateTime(), default=datetime.now())
    modified = Column("modified", DateTime(), default=datetime.now())
    url_site = Column("url_site", Text, nullable=False)
    enable = Column("enable", Boolean, default=True)
    message_type_id = Column("message_type_id", Integer, ForeignKey("logs_page_messagetype.id"))
    message_type = relationship("MessageType", back_populates="sites")
    site_register = relationship("SiteRegister", back_populates="page")


    def __str__(self):  # noqa
        return str(self.url_site)


class SiteRegister(Base):
    __tablename__ = "logs_page_siteregister"

    id = Column("id", Integer(), primary_key=True)
    uuid = Column("uuid", UUID(as_uuid=True), default=uuid4)
    created = Column("created", DateTime(), default=datetime.now())
    modified = Column("modified", DateTime(), default=datetime.now())
    message_error = Column("message_error", Text, nullable=False)
    status_code = Column("status_code", Text, nullable=False)
    page = relationship("SiteAlert", back_populates="site_register")
    page_id = Column("page_id", Integer, ForeignKey("logs_page_sitealert.id", ondelete="CASCADE"),
                  nullable=False)

    def __str__(self):  # noqa
        return f"{self.status_code} - {self.page}"
