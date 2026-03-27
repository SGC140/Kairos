import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import textwrap

PATH = "Insight Kairós.csv"

st.set_page_config(page_title="Dashboard Kairós", layout="wide")

st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    border: 1px solid #334155;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.3);
    margin-bottom: 1rem;
}
.kpi-title {color:#94a3b8; font-size:15px; text-transform: uppercase; font-weight: 700; letter-spacing: 1px;}
.kpi-value {color:#f8fafc; font-size:38px; font-weight:900; margin: 8px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);}
.kpi-percent {color:#eab308; font-size:14px; font-weight: 500;}

[data-testid="stVerticalBlockBorderWrapper"] {
    box-shadow: 0 8px 12px -3px rgba(0, 0, 0, 0.4);
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    df = pd.read_csv(PATH)
    
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
        
    df["Fecha_dt"] = pd.to_datetime(df["Fecha"])
    df["Fecha"] = df["Fecha_dt"].dt.date
    df["Año"] = df["Fecha_dt"].dt.year
    
    meses_esp = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 
                 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    df["Mes_Esp"] = df["Fecha_dt"].dt.month.map(meses_esp)
    
    if "Hora Post" in df.columns:
        df["Hora"] = pd.to_datetime(df["Hora Post"], format='%H:%M:%S', errors='coerce').dt.hour

    df["Desc_Hover"] = df["Descripción"].astype(str).apply(
        lambda x: "<br>".join(textwrap.wrap(x, width=60))
    )
    df["Desc_Eje"] = df["Descripción"].astype(str).apply(
        lambda x: x[:45] + "..." if len(x) > 45 else x
    )
    df["Días activo"] = (pd.Timestamp.today() - df["Fecha_dt"]).dt.days
    
    return df

df = load()
base_df = df.copy()

# ==============================
# BARRA LATERAL (FILTROS)
# ==============================
st.sidebar.header("Filtros")

año_disp = df["Año"].dropna().unique()
año = st.sidebar.multiselect("Año", año_disp, placeholder="Selecciona el año...")
if año:
    df = df[df["Año"].isin(año)]

min_date = df["Fecha"].min()
max_date = df["Fecha"].max()
fechas = st.sidebar.date_input("Rango de Fechas", [min_date, max_date], min_value=min_date, max_value=max_date)

if len(fechas) == 2:
    df = df[(df["Fecha"] >= fechas[0]) & (df["Fecha"] <= fechas[1])]

meses_disponibles = df["Mes_Esp"].unique()
mes = st.sidebar.multiselect("Mes", meses_disponibles, placeholder="Selecciona el mes...")
if mes:
    df = df[df["Mes_Esp"].isin(mes)]

if "Tipo de publicación" in df.columns:
    tipos_disp = df["Tipo de publicación"].dropna().unique()
    tipo = st.sidebar.multiselect("Tipo de publicación", tipos_disp, placeholder="Selecciona tipo...")
    if tipo:
        df = df[df["Tipo de publicación"].isin(tipo)]

desc_disp = df["Descripción"].dropna().unique()
desc = st.sidebar.multiselect("Descripción de post", desc_disp, placeholder="Selecciona publicaciones...")
if desc:
    df = df[df["Descripción"].isin(desc)]

# ==============================
# CUERPO DEL DASHBOARD
# ==============================
st.title("📊 Dashboard - Métricas de Instagram: Semillero Kairós")

# 1. KPIs Generales
with st.container(border=True):
    st.markdown("### Rendimiento General")
    c1, c2, c3, c4 = st.columns(4)

    def kpi(col, name, field):
        val = df[field].sum()
        total = base_df[field].sum()
        percent = (val / total * 100) if total != 0 else 0

        col.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">{name}</div>
            <div class="kpi-value">{int(val):,}</div>
            <div class="kpi-percent">{percent:.1f}% del histórico global</div>
        </div>
        """, unsafe_allow_html=True)

    kpi(c1, "Visualizaciones", "Visualizaciones")
    kpi(c2, "Alcance", "Alcance")
    kpi(c3, "Likes", "Me gusta")
    kpi(c4, "Comentarios", "Comentarios")

# 2. Evolución de Métricas
with st.container(border=True):
    st.markdown("### Evolución de métricas a lo largo del tiempo")
    df_time = df.groupby("Fecha")[["Visualizaciones", "Alcance", "Me gusta"]].sum().reset_index()
    
    fig_evol = go.Figure()
    palette = ["#3b82f6", "#a855f7", "#ec4899"] 
    metrics = ["Visualizaciones", "Alcance", "Me gusta"]

    for i, m in enumerate(metrics):
        fig_evol.add_trace(go.Scatter(
            x=df_time["Fecha"], y=df_time[m], name=m,
            mode="lines+markers+text", 
            text=[f"<b>{int(v)}</b>" if v > 0 else "" for v in df_time[m]],
            textposition="top center",
            textfont=dict(size=12, color=palette[i]),
            line=dict(shape="spline", width=4, color=palette[i]),
            marker=dict(size=8, line=dict(width=2, color="white"))
        ))

    fig_evol.update_layout(
        template="plotly_dark", height=450,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_evol, use_container_width=True)

# 3. Dispersión
with st.container(border=True):
    st.markdown("### Relación de interacciones y detección de Outliers")
    c_scat1, c_scat2 = st.columns(2)

    fig1 = px.scatter(
        df, x="Alcance", y="Me gusta", size="Visualizaciones", color="Me gusta",
        color_continuous_scale="Plasma", hover_name="Desc_Hover", trendline="ols",
        hover_data={"Desc_Hover": False, "Visualizaciones": True, "Me gusta": True},
        template="plotly_dark"
    )

    fig2 = px.scatter(
        df, x="Alcance", y="Comentarios", size="Visualizaciones", color="Comentarios",
        color_continuous_scale="Plasma", hover_name="Desc_Hover", trendline="ols",
        hover_data={"Desc_Hover": False, "Visualizaciones": True, "Comentarios": True},
        template="plotly_dark"
    )

    c_scat1.plotly_chart(fig1, use_container_width=True)
    c_scat2.plotly_chart(fig2, use_container_width=True)

# 4. Heatmap por publicación (Barras horizontales)
with st.container(border=True):
    st.markdown("### Rendimiento detallado por Publicación")
    
    metric = st.selectbox("Métrica a evaluar", ["Alcance", "Me gusta", "Comentarios", "Visualizaciones"], index=0)
    
    fig_bar = px.bar(
        df.sort_values(metric, ascending=True).tail(12),
        x=metric, y="Desc_Eje", orientation="h", color=metric,
        color_continuous_scale=["#1e40af", "#3b82f6", "#5eead4"], 
        text=metric,
        template="plotly_dark"
    )
    fig_bar.update_layout(yaxis_title=None, height=500)
    fig_bar.update_traces(textposition='auto')
    st.plotly_chart(fig_bar, use_container_width=True)

# 5. Boxplot y Efectividad
c_box, c_tipo = st.columns(2)

with c_box:
    with st.container(border=True):
        st.markdown("### Dispersión de Visualizaciones por Mes")
        orden_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        meses_presentes = [m for m in orden_meses if m in df["Mes_Esp"].unique()]
        
        fig_box = px.box(
            df, x="Mes_Esp", y="Visualizaciones", color="Mes_Esp",
            color_discrete_sequence=px.colors.sequential.Plasma,
            template="plotly_dark", category_orders={"Mes_Esp": meses_presentes}
        )
        fig_box.update_layout(xaxis_title=None, showlegend=False, height=450)
        st.plotly_chart(fig_box, use_container_width=True)

with c_tipo:
    if "Tipo de publicación" in df.columns:
        with st.container(border=True):
            st.markdown("### Efectividad por Tipo de Publicación")
            
            df_tipo = df.groupby("Tipo de publicación")[["Alcance", "Me gusta", "Comentarios"]].mean().reset_index()
            df_tipo["Efectividad %"] = ((df_tipo["Me gusta"] + df_tipo["Comentarios"]) / df_tipo["Alcance"]) * 100
            
            fig_tipo = make_subplots(specs=[[{"secondary_y": True}]])
            
            fig_tipo.add_trace(
                go.Bar(x=df_tipo["Tipo de publicación"], y=df_tipo["Alcance"], name="Alcance Promedio", 
                       marker_color="#a855f7", text=df_tipo["Alcance"].round(0), textposition="auto"),
                secondary_y=False
            )
            fig_tipo.add_trace(
                go.Scatter(x=df_tipo["Tipo de publicación"], y=df_tipo["Efectividad %"], name="% Efectividad", 
                           mode="lines+markers+text", line=dict(color="#eab308", width=3), marker=dict(size=10),
                           text=df_tipo["Efectividad %"].round(1).astype(str) + '%', textposition="top center"),
                secondary_y=True
            )
            
            fig_tipo.update_layout(template="plotly_dark", height=450, legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_tipo, use_container_width=True)

# 6. Gráfico de Prime Time
if "Hora" in df.columns and "Veces que se compartió" in df.columns and "Veces que se guardó" in df.columns:
    with st.container(border=True):
        st.markdown("### Análisis Combinado por Hora de Publicación (Prime Time)")
        
        df_hora = df.groupby("Hora").agg({
            "Veces que se guardó": "sum",
            "Veces que se compartió": "sum",
            "Alcance": "sum",
            "Me gusta": "sum",
            "Visualizaciones": "sum"
        }).reset_index()
        
        alcance_total = df_hora["Alcance"].sum()
        df_hora["% Alcance"] = (df_hora["Alcance"] / alcance_total * 100).fillna(0)
        df_hora["% Likeo vs Visitas"] = (df_hora["Me gusta"] / df_hora["Visualizaciones"] * 100).fillna(0)
        df_hora["Hora_Str"] = df_hora["Hora"].astype(str) + ":00"
        
        fig_hora = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig_hora.add_trace(go.Bar(
            x=df_hora["Hora_Str"], y=df_hora["Veces que se guardó"], name="Guardados", 
            marker_color="#a855f7", text=df_hora["Veces que se guardó"], textposition="inside"
        ), secondary_y=False)
        
        fig_hora.add_trace(go.Bar(
            x=df_hora["Hora_Str"], y=df_hora["Veces que se compartió"], name="Compartidos", 
            marker_color="#ec4899", text=df_hora["Veces que se compartió"], textposition="inside"
        ), secondary_y=False)
        
        fig_hora.add_trace(go.Scatter(
            x=df_hora["Hora_Str"], y=df_hora["% Alcance"], name="% Alcance Total", 
            mode="lines+markers+text", line=dict(color="#3b82f6", width=3, dash='dot'),
            text=df_hora["% Alcance"].round(1).astype(str) + '%', textposition="top center"
        ), secondary_y=True)
        
        fig_hora.add_trace(go.Scatter(
            x=df_hora["Hora_Str"], y=df_hora["% Likeo vs Visitas"], name="% Conversión (Likes/Vistas)", 
            mode="lines+markers+text", line=dict(color="#eab308", width=3),
            text=df_hora["% Likeo vs Visitas"].round(1).astype(str) + '%', textposition="bottom center"
        ), secondary_y=True)

        fig_hora.update_layout(barmode="stack", template="plotly_dark", height=500, legend=dict(orientation="h", y=1.1))
        fig_hora.update_yaxes(title_text="Total Interacciones", secondary_y=False)
        fig_hora.update_yaxes(title_text="Porcentaje (%)", secondary_y=True)
        
        st.plotly_chart(fig_hora, use_container_width=True)

# 7. Dataframe Final
with st.container(border=True):
    st.markdown("### Base de datos interactiva (Heatmap)")
    df_mostrar = df.drop(columns=["Desc_Hover", "Desc_Eje", "Fecha_dt"]).copy()
    
    columnas_metricas = ["Visualizaciones", "Alcance", "Me gusta", "Comentarios"]
    cols_existentes = [c for c in columnas_metricas if c in df_mostrar.columns]
    
    # Se usa PuRd para una gradiente que va de un tono claro hasta morado-rosado oscuro
    df_styled = df_mostrar.style.background_gradient(
        cmap='PuRd', subset=cols_existentes
    ).format(precision=0, subset=cols_existentes)
    
    st.dataframe(df_styled, use_container_width=True, height=400)