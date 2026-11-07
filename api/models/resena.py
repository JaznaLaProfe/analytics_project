from pydantic import BaseModel

class Resena(BaseModel):
    idPelicula: int
    usuario: str
    calificacion: int
    comentario: str
    fechaResena: str
