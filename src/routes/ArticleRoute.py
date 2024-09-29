from fastapi import APIRouter, HTTPException, Request
from pathlib import Path
import json

router = APIRouter()

def read_products_file():
    products_file = Path("data/products.json")
    if products_file.exists():
        with open(products_file, "r") as file:
            return json.load(file)
    else:
        raise HTTPException(status_code=404, detail="Products file not found")

@router.get("/product/{id}")
async def get_product(id: int):
    products_data = read_products_file()
    if 0 <= id < len(products_data):
        return {"product": products_data[id]}
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@router.get("/products")
async def get_products():
    products_data = read_products_file()
    return {"products": products_data}

@router.post("/product/post")
async def create_product(request: Request):
    # Implement product creation logic
    products_data = read_products_file()
    # Add new product to products_data
    # Write updated products_data back to file
    pass

@router.put("/product/update/{id}")
async def update_product(id: int, request: Request):
    # Implement product update logic
    products_data = read_products_file()
    # Update product in products_data
    # Write updated products_data back to file
    pass

@router.delete("/product/delete/{id}")
async def delete_product(id: int):
    # Implement product deletion logic
    products_data = read_products_file()
    # Remove product from products_data
    # Write updated products_data back to file
    pass
