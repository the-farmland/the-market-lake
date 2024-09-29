from fastapi import APIRouter, HTTPException, Depends, Request
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
async def get_product(id: str):  # Removed authentication
    products_data = read_products_file()
    for product in products_data:
        if product["id"] == id:
            return {"product": product}
    raise HTTPException(status_code=404, detail="Product not found")

@router.get("/products")
async def get_products():  # Removed authentication
    products_data = read_products_file()
    return {"products": products_data}

@router.post("/product/post")
async def create_product(request: Request):  # Removed authentication
    products_data = read_products_file()
    new_product = await request.json()
    products_data.append(new_product)  # Add new product to products_data
    # Write updated products_data back to file
    with open(Path("data/products.json"), "w") as file:
        json.dump(products_data, file)
    return {"product": new_product}

@router.put("/product/update/{id}")
async def update_product(id: str, request: Request):  # Removed authentication
    products_data = read_products_file()
    for i, product in enumerate(products_data):
        if product["id"] == id:
            products_data[i].update(await request.json())  # Update product
            # Write updated products_data back to file
            with open(Path("data/products.json"), "w") as file:
                json.dump(products_data, file)
            return {"product": products_data[i]}
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/product/delete/{id}")
async def delete_product(id: str):  # Removed authentication
    products_data = read_products_file()
    for i, product in enumerate(products_data):
        if product["id"] == id:
            del products_data[i]  # Remove product
            # Write updated products_data back to file
            with open(Path("data/products.json"), "w") as file:
                json.dump(products_data, file)
            return {"detail": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
