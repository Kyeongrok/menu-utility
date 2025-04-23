import uuid
from typing import Dict, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.plc_monitoring import Base, PlcMonitoring

class PlcMonitoringSqliteRepository:
    def __init__(self, db_path: str):
        self.engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_monitoring_data(self, data: Dict[str, Any]):
        session = self.Session()
        try:
            logid = data.get('logid', str(uuid.uuid4()))
            
            # Create monitoring record
            monitoring = PlcMonitoring(
                logid=logid,
                message_type=data['message_type'],
                deviceid=data['deviceid'],
                company_code=data['company_code'],
                send_datetime=data['sendDatetime'],
                message_version=data['messageVersion'],
                type=data['type'],
                address=data['address'],
                value=float(data['value'])
            )
            
            session.add(monitoring)
            session.commit()
            
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_monitoring_data(self, logid: str) -> Dict[str, Any]:
        session = self.Session()
        try:
            monitoring = session.query(PlcMonitoring).filter_by(logid=logid).first()
            
            if not monitoring:
                return None
            
            return {
                'logid': monitoring.logid,
                'message_type': monitoring.message_type,
                'deviceid': monitoring.deviceid,
                'company_code': monitoring.company_code,
                'sendDatetime': monitoring.send_datetime,
                'messageVersion': monitoring.message_version,
                'type': monitoring.type,
                'address': monitoring.address,
                'value': monitoring.value
            }
            
        finally:
            session.close()