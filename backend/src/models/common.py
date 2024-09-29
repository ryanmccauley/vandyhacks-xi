from pydantic import BaseModel
from typing import Optional

class EmailAddress(BaseModel):
  name: Optional[str]
  email: str

class EmailParticipants(BaseModel):
  sender: EmailAddress
  receiver: EmailAddress