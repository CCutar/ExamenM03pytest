###### Ejercicio 1: Inyección de Dependencias en FastAPI
#Define una función obtener_usuario que devuelve un diccionario con información básica de un usuario (por ejemplo, nombre y edad).
#Crea una ruta en FastAPI ("/usuario") que dependa de obtener_usuario e imprima la información del usuario en el navegador como respuesta.

from fastapi import Depends, FastAPI

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una función que devuelve un diccionario con información de usuario
def obtener_usuario():
    return {"nombre": "Usuario Ejemplo", "edad": 25}

# Crear una ruta que depende de la función obtener_usuario
@app.get("/usuario")
async def obtener_info_usuario(usuario: dict = Depends(obtener_usuario)):
    # Retornar el diccionario de usuario como respuesta
    return usuario



###### Ejercicio 2: Pruebas con Pytest y FastAPI
#Escribe una prueba utilizando Pytest para verificar que la ruta "/usuario" devuelve el diccionario de usuario correctamente.
#Utiliza TestClient de FastAPI para realizar una solicitud a la ruta y asegurarte de que la respuesta sea la esperada.

import pytest
from fastapi.testclient import TestClient

# Crear un fixture para obtener una instancia de TestClient
@pytest.fixture
def test_client():
    from app.main import app  # Importar la aplicación FastAPI
    return TestClient(app)

# Escribir una prueba para la ruta /usuario
def test_obtener_info_usuario(test_client):
    # Realizar una solicitud GET a la ruta /usuario utilizando TestClient
    response = test_client.get("/usuario")

    # Verificar que la respuesta tiene un código 200 y el contenido esperado
    assert response.status_code == 200
    assert response.json() == {"nombre": "Usuario Ejemplo", "edad": 25}



###### Ejercicio 3: Inyección de Dependencias Asíncronas en FastAPI
#Define una función asincrónica obtener_datos_asincronicos que devuelve algún dato asincrónico (puedes simular una llamada a una base de datos ficticia).
#Crea una ruta asincrónica en FastAPI ("/datos_asincronicos") que dependa de obtener_datos_asincronicos e imprima la información asincrónica como respuesta.

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import asyncio

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una función asincrónica que simula obtener datos asincrónicos (por ejemplo, una consulta a una base de datos)
async def obtener_datos_asincronicos():
    # Simulación de una operación asincrónica (por ejemplo, una consulta a una base de datos)
    await asyncio.sleep(2)
    return {"datos_asincronicos": "Información asincrónica"}

# Crear una ruta asincrónica que depende de la función obtener_datos_asincronicos
@app.get("/datos_asincronicos")
async def obtener_info_asincronica(datos: dict = Depends(obtener_datos_asincronicos)):
    # Retornar los datos asincrónicos como respuesta
    return datos



###### Ejercicio 4: Pruebas Asíncronas con Pytest y FastAPI
#Escribe una prueba asincrónica utilizando Pytest para verificar que la ruta "/datos_asincronicos" devuelve los datos asincrónicos correctamente.
#Utiliza AsyncClient de httpx para realizar una solicitud asincrónica a la ruta y asegúrate de que la respuesta sea la esperada.

import pytest
from httpx import AsyncClient

# Escribir una prueba asincrónica utilizando Pytest
@pytest.mark.asyncio
async def test_obtener_info_asincronica():
    from app.main import app  # Importar la aplicación FastAPI
    
    # Crear un cliente asincrónico para realizar solicitudes HTTP
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Realizar una solicitud GET a la ruta /datos_asincronicos
        response = await client.get("/datos_asincronicos")
        
        # Verificar que la respuesta tiene un código 200 y el contenido esperado
        assert response.status_code == 200
        assert response.json() == {"datos_asincronicos": "Información asincrónica"}
        


###### Ejercicio 5: Inyección de Dependencias con Parámetros en FastAPI
#Define una función llamada obtener_usuario_por_nombre que recibe un parámetro nombre de tipo cadena. La función debe devolver un diccionario con la información del usuario, donde el nombre es el proporcionado y la edad es 25. Crea una ruta en FastAPI ("/usuario_por_nombre") que dependa de esta función y devuelva la información del usuario como respuesta.

from fastapi import Depends, FastAPI, Query

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una función con parámetro para obtener información de usuario
def obtener_usuario_por_nombre(nombre: str = Query(..., title="Nombre del usuario")):
    return {"nombre": nombre, "edad": 25}

# Crear una ruta que depende de la función con parámetro
@app.get("/usuario_por_nombre")
async def obtener_info_usuario_por_nombre(usuario: dict = Depends(obtener_usuario_por_nombre)):
    # Retornar la información de usuario como respuesta
    return usuario

###### Ejercicio 6: Pruebas con Pytest y FastAPI con Parámetros
#Enunciado: Escribe una prueba utilizando Pytest para verificar que la ruta "/usuario_por_nombre" devuelve correctamente la información del usuario cuando se proporciona un nombre específico. Utiliza el cliente de prueba de FastAPI para realizar la solicitud y asegúrate de que la respuesta sea la esperada.

import pytest
from fastapi.testclient import TestClient

# Crear un fixture para obtener una instancia de TestClient
@pytest.fixture
def test_client():
    from app.main import app  # Importar la aplicación FastAPI
    return TestClient(app)

# Escribir una prueba para la ruta /usuario_por_nombre
def test_obtener_info_usuario_por_nombre(test_client):
    # Realizar una solicitud GET a la ruta /usuario_por_nombre con parámetros
    response = test_client.get("/usuario_por_nombre?nombre=John")

    # Verificar que la respuesta tiene un código 200 y el contenido esperado
    assert response.status_code == 200
    assert response.json() == {"nombre": "John", "edad": 25}

###### Ejercicio 7: Inyección de Dependencias Asíncronas con Pydantic en FastAPI
#Enunciado: Define una clase llamada DatosUsuario que herede de BaseModel de Pydantic y tenga dos campos: nombre de tipo cadena y edad de tipo entero. Crea una función asincrónica llamada obtener_datos_asincronicos que reciba un parámetro de tipo DatosUsuario. La función debe simular una operación asincrónica (por ejemplo, una consulta a una base de datos ficticia) y devolver un diccionario con información asincrónica. Crea una ruta asincrónica en FastAPI ("/datos_asincronicos") que dependa de esta función y devuelva los datos asincrónicos como respuesta.

from fastapi import Depends, FastAPI
from pydantic import BaseModel
import asyncio

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir un modelo Pydantic para datos de usuario
class DatosUsuario(BaseModel):
    nombre: str
    edad: int

# Definir una función asincrónica que simula obtener datos asincrónicos
async def obtener_datos_asincronicos(usuario: DatosUsuario):
    # Simulación de una operación asincrónica
    await asyncio.sleep(2)
    return {"datos_asincronicos": f"Información de {usuario.nombre}"}

# Crear una ruta asincrónica que depende de la función asincrónica
@app.post("/datos_asincronicos")
async def obtener_info_asincronica(datos: dict = Depends(obtener_datos_asincronicos)):
    # Retornar los datos asincrónicos como respuesta
    return datos

###### Ejercicio 8: Pruebas Asíncronas con Pytest y FastAPI con Pydantic
#Enunciado: Escribe una prueba asincrónica utilizando Pytest para verificar que la ruta "/datos_asincronicos" devuelve correctamente los datos asincrónicos cuando se envían datos de usuario válidos. Utiliza el cliente asincrónico de httpx para realizar la solicitud y asegúrate de que la respuesta sea la esperada.

import pytest
from httpx import AsyncClient

# Escribir una prueba asincrónica utilizando Pytest
@pytest.mark.asyncio
async def test_obtener_info_asincronica(test_client):
    from app.main import app  # Importar la aplicación FastAPI
    
    # Crear datos de usuario para la prueba
    data = {"nombre": "Alice", "edad": 30}
    
    # Realizar una solicitud POST a la ruta /datos_asincronicos con datos de usuario
    response = await test_client.post("/datos_asincronicos", json=data)
    
    # Verificar que la respuesta tiene un código 200 y el contenido esperado
    assert response.status_code == 200
    assert response.json() == {"datos_asincronicos": "Información de Alice"}

###### Ejercicio 9: Uso de Dependencias Personalizadas en FastAPI
#Enunciado: Define una función llamada obtener_token que utiliza OAuth2PasswordBearer como una dependencia personalizada. La función debe recibir un token como parámetro y devolver el token si es igual a "token-secreto". Si el token no es válido, la función debe lanzar una excepción HTTP con un código 401 y un detalle indicando "Token no válido". Crea una ruta en FastAPI ("/recurso_protegido") que dependa de esta función y devuelva un mensaje de "Acceso permitido" si el token es válido.

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Crear un esquema de seguridad OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Definir una función para obtener y validar el token
def obtener_token(token: str = Depends(oauth2_scheme)):
    if token != "token-secreto":
        # Lanzar una excepción HTTP si el token no es válido
        raise HTTPException(status_code=401, detail="Token no válido")
    return token

# Crear una ruta protegida que depende de la función para obtener el token
@app.get("/recurso_protegido")
async def recurso_protegido(token: str = Depends(obtener_token)):
    # Retornar un mensaje de acceso permitido si el token es válido
    return {"mensaje": "Acceso permitido"}


###### Ejercicio 10: Pruebas con Pytest y FastAPI con Dependencias Personalizadas
#Enunciado: Escribe dos pruebas utilizando Pytest para verificar el comportamiento de la ruta "/recurso_protegido". Una prueba debe asegurarse de que el recurso sea accesible correctamente cuando se proporciona un token válido en los encabezados de autorización. La otra prueba debe verificar que se recibe un código de estado 401 y un detalle adecuado cuando se intenta acceder al recurso sin un token válido.

import pytest
from fastapi.testclient import TestClient

# Crear un fixture para obtener una instancia de TestClient
@pytest.fixture
def test_client():
    from app.main import app  # Importar la aplicación FastAPI
    return TestClient(app)

# Escribir una prueba para el acceso permitido con un token válido
def test_recurso_protegido_con_token_valido(test_client):
    # Realizar una solicitud GET a la ruta protegida con un token válido en los encabezados
    response = test_client.get("/recurso_protegido", headers={"Authorization": "Bearer token-secreto"})
    
    # Verificar que la respuesta tiene un código 200 y el contenido esperado
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Acceso permitido"}

# Escribir una prueba para el acceso denegado sin un token válido
def test_recurso_protegido_sin_token(test_client):
    # Realizar una solicitud GET a la ruta protegida sin un token válido
    response = test_client.get("/recurso_protegido")
    
    # Verificar que la respuesta tiene un código 401 y el detalle esperado
    assert response.status_code == 401
    assert response.json() == {"detail": "Token no válido"}
