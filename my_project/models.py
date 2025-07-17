from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Message(Base):
    __tablename__ = "fct_messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)

class Detection(Base):
    __tablename__ = "fct_image_detections"
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("fct_messages.id"))
    detected_object_class = Column(String)
    confidence_score = Column(Float)
