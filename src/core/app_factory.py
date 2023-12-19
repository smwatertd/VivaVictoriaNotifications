from entrypoints import all_routers

from fastapi import FastAPI


def get_production_app() -> FastAPI:
    app = FastAPI()
    _include_routers(app)
    return app


def _include_routers(app: FastAPI) -> None:
    for router in all_routers:
        app.include_router(router)
