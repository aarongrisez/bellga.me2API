import importlib
import os
from api.config.settings import settings
from api.core.autoloading import get_initialization

def is_manager(name):
    """
    """
    return name in settings.allowed_managers

def init(app):
    return get_initialization("managers", __file__, is_manager)(app)