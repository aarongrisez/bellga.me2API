from functools import lru_cache
from pydantic import BaseSettings
from semver import VersionInfo
import os

class Settings(BaseSettings):
    service_name: str = "Bellga.me API"
    version: VersionInfo = VersionInfo.parse("1.0.0")
    admin_email: str = "aaron@aarongrisez.com"
    mongo_db_connection_uri: str = os.environ.get("MONGO_DB_CONNECTION_URI")
    cors_allowed_origin: str = os.environ.get("CORS_ALLOWED_ORIGIN", "")
    auth0_domain: str = os.environ.get("AUTH0_DOMAIN")
    api_identifier: str = os.environ.get("AUTH0_API_IDENTIFIER")
    jwt_signing_algo: str = os.environ.get("JWT_SIGNING_ALGO", "")


    # Middleware
    allowed_middleware: list = [
        "cors"
    ]

    # Managers
    allowed_managers: list = [
        "auth",
        "connection",
        "message"
    ]

    # Routers
    allowed_routers: list = [
        "test",
        "room"
    ]

    # Handlers
    allowed_handlers: list = [
        "auth"
    ]

    class Config:
        env_file = ".env"

settings = Settings()