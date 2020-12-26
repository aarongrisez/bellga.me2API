from fastapi.middleware.cors import CORSMiddleware
from api.config.settings import settings
import logging

logger = logging.getLogger("api")

def init(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origin,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )