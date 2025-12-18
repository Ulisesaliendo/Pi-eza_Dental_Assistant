from sqlalchemy import Column, Integer, String, Date, Time
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, index=True)
    name = Column(String, nullable=True)


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    reason = Column(String)
    date = Column(Date)
    time = Column(Time)
    status = Column(String, default="pending")
    created_by = Column(String)
