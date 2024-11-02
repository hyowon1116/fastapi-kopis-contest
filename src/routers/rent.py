from fastapi import APIRouter, Depends
from sqlmodel import select
from src.auth.authenticate import authenticate
from src.connection import get_session
from src.models.rent import Event, EventBase


router = APIRouter(prefix="/rent")

@router.get("/")
async def get_events(session=Depends(get_session), user: str=Depends(authenticate)):
	# SQLModel의 select ORM 이벤트 소유자의 이메일과 현재 요청한 유저가 같은 데이터만 가져온다
	_event = session.exec(select(Event).filter(Event.user_email == user)).all()
	return _event

@router.post("/create")
async def create_event(input: EventBase, session=Depends(get_session), user: str=Depends(authenticate)):
	# request input의 값을 딕셔너리로 넘겨준다. user_email이 input에 없으므로 따로 넣어준다.
    new_event = Event(**input.model_dump(), user_email=user)
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": f"The event for {user} was successfully created."
    }

@router.delete("/{event_id}")
async def delete_event(event_id: int, session=Depends(get_session), user: str=Depends(authenticate)):
    # 데이터를 가져오던 중 에러가 나면 예외처리 해준다.
    try:
        _event = session.exec(select(Event).filter(Event.id == event_id)).one()
        # 요청한 유저가 이벤트 소유자인지 검사한다. 아니라면 소유자가 아니므로 에러를 출력한다.
        if (user == _event.user_email):
            session.delete(_event)
            session.commit()
            return {
                "message": f"The event for {_event.user_email} was successfully deleted."
            }
        return {
            "message": "Failed to delete an event. Not event owner"
        }
    except Exception as e:
        return {
            "message": f"Failed to delete an event {e}"
        }