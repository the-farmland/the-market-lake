from fastapi import APIRouter, HTTPException, Depends, Request
from src.helpers.SerialAuth import is_authenticated_serial
from src.helpers.TheHasher import is_authenticated_hash
from pathlib import Path
import json
from src.subroutes.departments.groceries.Groceries_Savings_Subroute import read_groceries_savings

router = APIRouter()

# Modified authenticate function to optionally disable authentication
async def authenticate(request: Request, use_auth: bool = False):
    if use_auth:
        await is_authenticated_hash(request)
        await is_authenticated_serial(request)
    return True

def write_groceries_savings_file(data):
    groceries_savings_file = Path("data/dapartments/groceries/groceries-savings-goods.JSON")
    with open(groceries_savings_file, "w") as file:
        json.dump(data, file)

@router.get("/groceries/savings")
async def get_groceries_savings(auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    return {"savings": savings_data}

@router.get("/groceries/savings/{id}")
async def get_grocery_savings_by_id(id: str, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    for saving in savings_data:
        if saving["id"] == id:
            return {"saving": saving}
    raise HTTPException(status_code=404, detail="Grocery saving not found")

@router.post("/groceries/savings")
async def create_grocery_savings(request: Request, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    new_saving = await request.json()
    savings_data.append(new_saving)
    write_groceries_savings_file(savings_data)
    return {"saving": new_saving}

@router.put("/groceries/savings/{id}")
async def update_grocery_savings(id: str, request: Request, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    for i, saving in enumerate(savings_data):
        if saving["id"] == id:
            savings_data[i].update(await request.json())
            write_groceries_savings_file(savings_data)
            return {"saving": savings_data[i]}
    raise HTTPException(status_code=404, detail="Grocery saving not found")

@router.delete("/groceries/savings/{id}")
async def delete_grocery_savings(id: str, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    for i, saving in enumerate(savings_data):
        if saving["id"] == id:
            del savings_data[i]
            write_groceries_savings_file(savings_data)
            return {"detail": "Grocery saving deleted"}
    raise HTTPException(status_code=404, detail="Grocery saving not found")
