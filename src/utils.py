from importlib import import_module
from typing import List
from fastapi import APIRouter

from src.logger import ServingLogger

INSTALLED_ROUTERS = [
    "src.routers.main",
    "src.routers.kopis",

]
def get_all_user_routers() -> List[APIRouter]:
    routers = []
    for module_path in INSTALLED_ROUTERS:
        m = import_module(module_path)
        router = getattr(m, "router", None)
        if router and isinstance(router, APIRouter):
            routers.append(router)
        else:
            ServingLogger().debug(f"Can not import router class of {module_path}")

    return routers


def add_user_routers(app):
    for router in get_all_user_routers():
        app.include_router(router)