# Cine inteligente: API + dashboard

Aplicación de referencia para analizar una plataforma de cine inteligente. La arquitectura separa totalmente la visualización del acceso a datos:

```text
MongoDB Atlas <--> FastAPI (agregaciones y reglas de negocio) <--> Streamlit
```

Streamlit no tiene dependencia de `pymongo`, URI ni credenciales de Atlas: solo consulta la API HTTP. De esta forma se puede reemplazar Streamlit por otra herramienta de BI sin modificar la capa de datos.

## Objetivo

Mostrar a los estudiantes cómo diseñar APIs orientadas a analítica, no solo a operaciones CRUD

## Colecciones

- `directores`: datos de directores.
- `peliculas`: datos de peliculas.
- `resenas`: datos de las reseñas de las películas de parte de los usuarios.

## Estructura del proyecto
```
proyecto/
│
├── .env                 variables de entorno
├── .env_bdy0101/        entorno virtual (ignorado por Git)
├── api/
│
├── models/
│   ├── director.py
│   ├── resena.py
│   └── pelicula.py
│
├── routes/
│   ├── dashboard.py
│   ├── directores.py
│   └── peliculas.py
│
└── services/
    ├── dashboard_service.py
    ├── director_service.py
    └── pelicula_service.py 
├── dashboard/
│   └── app.py
└── utils/
    └── serializer.py
```
## Inicio rápido

Se requiere Python 3.10 o superior.

1. Cree el entorno e instale dependencias:

   ```bash
   python -m venv .env_bdy0101
   source .env_bdy0101/bin/activate
   pip install -r requirements.txt
   ```

2. Copie `.env.example` a `.env` y complete `MONGO_URI`. No suba ese archivo al repositorio.

3. Ejecute la API:

   ```bash
   uvicorn api.app:app --reload --reload-dir api
   ```

4. En otra terminal, ejecute el dashboard:

   ```bash
   streamlit run dashboard/app.py
   ```

La documentación interactiva queda disponible en `http://localhost:8000/docs`.

## endpoints CRUD expuestos

- 

```bash
GET    /peliculas
GET    /peliculas/{id}
POST   /peliculas
PUT    /peliculas/{id}
DELETE /peliculas/{id}
```

## endpoints analíticos expuestos

- 

```bash
GET /dashboard/kpis
GET /dashboard/top-peliculas
GET /dashboard/top-directores
GET /dashboard/distribucion-calificaciones
GET /dashboard/evolucion-resenas
GET /dashboard/resenas-por-genero
GET /dashboard/promedio-genero
```
