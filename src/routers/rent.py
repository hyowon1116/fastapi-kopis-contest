from fastapi import APIRouter, Depends
from sqlmodel import select
from src.models.users import User
from src.auth.authenticate import authenticate
from src.connection import get_session
from src.models.rent import Rent, RentBase


router = APIRouter(prefix="/rent")
@router.get("/")
async def get_rents(user:str, session=Depends(get_session)):
    try:
        _rent = session.exec(select(Rent).filter(Rent.user_email == user)).all()
        return _rent
    except:
        return []

@router.get("/received")
async def get_rents(user: str, session=Depends(get_session)):
    try:
        # SQLModel의 select ORM 이벤트 소유자의 이메일과 현재 요청한 유저가 같은 데이터만 가져온다
        _user = session.exec(select(User).filter(User.email == user)).one()
        _rent = session.exec(select(Rent).filter(Rent.mt30Id == _user.mt30Id)).all()
        return _rent
    except:
        return []

@router.post("/")
async def create_rent(input: RentBase, session=Depends(get_session)):
	# request input의 값을 딕셔너리로 넘겨준다. user_email이 input에 없으므로 따로 넣어준다.
    new_rent = Rent(**input.model_dump())
    session.add(new_rent)
    session.commit()
    session.refresh(new_rent)
    return {
        "message": f"The rent for {new_rent.id} was successfully created."
    }

@router.delete("/")
async def delete_rent(rent_id: int, user: str, session=Depends(get_session)):
    # 데이터를 가져오던 중 에러가 나면 예외처리 해준다.
    try:
        _rent = session.exec(select(Rent).filter(Rent.id == rent_id)).one()
        # 요청한 유저가 이벤트 소유자인지 검사한다. 아니라면 소유자가 아니므로 에러를 출력한다.
        if (user == _rent.user_email):
            session.delete(_rent)
            session.commit()
            return {
                "message": f"The rent for {_rent.id} was successfully deleted."
            }
        return {
            "message": "Failed to delete an rent. Not rent owner"
        }
    except Exception as e:
        return {
            "message": f"Failed to delete an rent {e}"
        }