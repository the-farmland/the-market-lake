from fastapi import APIRouter, HTTPException, Depends, Request
from pathlib import Path
import json
from src.helpers.SerialAuth import is_authenticated_serial
from src.helpers.TheHasher import is_authenticated_hash
from src.subroutes.departments.groceries.GroceriesSavingsSubroute import read_groceries_savings

router = APIRouter()

# Modified authenticate function to optionally disable authentication
async def authenticate(request: Request, use_auth: bool = True):
    if use_auth:
        await is_authenticated_hash(request)
        await is_authenticated_serial(request)
    return True

def read_groceries_file():
    groceries_file = Path("data/groceries.json")
    if groceries_file.exists():
        with open(groceries_file, "r") as file:
            return json.load(file)
    else:
        raise HTTPException(status_code=404, detail="Groceries file not found")

@router.get("/grocery/{id}")
async def get_grocery(id: str, auth: bool = Depends(authenticate)):  
    groceries_data = read_groceries_file()
    for grocery in groceries_data:
        if grocery["id"] == id:
            return {"grocery": grocery}
    raise HTTPException(status_code=404, detail="Grocery not found")

@router.get("/groceries")
async def get_groceries(auth: bool = Depends(authenticate)):
    groceries_data = read_groceries_file()
    return {"groceries": groceries_data}

@router.get("/groceries/savings")
async def get_grocery_savings(auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    return {"savings": savings_data}

@router.post("/grocery/post")
async def create_grocery(request: Request, auth: bool = Depends(authenticate)):
    groceries_data = read_groceries_file()
    # Add new grocery to groceries_data
    # Write updated groceries_data back to file
    pass

@router.put("/grocery/update/{id}")
async def update_grocery(id: str, request: Request, auth: bool = Depends(authenticate)):
    groceries_data = read_groceries_file()
    for i, grocery in enumerate(groceries_data):
        if grocery["id"] == id:
            # Update the grocery with the data from the request
            groceries_data[i].update(await request.json())
            with open(Path("data/groceries.json"), "w") as file:
                json.dump(groceries_data, file)
            return {"grocery": groceries_data[i]}
    raise HTTPException(status_code=404, detail="Grocery not found")

@router.delete("/grocery/delete/{id}")
async def delete_grocery(id: str, auth: bool = Depends(authenticate)):  
    groceries_data = read_groceries_file()
    for i, grocery in enumerate(groceries_data):
        if grocery["id"] == id:
            del groceries_data[i]
            with open(Path("data/groceries.json"), "w") as file:
                json.dump(groceries_data, file)
            return {"detail": "Grocery deleted"}
    raise HTTPException(status_code=404, detail="Grocery not found")
