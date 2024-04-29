import json
from contextlib import asynccontextmanager
from fastapi import FastAPI
from workout_api.routers import api_router
from fastapi_pagination import Page, add_pagination, paginate

@asynccontextmanager
async def lifespan(app: FastAPI):
    openapi_data = app.openapi()
    # Change "openapi.json" to desired filename
    with open("openapi.json", "w") as file:
        json.dump(openapi_data, file)
        yield

#usar a função lifespan apenas para gerar a documentação ao abrir/fechar a aplicação
#app = FastAPI(title='WorkoutApi', lifespan=lifespan)
app = FastAPI(title='WorkoutApi')
app.include_router(api_router)
add_pagination(app)

if __name__ == "main":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port="8000", log_level="info", reload=True)


