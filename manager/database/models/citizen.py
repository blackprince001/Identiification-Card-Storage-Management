from sqlalchemy.orm import declarative_base
from sqlalchemy import Boolean, Integer, String, Datetime

Base = declarative_base()

class Citizen(Base):
    __tablename__ = "person"
