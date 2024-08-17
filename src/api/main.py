from fastapi import FastAPI

from src.api.routes.category_route import router_category
from src.api.routes.location_route import router_location

app = FastAPI()

app.include_router(router=router_location)
app.include_router(router=router_category)
