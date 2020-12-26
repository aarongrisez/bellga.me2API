from fastapi import FastAPI
from api.exceptions.root import init as handler_init
from api.middlewares.root import init as middleware_init
from api.managers.root import init as manager_init
from api.routers.root import init as router_init
import logging

logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)
app = FastAPI()

@app.on_event("startup")
async def startup():
    middleware_init(app)
    manager_init(app)

    # Handlers should be initialized after managers so that manager functions available to handlers
    handler_init(app)
    
    # Routers should be initialized last so that all functions are available to routes
    router_init(app)
    print("App initialized")