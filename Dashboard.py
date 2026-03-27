import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from dotenv import load_dotenv

load_dotenv()

PATH = os.getenv("INPUT_DASH")

st.set_page_config(page_title="Dashboard Kairós", layout="wide")

# ======================
# ESTILO
# ======================
st.markdown("""
<style>
.card {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    border: 1px solid #334155;
    padding: 16px;
    border-radius: 12px;
}
.kpi-title {color:#94a3b8; font-size:12px;}
.kpi-value {color:#f1f5f9; font-size:26px; font-weight:bold;}
.pos {color:#22c55e;}
</style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard de Publicaciones")

# ======================
# DATA
# ======================

@st.cache_data
def load():
    df = pd.read_csv(PATH)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    df["Fecha"] = pd.to_datetime(df["Fecha"]).dt.date
    df["Mes"] = pd.to_datetime(df["Fecha"]).dt.to_period("M").astype(str)

    return df

df = load()
base_df = df.copy()

# ======================
# FILTROS
# ======================
st.sidebar.header("Filtros")

mes = st.sidebar.multiselect("Mes", df["Mes"].unique())
if mes:
    df = df[df["Mes"].isin(mes)]

desc = st.sidebar.multiselect("Descripción", df["Descripción"].dropna().unique())
if desc:
    df = df[df["Descripción"].isin(desc)]

# ======================
# KPIs (CORREGIDOS)
# ======================
st.markdown("## KPIs")

c1, c2, c3, c4 = st.columns(4)

def kpi(col, name, field):
    val = df[field].sum()
    total = df[field].sum()
    percent = (val / total * 100) if total != 0 else 0

    col.markdown(f"""
    <div class="card">
        <div class="kpi-title">{name}</div>
        <div class="kpi-value">{int(val):,}</div>
        <div class="pos">{percent:.1f}% del total filtrado</div>
    </div>
    """, unsafe_allow_html=True)

kpi(c1, "Visualizaciones", "Visualizaciones")
kpi(c2, "Alcance", "Alcance")
kpi(c3, "Likes", "Me gusta")
kpi(c4, "Comentarios", "Comentarios")

# ======================
# LÍNEA SUAVIZADA + LABELS
# ======================
st.markdown("## Evolución de métricas")

df_time = df.groupby("Fecha")[["Visualizaciones","Alcance","Me gusta"]].sum().reset_index()

fig = go.Figure()

palette = ["#3b82f6","#10b981","#f43f5e"]
metrics = ["Visualizaciones","Alcance","Me gusta"]

for i, m in enumerate(metrics):
    fig.add_trace(go.Scatter(
        x=df_time["Fecha"],
        y=df_time[m],
        name=m,
        mode="lines+markers+text",
        text=df_time[m],
        textposition="top center",
        line=dict(shape="spline", width=3, color=palette[i])
    ))

fig.update_layout(
    template="plotly_dark",
    height=350,
    legend=dict(orientation="h")
)

st.plotly_chart(fig, use_container_width=True)

# ======================
# SCATTERS BONITOS
# ======================
st.markdown("## Relación de métricas")

col1, col2 = st.columns(2)

fig1 = px.scatter(
    df,
    x="Alcance",
    y="Me gusta",
    size="Visualizaciones",
    color="Me gusta",
    trendline="ols",
    hover_data=["Descripción"],
    template="plotly_dark"
)

fig2 = px.scatter(
    df,
    x="Alcance",
    y="Comentarios",
    size="Visualizaciones",
    color="Comentarios",
    trendline="ols",
    hover_data=["Descripción"],
    template="plotly_dark"
)

col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

# ======================
# ALCANCE VS TIEMPO
# ======================
st.markdown("## ⏳ Alcance vs tiempo de publicación")

df["Fecha_dt"] = pd.to_datetime(df["Fecha"])
df["Días activo"] = (pd.Timestamp.today() - df["Fecha_dt"]).dt.days

fig_time = px.scatter(
    df,
    x="Días activo",
    y="Alcance",
    size="Visualizaciones",
    color="Alcance",
    trendline="ols",
    hover_data=["Descripción"],
    template="plotly_dark"
)

st.plotly_chart(fig_time, use_container_width=True)

# ======================
# COMPARACIÓN ENTRE POSTS
# ======================
st.markdown("## Comparación de publicaciones")

col1, col2 = st.columns([1,3])

metric = col1.selectbox("Métrica", ["Alcance","Me gusta","Comentarios","Visualizaciones"])

fig_bar = px.bar(
    df.sort_values(metric, ascending=False).head(20),
    x=metric,
    y="Descripción",
    orientation="h",
    color=metric,
    template="plotly_dark"
)

col2.plotly_chart(fig_bar, use_container_width=True)

# ======================
# RENDIMIENTO POR TIPO
# ======================
if "Tipo de publicación" in df.columns:
    st.markdown("## 📊 Rendimiento por tipo de publicación")

    tipo_df = df.groupby("Tipo de publicación")[[
        "Alcance", "Me gusta", "Comentarios", "Visualizaciones"
    ]].mean().reset_index()

    fig_tipo = px.bar(
        tipo_df,
        x="Tipo de publicación",
        y=["Alcance","Me gusta","Comentarios"],
        barmode="group",
        template="plotly_dark"
    )

    st.plotly_chart(fig_tipo, use_container_width=True)

# ======================
# DATA LIMPIA
# ======================
st.markdown("## Datos")



st.dataframe(df)