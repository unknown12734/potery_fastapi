import uvicorn
from fastapi import FastAPI

from api.app.routers.router import api_router
from api.core.config import settings


def inculde_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.APP_TITLE,
                  version=settings.VERSION)
    inculde_router(app)
    return app


if __name__ == "__main__":
    app = start_application()
    uvicorn.run(app, host= settings.HOST, port =int(settings.PORT))
