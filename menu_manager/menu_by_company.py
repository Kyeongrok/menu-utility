from code_map import code_map
import json

# Read menus from JSON file
menus = {}
with open('../menu_by_company.json', 'r', encoding='utf-8') as f:
    menus = json.load(f)

def dfs_collect(node, result=None, path=None):
    if result is None:
        result = []
    if path is None:
        path = []
        
    # Add current node info
    current = {
        'name': node['name'],
        'path': path.copy(),
        'depth': len(path)
    }
    result.append(current)
    
    # Traverse children
    if "child" in node:
        for child in node["child"]:
            path.append(node['name'])
            dfs_collect(child, result, path)
            path.pop()
            
    return result

# Collect all nodes with their paths
nodes = dfs_collect(menus['쓰리뷰'])

# for node in nodes:
#     print(code_map[node['name']])
#     print(f"{'  ' * node['depth']}- {node['name']} (Path: {' > '.join(node['path'])})")


def transform_menu_with_code(node):
    result = {
        "name": node["name"],
        "code": code_map[node["name"]]
    }
    
    if "child" in node:
        result["child"] = [transform_menu_with_code(child) for child in node["child"]]
    
    return result

# Initialize empty dictionary
r = {}

# Process each company's menu
for key, menu in menus.items():
    transformed_menu = transform_menu_with_code(menu)
    r[key] = transformed_menu  # Simply assign the transformed menu to the dictionary with company key

# Print to console and write to file
json_output = json.dumps(r, ensure_ascii=False, indent=2)
print(json_output)

# Write to file
# with open('menu_by_company.json', 'w', encoding='utf-8') as f:
#     f.write(json_output)
