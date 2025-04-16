import csv
import json
import os

from api.api_caller import ApiCaller


class MenuFactory:
    def csv_to_json(self, csv_file_name='menu.csv'):
        menu_data = []

        with open(csv_file_name, 'r', encoding='utf-8') as csvfile:
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

    def create_filtered_menu(self, file_name='menu.json', categories=['common']):
        # Read the menu data
        with open(file_name, 'r', encoding='utf-8') as f:
            menu_data = json.load(f)
        
        # Filter items by categories - check for any common elements between lists
        filtered_items = [item for item in menu_data if item['분류'] and any(cat in item['분류'] for cat in categories)]
        
        # Create menu structure
        menu = {
            "name": "루트",
            "code": "ROOT",
            "idx": 0,
            "parent_idx": None,
            "route": "/",
            "child": []
        }
        
        # Build tree structure
        def build_children(parent_idx):
            children = []
            for item in filtered_items:
                if item['parent_idx'] == parent_idx:
                    child = {
                        "name": item['항목'],
                        "code": item['코드'],
                        "idx": item['idx'],
                        "parent_idx": item['parent_idx'],
                        "route": item['Route']
                    }
                    child_items = build_children(item['idx'])
                    if child_items:
                        child["child"] = child_items
                    children.append(child)
            return children

        # Start building from root (parent_idx = 0)
        menu["child"] = build_children(0)
        
        return menu

def flatten_menu(menu_data, parent_id=None, result=None):
    if result is None:
        result = []
        
    # Add current node
    # {
    #     "code": "ROOT",
    #     "nodeIndex": 0,
    #     "nodeParentIndex": null,
    #     "description": "루트노드",
    #     "sortOrder": 0,
    #     "url": "/"
    #   },
    current = {
        "code": menu_data["code"],
        "nodeIndex": menu_data["idx"],
        "nodeParentIndex": menu_data["parent_idx"],
        "description": menu_data["name"],
        "sortOrder": 0,
        "url": menu_data["route"],
        "visibility": True
    }
    result.append(current)
    
    # Process children if they exist
    if "child" in menu_data:
        for child in menu_data["child"]:
            flatten_menu(child, menu_data["code"], result)
            
    return result


if __name__ == "__main__":
    l1 = [
        ["mv"],
        ["machiney"],
        ["plc"],
        ["panel_board"],
        ["mv", "machiney"],
        ["mv", "plc"],
        ["mv", "panel_board"],
        ["machiney", "plc"],
        ["machiney", "panel_board"],
        ["plc", "panel_board"],
        ["mv", "machiney", "plc"],
        ["mv", "machiney", "panel_board"],
        ["mv", "plc", "panel_board"],
        ["machiney", "plc", "panel_board"],
        ["mv", "machiney", "plc", "panel_board"]
    ]

    # 'common', 'mv', 'machiney', 'plc', 'panel_board'
    menu_factory = MenuFactory()
    BASE_URL = "http://localhost:8080"
    api = ApiCaller(BASE_URL)
    login_result = api.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    print(login_result['result']['accessJwt'])

    for combination in l1:
        name = ', '.join(item.upper() for item in combination)
        name = f"{name}메뉴"
        combination.append("common")
        menu_factory.csv_to_json('menu.csv')
        menu = menu_factory.create_filtered_menu('menu.json', combination)
        flat_menu = flatten_menu(menu)
        print(combination, json.dumps( flat_menu, ensure_ascii=False))
        api.create_menu(name, name, flat_menu)

