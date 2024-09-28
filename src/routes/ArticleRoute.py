from fastapi import APIRouter, HTTPException, Depends
from pathlib import Path
import json
from src.helpers.serialAuth import is_authenticated_serial

router = APIRouter()

# Placeholder for hash authentication
async def is_authenticated_hash(request):
    # Implement your hash authentication logic here
    return True

@router.get("/product/{id}")
async def get_product(
    id: int,
    auth_serial: bool = Depends(is_authenticated_serial),
    auth_hash: bool = Depends(is_authenticated_hash)
):
    products_file = Path("data/products.json")
    if products_file.exists():
        with open(products_file, "r") as file:
            products_data = json.load(file)
        if 0 <= id < len(products_data):
            return {"product": products_data[id]}
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    else:
        raise HTTPException(status_code=404, detail="Products file not found")

# You can add more routes here, following the pattern in the JavaScript version:
# @router.post("/product/post")
# @router.put("/product/update/{id}")
# @router.delete("/product/delete/{id}")
# @router.get("/products")
