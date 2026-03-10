from sqlalchemy import create_engine, MetaData, Table, Column, String, Float
from sqlalchemy.dialects.postgresql import insert

from config import DATABASE_URL

metadata = MetaData()

chapters = Table(
    "university_chapters",
    metadata,
    Column("chapter_id", String, primary_key=True),
    Column("chapter_name", String),
    Column("city", String),
    Column("state", String),
    Column("latitude", Float),
    Column("longitude", Float),
)

engine = create_engine(DATABASE_URL)


def init_db():
    metadata.create_all(engine)


def load_data(records):
    if not records:
        return

    stmt = insert(chapters).values(records)
    stmt = stmt.on_conflict_do_update(
        index_elements=["chapter_id"],
        set_={
            "chapter_name": stmt.excluded.chapter_name,
            "city": stmt.excluded.city,
            "state": stmt.excluded.state,
            "latitude": stmt.excluded.latitude,
            "longitude": stmt.excluded.longitude,
        },
    )

    with engine.begin() as conn:
        conn.execute(stmt)
