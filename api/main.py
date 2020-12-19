from fastapi import FastAPI, APIRouter
from api.managers.message import MessageManager
from fastapi.middleware.cors import CORSMiddleware
from api.routers import root
import logging
import os

logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)
app = FastAPI()
app.include_router(root.router)

origins = os.environ.get("CORS_ALLOWED_ORIGINS").split(",")  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    logger.info("Running Startup Initialization")
