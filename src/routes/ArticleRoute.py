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
    index = id - 1  # Adjust ID to match 0-based index
    if 0 <= index < len(products_data):
        return {"product": products_data[index]}
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
    products_data = read_products_file()
    index = id - 1  # Adjust ID to match 0-based index
    if 0 <= index < len(products_data):
        # Update product in products_data
        # Write updated products_data back to file
        pass
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/product/delete/{id}")
async def delete_product(id: int):
    products_data = read_products_file()
    index = id - 1  # Adjust ID to match 0-based index
    if 0 <= index < len(products_data):
        # Remove product from products_data
        # Write updated products_data back to file
        pass
    else:
        raise HTTPException(status_code=404, detail="Product not found")
