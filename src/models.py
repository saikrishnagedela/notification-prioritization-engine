from pydantic import BaseModel

class Notification(BaseModel):
    user_id: str
    event_type: str
    message: str
    priority_hint: str = "medium"