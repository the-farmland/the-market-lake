import json
from pathlib import Path
from fastapi import HTTPException

def read_groceries_savings():
    groceries_file = Path("data/products.JSON")
    if not groceries_file.exists():
        raise HTTPException(status_code=404, detail="groceries savings file not found")

    savings = []
    
    # Read the JSON file line by line
    with open(groceries_file, "r") as file:
        # Load only the relevant JSON array portion
        data_started = False
        for line in file:
            line = line.strip()
            if line.startswith("["):  # Detect the start of the JSON array
                data_started = True
            
            if data_started:
                if line.endswith("]"):  # End of the JSON array
                    # Process the last line of the JSON array
                    item = json.loads(line[:-1])  # Remove the closing bracket for parsing
                    if item.get("product_is_saving", "false").lower() == "true":
                        savings.append(item)
                    break
                
                # Process individual items in the array
                if line.endswith(","):  # This is part of a JSON object
                    line = line[:-1]  # Remove the trailing comma
                try:
                    item = json.loads(line)
                    if item.get("product_is_saving", "false").lower() == "true":
                        savings.append(item)
                except json.JSONDecodeError:
                    continue  # Skip lines that cannot be parsed

    return savings

def check_product_savings():
    products_on_sale = read_groceries_savings()
    for product in products_on_sale:
        print(f"Product ID {product['id']} - Passed (Saving)")

# Example usage
check_product_savings()
