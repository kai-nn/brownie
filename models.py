from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(100))
    is_active = Column(Boolean)

    login = Column(String(50), unique=True)
    pwd = Column(String(50))

    houses = relationship('Home', back_populates='owner')


class Home(Base):
    __tablename__ = 'home'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(200))

    user_id = Column(Integer, ForeignKey('user.id'))

    owner = relationship('User', back_populates='houses')


class Device(Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(200))
