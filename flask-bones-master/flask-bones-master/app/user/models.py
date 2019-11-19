import datetime
from flask_login import UserMixin
from app.extensions import bcrypt
from ..database import db, CRUDMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

class User(CRUDMixin, UserMixin, db.Model):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    pw_hash = Column(String(60), nullable=False)
    remote_addr = Column(String(20))
    active = Column(Boolean())
    is_admin = Column(Boolean())
    parent_id_pomocna = Column(Integer, ForeignKey('PomocnaUserToGroup.id'))
    def __init__(self, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(password)

    def __repr__(self):
        return '<User #%s:%r>' % (self.id, self.username)

    def set_password(self, password):
        hash_ = bcrypt.generate_password_hash(password, 10).decode('utf-8')
        self.pw_hash = hash_

    def check_password(self, password):
        return bcrypt.check_password_hash(self.pw_hash, password)

class Firma(CRUDMixin, db.Model):
    __tablename__ = 'Firma'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    ICO = Column(String(128), nullable=False, unique=True)
    created_ts = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    updated_ts = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    parent_id_group = Column(Integer, ForeignKey('Group.id'))

class PomocnaUserToGroup(CRUDMixin , db.Model):
    __tablename__ = 'PomocnaUserToGroup'
    id = Column(Integer, primary_key=True)
    children_user = relationship("User")
    children_group = relationship("Group")

class Group(CRUDMixin, db.Model):
    __tablename__ = 'Group'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    created_ts = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    updated_ts = Column(
        DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )

    parent_id_pomocna = Column(Integer, ForeignKey('PomocnaUserToGroup.id'))
    children_firma = relationship("Firma")
