from sqlalchemy import Column, Integer, String
from database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(String)
    link = Column(String)

class EmailSubscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    event_link = Column(String)

