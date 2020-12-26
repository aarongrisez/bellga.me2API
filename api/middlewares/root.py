import importlib
import os
from api.config.settings import settings
from api.core.autoloading import get_initialization

def is_middleware(name):
    """
    """
    return name in settings.allowed_middleware

def init(app):
    return get_initialization("middleware", __file__, is_middleware)(app)