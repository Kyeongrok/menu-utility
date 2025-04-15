from copy import deepcopy

from menu import Menu
from menu_by_company import menus
import json


# 트리 구조를 계층적으로 들여쓰며 출력하는 함수
def render_tree_structure(flat_list, parent_id=None, level=0, prefix=""):
    result = ""
    children = [item for item in flat_list if item["parent_id"] == parent_id]
    for idx, child in enumerate(children):
        is_last = (idx == len(children) - 1)
        branch = "└─" if is_last else "├─"
        indent = "    " * (level - 1) + ("│   " if level > 0 and not is_last else "    ") if level > 0 else ""
        result += f"{indent}{branch} [{child['id']} {child['name']}]\n"
        result += render_tree_structure(flat_list, child["id"], level + 1)
    return result


def assign_new_ids(node, parent_id=None):
    global new_id_counter
    node["id"] = new_id_counter
    node["parent_id"] = parent_id
    this_id = new_id_counter
    new_id_counter += 1
    flat_list = [node]
    for child in node.get("child", []):
        flat_list.extend(assign_new_ids(child, this_id))
    return flat_list



# ID 재부여 함수
new_id_counter = 0

# 트리 ID 재정렬 및 평탄화
tree_menu = menus["삼진정공_전주"]
flat_list = assign_new_ids(deepcopy(tree_menu))

# print(flat_list)
menu = Menu(flat_list)
menu.print_tree()