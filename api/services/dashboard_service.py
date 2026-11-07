from api.database import db

class DashboardService:

    @staticmethod
    def get_kpis():
        """
        Retorna las métricas macro principales:
        - Total de directores
        - Total de películas
        - Total de reseñas
        - Promedio general de calificación de reseñas
        """
        # Obtiene totales de cada colección
        total_directores = db.directores.count_documents({})
        total_peliculas = db.peliculas.count_documents({})
        total_resenas = db.resenas.count_documents({})

        # Obtiene promedios
        pipeline_promedio = [
            {
                "$group": {
                    "_id": None,
                    "promedio_general": {"$avg": "$calificacion"}
                }
            }
        ]
        res_promedio = list(db.resenas.aggregate(pipeline_promedio))
        promedio_general = res_promedio[0]["promedio_general"] if res_promedio else 0.0

        return {
            "total_directores": total_directores,
            "total_peliculas": total_peliculas,
            "total_resenas": total_resenas,
            "promedio_calificacion_general": round(promedio_general, 2)
        }

    @staticmethod
    def get_top_peliculas(limit: int = 5):
        """
        Retorna el Top N de películas con mejor promedio de calificación en reseñas.
        Realiza un $lookup de resenas -> peliculas.
        """
        
        pipeline = [
            {
                "$group": {
                    "_id": "$idPelicula",
                    "promedio_calificacion": {"$avg": "$calificacion"},
                    "total_resenas": {"$sum": 1}
                }
            },
            {
                "$lookup": {
                    "from": "peliculas",
                    "localField": "_id",
                    "foreignField": "idPelicula",
                    "as": "pelicula_info"
                }
            },
            {"$unwind": "$pelicula_info"},
            {
                "$project": {
                    "_id": 0,
                    "idPelicula": "$_id",
                    "titulo": "$pelicula_info.titulo",
                    "genero": "$pelicula_info.genero",
                    "anioEstreno": "$pelicula_info.anioEstreno",
                    "promedioCalificacion": {"$round": ["$promedio_calificacion", 2]},
                    "totalResenas": "$total_resenas"
                }
            },
            {"$sort": {"promedioCalificacion": -1, "totalResenas": -1}},
            {"$limit": limit}
        ]
        return list(db.resenas.aggregate(pipeline))

    @staticmethod
    def get_top_directores(limit: int = 5):
        """
        Retorna los directores con mejor promedio de calificación en sus películas.
        Cruza resenas -> peliculas -> directores.
        """
        
        pipeline = [
            {
                "$lookup": {
                    "from": "peliculas",
                    "localField": "idPelicula",
                    "foreignField": "idPelicula",
                    "as": "pelicula"
                }
            },
            {"$unwind": "$pelicula"},
            {
                "$group": {
                    "_id": "$pelicula.idDirector",
                    "promedioCalificacion": {"$avg": "$calificacion"},
                    "totalResenas": {"$sum": 1}
                }
            },
            {
                "$lookup": {
                    "from": "directores",
                    "localField": "_id",
                    "foreignField": "idDirector",
                    "as": "director"
                }
            },
            {"$unwind": "$director"},
            {
                "$project": {
                    "_id": 0,
                    "idDirector": "$_id",
                    "nombreCompleto": {"$concat": ["$director.nombre", " ", "$director.apellido"]},
                    "pais": "$director.pais",
                    "promedioCalificacion": {"$round": ["$promedioCalificacion", 2]},
                    "totalResenas": "$totalResenas"
                }
            },
            {"$sort": {"promedioCalificacion": -1}},
            {"$limit": limit}
        ]
        return list(db.resenas.aggregate(pipeline))

    @staticmethod
    def get_distribucion_calificaciones():
        """
        Retorna el conteo de reseñas recibidas por cada estrella/calificación (del 1 al 5).
        """
        
        pipeline = [
            {
                "$group": {
                    "_id": "$calificacion",
                    "cantidad": {"$sum": 1}
                }
            },
            {"$sort": {"_id": 1}},
            {
                "$project": {
                    "_id": 0,
                    "calificacion": "$_id",
                    "cantidad": 1
                }
            }
        ]
        return list(db.resenas.aggregate(pipeline))

    @staticmethod
    def get_evolucion_resenas():
        """
        Agrupa y cuenta las reseñas emitidas por mes/año según `fechaResena`.
        """
        
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "anio": {"$year": "$fechaResena"},
                        "mes": {"$month": "$fechaResena"}
                    },
                    "totalResenas": {"$sum": 1}
                }
            },
            {"$sort": {"_id.anio": 1, "_id.mes": 1}},
            {
                "$project": {
                    "_id": 0,
                    "periodo": {
                        "$concat": [
                            {"$toString": "$_id.anio"},
                            "-",
                            {"$cond": [
                                {"$lt": ["$_id.mes", 10]},
                                {"$concat": ["0", {"$toString": "$_id.mes"}]},
                                {"$toString": "$_id.mes"}
                            ]}
                        ]
                    },
                    "totalResenas": 1
                }
            }
        ]
        return list(db.resenas.aggregate(pipeline))

    @staticmethod
    def get_resenas_por_genero():
        """
        Cuenta el total de reseñas por cada género cinematográfico.
        """
        
        pipeline = [
            {
                "$lookup": {
                    "from": "peliculas",
                    "localField": "idPelicula",
                    "foreignField": "idPelicula",
                    "as": "pelicula"
                }
            },
            {"$unwind": "$pelicula"},
            {
                "$group": {
                    "_id": "$pelicula.genero",
                    "totalResenas": {"$sum": 1}
                }
            },
            {"$sort": {"totalResenas": -1}},
            {
                "$project": {
                    "_id": 0,
                    "genero": "$_id",
                    "totalResenas": 1
                }
            }
        ]
        return list(db.resenas.aggregate(pipeline))

    @staticmethod
    def get_promedio_genero():
        """
        Retorna el promedio de calificación obtenida por cada género de películas.
        """
        
        pipeline = [
            {
                "$lookup": {
                    "from": "peliculas",
                    "localField": "idPelicula",
                    "foreignField": "idPelicula",
                    "as": "pelicula"
                }
            },
            {"$unwind": "$pelicula"},
            {
                "$group": {
                    "_id": "$pelicula.genero",
                    "promedioCalificacion": {"$avg": "$calificacion"},
                    "totalPeliculas": {"$addToSet": "$idPelicula"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "genero": "$_id",
                    "promedioCalificacion": {"$round": ["$promedioCalificacion", 2]},
                    "cantidadPeliculas": {"$size": "$totalPeliculas"}
                }
            },
            {"$sort": {"promedioCalificacion": -1}}
        ]
        return list(db.resenas.aggregate(pipeline))