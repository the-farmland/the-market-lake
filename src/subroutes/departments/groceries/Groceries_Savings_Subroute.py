# main_file.py (where read_groceries_savings is defined)
import json
from fastapi import HTTPException
from src.library.The_Products import products_on_sale, groceries_file_path  # Import products_on_sale and groceries_file_path

def read_groceries_savings():
    if Path(groceries_file_path).exists():
        with open(groceries_file_path, "r") as file:
            groceries_data = json.load(file)
            # Return both groceries data and products on sale
            return {"groceries": groceries_data, "products_on_sale": products_on_sale}
    else:
        raise HTTPException(status_code=404, detail="Groceries savings file not found")

# Example usage
if __name__ == "__main__":
    result = read_groceries_savings()
    print(result)
