# 📊 Instagram Analytics Dashboard: Semillero Kairós

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-23F18F?style=for-the-badge&logo=plotly&logoColor=white)
![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

This repository hosts a comprehensive solution for analyzing and visualizing Instagram performance metrics, specifically designed for "Semillero Kairós". The tool processes raw Instagram insights data and presents it through an interactive dashboard, facilitating strategic decision-making in content management and digital presence optimization.

## 📝 Table of Contents

1.  [Project Overview](#1-project-overview)
2.  [Business Value and Key Questions](#2-business-value-and-key-questions)
3.  [System Architecture](#3-system-architecture)
4.  [Data Pipeline and Payload](#4-data-pipeline-and-payload)
    *   [Data Source](#41-data-source)
    *   [Data Processing (`Instagram_Insight.py`)](#42-data-processing-instagram_insightpy)
    *   [Processed Data Output](#43-processed-data-output)
    *   [Dashboard Consumption (`Dashboard.py`)](#44-dashboard-consumption-dashboardpy)
5.  [Environment Setup](#5-environment-setup)
    *   [Operating System Dependencies](#51-operating-system-dependencies)
    *   [Python Dependencies](#52-python-dependencies)
    *   [Dev Containers Configuration](#53-dev-containers-configuration)
6.  [Key Features and Technical Details of the Dashboard](#6-key-features-and-technical-details-of-the-dashboard)
    *   [Preprocessing and Caching](#61-preprocessing-and-caching)
    *   [Key Performance Indicators (KPIs)](#62-key-performance-indicators-kpis)
    *   [Temporal Trend Analysis](#63-temporal-trend-analysis)
    *   [Dispersion and Outlier Analysis](#64-dispersion-and-outlier-analysis)
    *   [Performance by Post](#65-performance-by-post)
    *   [Monthly Dispersion and Effectiveness by Post Type](#66-monthly-dispersion-and-effectiveness-by-post-type)
    *   [Prime Time Analysis](#67-prime-time-analysis)
    *   [Interactive Data Table](#68-interactive-data-table)
7.  [Usage](#7-usage)
8.  [Contributions](#8-contributions)
9.  [License](#9-license)

---

## 1. Project Overview

This project provides a Business Intelligence solution for Instagram data analysis. It consists of a data processing script that transforms raw Instagram reports into a structured format and an interactive dashboard, built with Streamlit and Plotly, which visualizes key performance metrics. The objective is to offer clear and actionable insights into the impact of published content, audience interaction, and the efficiency of the posting strategy.

## 2. Business Value and Key Questions

This dashboard is designed to answer critical business questions and provide strategic value:

*   **What is displayed?**
    *   Aggregated performance metrics (Impressions, Reach, Likes, Comments, Saves, Shares, Follows).
    *   Temporal trends of key metrics.
    *   Relationship between different interaction metrics.
    *   Individual performance of each post.
    *   Distribution of interaction over time (months, hours).
    *   Comparative effectiveness between different post types.

*   **What does it allow to measure?**
    *   **Engagement Rate:** Through the relationship between likes, comments, saves, shares, and reach/impressions.
    *   **Reach and Visibility:** How many unique people see the content and how many times it is seen.
    *   **Content Longevity:** How reach is maintained or evolves over time since publication.
    *   **Content Effectiveness:** Which types of posts generate greater interaction and conversion.
    *   **Optimal Posting Times (Prime Time):** The hours of the day with the highest interaction and reach.

*   **What does it allow to diagnose?**
    *   **Low-Performing Content:** Identify posts with below-average metrics.
    *   **Interaction Outliers:** Detect exceptionally successful or failed posts.
    *   **Decline/Ascent Patterns:** Observe performance trends that may indicate changes in strategy or audience.
    *   **Content Strategy Inefficiencies:** Determine if certain post types are not resonating with the audience.

*   **What does it allow to solve, narrow down, optimize, standardize, and rethink?**
    *   **Solve:** Problems of low interaction or reach by identifying underlying causes (content type, posting time, description).
    *   **Narrow down:** The target audience and most relevant content topics, focusing efforts where they generate the greatest impact.
    *   **Optimize:** Content strategy, posting schedules, and content formats to maximize engagement and reach.
    *   **Standardize:** The process of monitoring and reporting Instagram metrics, ensuring consistent performance evaluation.
    *   **Rethink:**
        *   **Content Strategy:** Question the effectiveness of current formats and explore new data-driven approaches. For example, if Reels have high effectiveness but low reach, how can their visibility be increased?
        *   **Editorial Calendar:** Re-evaluate posting days and times to align with audience activity peaks.
        *   **Narrative and Calls to Action:** Analyze which descriptions and CTAs generate more comments or saves, and replicate those practices.
        *   **Content Investment:** Justify resource allocation to the creation of certain content types based on their interaction return.
        *   **Internal Benchmarking:** Establish performance benchmarks for different post types and monitor progress over time.

In summary, this project transforms raw data into actionable intelligence, enabling content managers to make informed decisions to boost "Semillero Kairós"'s presence on Instagram.

## 3. System Architecture

The project's architecture consists of two main modules that operate in a logical sequence:

1.  **Extraction and Transformation (ETL) Module: `Instagram_Insight.py`**
    *   **Function:** This script is responsible for loading raw data exported directly from Instagram Insights (in CSV format), performing initial cleaning and transformation, and structuring it into a format optimized for analysis.
    *   **Technology:** Python with the `pandas` library.
    *   **Output:** Generates a CSV file (`insight_kairos.csv`) that serves as the clean data source for the dashboard.

2.  **Interactive Visualization and Analysis Module: `Dashboard.py`**
    *   **Function:** This script consumes the `insight_kairos.csv` file and builds an interactive dashboard using Streamlit. It allows users to explore performance metrics through various charts and filters, facilitating trend analysis and insight identification.
    *   **Technology:** Python with the `streamlit`, `pandas`, `plotly.express`, `plotly.graph_objects`, and `textwrap` libraries.
    *   **Interface:** An interactive web application accessible via the browser.

**Data Flow:**

`Raw Instagram Data (CSV)` --(`Instagram_Insight.py`)--> `insight_kairos.csv` --(`Dashboard.py`)--> `Interactive Dashboard`

## 4. Data Pipeline and Payload

### 4.1. Data Source

The pipeline starts with a CSV file exported directly from the Instagram Insights section. This file contains detailed metrics for a specific account's posts over a given period.

**Example Source File Name:** `Mar-26-2025_Mar-26-2026_949104527769166.csv`

### 4.2. Data Processing (`Instagram_Insight.py`)

The `Instagram_Insight.py` script performs the following transformations:

1.  **Data Loading:** Reads the source CSV file.
2.  **Column Selection:** Filters and selects a specific subset of columns relevant for analysis, discarding redundant or unnecessary information.
    ```python
    headers_necesarios = ['Nombre de la cuenta', 'Descripción', 
                          'Hora de publicación', 'Enlace permanente','Tipo de publicación', 'Visualizaciones', 
                          'Alcance', 'Me gusta', 'Veces que se compartió','Seguimientos', 'Comentarios', 'Veces que se guardó']
    analyitics_kairos = datos[headers_necesarios]
    ```
3.  **Column Renaming:** Standardizes the names of some columns for clarity and consistency.
    ```python
    analyitics_kairos = analyitics_kairos.rename(columns={'Identificador de la publicación': 'ID Publicación', 
                                                          'Identificador de la cuenta': 'ID Cuenta', 
                                                          'Hora de publicación': 'Fecha Post'})
    ```
4.  **Date and Time Conversion:** Transforms the `Fecha Post` column to datetime format, extracting the date and time into separate columns to facilitate temporal analysis.
    ```python
    analyitics_kairos['Fecha Post'] = pd.to_datetime(analyitics_kairos['Fecha Post'], errors='coerce')
    analyitics_kairos['Fecha'] = analyitics_kairos['Fecha Post'].dt.date
    analyitics_kairos['Hora Post'] = analyitics_kairos['Fecha Post'].dt.time
    analyitics_kairos.drop(columns=['Fecha Post'], inplace=True)
    ```
5.  **Null Value Handling:** Fills null values in the `Seguimientos` column with zero, assuming a null value implies the absence of new followers.
    ```python
    analyitics_kairos['Seguimientos'] = analyitics_kairos['Seguimientos'].fillna(0)
    ```
6.  **Description Cleaning:** Extracts only the first line of the `Descripción` column, as Instagram descriptions often contain multiple lines that can be excessive for direct visualization.
    ```python
    analyitics_kairos['Descripción'] = (analyitics_kairos['Descripción'].str.split('\n').str[0])
    ```
7.  **Export:** Saves the processed DataFrame to a new CSV file.
    ```python
    analyitics_kairos.to_csv("insight_kairos.csv")
    ```

### 4.3. Processed Data Output

The `Instagram_Insight.py` script generates the `insight_kairos.csv` file. Below is an example of this file's structure:

```csv
"","Account Name","Description","Permalink","Post Type","Impressions","Reach","Likes","Shares","Follows","Comments","Saves","Date","Post Time"
0,"Usuario 1","Description of post 1","https://instagram.com/p/ABCDEF","IMAGE",1500,1200,80,5,10,3,12,"2023-01-15","14:30:00"
1,"Usuario 1","Description of post 2","https://instagram.com/p/GHIJKL","VIDEO",2500,2000,150,12,25,8,20,"2023-01-16","10:00:00"
2,"Usuario 1","Description of post 3","https://instagram.com/p/MNOPQR","CAROUSEL",3000,2500,200,18,30,15,25,"2023-01-17","18:45:00"
3,"Usuario 1","Description of post 4","https://instagram.com/p/STUVWX","REEL",4000,3500,300,25,40,20,35,"2023-01-18","09:15:00"
```

### 4.4. Dashboard Consumption (`Dashboard.py`)

The dashboard loads the `insight_kairos.csv` file and performs additional transformations for visualization:

1.  **Loading and Caching:** Uses `@st.cache_data` to efficiently load the CSV and prevent unnecessary reloads.
2.  **`Unnamed: 0` Column Cleaning:** Removes the index column generated by `to_csv`.
3.  **Datetime Conversion and Component Extraction:** Converts the `Fecha` column to datetime type and extracts the year (`Año`), month in Spanish (`Mes_Esp`), and hour (`Hora`) for filters and groupings.
4.  **Description Generation for Hover and Axes:** Creates truncated and formatted versions of the description to improve readability in tooltips and chart axes.
5.  **`Días activo` Calculation:** Determines the age of each post from the current date.

These transformations prepare the data to be consumed by the various visual components of the dashboard.

## 5. Environment Setup

To run this project, it is recommended to use an isolated development environment. The configuration provided with `devcontainer.json` simplifies this process.

### 5.1. Operating System Dependencies

The `.devcontainer/devcontainer.json` file includes an `updateContentCommand` section that checks for the existence of a `packages.txt` file. If this file exists, it will be used to install operating system-level dependencies (e.g., `apt install`). For this specific project, no additional OS dependencies are required beyond those already included in the base Python image.

### 5.2. Python Dependencies

The necessary Python libraries are managed through a `requirements.txt` file (implicit in `devcontainer.json` although not directly provided in the code). The main libraries are:

*   `pandas`: For data manipulation and analysis.
*   `streamlit`: For building the interactive dashboard.
*   `plotly`: For generating interactive and aesthetic charts.
*   `textwrap`: Used for formatting text in post descriptions.

To install these dependencies manually (outside a dev container):

```bash
pip install pandas streamlit plotly textwrap
```

### 5.3. Dev Containers Configuration

The project is configured to be easily run in a Dev Container (e.g., with VS Code Dev Containers or GitHub Codespaces).

The `.devcontainer/devcontainer.json` file defines:

*   **Base Image:** `mcr.microsoft.com/devcontainers/python:1-3.11-bookworm` (Python 3.11 on Debian Bookworm).
*   **VS Code Extensions:** `ms-python.python`, `ms-python.vscode-pylance`.
*   **Initialization Commands:**
    *   `updateContentCommand`: Installs dependencies from `packages.txt` (if it exists) and `requirements.txt` (if it exists), and `streamlit`.
    *   `postAttachCommand`: Automatically starts the Streamlit dashboard when attaching to the container.
        ```json
        "postAttachCommand": {
          "server": "streamlit run Dashboard.py --server.enableCORS false --server.enableXsrfProtection false"
        }
        ```
*   **Port Configuration:** Redirects port 8501 (default Streamlit port) and automatically opens it in a preview.

**To start the environment with Dev Containers:**

1.  Make sure Docker is installed and running.
2.  Open the project in VS Code.
3.  VS Code will detect the `.devcontainer/devcontainer.json` file and ask if you want to "Reopen in Container". Accept.
4.  The container will build, and the dashboard will automatically start, opening a preview in your browser or within VS Code.

## 6. Key Features and Technical Details of the Dashboard

`Dashboard.py` is the heart of the visualization, using Streamlit for the interface and Plotly for interactive charts.

### 6.1. Preprocessing and Caching

The `load()` function is responsible for loading and preprocessing the data. The `@st.cache_data` directive is crucial for optimizing performance, as it caches the resulting DataFrame. This prevents data loading and processing from repeating every time the user interacts with filters, significantly improving the dashboard's fluidity.

```python
@st.cache_data
def load():
    df = pd.read_csv(PATH)
    # ... (date, time, description transformations, etc.)
    return df

df = load()
base_df = df.copy() # For percentage calculations against the historical total
```

### 6.2. Key Performance Indicators (KPIs)

Four main KPIs (Impressions, Reach, Likes, Comments) are presented in custom CSS cards. Each KPI shows the total filtered value and its percentage relative to the historical total in the database, providing immediate context of performance.

```python
# Example KPI function
def kpi(col, name, field):
    val = df[field].sum()
    total = base_df[field].sum()
    percent = (val / total * 100) if total != 0 else 0

    col.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">{name}</div>
        <div class="kpi-value">{int(val):,}</div>
        <div class="kpi-percent">{percent:.1f}% of global historical total</div>
    </div>
    """, unsafe_allow_html=True)

kpi(c1, "Impressions", "Visualizaciones") # "Visualizaciones" is the original column name
# ... other KPIs
```
The implementation of custom CSS (`st.markdown("""<style>...""")`) allows for an aesthetic and consistent design for the KPI cards, enhancing the user's visual experience.

### 6.3. Temporal Trend Analysis

An interactive line chart shows the evolution of Impressions, Reach, and Likes over time. It uses `plotly.graph_objects.Scatter` with `mode="lines+markers+text"` to highlight data points and their values, facilitating the identification of performance peaks and valleys.

```python
fig_evol = go.Figure()
palette = ["#3b82f6", "#a855f7", "#ec4899"] 
metrics = ["Visualizaciones", "Alcance", "Me gusta"] # Original column names

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
The use of `shape="spline"` for lines smooths the visualization of trends, while the horizontal legend and left alignment optimize space.

### 6.4. Dispersion and Outlier Analysis

Scatter plots (`plotly.express.scatter`) are used to visualize the relationship between metrics such as Reach, Likes, Comments, and Impressions. The inclusion of `trendline="ols"` (Ordinary Least Squares) allows for quick identification of correlations and detection of posts that deviate significantly from the trend (potential high or low-performing outliers).

```python
fig1 = px.scatter(
    df, x="Alcance", y="Me gusta", size="Visualizaciones", color="Me gusta", # Original column names
    color_continuous_scale="Plasma", hover_name="Desc_Hover", trendline="ols",
    hover_data={"Desc_Hover": False, "Visualizaciones": True, "Me gusta": True}, # Original column names
    template="plotly_dark"
)
```
An additional scatter plot analyzes content "Longevity", correlating `Días activo` with `Alcance`, which helps understand how time affects post visibility.

### 6.5. Performance by Post

A horizontal bar chart (`plotly.express.bar`) allows comparing the performance of individual posts based on a selected metric (Reach, Likes, Comments, Impressions). The ability to select the metric to evaluate (`st.selectbox`) adds interactivity and flexibility to the analysis.

```python
metric = st.selectbox("Metric to evaluate", ["Alcance", "Me gusta", "Comentarios", "Visualizaciones"], index=0) # Original column names
fig_bar = px.bar(
    df.sort_values(metric, ascending=True).tail(12), # Shows the top 12
    x=metric, y="Desc_Eje", orientation="h", color=metric,
    color_continuous_scale=["#1e40af", "#3b82f6", "#5eead4"], 
    text=metric,
    template="plotly_dark"
)
```
Visualizing the top 12 performing posts (`.tail(12)`) is an effective strategy to highlight the most successful content.

### 6.6. Monthly Dispersion and Effectiveness by Post Type

*   **Boxplot of Impressions by Month:** A box plot (`plotly.express.box`) shows the distribution of impressions by month. This helps identify variability and outliers in monthly performance, which may indicate seasonality or specific events.
    ```python
    fig_box = px.box(
        df, x="Mes_Esp", y="Visualizaciones", color="Mes_Esp", # Original column names
        color_discrete_sequence=px.colors.sequential.Plasma,
        template="plotly_dark", category_orders={"Mes_Esp": meses_presentes}
    )
    ```
*   **Effectiveness by Post Type:** A combined bar and line chart (`plotly.subplots.make_subplots`) compares the average reach of different post types with their effectiveness percentage (likes + comments / reach). This is fundamental for optimizing content strategy, identifying which formats generate greater interaction.
    ```python
    df_tipo["Efectividad %"] = ((df_tipo["Me gusta"] + df_tipo["Comentarios"]) / df_tipo["Alcance"]) * 100 # Original column names
    fig_tipo = make_subplots(specs=[[{"secondary_y": True}]])
    # ... (addition of bar and scatter traces)
    ```
    The use of a secondary Y-axis allows comparing metrics with very different scales (Reach vs. Effectiveness Percentage) in a single chart.

### 6.7. Prime Time Analysis

A combined chart (`plotly.subplots.make_subplots`) analyzes interactions (Saves, Shares) and key percentages (% Total Reach, % Likes/Views Conversion) by posting hour. This is crucial for identifying "prime times" when the audience is most active and receptive.

```python
fig_hora = make_subplots(specs=[[{"secondary_y": True}]])
# ... (addition of bar traces for Saves/Shares and scatter for percentages)
fig_hora.update_yaxes(title_text="Total Interactions", secondary_y=False)
fig_hora.update_yaxes(title_text="Percentage (%)", secondary_y=True)
```
This chart uses `barmode="stack"` for saves and shares, and lines for percentages, offering a comprehensive view of hourly behavior.

### 6.8. Interactive Data Table

Finally, an interactive table of the processed DataFrame is presented, allowing users to explore the underlying data. The table is styled with a `background_gradient` on the metric columns to visually highlight higher values, facilitating quick identification of standout posts.

```python
df_styled = df_mostrar.style.background_gradient(
    cmap='PuRd', subset=cols_existentes
).format(precision=0, subset=cols_existentes)
st.dataframe(df_styled, use_container_width=True, height=400)
```
Using `st.dataframe` with Pandas styling is an effective way to present tabular data attractively and functionally.

## 7. Usage

To use the dashboard:

1.  **Prepare the data:** Make sure you have the `insight_kairos.csv` file in the project root. If not, run the `Instagram_Insight.py` script with your raw Instagram Insights data file (renamed to `Mar-26-2025_Mar-26-2026_949104527769166.csv` or by adjusting the path in the script).
    ```bash
    python Instagram_Insight.py
    ```
2.  **Run the dashboard:**
    *   **With Dev Containers (recommended):** Follow the steps in the [Dev Containers Configuration](#53-dev-containers-configuration) section. The dashboard will start automatically.
    *   **Manually:** Open your terminal in the project root and run:
        ```bash
        streamlit run Dashboard.py
        ```
        This will open the dashboard in your web browser, usually at `http://localhost:8501`.

Once opened, you can interact with the sidebar filters to segment data by year, date range, month, post type, and description, and observe how the charts dynamically update.

## 8. Contributions

Contributions are welcome. If you wish to improve this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/new-functionality`).
3.  Make your changes and commit (`git commit -am 'Add new functionality'`).
4.  Push your changes to your fork (`git push origin feature/new-functionality`).
5.  Open a Pull Request.

## 9. License

This project is licensed under the MIT License. See the `LICENSE` file for more details.