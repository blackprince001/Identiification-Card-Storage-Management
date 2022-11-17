import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from schemas.citizen import CitizenCreate as CitizenSchema
from schemas.immigrant import ImmigrantCreate as ImmigrantSchema

Base = declarative_base()


@pytest.fixture(scope="session")
def engine():
    return create_engine(url="sqlite+pysqlite:///database.db", future=True)
