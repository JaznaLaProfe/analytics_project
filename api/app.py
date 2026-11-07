from fastapi import FastAPI

from api.routes import (
    directores,
    peliculas, resenas, dashboard 
)
tags_metadata = [
    {
        "name": "General",
        "description": "Operaciones generales de la API"
    },
    {
        "name": "Directores",
        "description": "CRUD de directores"
    },
    {
        "name": "Películas",
        "description": "CRUD de películas"
    },
    {
        "name": "Reseñas",
        "description": "CRUD de reseñas"
    },
    {
        "name": "Estadísticas",
        "description": "Obtención de estadísticas de la base de datos"
    }
]

app = FastAPI(
    title="API cine - 2026",
    version="1.0",
    openapi_tags=tags_metadata
)

app.include_router(directores.router)
app.include_router(peliculas.router)
#app.include_router(estadisticas.router)
app.include_router(resenas.router)
app.include_router(dashboard.router)

@app.get("/", tags=["General"])
def inicio():
    return {"mensaje": "API Cine funcionando correctamente"}



