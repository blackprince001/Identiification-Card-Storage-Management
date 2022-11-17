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

        nat = data["nationality"]
        data["card_number"] = f"{nat[0:3].upper()}-{uniq}-{name[0:3].upper()}"
        super().__init__(**data)


class Immigrant(ImmigrantBase):
    class Config:
        orm_mode = True
        arbitrary_allowed_types = True
