class codeMapper:
    def __init__(self):
        pass

code_map = {
  "루트": "ROOT",
  "홈": "HOME",
  "차트": "PANEL_BOARD_CHART",
  "설비": "SETTINGS_MACHINE",
  "ESG": "CHART_ESG",
  "생산": "CHART_PRODUCTION",
  "MV": "MV",
  "PLC": "PLC",
  "현황": "PANEL_BOARD_STATUS",
  "기록": "PANEL_BOARD_RECORD",
  "알람": "PLC_ALARM",
  "알람 코드": "PLC_ALARM_CODE",
  "분석": "MACHINE_ANALYSIS",
  "분전반": "SETTINGS_PANEL_BOARD",
  "설정": "SETTINGS",
  "터미널": "SETTINGS_TERMINAL",
  "센서": "SETTINGS_SENSOR",
  "데이터 타입": "SETTINGS_DATATYPE",
  "공장": "SETTINGS_FACTORY",
  "회사": "SETTINGS_COMPANY",
  "분전반 관리": "SETTINGS_PANEL_BOARD_MANAGE",
  "분전반-설비 관리": "SETTINGS_PANEL_BOARD_FACILITY",
  "목표 Peak 관리": "SETTINGS_PANEL_BOARD_PEAK",
  "사용자": "SETTINGS_USER",
  "알림": "SETTINGS_NOTIFICATION",
  "모바일 기기": "SETTINGS_MOBILE",
  "앱 설정": "SETTINGS_APP",
  "사용자 정보": "USER_INFO",
  "주간 리포트": "WEEKLY_REPORT",
  "월간 리포트": "MONTHLY_REPORT",
}

url_map = { 
    "ROOT":"/", 
    "HOME":"/dashboard" ,
    "PANEL_BOARD_CHART":"/chart",
    "SETTINGS_MACHINE":"/chart?tab=machine",
    "CHART_ESG":"/chart?tab=esg",
    "CHART_PRODUCTION":"/chart?tab=production",
    "MV":"/mv",
    "PLC":"/plc",
    "PLC_STATUS":"/plc",
    "PLC_CHART":"/plc/chart",
    "PLC_RECORD":"/plc/log",
    "PLC_ALARM":"/plc/history",
    "PLC_ALARM_CODE":"/plc/\{place_holder\}/manual",
    "MACHINE":"/machine",
    "MACHINE_ANALYSIS":"/machine",
    "PANEL_BOARD":"/panel-board",
    "PANEL_BOARD_STATUS":"/panel-board/daily",
    "PANEL_BOARD_LOG":"/panel-board/log",
    "PANEL_BOARD_RECORD":"/panel-board/log",
    "PANEL_BOARD_CHART":"/panel-board/chart",
    "PANEL_BOARD_KEPCO":"/panel-board/kepco",
    "PANEL_BOARD_KEPCO_LOG":"/panel-board/kepco/log",
    "SETTINGS":"/setting",
    "SETTINGS_TERMINAL":"/setting/terminal",
    "SETTINGS_SENSOR":"/setting/sensor",
    "SETTINGS_DATATYPE":"/setting/data-type",
    "SETTINGS_FACTORY":"/setting/factory",
    "SETTINGS_COMPANY":"/setting/company",
    "SETTINGS_PANEL_BOARD_MANAGE":"/setting/panel-board/management",
    "SETTINGS_PANEL_BOARD_FACILITY":"/setting/panel-board/equipment",
    "SETTINGS_PANEL_BOARD_PEAK":"/setting/panel-board/target-peak",
    "SETTINGS_USER":"/setting/user",
    "SETTINGS_NOTIFICATION":"/setting/notification",
    "SETTINGS_MOBILE":"/setting/mobile-device",
    "SETTINGS_APP":"/setting/app-config",
    "USER_INFO":"/user/info",
    "WEEKLY_REPORT": None,
    "MONTHLY_REPORT": None,
}


idx = 1
for key, value in code_map.items():
    try:
        print(f"{key},{value},{idx},{url_map[value]}")
    except KeyError:
        print(f"{key},{value},{idx},None")
    idx += 1