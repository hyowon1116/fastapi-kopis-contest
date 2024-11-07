from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, Relationship, SQLModel

from src.models.users import User


# 실질적인 Event모델
class RentBase(SQLModel):
	mt10Id: str #공연시설 id
	fcltynm: str
	prfplcnm: str
	entrpsnm: str
	telno: str
	repnm: str
	prfruntime: str
	prfpdfrom: str
	prfpdto: str
	dtguidance : str
	prfnm: str
	prfdescribe: str
	user_email:str
	mt30Id: Optional[str]

# RentBase를 상속하여 사용
class Rent(RentBase, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)