from functools import lru_cache

from fastapi import FastAPI

from src.utils import add_user_routers

app = FastAPI()

add_user_routers(app)