from menu_manager.repository.plc_tag_sqlite_repository import PlcTagSqliteRepository
from menu_manager.models.plc_tag import Base, PlcTag
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create database engine and tables
engine = create_engine('sqlite:///plc_monitoring.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
try:
    session.query(PlcTag).delete()
    session.commit()
finally:
    session.close()

# Initialize repository and continue with data insertion
plc_tag_repo = PlcTagSqliteRepository("plc_monitoring.db")

# PLC Tag 데이터 저장
j_company_tags = [
    {
        "company_code": "J",
        "tag_name": "메인모터 전류",
        "address": "D1000",
        "unit": "A",
        "data_type": "FLOAT",
        "description": "메인모터 전류값"
    },
    # ... rest of j_company_tags ...
]

h_company_tags = [
    {
        "company_code": "H",
        "tag_name": "생산속도",
        "address": "D138",
        "unit": "EA/min",
        "data_type": "INT",
        "description": "현재 생산 속도"
    },
    # ... rest of h_company_tags ...
]

# Save PLC Tag data
for tag in j_company_tags:
    plc_tag_repo.save_tag(tag)

for tag in h_company_tags:
    plc_tag_repo.save_tag(tag)