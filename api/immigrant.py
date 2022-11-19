from sqlalchemy.orm import Session

from database.models import Immigrant as ImmigrantModel
from schemas.immigrant import ImmigrantCreate


def create_immigrant(db: Session, new_immigrant: ImmigrantCreate) -> ImmigrantModel:
    db_immigrant = ImmigrantModel(**new_immigrant.dict())

    db.add(db_immigrant)
    db.commit()
    db.refresh(db_immigrant)

    return db_immigrant


def get_immigrant(db: Session, immigrant_id: int) -> ImmigrantModel | None:
    return db.get(ImmigrantModel, immigrant_id)
