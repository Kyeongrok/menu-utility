import csv
import json

def csv_to_json():
    menu_data = []
    
    with open('menu.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert string 'null' to None
            if row.get('parent_idx') == 'null':
                row['parent_idx'] = None
            else:
                # Convert numeric strings to integers
                row['parent_idx'] = int(row['parent_idx'])
            
            # Convert other numeric fields
            row['No'] = int(row['No'])
            row['idx'] = int(row['idx'])
            
            # Handle empty routes
            if row['Route'].strip() == '':
                row['Route'] = None
            
            # Handle empty categories
            if row['분류'].strip() == '':
                row['분류'] = None
            else:
                row['분류'] = [cat.strip() for cat in row['분류'].split('&')]

            
            # Handle empty codes
                
            menu_data.append(row)
    
    # Write to JSON file
    with open('menu.json', 'w', encoding='utf-8') as jsonfile:
        return json.dump(menu_data, jsonfile, ensure_ascii=False, indent=2)

def create_common_menu(categories=['common']):
    # Read the menu data
    with open('menu.json', 'r', encoding='utf-8') as f:
        menu_data = json.load(f)
    
    # Filter items by categories - check for any common elements between lists
    filtered_items = [item for item in menu_data if item['분류'] and any(cat in item['분류'] for cat in categories)]
    
    # Create menu structure
    menu = {
        "name": "루트",
        "code": "ROOT",
        "child": []
    }
    
    # Build tree structure
    def build_children(parent_idx):
        children = []
        for item in filtered_items:
            if item['parent_idx'] == parent_idx:
                child = {
                    "name": item['항목'],
                    "code": item['코드']
                }
                child_items = build_children(item['idx'])
                if child_items:
                    child["child"] = child_items
                children.append(child)
        return children

    # Start building from root (parent_idx = 0)
    menu["child"] = build_children(0)
    
    return menu

if __name__ == "__main__":
    # Example usage with multiple categories
    menu = create_common_menu(['common', 'mv'])
    with open('filtered_menu.json', 'w', encoding='utf-8') as f:
        json.dump(menu, f, ensure_ascii=False, indent=2)
    # csv_to_json()