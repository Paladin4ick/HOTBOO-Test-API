from fastapi import FastAPI


routers = []


def create_app() -> FastAPI:
    app = FastAPI()
    
    for router in routers:
        app.include_router(router)
    
    return app