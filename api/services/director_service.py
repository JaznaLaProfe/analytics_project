from datetime import datetime

from api.database import db
from api.models.director import Director

from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

from api.utils.serializer import serializar_lista, serializar_documento

def listar_directores():
    return serializar_lista(db.directores.find())

def obtener_director_por_id(id: int):
    return serializar_documento(db.directores.find_one({"idDirector": id}))

def agregar_director(director: Director):
    """ 
        Agrega un nuevo director 
        params:
            director: datos a a agregar        
    """
    documento = {
        "idDirector": director.id,
        "nombre": director.nombre,
        "apellido": director.apellido,
        "pais": director.pais,
        # Transformar la fecha de nacimiento a un formato compatible con MongoDB
        "fechaNacimiento": datetime.strptime(director.fechaNacimiento, "%Y-%m-%d")
    }

    try:
        db.directores.insert_one(documento)

        return {
            "mensaje": "Director agregado correctamente"
        }

    except DuplicateKeyError:
        return None

def actualizar_director(id: int, director: Director):
    documento = {
        "nombre": director.nombre,
        "apellido": director.apellido,
        "pais": director.pais,
        "fechaNacimiento": datetime.strptime(director.fechaNacimiento, "%Y-%m-%d")
    }

    resultado = db.directores.update_one(
        {"idDirector": id},
        {"$set": documento}
    )

    return resultado    