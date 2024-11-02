from fastapi import APIRouter, Depends
from sqlmodel import select
from src.auth.authenticate import authenticate
from src.connection import get_session
from src.models.rent import Rent, RentBase


router = APIRouter(prefix="/rent")

@router.get("/")
async def get_rents(session=Depends(get_session), user: str=Depends(authenticate)):
	# SQLModel의 select ORM 이벤트 소유자의 이메일과 현재 요청한 유저가 같은 데이터만 가져온다
	_rent = session.exec(select(Rent).filter(Rent.user_email == user)).all()
	return _rent

@router.post("/create")
async def create_rent(input: RentBase, session=Depends(get_session), user: str=Depends(authenticate)):
	# request input의 값을 딕셔너리로 넘겨준다. user_email이 input에 없으므로 따로 넣어준다.
    new_rent = Rent(**input.model_dump(), user_email=user)
    session.add(new_rent)
    session.commit()
    session.refresh(new_rent)
    return {
        "message": f"The rent for {user} was successfully created."
    }

@router.delete("/{rent_id}")
async def delete_rent(rent_id: int, session=Depends(get_session), user: str=Depends(authenticate)):
    # 데이터를 가져오던 중 에러가 나면 예외처리 해준다.
    try:
        _rent = session.exec(select(Rent).filter(Rent.id == rent_id)).one()
        # 요청한 유저가 이벤트 소유자인지 검사한다. 아니라면 소유자가 아니므로 에러를 출력한다.
        if (user == _rent.user_email):
            session.delete(_rent)
            session.commit()
            return {
                "message": f"The rent for {_rent.user_email} was successfully deleted."
            }
        return {
            "message": "Failed to delete an rent. Not rent owner"
        }
    except Exception as e:
        return {
            "message": f"Failed to delete an rent {e}"
        }