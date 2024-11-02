from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, Relationship, SQLModel

from models.users import User

# 실질적인 Event모델
class EventBase(SQLModel):
	title: str
	description: Optional[str] = None
	date: datetime
	location: Optional[str] = None

# EventBase를 상속하여 사용
class Event(EventBase, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
    # User의 email컬럼을 외래키로 받아온다.
	user_email: EmailStr = Field(foreign_key='user.email')
    # User모델과의 관계를 정의함
	user: Optional["User"] = Relationship(back_populates="events")