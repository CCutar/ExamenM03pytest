from fastapi import Depends, FastAPI
import uvicorn

from api import API
from respositori_apis import RepositoriAPIs


app = FastAPI()

@app.get("/cristian", response_model=list[API])
async def obtenir_apis(repositori: RepositoriAPIs = Depends()):
    return await repositori.obtenir_apis()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8887)

