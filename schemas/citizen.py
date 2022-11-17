from datetime import datetime

from pydantic import BaseModel


class CitizenBase(BaseModel):
    pass


class CitizenCreate(CitizenBase):
    firstnames: str
    surnames: str
    age: int
    sex: str

    social_security_number: str = None
    date_of_birth: datetime
    place_of_birth: str
    card_number: str

    is_registered_voter: bool

    def __init__(self, **data):
        # generates card number for every instance
        name = data["surnames"]
        uniq = (
            hash(
                data["date_of_birth"].day
                + (
                    len(data["surnames"])
                    * len(data["surnames"])
                    / data["date_of_birth"].year
                    + data["date_of_birth"].month
                )
            )
            % 30_000_000
        )

        data["card_number"] = f"GHA-{uniq}-{name[0:3].upper()}"
        super().__init__(**data)


class Citizen(CitizenBase):
    class Config:
        orm_mode = True
        arbitrary_allowed_types = True
