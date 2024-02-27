from httpx import AsyncClient
from api import API

class RepositoriAPIs:
    async def obtenir_apis(self) -> list[API]:
        async with AsyncClient() as client:
            resposta = await client.get("https://api.publicapis.org/entries")
            dades = resposta.json()                
            return [API(API=api["API"], Descripcion=api["Description"]) for api in dades["entries"]]
