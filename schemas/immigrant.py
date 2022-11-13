from datetime import datetime

from pydantic import BaseModel


class ImmigrantBase(BaseModel):
    pass


class ImmigrantCreate(ImmigrantBase):
    firstnames: str
    surnames: str
    age: int
    sex: str

    nationality: str
    date_of_birth: datetime
    card_number: str

    # TODO validate the country of an immigrant
    def _is_from_country(self):
        pass

    # TODO validate the card_number of an immigrant
    def _card_validator(self):
        pass


class Immigrant(ImmigrantBase):
    class Config:
        orm_mode = True
        arbitrary_allowed_types = True
