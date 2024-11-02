from fastapi import FastAPI

from src.connection import conn
from src.utils import add_user_routers


app = FastAPI()


add_user_routers(app)

@app.on_event("startup")
def on_startup():
	conn()
