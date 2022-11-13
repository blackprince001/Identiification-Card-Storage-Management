from datetime import datetime

from pydantic import BaseModel


class CitizenBase(BaseModel):
    pass


class CitizenCreate(CitizenBase):
    firstnames: str
    surnames: str
    age: int
    sex: str

    social_security_number: str
    date_of_birth: datetime
    place_of_birth: str
    card_number: str

    is_registered_voter: bool

    # TODO validate the card_number of a Citizen
    def _card_validator(self):
        pass


class Citizen(CitizenBase):
    class Config:
        orm_mode = True
        arbitrary_allowed_types = True
