from menu_manager.repository.plc_monitoring_sqlite_repository import PlcMonitoringSqliteRepository
from menu_manager.models.plc_monitoring import Base
from sqlalchemy import create_engine

# Create database engine and tables
engine = create_engine('sqlite:///plc_monitoring.db')
Base.metadata.create_all(engine)

# Initialize repository
plc_monitoring_repo = PlcMonitoringSqliteRepository("plc_monitoring.db")

# J사 데이터 저장
j_company_data = [
    {
        "message_type": "PLC_V2",
        "deviceid": "device001",
        "company_code": "J",
        "sendDatetime": "2025-04-10T16:17:01",
        "messageVersion": 100,
        "type": "D",
        "address": "1000",
        "value": 123.45
    },
    # ... rest of j_company_data ...
]

h_company_data = [
    {
        "message_type": "PLC_V2",
        "deviceid": "device002",
        "company_code": "H",
        "sendDatetime": "2025-04-10T16:17:01",
        "messageVersion": 100,
        "type": "D",
        "address": "138",
        "value": 500
    },
    # ... rest of h_company_data ...
]

# Save monitoring data
for data in j_company_data:
    plc_monitoring_repo.save_monitoring_data(data)

for data in h_company_data:
    plc_monitoring_repo.save_monitoring_data(data)