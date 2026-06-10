# 📊 Instagram Analytics Dashboard: Semillero Kairós

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-23F18F?style=for-the-badge&logo=plotly&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Este repositorio alberga una solución integral para el análisis y visualización de métricas de rendimiento de Instagram, específicamente diseñada para el "Semillero Kairós". La herramienta procesa datos brutos de insights de Instagram y los presenta a través de un dashboard interactivo, facilitando la toma de decisiones estratégicas en la gestión de contenido y la optimización de la presencia digital.

## 📝 Tabla de Contenidos

1.  [Visión General del Proyecto](#1-visión-general-del-proyecto)
2.  [Valor de Negocio y Preguntas Clave](#2-valor-de-negocio-y-preguntas-clave)
3.  [Arquitectura del Sistema](#3-arquitectura-del-sistema)
4.  [Pipeline de Datos y Payload](#4-pipeline-de-datos-y-payload)
    *   [Origen de Datos](#41-origen-de-datos)
    *   [Procesamiento de Datos (`Instagram_Insight.py`)](#42-procesamiento-de-datos-instagram_insightpy)
    *   [Salida de Datos Procesados](#43-salida-de-datos-procesados)
    *   [Consumo en el Dashboard (`Dashboard.py`)](#44-consumo-en-el-dashboard-dashboardpy)
5.  [Configuración del Entorno](#5-configuración-del-entorno)
    *   [Dependencias a Nivel de Sistema Operativo](#51-dependencias-a-nivel-de-sistema-operativo)
    *   [Dependencias de Python](#52-dependencias-de-python)
    *   [Configuración con Dev Containers](#53-configuración-con-dev-containers)
6.  [Características Clave y Detalles Técnicos del Dashboard](#6-características-clave-y-detalles-técnicos-del-dashboard)
    *   [Preprocesamiento y Caching](#61-preprocesamiento-y-caching)
    *   [Key Performance Indicators (KPIs)](#62-key-performance-indicators-kpis)
    *   [Análisis de Tendencias Temporales](#63-análisis-de-tendencias-temporales)
    *   [Análisis de Dispersión y Outliers](#64-análisis-de-dispersión-y-outliers)
    *   [Rendimiento por Publicación](#65-rendimiento-por-publicación)
    *   [Dispersión Mensual y Efectividad por Tipo de Publicación](#66-dispersión-mensual-y-efectividad-por-tipo-de-publicación)
    *   [Análisis de Prime Time](#67-análisis-de-prime-time)
    *   [Tabla de Datos Interactiva](#68-tabla-de-datos-interactiva)
7.  [Uso](#7-uso)
8.  [Contribuciones](#8-contribuciones)
9.  [Licencia](#9-licencia)

---

## 1. Visión General del Proyecto

Este proyecto proporciona una solución de Business Intelligence para el análisis de datos de Instagram. Consiste en un script de procesamiento de datos que transforma los informes brutos de Instagram en un formato estructurado y un dashboard interactivo, construido con Streamlit y Plotly, que visualiza las métricas clave de rendimiento. El objetivo es ofrecer una visión clara y accionable sobre el impacto del contenido publicado, la interacción de la audiencia y la eficiencia de la estrategia de publicación.

## 2. Valor de Negocio y Preguntas Clave

Este dashboard está diseñado para responder a preguntas críticas de negocio y proporcionar valor estratégico:

*   **¿Qué se muestra?**
    *   Métricas agregadas de rendimiento (Visualizaciones, Alcance, Me gusta, Comentarios, Guardados, Compartidos, Seguimientos).
    *   Tendencias temporales de las métricas clave.
    *   Relación entre diferentes métricas de interacción.
    *   Rendimiento individual de cada publicación.
    *   Distribución de la interacción a lo largo del tiempo (meses, horas).
    *   Efectividad comparativa entre diferentes tipos de publicaciones.

*   **¿Qué permite medir?**
    *   **Engagement Rate:** A través de la relación entre likes, comentarios, guardados, compartidos y el alcance/visualizaciones.
    *   **Alcance y Visibilidad:** Cuántas personas únicas ven el contenido y cuántas veces es visto.
    *   **Longevidad del Contenido:** Cómo el alcance se mantiene o evoluciona con el tiempo desde la publicación.
    *   **Eficacia del Contenido:** Qué tipos de publicaciones generan mayor interacción y conversión.
    *   **Momentos Óptimos de Publicación (Prime Time):** Las horas del día con mayor interacción y alcance.

*   **¿Qué permite diagnosticar?**
    *   **Contenido de Bajo Rendimiento:** Identificar publicaciones con métricas por debajo del promedio.
    *   **Outliers de Interacción:** Detectar publicaciones excepcionalmente exitosas o fallidas.
    *   **Patrones de Descenso/Ascenso:** Observar tendencias en el rendimiento que pueden indicar cambios en la estrategia o en la audiencia.
    *   **Ineficiencias en la Estrategia de Contenido:** Determinar si ciertos tipos de publicaciones no están resonando con la audiencia.

*   **¿Qué permite resolver, acotar, optimizar, estandarizar y repensar?**
    *   **Resolver:** Problemas de baja interacción o alcance al identificar las causas subyacentes (tipo de contenido, hora de publicación, descripción).
    *   **Acotar:** El público objetivo y los temas de contenido más relevantes, enfocando los esfuerzos donde generan mayor impacto.
    *   **Optimizar:** La estrategia de contenido, los horarios de publicación y los formatos de contenido para maximizar el engagement y el alcance.
    *   **Estandarizar:** El proceso de monitoreo y reporte de métricas de Instagram, asegurando una evaluación consistente del rendimiento.
    *   **Repensar:**
        *   **Estrategia de Contenido:** Cuestionar la efectividad de los formatos actuales y explorar nuevos enfoques basados en datos. Por ejemplo, si los Reels tienen una alta efectividad pero bajo alcance, ¿cómo se puede aumentar su visibilidad?
        *   **Calendario Editorial:** Reevaluar los días y horas de publicación para alinearlos con los picos de actividad de la audiencia.
        *   **Narrativa y Llamadas a la Acción:** Analizar qué descripciones y CTAs generan más comentarios o guardados, y replicar esas prácticas.
        *   **Inversión en Contenido:** Justificar la asignación de recursos a la creación de ciertos tipos de contenido basándose en su retorno de interacción.
        *   **Benchmarking Interno:** Establecer puntos de referencia de rendimiento para diferentes tipos de publicaciones y monitorear el progreso a lo largo del tiempo.

En resumen, este proyecto transforma datos brutos en inteligencia accionable, permitiendo a los gestores de contenido tomar decisiones informadas para potenciar la presencia de "Semillero Kairós" en Instagram.

## 3. Arquitectura del Sistema

La arquitectura del proyecto se compone de dos módulos principales que operan en una secuencia lógica:

1.  **Módulo de Extracción y Transformación (ETL): `Instagram_Insight.py`**
    *   **Función:** Este script es responsable de cargar los datos brutos exportados directamente desde Instagram Insights (en formato CSV), realizar una limpieza y transformación inicial, y estructurarlos en un formato optimizado para el análisis.
    *   **Tecnología:** Python con la librería `pandas`.
    *   **Salida:** Genera un archivo CSV (`insight_kairos.csv`) que sirve como fuente de datos limpia para el dashboard.

2.  **Módulo de Visualización y Análisis Interactivo: `Dashboard.py`**
    *   **Función:** Este script consume el archivo `insight_kairos.csv` y construye un dashboard interactivo utilizando Streamlit. Permite a los usuarios explorar las métricas de rendimiento a través de diversos gráficos y filtros, facilitando el análisis de tendencias y la identificación de insights.
    *   **Tecnología:** Python con las librerías `streamlit`, `pandas`, `plotly.express`, `plotly.graph_objects` y `textwrap`.
    *   **Interfaz:** Una aplicación web interactiva accesible a través del navegador.

**Flujo de Datos:**

`Datos Brutos de Instagram (CSV)` --(`Instagram_Insight.py`)--> `insight_kairos.csv` --(`Dashboard.py`)--> `Dashboard Interactivo`

## 4. Pipeline de Datos y Payload

### 4.1. Origen de Datos

El pipeline se inicia con un archivo CSV exportado directamente desde la sección de Instagram Insights. Este archivo contiene métricas detalladas para las publicaciones de una cuenta específica durante un período determinado.

**Ejemplo de Nombre de Archivo de Origen:** `Mar-26-2025_Mar-26-2026_949104527769166.csv`

### 4.2. Procesamiento de Datos (`Instagram_Insight.py`)

El script `Instagram_Insight.py` ejecuta las siguientes transformaciones:

1.  **Carga de Datos:** Lee el archivo CSV de origen.
2.  **Selección de Columnas:** Filtra y selecciona un subconjunto específico de columnas relevantes para el análisis, descartando información redundante o no necesaria.
    ```python
    headers_necesarios = ['Nombre de la cuenta', 'Descripción', 
                          'Hora de publicación', 'Enlace permanente','Tipo de publicación', 'Visualizaciones', 
                          'Alcance', 'Me gusta', 'Veces que se compartió','Seguimientos', 'Comentarios', 'Veces que se guardó']
    analyitics_kairos = datos[headers_necesarios]
    ```
3.  **Renombrado de Columnas:** Estandariza los nombres de algunas columnas para mayor claridad y consistencia.
    ```python
    analyitics_kairos = analyitics_kairos.rename(columns={'Identificador de la publicación': 'ID Publicación', 
                                                          'Identificador de la cuenta': 'ID Cuenta', 
                                                          'Hora de publicación': 'Fecha Post'})
    ```
4.  **Conversión de Fechas y Horas:** Transforma la columna `Fecha Post` a formato datetime, extrayendo la fecha y la hora en columnas separadas para facilitar el análisis temporal.
    ```python
    analyitics_kairos['Fecha Post'] = pd.to_datetime(analyitics_kairos['Fecha Post'], errors='coerce')
    analyitics_kairos['Fecha'] = analyitics_kairos['Fecha Post'].dt.date
    analyitics_kairos['Hora Post'] = analyitics_kairos['Fecha Post'].dt.time
    analyitics_kairos.drop(columns=['Fecha Post'], inplace=True)
    ```
5.  **Manejo de Valores Nulos:** Rellena los valores nulos en la columna `Seguimientos` con cero, asumiendo que un valor nulo implica la ausencia de nuevos seguidores.
    ```python
    analyitics_kairos['Seguimientos'] = analyitics_kairos['Seguimientos'].fillna(0)
    ```
6.  **Limpieza de Descripción:** Extrae solo la primera línea de la columna `Descripción`, ya que las descripciones de Instagram a menudo contienen múltiples líneas que pueden ser excesivas para la visualización directa.
    ```python
    analyitics_kairos['Descripción'] = (analyitics_kairos['Descripción'].str.split('\n').str[0])
    ```
7.  **Exportación:** Guarda el DataFrame procesado en un nuevo archivo CSV.
    ```python
    analyitics_kairos.to_csv("insight_kairos.csv")
    ```

### 4.3. Salida de Datos Procesados

El script `Instagram_Insight.py` genera el archivo `insight_kairos.csv`. A continuación, se muestra un ejemplo de la estructura de este archivo:

```csv
"","Nombre de la cuenta","Descripción","Enlace permanente","Tipo de publicación","Visualizaciones","Alcance","Me gusta","Veces que se compartió","Seguimientos","Comentarios","Veces que se guardó","Fecha","Hora Post"
0,"Usuario 1","Descripción de la publicación 1","https://instagram.com/p/ABCDEF","IMAGEN",1500,1200,80,5,10,3,12,"2023-01-15","14:30:00"
1,"Usuario 1","Descripción de la publicación 2","https://instagram.com/p/GHIJKL","VIDEO",2500,2000,150,12,25,8,20,"2023-01-16","10:00:00"
2,"Usuario 1","Descripción de la publicación 3","https://instagram.com/p/MNOPQR","CARRUSEL",3000,2500,200,18,30,15,25,"2023-01-17","18:45:00"
3,"Usuario 1","Descripción de la publicación 4","https://instagram.com/p/STUVWX","REEL",4000,3500,300,25,40,20,35,"2023-01-18","09:15:00"
```

### 4.4. Consumo en el Dashboard (`Dashboard.py`)

El dashboard carga el archivo `insight_kairos.csv` y realiza transformaciones adicionales para la visualización:

1.  **Carga y Caching:** Utiliza `@st.cache_data` para cargar eficientemente el CSV y evitar recargas innecesarias.
2.  **Limpieza de Columna `Unnamed: 0`:** Elimina la columna de índice generada por `to_csv`.
3.  **Conversión a Datetime y Extracción de Componentes:** Convierte la columna `Fecha` a tipo datetime y extrae el año (`Año`), el mes en español (`Mes_Esp`) y la hora (`Hora`) para filtros y agrupaciones.
4.  **Generación de Descripciones para Hover y Ejes:** Crea versiones truncadas y formateadas de la descripción para mejorar la legibilidad en tooltips y ejes de gráficos.
5.  **Cálculo de `Días activo`:** Determina la antigüedad de cada publicación desde la fecha actual.

Estas transformaciones preparan los datos para ser consumidos por los diversos componentes visuales del dashboard.

## 5. Configuración del Entorno

Para ejecutar este proyecto, se recomienda utilizar un entorno de desarrollo aislado. La configuración proporcionada con `devcontainer.json` simplifica este proceso.

### 5.1. Dependencias a Nivel de Sistema Operativo

El archivo `.devcontainer/devcontainer.json` incluye una sección `updateContentCommand` que verifica la existencia de un archivo `packages.txt`. Si este archivo existe, se utilizará para instalar dependencias a nivel de sistema operativo (ej. `apt install`). Para este proyecto específico, no se requieren dependencias de SO adicionales más allá de las que ya incluye la imagen base de Python.

### 5.2. Dependencias de Python

Las librerías de Python necesarias se gestionan a través de un archivo `requirements.txt` (implícito en el `devcontainer.json` aunque no proporcionado directamente en el código). Las principales librerías son:

*   `pandas`: Para manipulación y análisis de datos.
*   `streamlit`: Para la construcción del dashboard interactivo.
*   `plotly`: Para la generación de gráficos interactivos y estéticos.
*   `textwrap`: Utilizado para formatear texto en las descripciones de las publicaciones.

Para instalar estas dependencias manualmente (fuera de un dev container):

```bash
pip install pandas streamlit plotly textwrap
```

### 5.3. Configuración con Dev Containers

El proyecto está configurado para ser ejecutado fácilmente en un Dev Container (por ejemplo, con VS Code Dev Containers o GitHub Codespaces).

El archivo `.devcontainer/devcontainer.json` define:

*   **Imagen Base:** `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm` (Python 3.11 en Debian Bookworm).
*   **Extensiones VS Code:** `ms-python.python`, `ms-python.vscode-pylance`.
*   **Comandos de Inicialización:**
    *   `updateContentCommand`: Instala dependencias de `packages.txt` (si existe) y `requirements.txt` (si existe), y `streamlit`.
    *   `postAttachCommand`: Inicia automáticamente el dashboard de Streamlit al adjuntar al contenedor.
        ```json
        "postAttachCommand": {
          "server": "streamlit run Dashboard.py --server.enableCORS false --server.enableXsrfProtection false"
        }
        ```
*   **Configuración de Puertos:** Redirecciona el puerto 8501 (puerto por defecto de Streamlit) y lo abre automáticamente en una vista previa.

**Para iniciar el entorno con Dev Containers:**

1.  Asegúrate de tener Docker instalado y funcionando.
2.  Abre el proyecto en VS Code.
3.  VS Code detectará el archivo `.devcontainer/devcontainer.json` y te preguntará si deseas "Reopen in Container". Acepta.
4.  El contenedor se construirá y el dashboard se iniciará automáticamente, abriendo una vista previa en tu navegador o en VS Code.

## 6. Características Clave y Detalles Técnicos del Dashboard

El `Dashboard.py` es el corazón de la visualización, utilizando Streamlit para la interfaz y Plotly para los gráficos interactivos.

### 6.1. Preprocesamiento y Caching

La función `load()` se encarga de cargar y preprocesar los datos. La directiva `@st.cache_data` es crucial para optimizar el rendimiento, ya que almacena en caché el DataFrame resultante. Esto evita que la carga y el procesamiento de datos se repitan cada vez que el usuario interactúa con los filtros, mejorando significativamente la fluidez del dashboard.

```python
@st.cache_data
def load():
    df = pd.read_csv(PATH)
    # ... (transformaciones de fecha, hora, descripción, etc.)
    return df

df = load()
base_df = df.copy() # Para cálculos de porcentaje sobre el total histórico
```

### 6.2. Key Performance Indicators (KPIs)

Se presentan cuatro KPIs principales (Visualizaciones, Alcance, Me gusta, Comentarios) en tarjetas personalizadas con CSS. Cada KPI muestra el valor total filtrado y su porcentaje respecto al total histórico de la base de datos, proporcionando un contexto inmediato del rendimiento.

```python
# Ejemplo de función KPI
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
# ... otros KPIs
```
La implementación de CSS personalizado (`st.markdown("""<style>...""")`) permite un diseño estético y coherente para las tarjetas KPI, mejorando la experiencia visual del usuario.

### 6.3. Análisis de Tendencias Temporales

Un gráfico de líneas interactivo muestra la evolución de las Visualizaciones, Alcance y Me gusta a lo largo del tiempo. Utiliza `plotly.graph_objects.Scatter` con `mode="lines+markers+text"` para resaltar los puntos de datos y sus valores, facilitando la identificación de picos y valles de rendimiento.

```python
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
fig_evol.update_layout(template="plotly_dark", height=450, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0))
```
El uso de `shape="spline"` en las líneas suaviza la visualización de las tendencias, mientras que la leyenda horizontal y la alineación a la izquierda optimizan el espacio.

### 6.4. Análisis de Dispersión y Outliers

Se utilizan gráficos de dispersión (`plotly.express.scatter`) para visualizar la relación entre métricas como Alcance, Me gusta, Comentarios y Visualizaciones. La inclusión de `trendline="ols"` (Ordinary Least Squares) permite identificar rápidamente correlaciones y detectar publicaciones que se desvían significativamente de la tendencia (posibles outliers de alto o bajo rendimiento).

```python
fig1 = px.scatter(
    df, x="Alcance", y="Me gusta", size="Visualizaciones", color="Me gusta",
    color_continuous_scale="Plasma", hover_name="Desc_Hover", trendline="ols",
    hover_data={"Desc_Hover": False, "Visualizaciones": True, "Me gusta": True},
    template="plotly_dark"
)
```
Un gráfico adicional de dispersión analiza la "Longevidad" del contenido, correlacionando `Días activo` con `Alcance`, lo que permite entender cómo el tiempo afecta la visibilidad de las publicaciones.

### 6.5. Rendimiento por Publicación

Un gráfico de barras horizontales (`plotly.express.bar`) permite comparar el rendimiento de las publicaciones individuales según una métrica seleccionada (Alcance, Me gusta, Comentarios, Visualizaciones). La capacidad de seleccionar la métrica a evaluar (`st.selectbox`) añade interactividad y flexibilidad al análisis.

```python
metric = st.selectbox("Métrica a evaluar", ["Alcance", "Me gusta", "Comentarios", "Visualizaciones"], index=0)
fig_bar = px.bar(
    df.sort_values(metric, ascending=True).tail(12), # Muestra las 12 mejores
    x=metric, y="Desc_Eje", orientation="h", color=metric,
    color_continuous_scale=["#1e40af", "#3b82f6", "#5eead4"], 
    text=metric,
    template="plotly_dark"
)
```
La visualización de las 12 publicaciones con mejor rendimiento (`.tail(12)`) es una estrategia efectiva para destacar el contenido más exitoso.

### 6.6. Dispersión Mensual y Efectividad por Tipo de Publicación

*   **Boxplot de Visualizaciones por Mes:** Un gráfico de caja (`plotly.express.box`) muestra la distribución de las visualizaciones por mes. Esto ayuda a identificar la variabilidad y los valores atípicos en el rendimiento mensual, lo que puede indicar estacionalidad o eventos específicos.
    ```python
    fig_box = px.box(
        df, x="Mes_Esp", y="Visualizaciones", color="Mes_Esp",
        color_discrete_sequence=px.colors.sequential.Plasma,
        template="plotly_dark", category_orders={"Mes_Esp": meses_presentes}
    )
    ```
*   **Efectividad por Tipo de Publicación:** Un gráfico combinado de barras y líneas (`plotly.subplots.make_subplots`) compara el alcance promedio de diferentes tipos de publicaciones con su porcentaje de efectividad (likes + comentarios / alcance). Esto es fundamental para optimizar la estrategia de contenido, identificando qué formatos generan mayor interacción.
    ```python
    df_tipo["Efectividad %"] = ((df_tipo["Me gusta"] + df_tipo["Comentarios"]) / df_tipo["Alcance"]) * 100
    fig_tipo = make_subplots(specs=[[{"secondary_y": True}]])
    # ... (adición de trazas de barras y scatter)
    ```
    La utilización de un eje Y secundario permite comparar métricas con escalas muy diferentes (Alcance vs. Porcentaje de Efectividad) en un solo gráfico.

### 6.7. Análisis de Prime Time

Un gráfico combinado (`plotly.subplots.make_subplots`) analiza las interacciones (Guardados, Compartidos) y porcentajes clave (% Alcance Total, % Conversión Likes/Vistas) por hora de publicación. Esto es crucial para identificar los "prime times" donde la audiencia está más activa y receptiva.

```python
fig_hora = make_subplots(specs=[[{"secondary_y": True}]])
# ... (adición de trazas de barras para Guardados/Compartidos y scatter para porcentajes)
fig_hora.update_yaxes(title_text="Total Interacciones", secondary_y=False)
fig_hora.update_yaxes(title_text="Porcentaje (%)", secondary_y=True)
```
Este gráfico utiliza un `barmode="stack"` para los guardados y compartidos, y líneas para los porcentajes, ofreciendo una visión completa del comportamiento horario.

### 6.8. Tabla de Datos Interactiva

Finalmente, se presenta una tabla interactiva del DataFrame procesado, permitiendo a los usuarios explorar los datos subyacentes. La tabla se estiliza con un `background_gradient` en las columnas de métricas para resaltar visualmente los valores más altos, facilitando la identificación rápida de publicaciones destacadas.

```python
df_styled = df_mostrar.style.background_gradient(
    cmap='PuRd', subset=cols_existentes
).format(precision=0, subset=cols_existentes)
st.dataframe(df_styled, use_container_width=True, height=400)
```
El uso de `st.dataframe` con estilizado de Pandas es una forma efectiva de presentar datos tabulares de manera atractiva y funcional.

## 7. Uso

Para utilizar el dashboard:

1.  **Preparar los datos:** Asegúrate de tener el archivo `insight_kairos.csv` en la raíz del proyecto. Si no lo tienes, ejecuta el script `Instagram_Insight.py` con tu archivo de datos brutos de Instagram Insights (renombrado a `Mar-26-2025_Mar-26-2026_949104527769166.csv` o ajustando la ruta en el script).
    ```bash
    python Instagram_Insight.py
    ```
2.  **Ejecutar el dashboard:**
    *   **Con Dev Containers (recomendado):** Sigue los pasos en la sección [Configuración con Dev Containers](#53-configuración-con-dev-containers). El dashboard se iniciará automáticamente.
    *   **Manualmente:** Abre tu terminal en la raíz del proyecto y ejecuta:
        ```bash
        streamlit run Dashboard.py
        ```
        Esto abrirá el dashboard en tu navegador web, generalmente en `http://localhost:8501`.

Una vez abierto, puedes interactuar con los filtros de la barra lateral para segmentar los datos por año, rango de fechas, mes, tipo de publicación y descripción, y observar cómo los gráficos se actualizan dinámicamente.

## 8. Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor, sigue estos pasos:

1.  Haz un fork del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3.  Realiza tus cambios y commitea (`git commit -am 'Añadir nueva funcionalidad'`).
4.  Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5.  Abre un Pull Request.

## 9. Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.