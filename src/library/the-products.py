# the_products_library.py

import json
from pathlib import Path
from fastapi import HTTPException

class ProductLibrary:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.products = self.load_products()

    def load_products(self):
        """Loads the products from the JSON file."""
        if not self.file_path.exists():
            raise HTTPException(status_code=404, detail="JSON file not found")

        with open(self.file_path, "r") as file:
            return json.load(file)

    def get_products_on_sale(self):
        """Returns a list of products that are marked as saving."""
        return [product for product in self.products if product.get("product_is_saving", "false").lower() == "true"]

    def product_exists(self, product_id):
        """Check if a product exists by its ID."""
        return any(product for product in self.products if product.get("id") == product_id)

# Specify the path to your JSON file
file_path = "data/products.json"
product_library = ProductLibrary(file_path)
