# main.py
from src.library.The_Products import product_library

def read_groceries_savings():
    """Reads products from the library and checks for savings."""
    products_on_sale = product_library.get_products_on_sale()
    
    if not products_on_sale:
        print("No products are currently on sale.")
    else:
        for product in products_on_sale:
            print(f"Product ID {product['id']} - Passed (Saving)")

# Example usage
read_groceries_savings()
