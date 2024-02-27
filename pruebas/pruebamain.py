from typing import Annotated

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

# Un token de seguridad ficticio
fake_secret_token = "coneofsilence"

# Una base de datos ficticia de elementos
fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir un modelo Pydantic para los elementos
class Item(BaseModel):
    id: str
    title: str
    description: str | None = None

# Definir una ruta para obtener detalles de un elemento
@app.get("/items/{item_id}", response_model=Item)
async def read_main(item_id: str, x_token: Annotated[str, Header()]):
    # Verificar si el token en el encabezado X-Token es válido
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    
    # Verificar si el elemento existe en la base de datos ficticia
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Retornar los detalles del elemento si todo es válido
    return fake_db[item_id]

# Definir una ruta para crear un nuevo elemento
@app.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: Annotated[str, Header()]):
    # Verificar si el token en el encabezado X-Token es válido
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    
    # Verificar si el elemento ya existe en la base de datos ficticia
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    # Agregar el nuevo elemento a la base de datos ficticia
    fake_db[item.id] = item
    
    # Retornar el nuevo elemento creado
    return item