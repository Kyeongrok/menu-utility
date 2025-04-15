import json


class Menu:

    def __init__(self, flat_list):
        self.flat_list = flat_list


    def _render_tree_structure(self, flat_list, parent_id=None, level=0, prefix=""):
        result = ""
        children = [item for item in flat_list if item["parent_id"] == parent_id]
        for idx, child in enumerate(children):
            is_last = (idx == len(children) - 1)
            branch = "└─" if is_last else "├─"
            indent = "    " * (level - 1) + ("│   " if level > 0 and not is_last else "    ") if level > 0 else ""
            result += f"{indent}{branch} [{child['id']} {child['name']}]\n"
            result += self._render_tree_structure(flat_list, child["id"], level + 1)
        return result

    def print_rendered_tree(self):
        result = self._render_tree_structure(self.flat_list)
        print(result)

    def print_tree(self):
        for item in self.flat_list:
            # Convert name to uppercase English code
            code = item["name"].upper()
            if code == "루트":
                code = "ROOT"
            elif code == "홈":
                code = "HOME"
            
            # Generate URL from name
            url = "/"
            if item["name"] != "루트":
                url = f"/{item['name'].lower()}"
                if item["name"] == "홈":
                    url = "/home"
            
            node_data = {
                "code": code,
                "nodeIndex": item["id"],
                "parentNodeIndex": item["parent_id"],
                "description": item["name"],
                "sortOrder": 0,
                "url": url
            }
            print(json.dumps(node_data, ensure_ascii=False, indent=2))
