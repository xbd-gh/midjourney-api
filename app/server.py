import uvicorn
from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from exceptions import APPBaseException


def init_app():
    _app = FastAPI(title="Midjourney API")

    register_blueprints(_app)
    exc_handler(_app)

    return _app


def exc_handler(_app):
    @_app.exception_handler(RequestValidationError)
    def validation_exception_handler(_, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=f"request params error: {exc.body}",
        )

    @_app.exception_handler(APPBaseException)
    def validation_exception_handler(_, exc: APPBaseException):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=exc.message,
        )


def register_blueprints(_app):
    from app import routers
    _app.include_router(routers.router, prefix="/v1/api")


def run(host, port):
    _app = init_app()
    uvicorn.run(_app, port=port, host=host)
