from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []


class Item(BaseModel):
    name: str
    price: float


# Tarefa 1: crie a rota GET "/" aqui.

# Tarefa 2: crie a rota GET "/items/{item_id}" aqui.

# Tarefa 3: crie a rota POST "/items" aqui.

# Tarefa 4: adicione o tratamento de erro 404 na rota GET "/items/{item_id}".
