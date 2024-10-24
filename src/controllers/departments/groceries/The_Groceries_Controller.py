from fastapi import APIRouter, HTTPException, Depends, Request
import logging
from src.helpers.SerialAuth import is_authenticated_serial
from src.helpers.TheHasher import is_authenticated_hash
from src.subcontroller.departments.groceries.Groceries_Savings_Subcontroller import (
    get_all_savings, create_saving, update_saving, delete_saving
)

router = APIRouter()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Authenticate function (optional)
async def authenticate(request: Request, use_auth: bool = False):
    if use_auth:
        await is_authenticated_hash(request)
        await is_authenticated_serial(request)
    return True

# Get all groceries
@router.get("/groceries")
async def get_groceries(auth: bool = Depends(authenticate)):
    groceries_data = await get_all_savings(auth)
    return {"groceries": groceries_data}

# Get grocery by ID
@router.get("/grocery/{id}")
async def get_grocery(id: str, auth: bool = Depends(authenticate)):  
    groceries_data = await get_all_savings(auth)
    for grocery in groceries_data:
        if grocery["id"] == id:
            return {"grocery": grocery}
    raise HTTPException(status_code=404, detail="Grocery not found")

# New route to get grocery saving by ID
@router.get("/groceries/saving/{id}")
async def get_grocery_saving_by_id(id: str, auth: bool = Depends(authenticate)):
    groceries_data = await get_all_savings(auth)
    for grocery in groceries_data:
        if grocery["id"] == id:
            return {"saving": grocery}
    raise HTTPException(status_code=404, detail="Saving not found")

# New route to get savings by category
@router.get("/groceries/savings/category/{category}")
async def get_savings_by_category(category: str, auth: bool = Depends(authenticate)):
    groceries_data = await get_all_savings(auth)
    savings_by_category = [
        grocery for grocery in groceries_data 
        if grocery.get("product_category", "").lower() == category.lower() and grocery.get("product_is_saving", "false").lower() == "true"
    ]
    logger.info("Savings in category '%s': %s", category, savings_by_category)
    if not savings_by_category:
        raise HTTPException(status_code=404, detail="No savings found in this category")
    return {"savings": savings_by_category}

# Create new grocery
@router.post("/grocery")
async def create_grocery(request: Request, auth: bool = Depends(authenticate)):
    groceries_data = await get_all_savings(auth)
    new_grocery = await request.json()
    groceries_data.append(new_grocery)
    return new_grocery  # Return the newly created grocery

# Update grocery by ID
@router.put("/grocery/{id}")
async def update_grocery(id: str, request: Request, auth: bool = Depends(authenticate)):
    groceries_data = await get_all_savings(auth)
    for i, grocery in enumerate(groceries_data):
        if grocery["id"] == id:
            groceries_data[i].update(await request.json())
            return groceries_data[i]
    raise HTTPException(status_code=404, detail="Grocery not found")

# Delete grocery by ID
@router.delete("/grocery/{id}")
async def delete_grocery(id: str, auth: bool = Depends(authenticate)):
    groceries_data = await get_all_savings(auth)
    for i, grocery in enumerate(groceries_data):
        if grocery["id"] == id:
            del groceries_data[i]
            return {"detail": "Grocery deleted"}
    raise HTTPException(status_code=404, detail="Grocery not found")

# ---- Savings Routes ----
@router.get("/groceries/savings")
async def get_savings(auth: bool = Depends(authenticate)):
    return {"savings": await get_all_savings(auth)}

# Get all groceries with savings (product_is_saving = true)
@router.get("/groceries/savings/all")
async def get_all_savings_with_product_is_saving(auth: bool = Depends(authenticate)):
    groceries_data = await get_all_savings(auth)
    logger.info("Retrieved groceries data: %s", groceries_data)
    savings_products = [
        grocery for grocery in groceries_data 
        if grocery.get("product_is_saving", "false").lower() == "true"
    ]
    for index, product in enumerate(savings_products):
        product["id"] = index + 1
    logger.info("Filtered savings products: %s", savings_products)
    return {"savings": savings_products}

@router.post("/groceries/savings")
async def create_saving_entry(request: Request, auth: bool = Depends(authenticate)):
    return await create_saving(request, auth)

@router.put("/groceries/savings/{id}")
async def update_saving_entry(id: str, request: Request, auth: bool = Depends(authenticate)):
    return await update_saving(id, request, auth)

@router.delete("/groceries/savings/{id}")
async def delete_saving_entry(id: str, auth: bool = Depends(authenticate)):
    return await delete_saving(id, auth)
