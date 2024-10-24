from fastapi import APIRouter
from src.controllers.departments.groceries.TheGroceriesController import router as groceries_router

groceries_route = APIRouter()

# Include all routes from groceries_controller
groceries_route.include_router(groceries_router)
