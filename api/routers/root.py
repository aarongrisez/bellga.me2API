import importlib
import os
from api.config.settings import settings
from api.core.autoloading import get_initialization

def is_router(name):
    """
    """
    return name in settings.allowed_routers

def init(app):
    return get_initialization("routers", __file__, is_router)(app)