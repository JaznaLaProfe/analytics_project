from datetime import datetime
from api.database import db
from api.models.resena import Resena

from api.utils.serializer import serializar_lista

def listar_resenas():
    return serializar_lista(db.resenas.find())

def listar_resenas_por_pelicula(idPelicula: int):
    return serializar_lista(list(db.resenas.find({"idPelicula": idPelicula})))

def agregar_resena(resena: Resena):
    documento = {
        "idPelicula": resena.idPelicula,
        "usuario": resena.usuario,
        "calificacion": resena.calificacion,
        "comentario": resena.comentario,
        "fechaResena": datetime.strptime(resena.fechaResena, "%Y-%m-%d")
    }
    
    resultado = db.resenas.insert_one(documento)
    return {
        "mensaje": "Reseña agregada correctamente",
        "_id": str(resultado.inserted_id)
    }

# Filtrar reseñas por rango de fechas
def listar_resenas_por_fecha(fecha_inicio: str, fecha_fin: str):
    fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")

    resultado = db.resenas.find({
        "fechaResena": {
            "$gte": fecha_inicio_dt,
            "$lte": fecha_fin_dt
        }
    })

    return serializar_lista(resultado)


