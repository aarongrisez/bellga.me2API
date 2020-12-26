from fastapi import APIRouter, Request
from api.config.settings import settings
from api import app

router = APIRouter()

@router.get("/test")
async def root():
    return {"message": "test route"}

@app.managers.auth.require_auth
def handle_protected_route(request: Request):
    return {"message": "test route"}

@router.get("/test-token")
async def root(request: Request):
    return handle_protected_route(request=request)

def init(app):
    app.include_router(router)