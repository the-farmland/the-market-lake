# The_Products_Library.py
import json

class JsonDataHandler:
    def __init__(self, file_path):
        self.data = self.load_json(file_path)

    def load_json(self, file_path):
        """Load JSON data from a file."""
        with open(file_path, 'r') as file:
            return json.load(file)

    def get_products_on_sale(self):
        """Return products that are on sale."""
        return [product for product in self.data if product.get("product_is_saving") == "true"]

# Initialize the handler and export products on sale
json_file_path = 'products.json'  # Path to your product JSON file
handler = JsonDataHandler(json_file_path)
products_on_sale = handler.get_products_on_sale()

# Define the path for groceries data
groceries_file_path = 'data/dapartments/groceries/groceries-savings-goods.JSON'
