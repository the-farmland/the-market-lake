from fastapi import HTTPException, Depends, Request
from pathlib import Path
import json
from src.helpers.SerialAuth import is_authenticated_serial
from src.helpers.TheHasher import is_authenticated_hash
from src.subroutes.departments.groceries.Groceries_Savings_Subroute import read_groceries_savings

# Authenticate function (optional)
async def authenticate(request: Request, use_auth: bool = False):
    if use_auth:
        await is_authenticated_hash(request)
        await is_authenticated_serial(request)
    return True

def write_groceries_savings_file(data):
    savings_file = Path("data/dapartments/groceries/groceries-savings-goods.JSON")
    with open(savings_file, "w") as file:
        json.dump(data, file)

# Get all grocery savings
async def get_all_savings(auth: bool = Depends(authenticate)):
    return read_groceries_savings()

# Get grocery saving by ID
async def get_saving_by_id(id: str, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    for saving in savings_data:
        if saving["id"] == id:
            return saving
    raise HTTPException(status_code=404, detail="Saving not found")

# Create a new grocery saving
async def create_saving(request: Request, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    new_saving = await request.json()
    savings_data.append(new_saving)
    write_groceries_savings_file(savings_data)
    return new_saving

# Update grocery saving by ID
async def update_saving(id: str, request: Request, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    for i, saving in enumerate(savings_data):
        if saving["id"] == id:
            savings_data[i].update(await request.json())
            write_groceries_savings_file(savings_data)
            return savings_data[i]
    raise HTTPException(status_code=404, detail="Saving not found")

# Delete grocery saving by ID
async def delete_saving(id: str, auth: bool = Depends(authenticate)):
    savings_data = read_groceries_savings()
    for i, saving in enumerate(savings_data):
        if saving["id"] == id:
            del savings_data[i]
            write_groceries_savings_file(savings_data)
            return {"detail": "Saving deleted"}
    raise HTTPException(status_code=404, detail="Saving not found")
