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
  "월간 리포트": "MONTHLY_REPORT"
}

idx = 1
for key, value in code_map.items():
    print(f"{key},{value},{idx}")
    idx += 1