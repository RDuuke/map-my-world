from fastapi import FastAPI

from src.api.routes.location_route import router

app = FastAPI()

app.include_router(router=router)
