from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from menu_manager.models.plc_tag import PlcTag
import uuid

class PlcTagSqliteRepository:
    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}')
        self.Session = sessionmaker(bind=self.engine)

    def save_tag(self, tag_data):
        session = self.Session()
        try:
            tag = PlcTag(
                company_code=tag_data['company_code'],
                tag_name=tag_data['tag_name'],
                address=tag_data['address'],
                unit=tag_data['unit'],
                data_type=tag_data['data_type'],
                description=tag_data['description']
            )
            session.add(tag)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_all_tags(self):
        session = self.Session()
        try:
            return session.query(PlcTag).all()
        finally:
            session.close()

    def get_tag_by_id(self, tag_id):
        session = self.Session()
        try:
            return session.query(PlcTag).filter_by(id=tag_id).first()
        finally:
            session.close()

    def update_tag(self, tag_id, tag_data):
        session = self.Session()
        try:
            tag = session.query(PlcTag).filter_by(id=tag_id).first()
            if tag:
                for key, value in tag_data.items():
                    setattr(tag, key, value)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_tag(self, tag_id):
        session = self.Session()
        try:
            tag = session.query(PlcTag).filter_by(id=tag_id).first()
            if tag:
                session.delete(tag)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()