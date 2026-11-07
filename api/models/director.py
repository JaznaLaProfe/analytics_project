from pydantic import BaseModel

class Director(BaseModel):
    id: int
    pais: str
    nombre: str
    apellido: str
    fechaNacimiento: str