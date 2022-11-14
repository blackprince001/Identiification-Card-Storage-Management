from sqlalchemy.orm import Session

from database.models import Citizen as CitizenModel
from schemas.immigrant import CitizenCreate


def create_citizen(db: Session, new_citizen: CitizenCreate) -> CitizenModel:
    db_citizen = CitizenModel(**new_citizen.dict())

    db.add(db_citizen)
    db.commit()
    db.refresh(db_citizen)

    return db_citizen


def get_citizen(db: Session, citizen_id: int) -> CitizenModel | None:
    return db.get(CitizenModel, citizen_id)
