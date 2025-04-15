from copy import deepcopy

from domain.menu import Menu
from menu_by_company import menus
import json


# ID 재부여 함수
def assign_new_ids(node, parent_id=None, counter=0):
    node["id"] = counter
    node["parent_id"] = parent_id
    this_id = counter
    flat_list = [node]
    
    for child in node.get("child", []):
        child_flat_list, counter = assign_new_ids(child, this_id, counter + 1)
        flat_list.extend(child_flat_list)
    
    return flat_list, counter + 1

# Usage example:
tree_menu = menus["삼진정공_전주"]
flat_list, _ = assign_new_ids(deepcopy(tree_menu))

menu = Menu(flat_list)
menu.print_tree()