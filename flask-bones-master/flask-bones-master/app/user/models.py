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
    name = Column(String(20), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=False)
    cas_od_do = Column(Integer, ForeignKey('Cas.id'))
    def __init__(self, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(password)
    def __repr__(self):
        return '<User #%s:%r>' % (self.id, self.name)
    def set_password(self, password):
        hash_ = bcrypt.generate_password_hash(password, 10).decode('utf-8')
        self.pw_hash = hash_
    def check_password(self, password):
        return bcrypt.check_password_hash(self.pw_hash, password)
    id_firma = Column(Integer, ForeignKey('Firma.id'))
    id_skupina = Column(Integer, ForeignKey('Skupina.id'))
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
    User_child_firma = relationship("User")
class Skupina(CRUDMixin, db.Model):
    __tablename__ = 'Skupina'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    id_typ = Column(Integer)
    User_child_skupina = relationship("User")
    typ_id = Column(Integer, ForeignKey('Prava.id'))

class Cas(CRUDMixin, db.Model):
    __tablename__ = 'Cas'
    id = Column(Integer, primary_key=True)
    cas_od_do = Column(DateTime)
    User_child_cas = relationship("User")

class Prava(CRUDMixin, db.Model):
    __tablename__ = 'Prava'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    User_child_prava = relationship("Skupina")