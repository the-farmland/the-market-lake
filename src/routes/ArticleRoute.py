from fastapi import APIRouter, HTTPException, Depends, Request
from pathlib import Path
import json
from src.helpers.SerialAuth import is_authenticated_serial
from src.helpers.TheHasher import is_authenticated_hash

router = APIRouter()

async def authenticate(request: Request):
    await is_authenticated_hash(request)
    await is_authenticated_serial(request)
    return True

@router.get("/product/{id}")
async def get_product(id: int, auth: bool = Depends(authenticate)):
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

@router.post("/product/post")
async def create_product(request: Request, auth: bool = Depends(authenticate)):
    # Implement product creation logic
    pass

@router.put("/product/update/{id}")
async def update_product(id: int, request: Request, auth: bool = Depends(authenticate)):
    # Implement product update logic
    pass

@router.delete("/product/delete/{id}")
async def delete_product(id: int, auth: bool = Depends(authenticate)):
    # Implement product deletion logic
    pass

@router.get("/products")
async def get_products(auth: bool = Depends(authenticate)):
    # Implement logic to get all products
    pass
