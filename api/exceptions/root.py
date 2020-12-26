import importlib
import os
from api.config.settings import settings
from api.core.autoloading import get_initialization

def is_handler(name):
    """
    """
    return name in settings.allowed_handlers

def init(app):
    return get_initialization("handlers", __file__, is_handler)(app)