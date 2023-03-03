from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Sequence, ARRAY
from database  import metadata


documents_tb = Table(
    'documents_tb',
    metadata,
    Column("id", Integer, Sequence('docs_id_seq'), primary_key=True),
    Column("rubrics", ARRAY(String)),
    Column("text", String),
    Column("created_date", TIMESTAMP)
)

