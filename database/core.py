from sqlalchemy import create_engine

url = "sqlite+pysqlite:///./database.db"

engine = create_engine(
    url=url,
    echo=False,
    future=True,
    connect_args={"check_same_thread": False},
)