import json

element = {
    "name": "루트", "code": "ROOT", "child": [
        {"name": "홈", "code": "HOME"},
        {"name": "차트", "code": "CHART", "child": [
            {"name": "설비", "code": "CHART_FACILITY"},
            {"name": "ESG", "code": "CHART_ESG"},
            {"name": "생산", "code": "CHART_PRODUCTION"},
        ]},
        {"name": "MV", "code": "MV"},
        {"name": "PLC", "code": "PLC", "child": [
            {"name": "현황", "code": "PLC_STATUS"},
            {"name": "차트", "code": "PLC_CHART"},
            {"name": "기록", "code": "PLC_RECORD"},
            {"name": "알람", "code": "PLC_ALARM"},
            {"name": "알람 코드", "code": "PLC_ALARM_CODE"},
        ]},
        {"name": "설비", "code": "MACHINE", "child": [
            {"name": "분석", "code": "MACHINE_ANALYSIS"},
        ]},
        {"name": "기록", "code": "RECORD"},
        {"name": "분전반", "code": "PANEL_BOARD", "child": [
            {"name": "현황", "code": "PANEL_BOARD_STATUS"},
            {"name": "기록", "code": "PANEL_BOARD_RECORD"},
            {"name": "차트", "code": "PANEL_BOARD_CHART"},
        ]},
        {"name": "설정", "code": "SETTINGS", "child": [
            {"name": "설비", "code": "SETTINGS_MACHINE"},
            {"name": "터미널", "code": "SETTINGS_TERMINAL"},
            {"name": "센서", "code": "SETTINGS_SENSOR"},
            {"name": "데이터 타입", "code": "SETTINGS_DATATYPE"},
            {"name": "공장", "code": "SETTINGS_FACTORY"},
            {"name": "회사", "code": "SETTINGS_COMPANY"},
            {"name": "분전반", "code": "SETTINGS_PANEL_BOARD", "child": [
                {"name": "분전반 관리", "code": "SETTINGS_PANEL_BOARD_MANAGE"},
                {"name": "분전반-설비 관리", "code": "SETTINGS_PANEL_BOARD_FACILITY"},
                {"name": "목표 Peak 관리", "code": "SETTINGS_PANEL_BOARD_PEAK"},
            ]},
            {"name": "사용자", "code": "SETTINGS_USER"},
            {"name": "알림", "code": "SETTINGS_NOTIFICATION"},
            {"name": "모바일 기기", "code": "SETTINGS_MOBILE"},
            {"name": "앱 설정", "code": "SETTINGS_APP"},
        ]},
        {"name": "사용자 정보", "code": "USER_INFO"},
        {"name": "주간 리포트", "code": "WEEKLY_REPORT"},
        {"name": "월간 리포트", "code": "MONTHLY_REPORT"},
    ]
}


def create_name_code_map(tree_data):
    name_code_map = {}
    
    def traverse(node):
        name_code_map[node["name"]] = node["code"]
        if "child" in node:
            for child in node["child"]:
                traverse(child)
    
    traverse(tree_data)
    return name_code_map

# Create the map
name_to_code = create_name_code_map(element)

# Print the result
for name, code in name_to_code.items():
    print(f"{name}: {code}")

print(json.dumps(name_to_code, ensure_ascii=False, indent=2))


