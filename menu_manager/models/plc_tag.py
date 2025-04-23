from sqlalchemy import Column, String, Integer, Boolean, DateTime, func, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PlcTag(Base):
    __tablename__ = 'plc_tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_code = Column(String, nullable=False)
    tag_name = Column(String(100), nullable=False)
    address = Column(String(50), nullable=False)
    unit = Column(String(20))
    data_type = Column(String(20))
    description = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    # Composite unique constraint for company_code + address combination
    __table_args__ = (
        UniqueConstraint('company_code', 'address', name='uq_company_address'),
    )