from fastapi import APIRouter, HTTPException
from api.services.director_service import listar_directores, obtener_director_por_id, agregar_director, actualizar_director
from api.models.director import Director

router = APIRouter(
    prefix="/directores",
    tags=["Directores"]
)

@router.get("/")
def obtener_directores():
    return listar_directores()

@router.get("/{id}")
def obtener_director(id: int):
    director = obtener_director_por_id(id)
    if director is None:
        raise HTTPException(
            status_code=404,
            detail="Director no encontrado"
        )

    return director

@router.post("/")
def crear_director(director: Director):
    director = agregar_director(director)
    if director is None:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un director con ese ID."
        )
    return director

@router.put("/{id}")
def modificar_director(id: int, director: Director):
    resultado = actualizar_director(id, director)

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Director no encontrado"
        )

    return {
        "mensaje": "Director actualizado correctamente",
        "documentos_encontrados": resultado.matched_count,
        "documentos_modificados": resultado.modified_count
    }  