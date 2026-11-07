import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Configuración básica de la página
st.set_page_config(
    page_title="Analytics Dashboard | 2026 Cine",
    page_icon="🎬",
    layout="wide"
)

# URL base del controlador de Dashboard en FastAPI
API_BASE_URL = "http://127.0.0.1:8000/dashboard"

@st.cache_data(ttl=30)
def fetch_dashboard_data(endpoint: str, params: dict = None):
    """
    Función auxiliar para realizar peticiones GET a los endpoints del dashboard.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/{endpoint}", params=params)
        if response.status_code == 200:
            return response.json()
        st.error(f"Error {response.status_code} al consultar /{endpoint}: {response.text}")
    except Exception as e:
        st.error(f"Error de conexión con la API FastAPI: {e}")
    return None

# Título Principal del Dashboard
st.title("🎬 Dashboard Cine")
st.caption("Visualizaciones de indicadores clave y métricas agregadas de cine y reseñas en tiempo real.")

# Botón de refresco manual
if st.button("🔄 Actualizar Datos"):
    st.cache_data.clear()

st.divider()

# ==========================================
# SECCIÓN 1: KPIs GLOBALES
# ==========================================
kpis = fetch_dashboard_data("kpis")

if kpis:
    st.subheader("📌 Indicadores Clave (KPIs)")
    c1, c2, c3, c4 = st.columns(4)
    
    c1.metric(label="Total Directores", value=f"{kpis.get('total_directores', 0):,}")
    c2.metric(label="Total Películas", value=f"{kpis.get('total_peliculas', 0):,}")
    c3.metric(label="Total Reseñas", value=f"{kpis.get('total_resenas', 0):,}")
    c4.metric(
        label="Calificación Promedio General", 
        value=f"⭐ {kpis.get('promedio_calificacion_general', 0.0):.2f} / 5.0"
    )

st.divider()

# ==========================================
# SECCIÓN 2: TOPS (PELÍCULAS Y DIRECTORES)
# ==========================================
st.subheader("🏆 Rankings de Desempeño")

# Filtro de cantidad para el Top
top_limit = st.slider("Seleccione el tamaño del ranking (Top N):", min_value=3, max_value=20, value=5, step=1)

col_top_pelis, col_top_dir = st.columns(2)

# GET /dashboard/top-peliculas
with col_top_pelis:
    st.markdown("##### 🥇 Películas Mejor Valoradas")
    top_pelis_data = fetch_dashboard_data("top-peliculas", params={"limit": top_limit})
    
    if top_pelis_data:
        df_top_pelis = pd.DataFrame(top_pelis_data)
        
        fig_top_pelis = px.bar(
            df_top_pelis,
            x="promedioCalificacion",
            y="titulo",
            orientation="h",
            text="promedioCalificacion",
            color="promedioCalificacion",
            hover_data=["genero", "anioEstreno", "totalResenas"],
            labels={
                "promedioCalificacion": "Promedio",
                "titulo": "Película",
                "totalResenas": "Total Reseñas"
            },
            color_continuous_scale="Blues"
        )
        # Setear el formato del ejes
        fig_top_pelis.update_layout(
            xaxis_title_font=dict(weight="bold", size=14),
            yaxis_title_font=dict(weight="bold", size=14)   
        )
        fig_top_pelis.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
        st.plotly_chart(fig_top_pelis, use_container_width=True)

# GET /dashboard/top-directores
with col_top_dir:
    st.markdown("##### 🎬 Directores Mejor Evaluados")
    top_dir_data = fetch_dashboard_data("top-directores", params={"limit": top_limit})
    
    if top_dir_data:
        df_top_dir = pd.DataFrame(top_dir_data)
        
        fig_top_dir = px.bar(
            df_top_dir,
            x="promedioCalificacion",
            y="nombreCompleto",
            orientation="h",
            text="promedioCalificacion",
            color="promedioCalificacion",
            hover_data=["pais", "totalResenas"],
            labels={
                "promedioCalificacion": "Promedio",
                "nombreCompleto": "Director",
                "pais": "País"
            },
            color_continuous_scale="Viridis"
        )
        fig_top_dir.update_layout(
            xaxis_title_font=dict(weight="bold", size=14),
            yaxis_title_font=dict(weight="bold", size=14)   
        )

        fig_top_dir.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
        st.plotly_chart(fig_top_dir, use_container_width=True)

st.divider()

# ==========================================
# SECCIÓN 3: COMPORTAMIENTO Y DISTRIBUCIÓN DE RESEÑAS
# ==========================================
col_dist, col_evol = st.columns(2)

# GET /dashboard/distribucion-calificaciones
with col_dist:
    st.subheader("⭐ Distribución de Calificaciones")
    st.caption("Frecuencia de evaluaciones recibidas de 1 a 5 estrellas.")
    dist_data = fetch_dashboard_data("distribucion-calificaciones")
    
    if dist_data:
        df_dist = pd.DataFrame(dist_data)
        
        fig_dist = px.pie(
            df_dist,
            names="calificacion",
            values="cantidad",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_dist.update_traces(textinfo="percent+value")
        st.plotly_chart(fig_dist, use_container_width=True)

# GET /dashboard/evolucion-resenas
with col_evol:
    st.subheader("📈 Evolución Temporal de Reseñas")
    st.caption("Volumen de interacción y opiniones registradas mes a mes.")
    evol_data = fetch_dashboard_data("evolucion-resenas")
    
    if evol_data:
        df_evol = pd.DataFrame(evol_data)
        
        fig_evol = px.line(
            df_evol,
            x="periodo",
            y="totalResenas",
            markers=True,
            labels={"periodo": "Año-Mes", "totalResenas": "Cantidad de Reseñas"}
        )
        # Setear el formato del ejes
        fig_evol.update_layout(
            xaxis_title_font=dict(weight="bold", size=14),
            yaxis_title_font=dict(weight="bold", size=14)   
        )

        fig_evol.update_traces(line_color="#E50914", line_width=3)
        st.plotly_chart(fig_evol, use_container_width=True)

st.divider()

# ==========================================
# SECCIÓN 4: ANÁLISIS POR GÉNERO CINEMATOGRÁFICO
# ==========================================
st.subheader("🎭 Análisis Comparativo por Género")

col_gen_cant, col_gen_prom = st.columns(2)

# GET /dashboard/resenas-por-genero
with col_gen_cant:
    st.markdown("##### 🍿 Volumen de Reseñas por Género")
    resenas_gen_data = fetch_dashboard_data("resenas-por-genero")
    
    if resenas_gen_data:
        df_resenas_gen = pd.DataFrame(resenas_gen_data)
        
        fig_gen_cant = px.bar(
            df_resenas_gen,
            x="genero",
            y="totalResenas",
            text="totalResenas",
            labels={"genero": "Género", "totalResenas": "Total Reseñas"},
            color="genero",
            
        )
        fig_gen_cant.update_layout(
            xaxis_title_font=dict(weight="bold", size=14),
            yaxis_title_font=dict(weight="bold", size=14)   
        )
        st.plotly_chart(fig_gen_cant, use_container_width=True)

# GET /dashboard/promedio-genero
with col_gen_prom:
    st.markdown("##### 📊 Calificación Promedio por Género")
    prom_gen_data = fetch_dashboard_data("promedio-genero")
    
    if prom_gen_data:
        df_prom_gen = pd.DataFrame(prom_gen_data)
        
        fig_gen_prom = px.bar(
            df_prom_gen,
            x="genero",
            y="promedioCalificacion",
            text="promedioCalificacion",
            hover_data=["cantidadPeliculas"],
            labels={
                "genero": "Género", 
                "promedioCalificacion": "Promedio",
                "cantidadPeliculas": "N° de Películas"
            },
            color="promedioCalificacion",
            color_continuous_scale="Magma"
        )
        # Setear el formato del ejes
        fig_gen_prom.update_layout(
            xaxis_title_font=dict(weight="bold", size=14),
            yaxis_title_font=dict(weight="bold", size=14)   
        )
        st.plotly_chart(fig_gen_prom, use_container_width=True)