import json


class Menu:
    node_name_column = "code"
    parent_node_column = "parentNodeIndex"
    node_index_column = "nodeIndex"

    def __init__(self, flat_list):
        self.flat_list = flat_list


    def _render_tree_structure(self, flat_list, parent_id=None, level=0, prefix=""):
        result = ""
        children = [item for item in flat_list if item[self.parent_node_column] == parent_id]
        for idx, child in enumerate(children):
            is_last = (idx == len(children) - 1)
            branch = "└─" if is_last else "├─"
            indent = "    " * (level - 1) + ("│   " if level > 0 and not is_last else "    ") if level > 0 else ""
            result += f"{indent}{branch} [{child[self.node_index_column]} {child[self.node_name_column]}]\n"
            result += self._render_tree_structure(flat_list, child[self.node_index_column], level + 1)
        return result

    def print_rendered_tree(self):
        result = self._render_tree_structure(self.flat_list)
        print(result)

    def print_tree(self):
        for item in self.flat_list:
            # Convert name to uppercase English code
            code = item["code"].upper()
            
            # Generate URL from name
            url = "/"
            if item[self.node_name_column] != "루트":
                url = f"/{item[self.node_name_column].lower()}"
                if item[self.node_name_column] == "홈":
                    url = "/home"
            
            node_data = {
                "code": code,
                "nodeIndex": item["nodeIndex"],
                "parentNodeIndex": item["parentNodeIndex"],
                "description": item[self.node_name_column],
                "sortOrder": 0,
                "url": url
            }
            print(json.dumps(node_data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    menu_item = json.loads("""
    [
      {
        "nodeIndex": 0,
        "parentNodeIndex": null,
        "sortOrder": 0,
        "visibility": false,
        "code": "ROOT",
        "url": "/",
        "description": "루트"
      },
      {
        "nodeIndex": 1,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "HOME",
        "url": "/dashboard",
        "description": "홈"
      },
      {
        "nodeIndex": 2,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "CHART",
        "url": "/chart",
        "description": "차트"
      },
      {
        "nodeIndex": 3,
        "parentNodeIndex": 2,
        "sortOrder": 0,
        "visibility": false,
        "code": "CHART_MACHINE",
        "url": "/chart/machine",
        "description": "설비"
      },
      {
        "nodeIndex": 4,
        "parentNodeIndex": 2,
        "sortOrder": 0,
        "visibility": false,
        "code": "CHART_ESG",
        "url": "/chart/esg",
        "description": "ESG"
      },
      {
        "nodeIndex": 5,
        "parentNodeIndex": 2,
        "sortOrder": 0,
        "visibility": false,
        "code": "CHART_PRODUCTION",
        "url": "/chart/production",
        "description": "생산"
      },
      {
        "nodeIndex": 6,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "MV",
        "url": "/mv",
        "description": "MV"
      },
      {
        "nodeIndex": 7,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "PLC",
        "url": "/plc",
        "description": "PLC"
      },
      {
        "nodeIndex": 8,
        "parentNodeIndex": 7,
        "sortOrder": 0,
        "visibility": false,
        "code": "PLC_DASHBOARD",
        "url": "/plc",
        "description": "현황(PLC)"
      },
      {
        "nodeIndex": 9,
        "parentNodeIndex": 7,
        "sortOrder": 0,
        "visibility": false,
        "code": "PLC_CHART",
        "url": "/plc/chart",
        "description": "차트(PLC)"
      },
      {
        "nodeIndex": 10,
        "parentNodeIndex": 7,
        "sortOrder": 0,
        "visibility": false,
        "code": "PLC_LOG",
        "url": "/plc/log",
        "description": "기록(PLC)"
      },
      {
        "nodeIndex": 11,
        "parentNodeIndex": 7,
        "sortOrder": 0,
        "visibility": false,
        "code": "PLC_ALARM_HISTORY",
        "url": "/plc/history",
        "description": "알람(PLC)"
      },
      {
        "nodeIndex": 12,
        "parentNodeIndex": 7,
        "sortOrder": 0,
        "visibility": false,
        "code": "PLC_ALARM_CODE",
        "url": "/plc/{place_holder}/manual",
        "description": "알람 코드(PLC)"
      },
      {
        "nodeIndex": 13,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "MACHINE",
        "url": "/machine",
        "description": "설비"
      },
      {
        "nodeIndex": 14,
        "parentNodeIndex": 13,
        "sortOrder": 0,
        "visibility": false,
        "code": "MACHINE_ANALYSIS",
        "url": "/machine",
        "description": "분석(MACHINE)"
      },
      {
        "nodeIndex": 15,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "PANELBOARD",
        "url": "/panel-board",
        "description": "분전반"
      },
      {
        "nodeIndex": 16,
        "parentNodeIndex": 15,
        "sortOrder": 0,
        "visibility": false,
        "code": "PANELBOARD_STATUS",
        "url": "/panel-board/daily",
        "description": "현황(분전반)"
      },
      {
        "nodeIndex": 17,
        "parentNodeIndex": 15,
        "sortOrder": 0,
        "visibility": false,
        "code": "PANELBOARD_LOG",
        "url": "/panel-board/log",
        "description": "기록(분전반)"
      },
      {
        "nodeIndex": 18,
        "parentNodeIndex": 15,
        "sortOrder": 0,
        "visibility": false,
        "code": "PANELBOARD_CHART",
        "url": "/panel-board/chart",
        "description": "차트(분전반)"
      },
      {
        "nodeIndex": 19,
        "parentNodeIndex": 15,
        "sortOrder": 0,
        "visibility": false,
        "code": "PANELBOARD_KEPCO",
        "url": "/panel-board/kepco",
        "description": "한전(분전반)"
      },
      {
        "nodeIndex": 20,
        "parentNodeIndex": 19,
        "sortOrder": 0,
        "visibility": false,
        "code": "PANELBOARD_KEPCO_DASHBOARD",
        "url": "/panel-board/kepco",
        "description": "한전(분전반)"
      },
      {
        "nodeIndex": 21,
        "parentNodeIndex": 19,
        "sortOrder": 0,
        "visibility": false,
        "code": "PANELBOARD_KEPCO_LOG",
        "url": "/panel-board/kepco/log",
        "description": "기록(한전)"
      },
      {
        "nodeIndex": 22,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "LOG",
        "url": "/log",
        "description": "기록"
      },
      {
        "nodeIndex": 23,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING",
        "url": "/setting",
        "description": "설정"
      },
      {
        "nodeIndex": 24,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_MACHINE",
        "url": "/setting/machine",
        "description": "설비"
      },
      {
        "nodeIndex": 25,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_TERMINAL",
        "url": "/setting/terminal",
        "description": "터미널"
      },
      {
        "nodeIndex": 26,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_SENSOR",
        "url": "/setting/sensor",
        "description": "센서"
      },
      {
        "nodeIndex": 27,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_DATATYPE",
        "url": "/setting/data-type",
        "description": "데이터 타입"
      },
      {
        "nodeIndex": 28,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_FACTORY",
        "url": "/setting/factory",
        "description": "공장"
      },
      {
        "nodeIndex": 29,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_COMPANY",
        "url": "/setting/company",
        "description": "회사"
      },
      {
        "nodeIndex": 30,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_PANELBOARD",
        "url": "/setting/panel-board",
        "description": "분전반"
      },
      {
        "nodeIndex": 31,
        "parentNodeIndex": 30,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_PANELBOARD_MANAGEMENT",
        "url": "/setting/panel-board/management",
        "description": "분전반 관리"
      },
      {
        "nodeIndex": 32,
        "parentNodeIndex": 30,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_PANELBOARD_EQUIPMENT",
        "url": "/setting/panel-board/equipment",
        "description": "분전반-설비 관리"
      },
      {
        "nodeIndex": 33,
        "parentNodeIndex": 30,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTINGS_PANELBOARD_TARGETPEAK",
        "url": "/setting/panel-board/target-peak",
        "description": "목표 Peak 관리"
      },
      {
        "nodeIndex": 34,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_USER",
        "url": "/setting/user",
        "description": "사용자"
      },
      {
        "nodeIndex": 35,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_NOTIFICATION",
        "url": "/setting/notification",
        "description": "알림"
      },
      {
        "nodeIndex": 36,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_MOBILEDEVICE",
        "url": "/setting/mobile-device",
        "description": "모바일 기기"
      },
      {
        "nodeIndex": 37,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_APPCONFIG",
        "url": "/setting/app-config",
        "description": "앱 설정"
      },
      {
        "nodeIndex": 38,
        "parentNodeIndex": 23,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_MENU",
        "url": "/setting/menu",
        "description": "메뉴"
      },
      {
        "nodeIndex": 39,
        "parentNodeIndex": 38,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_MENU_CRUD",
        "url": "/setting/menu/crud",
        "description": "메뉴관리"
      },
      {
        "nodeIndex": 40,
        "parentNodeIndex": 38,
        "sortOrder": 0,
        "visibility": false,
        "code": "SETTING_MENU_MAPPING",
        "url": "/setting/menu/mapping",
        "description": "메뉴매핑"
      },
      {
        "nodeIndex": 41,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "USER_INFO",
        "url": "/user/info",
        "description": "사용자 정보"
      },
      {
        "nodeIndex": 42,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "WEEKLY_REPORT",
        "url": null,
        "description": "주간 리포트"
      },
      {
        "nodeIndex": 43,
        "parentNodeIndex": 0,
        "sortOrder": 0,
        "visibility": false,
        "code": "MONTHLY_REPORT",
        "url": null,
        "description": "월간 리포트"
      }
    ]
    """)
    print(menu_item)
    menu1 = Menu(menu_item)
    menu1.print_rendered_tree()