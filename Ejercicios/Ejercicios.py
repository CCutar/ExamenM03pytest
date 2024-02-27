###### Ejercicio 1: Ruta con Parámetros
#Crea una nueva ruta en tu aplicación FastAPI en la que se pueda obtener información de un usuario por su ID.
#La ruta debe aceptar un parámetro de ruta user_id y un parámetro de consulta role.
#Si el role es proporcionado, la respuesta debe incluir también la información del rol del usuario.

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/user/{user_id}")
async def read_user(user_id: int, role: str = Query(None, title="Role")):
    user_info = {"user_id": user_id}
    if role:
        user_info["role"] = role
    return user_info

###### Ejercicio 2: Pruebas con Pytest
#Escribe una prueba utilizando Pytest para la nueva ruta creada en el ejercicio anterior.
#Asegúrate de cubrir casos donde se proporciona tanto user_id como role, solo user_id, y casos donde el usuario no existe.

import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def test_client():
    from main import app
    return TestClient(app)

def test_read_user(test_client):
    response = test_client.get("/user/123?role=admin")
    assert response.status_code == 200
    assert response.json() == {"user_id": 123, "role": "admin"}

def test_read_user_no_role(test_client):
    response = test_client.get("/user/456")
    assert response.status_code == 200
    assert response.json() == {"user_id": 456}

def test_read_user_invalid_user(test_client):
    response = test_client.get("/user/not_an_int?role=user")
    assert response.status_code == 422


###### Ejercicio 3: Validación de Datos con Pydantic
#Crea un modelo Pydantic llamado UpdateItem que incluya campos para actualizar el título y la descripción de un elemento.
#Modifica la ruta de creación de elementos para aceptar el nuevo modelo y actualizar un elemento existente si ya existe.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UpdateItem(BaseModel):
    title: str
    description: str

fake_db = {}

@app.put("/update_item/{item_id}")
async def update_item(item_id: str, update_item: UpdateItem):
    if item_id in fake_db:
        fake_db[item_id].update(update_item.dict())
        return fake_db[item_id]
    else:
        return {"error": "Item not found"}

###### Ejercicio 4: Pruebas Asíncronas con Pytest
#Crea una nueva ruta asincrónica en tu aplicación FastAPI que simule una operación asincrónica, como obtener datos de una base de datos asincrónica.
#Escribe una prueba asincrónica utilizando Pytest para la nueva ruta asincrónica.

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_async_route(test_client):
    from .main import app
    
    data = {"name": "Alice", "age": 30}
    response = await test_client.post("/async_route", json=data)
    
    assert response.status_code == 200
    assert response.json() == {"async_data": "Data processed: Alice, 30"}

###### Ejercicio 5: Dependencias Personalizadas
#Crea una dependencia personalizada que verifique la autenticidad de un token en un encabezado Authorization.
#Utiliza esta dependencia en una ruta protegida que devuelva información solo si el token es válido.

from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

def verify_token(authorization: str = Header(...)):
    token = authorization.split(" ")[-1]
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/protected")
async def protected_route(token: str = Depends(verify_token)):
    return {"message": "Access granted"}