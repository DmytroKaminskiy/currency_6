from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def root():
    return {"message": "Root Post"}


@app.get("/items/{item_id}")
# def items(item_id: int, count: Optional[int] = None):
def items(item_id: int, count):
# def items(item_id: int, count: int = 0):
    print(count)
    return {'item_id': item_id}
