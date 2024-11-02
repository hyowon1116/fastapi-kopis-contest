from pydantic_settings import BaseSettings
from sqlmodel import SQLModel, create_engine, Session

from src.config import get_settings

#디비 파일명
database_file = get_settings().DATABASE_FILE

#디비연결. 
database_connection_string = f'sqlite:///{database_file}'
connect_args = {"check_same_thread":False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)


# Table 생성
def conn():
    SQLModel.metadata.create_all(engine_url)

#세션 사용 후 자동종료
def get_session():
    with Session(engine_url) as session:
        yield session
        