import datetime
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from schemas.citizen import CitizenCreate as CitizenSchema
from schemas.immigrant import ImmigrantCreate as ImmigrantSchema
from database.models import Base


@pytest.fixture(scope="session")
def engine():
    return create_engine(url="sqlite+pysqlite:///database.db", future=True)


@pytest.fixture(scope="session")
def citizen():
    doB = datetime.datetime.now()
    return CitizenSchema(
        firstnames="Prince",
        surnames="Appiah",
        age=99,
        sex="M",
        date_of_birth=doB,
        place_of_birth="Amakom Kumasi",
        is_registered_voter=False,
    )


@pytest.fixture(scope="session")
def immigrant():
    doB = datetime.datetime.now()
    return ImmigrantSchema(
        firstnames="Black",
        surnames="Prince",
        age=99,
        sex="F",
        date_of_birth=doB,
        nationality="Pirate",
    )


@pytest.fixture
def db(engine):
    with Session(engine) as session:
        Base.metadata.create_all(bind=engine)
        yield session
