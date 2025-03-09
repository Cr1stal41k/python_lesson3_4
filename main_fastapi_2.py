from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from app_config import app_config


# Определим модель для данных, которые будем получать через POST-запрос
class Item(BaseModel):
    name: str
    description: str = None
    price: float

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Привет, user!"}

# Обработка GET-запроса с параметром пути
@app.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Обработка POST-запроса с JSON-данными
@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

# Обработка PUT-запроса для обновления данных
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

# Обработка DELETE-запроса
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}


if __name__ == "__main__":
    uvicorn.run("main_fastapi_2:app", host=app_config.host, port=app_config.port)





