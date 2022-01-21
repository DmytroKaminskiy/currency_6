from os import environ
import databases

from models import zoom_webhook_events_table

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


# берем параметры БД из переменных окружения
DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASS", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = environ.get("DB_NAME", "localhost")
DB_PORT = environ.get("DB_PORT", "5432")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)


class ZoomWebhookItem(BaseModel):
    payload: dict
    event_ts: int
    event: str


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post('/zoom/webhook')
async def zoom_webhook(zoom_webhook_item: ZoomWebhookItem):
    # print(zoom_webhook_item.payload)
    # print(zoom_webhook_item.event_ts)
    # print(zoom_webhook_item.event)
    query = zoom_webhook_events_table.insert().values(**zoom_webhook_item.dict())
    item_id = await database.execute(query)
    print(item_id)
    return {}
