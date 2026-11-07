from api.database import db
from api.models.pelicula import Pelicula

from pymongo.errors import DuplicateKeyError

from api.utils.serializer import serializar_lista, serializar_documento

def listar_peliculas():
    """
    Obtiene los documentos
    """
    return serializar_lista(db.peliculas.find())

def filtrar_peliculas(titulo: str):
    peliculas = list(db.peliculas.find({                
                    "titulo": {
                        "$regex": titulo,
                        "$options": "i"
                    }
            }))
    return serializar_lista(peliculas)

def filtrar_por_director(id_director: int):
    return serializar_lista(db.peliculas.find({"idDirector": id_director}))

def filtrar_por_anio(anio: int):
    return serializar_lista(db.peliculas.find({"anioEstreno":{"$gte" : anio} }))

def agregar_pelicula(pelicula: Pelicula) -> dict:
    """ 
        Agrega una nueva pelicula
        params:
            pelicula: datos a a agregar        
    """
    documento = {
        "idPelicula": pelicula.id,
        "titulo": pelicula.titulo,
        "anioEstreno": pelicula.anioEstreno,
        "genero": pelicula.genero,
        "idDirector": pelicula.idDirector,
        "duracion": pelicula.duracion
    }
    
    db.peliculas.insert_one(documento)

    return {
        "mensaje": "Película agregada correctamente"
    }
