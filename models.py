from sqlalchemy import Column, Integer, Float, DateTime
from .database import Base

class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    temperature = Column(Float)
    pressure = Column(Float)