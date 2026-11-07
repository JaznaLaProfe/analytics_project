from fastapi import APIRouter, Query
from api.services.dashboard_service import DashboardService


router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/kpis")
def get_kpis():
    """Retorna los indicadores clave de rendimiento (KPIs) del sistema."""
    return DashboardService.get_kpis()

@router.get("/top-peliculas")
def get_top_peliculas(limit: int = Query(5, ge=1, le=50)):
    """Retorna las películas mejor valoradas."""
    return DashboardService.get_top_peliculas(limit)

@router.get("/top-directores")
def get_top_directores(limit: int = Query(5, ge=1, le=50)):
    """Retorna los directores con mejor promedio en sus películas."""
    return DashboardService.get_top_directores(limit)

@router.get("/distribucion-calificaciones")
def get_distribucion_calificaciones():
    """Retorna el desglose de cuántas reseñas se han emitido por nivel de calificación (1-5)."""
    return DashboardService.get_distribucion_calificaciones()

@router.get("/evolucion-resenas")
def get_evolucion_resenas():
    """Retorna el volumen de reseñas acumulado en el tiempo por mes/año."""
    return DashboardService.get_evolucion_resenas()

@router.get("/resenas-por-genero")
def get_resenas_por_genero():
    """Retorna el número de reseñas acumuladas agrupadas por género cinematográfico."""
    return DashboardService.get_resenas_por_genero()

@router.get("/promedio-genero")
def get_promedio_genero():
    """Retorna la calificación promedio recibida por cada género de película."""
    return DashboardService.get_promedio_genero()