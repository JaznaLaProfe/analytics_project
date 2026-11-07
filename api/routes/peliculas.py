from fastapi import APIRouter, HTTPException
from api.services.pelicula_service import listar_peliculas, filtrar_peliculas, agregar_pelicula, filtrar_por_director, filtrar_por_anio
from api.models.pelicula import Pelicula

router = APIRouter(
    prefix="/peliculas",
    tags=["Películas"]
)

@router.get("/")
def obtener_peliculas():
    return listar_peliculas()

@router.get("/{titulo}")
def filtro_por_titulo(titulo: str):
    resultado = filtrar_peliculas(titulo)
    if not resultado :
        raise HTTPException(
            status_code=404,
            detail="Sin resultados"
        )

    return resultado

@router.get("/director/{id_director}")
def filtro_por_director(id_director: int):
    resultado = filtrar_por_director(id_director)
    if not resultado:
        raise HTTPException(
            status_code=404,
            detail=f"Sin resultados para director {id_director}"
        )

    return resultado

@router.get("/year/{year}")
def filtro_por_anio(year: int):
    resultado = filtrar_por_anio(year)
    if not resultado:
        raise HTTPException(
            status_code=404,
            detail=f"No hay peliculas superiores al año {year}"
        )

    return resultado

@router.post("/")
def crear_pelicula(p: Pelicula):
    return agregar_pelicula(p)

