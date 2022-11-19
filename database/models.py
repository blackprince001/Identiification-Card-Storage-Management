from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Citizen(Base):
    __tablename__ = "citizen"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    firstnames = Column(
        String,
        nullable=False,
    )
    surnames = Column(
        String,
        nullable=False,
    )
    age = Column(
        Integer,
        nullable=False,
    )
    sex = Column(
        String,
        nullable=False,
    )

    social_security_number = Column(
        String,
        nullable=True,
        default="None",
    )
    date_of_birth = Column(
        DateTime,
        nullable=False,
    )
    place_of_birth = Column(String, nullable=False)
    place_of_issuance = Column(
        String,
        nullable=False,
    )
    card_number = Column(String, nullable=False)

    is_registered_voter = Column(Boolean, nullable=False, default=False)

    def _to_dict(self):
        return {
            "personal": {
                "id": self.id,
                "firstname": self.firstnames,
                "surname": self.surnames,
                "age": self.age,
                "sex": self.sex,
                "DoB": self.date_of_birth,
            },
            "government_details": {
                "social_security_number": self.social_security_number,
                "place_of_birth": self.place_of_birth,
                "place_of_issuance": self.place_of_issuance,
                "card_number": self.card_number,
            },
            "is_registerd_voter": self.is_registered_voter,
        }


class Immigrant(Base):
    __tablename__ = "immigrant"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    firstnames = Column(
        String,
        nullable=False,
    )
    surnames = Column(
        String,
        nullable=False,
    )
    age = Column(
        Integer,
        nullable=False,
    )
    sex = Column(
        String,
        nullable=False,
    )

    date_of_birth = Column(
        DateTime,
        nullable=False,
    )
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
                "DoB": self.date_of_birth,
            },
            "government_details": {
                "nationality": self.nationality,
                "card_number": self.card_number,
            },
        }
