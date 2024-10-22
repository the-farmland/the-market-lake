import json

class JsonDataHandler:
    def __init__(self, file_path):
        self.data = self.load_json(file_path)

    def load_json(self, file_path):
        """Load JSON data from a file."""
        with open(file_path, 'r') as file:
            return json.load(file)

    def get_all_products(self):
        """Return all products."""
        return self.data

    def get_product_by_id(self, product_id):
        """Return a product by its ID."""
        for product in self.data:
            if product.get("id") == product_id:
                return product
        return None

    def get_available_products(self):
        """Return products that are currently available."""
        return [product for product in self.data if not product.get("productIsCurrentlyUnavailableBUYBOX", False)]

    def get_products_on_sale(self):
        """Return products that are on sale."""
        return [product for product in self.data if product.get("product_is_saving") == "true"]

# Example usage
if __name__ == "__main__":
    json_file_path = 'products.json'  # Path to your JSON file
    handler = JsonDataHandler(json_file_path)
    
    # Example queries
    all_products = handler.get_all_products()
    product_by_id = handler.get_product_by_id("p12")
    available_products = handler.get_available_products()
    products_on_sale = handler.get_products_on_sale()

    print("All Products:", all_products)
    print("Product by ID:", product_by_id)
    print("Available Products:", available_products)
    print("Products on Sale:", products_on_sale)
