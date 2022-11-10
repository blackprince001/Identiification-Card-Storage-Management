from sqlalchemy.orm import declarative_base
from sqlalchemy import Boolean, Integer, String, Datetime

Base = declarative_base()

class Immigrant(Base):
    __tablename__ = "immigrant"

