from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select

from src.auth.authenticate import authenticate
from src.auth.jwt import create_access_token
from src.connection import get_session
from src.data.users import TokenResponse
from src.models.users import Signup, User
from src.logger import ServingLogger


router = APIRouter(prefix="/user")


@router.get("/")
def get_user(user:str, session=Depends(get_session)):
	# SQLModel의 select ORM 이벤트 소유자의 이메일과 현재 요청한 유저가 같은 데이터만 가져온다
	_user = session.exec(select(User).filter(User.email == user)).one()
	return _user

# Response를 TokenResponse 모델로 지정
@router.post("/login", response_model=TokenResponse)
async def login(input: Signup,session=Depends(get_session)) -> dict:
	# 로그인 유저가 DB에 있는지 검사한뒤
	existing_user = session.get(User , input.email)
	try:
	    # 있다면 토큰을 발행하고 리턴
		if existing_user:
			access_token = create_access_token(input.email, input.exp)
		else: 
        # 없다면 DB에 저장하고 리턴
			_user = User(email=input.email, username=input.username )
			session.add(_user)
			session.commit()
			session.refresh(_user)
			access_token = create_access_token(input.email, input.exp)
		return {
				"access_token": access_token,
				"token_type": "Bearer"
			}
	except:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Bad Parameter",
		)