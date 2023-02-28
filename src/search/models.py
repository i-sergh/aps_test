from sqlalchemy import Table, Column, Integer, String, TIMESTAMP
from database  import metadata


documents_tb = Table(
    'documents_tb',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("rubrics", String),
    Column("text", String),
    Column("created_date", TIMESTAMP)
)

