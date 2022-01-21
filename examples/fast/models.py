import sqlalchemy
from sqlalchemy.types import JSON


metadata = sqlalchemy.MetaData()


zoom_webhook_events_table = sqlalchemy.Table(
    "zoom_webhook_events",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("event", sqlalchemy.String(100), index=True),
    sqlalchemy.Column("event_ts", sqlalchemy.BigInteger),
    sqlalchemy.Column('payload', JSON),
)
