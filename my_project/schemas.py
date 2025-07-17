from pydantic import BaseModel

class DetectionSchema(BaseModel):
    message_id: int
    detected_object_class: str
    confidence_score: float

    class Config:
        orm_mode = True

class MessageSchema(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True
