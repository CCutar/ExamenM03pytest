import pytest
import requests
from main import obtenir_apis

from respositori_apis import RepositoriAPIs


@pytest.mark.asyncio
async def test_obtenir_apis():
    # Crear el repositori
    repositori = RepositoriAPIs()
    # Obtenir les apis
    apis = await obtenir_apis(repositori=repositori)
    # Validar els resultats
    assert len(apis) == 2

def test_api_status_code():
    url = "https://api.publicapis.org/entries"
    resposta = requests.get(url)
    assert resposta.status_code == 200

   

