import json
from pathlib import Path
from fastapi import HTTPException

def read_groceries_savings():
    groceries_file = Path("data/groceries-savings-goods.JSON")
    if groceries_file.exists():
        with open(groceries_file, "r") as file:
            return json.load(file)
    else:
        raise HTTPException(status_code=404, detail="Groceries savings file not found")
