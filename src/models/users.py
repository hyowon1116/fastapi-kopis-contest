from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
	email: EmailStr = Field(primary_key=True)
	username: str
    
class Signup(SQLModel):
	email: EmailStr
	username: str
    # exp는 사실 저장할 필요가 없다. post용 모델을 따로 선언해주기 귀찮아서 선언했다.
	exp: int
    # 로그인 유저 인증은 구글에서 해주니까 비밀번호는 필요 없다.
