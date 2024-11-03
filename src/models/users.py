from typing import List, Optional
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, Relationship, SQLModel


class Signup(SQLModel):
	email: EmailStr
	username: str
    # exp는 사실 저장할 필요가 없다. post용 모델을 따로 선언해주기 귀찮아서 선언했다.
	exp: int
    # 로그인 유저 인증은 구글에서 해주니까 비밀번호는 필요 없다.

class User(SQLModel, table=True):
	email: EmailStr = Field(primary_key=True)
	username: Optional[str]
	role: str = Field(default="general")#공연제작자: company / 공연시설: theater/ 일반: general
	mt30Id: Optional[str] # company id
	mt10Id: Optional[str] # 공연시설id
	likedfcltys: Optional[str] # mt10Id. 공연시설id 저장.

