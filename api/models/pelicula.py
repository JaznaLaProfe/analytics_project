from pydantic import BaseModel

class Pelicula(BaseModel):
    id: int
    titulo: str
    anioEstreno: int
    duracion: int
    genero: str
    idDirector: int