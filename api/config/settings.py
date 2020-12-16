from functools import lru_cache
from pydantic import BaseSettings
from semver import VersionInfo

class Settings(BaseSettings):
    service_name: str = "Magenta Rapids API"
    version: VersionInfo = VersionInfo.parse("1.0.0")
    admin_email: str = "aaron@aarongrisez.com"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()