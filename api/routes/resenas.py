from fastapi import APIRouter, HTTPException
from api.services.resena_service import listar_resenas, listar_resenas_por_pelicula, agregar_resena, listar_resenas_por_fecha
from api.models.resena import Resena

router = APIRouter(
    prefix="/resenas",
    tags=["Reseñas"]
)

@router.get("/")
def obtener_resenas():
    return listar_resenas()

@router.get("/{pelicula_id}")
def filtro_por_titulo(pelicula_id: int):
    resultado = listar_resenas_por_pelicula(pelicula_id)
    if not resultado :
        raise HTTPException(
            status_code=404,
            detail="Sin resultados"
        )

    return resultado

@router.get("/fecha/{fecha_inicio}/{fecha_fin}")
def filtrar_resenas_por_fecha(fecha_inicio: str, fecha_fin: str):
    resultado = listar_resenas_por_fecha(fecha_inicio, fecha_fin)
    if not resultado:
        raise HTTPException(
            status_code=404,
            detail=f"Sin resultados para el rango de fechas {fecha_inicio} - {fecha_fin}"
        )

    return resultado

@router.post("/")
def crear_resena(r: Resena):
    return agregar_resena(r)

