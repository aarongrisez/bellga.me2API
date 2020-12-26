
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def init(app):

    @app.exception_handler(AuthError)
    async def auth_exception_handler(request: Request, exc: AuthError):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.error
        )