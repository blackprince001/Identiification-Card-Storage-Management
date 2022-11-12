from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Immigrant(Base):
    __tablename__ = "immigrant"

    id = Column(Integer, primary_key=True, autoincrement=True,)
    
    firstnames = Column(String, nullable=False,)
    surnames = Column(String, nullable=False,)
    age = Column(Integer, nullable=False,)
    sex = Column(String, nullable=False,)

    date_of_birth = Column(DateTime, nullable=False,)
    nationality = Column(String, nullable=False)
    card_number = Column(String, nullable=False)


    def _to_dict(self):
        return {
            "personal": {
                "id": self.id,
                "firstname": self.firstnames,
                "surname": self.surnames,
                "age": self.age,
                "sex": self.sex,
                "DoB": self.date_of_birth
            },
            "government_details": {
                "nationality": self.nationality,
                "card_number": self.card_number
            },
        }