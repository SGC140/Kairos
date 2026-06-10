# Badges
[![Python](https://img.shields.io/badge/Python-Streamlit-blue)](https://streamlit.io/)
[![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Pandas-orange)](https://pandas.pydata.org/)
[![Visualization](https://img.shields.io/badge/Visualization-Plotly-red)](https://plotly.com/)

# Índice
1. [Introducción](#introducción)
2. [Arquitectura y Dependencias](#arquitectura-y-dependencias)
3. [Configuración](#configuración)
4. [Ejemplos de Salida](#ejemplos-de-salida)
5. [Valor Agregado y Tecnologías Utilizadas](#valor-agregado-y-tecnologías-utilizadas)
6. [Segmentación del Código](#segmentación-del-código)

## Introducción
Este proyecto se enfoca en el análisis de métricas de Instagram para el semillero Kairós. El objetivo es proporcionar una herramienta interactiva para visualizar y analizar los datos de rendimiento de las publicaciones en Instagram.

## Arquitectura y Dependencias
La arquitectura del proyecto se basa en los siguientes componentes:
- **Dashboard.py**: Script principal que carga los datos y crea el dashboard interactivo utilizando Streamlit.
- **Instagram_Insight.py**: Script que procesa los datos raw de Instagram y los convierte en un formato adecuado para el análisis.
- **.devcontainer/devcontainer.json**: Configuración del contenedor de desarrollo que utiliza Docker y VS Code.

Las dependencias principales son:
- **Streamlit**: Biblioteca para crear aplicaciones web interactivas.
- **Pandas**: Biblioteca para el análisis de datos.
- **Plotly**: Biblioteca para la visualización de datos.

## Configuración
Para ejecutar el proyecto, se requieren las siguientes configuraciones:
- Instalar Python y las bibliotecas necesarias (Streamlit, Pandas, Plotly).
- Configurar el contenedor de desarrollo utilizando Docker y VS Code.
- Preparar los datos de Instagram en un archivo CSV.

## Ejemplos de Salida
La salida del proyecto es un dashboard interactivo que muestra las siguientes secciones:
- **Rendimiento General**: KPIs generales de las publicaciones (visualizaciones, alcance, likes, comentarios).
- **Evolución de Métricas**: Gráfico de línea que muestra la evolución de las métricas a lo largo del tiempo.
- **Dispersión**: Gráfico de dispersión que muestra la relación entre las interacciones y las visualizaciones.
- **Longevidad**: Gráfico de dispersión que muestra la relación entre el alcance y el tiempo de publicación.
- **Rendimiento Detallado**: Gráfico de barras que muestra el rendimiento detallado por publicación.
- **Boxplot y Efectividad**: Gráfico de boxplot que muestra la dispersión de las visualizaciones por mes y la efectividad por tipo de publicación.

## Valor Agregado y Tecnologías Utilizadas
El valor agregado de este proyecto es proporcionar una herramienta interactiva para visualizar y analizar los datos de rendimiento de las publicaciones en Instagram. Las tecnologías utilizadas son:
- **Streamlit**: Permite crear aplicaciones web interactivas de manera rápida y sencilla.
- **Pandas**: Permite el análisis de datos de manera eficiente y efectiva.
- **Plotly**: Permite la visualización de datos de manera interactiva y personalizable.

## Segmentación del Código
El código se segmenta en las siguientes secciones:
- **Carga de Datos**: Se carga el archivo CSV que contiene los datos de Instagram.
- **Procesamiento de Datos**: Se procesan los datos para convertirlos en un formato adecuado para el análisis.
- **Creación del Dashboard**: Se crea el dashboard interactivo utilizando Streamlit.
- **Visualización de Datos**: Se visualizan los datos utilizando Plotly.

```python
# Ejemplo de código que muestra la estructura de la salida
data = {
    "Visualizaciones": [100, 200, 300],
    "Alcance": [500, 600, 700],
    "Likes": [10, 20, 30],
    "Comentarios": [5, 10, 15]
}

df = pd.DataFrame(data)

# Se muestra la estructura de la salida
print(df)
```

```markdown
# Estructura de la salida
| Visualizaciones | Alcance | Likes | Comentarios |
| --- | --- | --- | --- |
| 100 | 500 | 10 | 5 |
| 200 | 600 | 20 | 10 |
| 300 | 700 | 30 | 15 |
```