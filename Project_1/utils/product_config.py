import json

def load_product_mapping(json_file):
    with open(json_file, encoding='utf-8') as f:
        return json.load(f)

def product_name_from_id(product_id: int) -> str:
    product_map = load_product_mapping("config/product_mapping.json")
    return product_map[str(product_id)]