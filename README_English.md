# Badges
[![Python](https://img.shields.io/badge/Python-Streamlit-blue)](https://streamlit.io/)
[![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Pandas-orange)](https://pandas.pydata.org/)
[![Visualization](https://img.shields.io/badge/Visualization-Plotly-red)](https://plotly.com/)

# Index
1. [Introduction](#introduction)
2. [Architecture and Dependencies](#architecture-and-dependencies)
3. [Configuration](#configuration)
4. [Output Examples](#output-examples)
5. [Added Value and Technologies Used](#added-value-and-technologies-used)
6. [Code Segmentation](#code-segmentation)

## Introduction
This project focuses on analyzing Instagram metrics for the Kairós incubator. The goal is to provide an interactive tool to visualize and analyze the performance data of Instagram posts.

## Architecture and Dependencies
The project architecture is based on the following components:
- **Dashboard.py**: The main script that loads the data and creates the interactive dashboard using Streamlit.
- **Instagram_Insight.py**: The script that processes the raw Instagram data and converts it into a suitable format for analysis.
- **.devcontainer/devcontainer.json**: The development container configuration that uses Docker and VS Code.

The main dependencies are:
- **Streamlit**: A library for creating interactive web applications.
- **Pandas**: A library for data analysis.
- **Plotly**: A library for data visualization.

## Configuration
To run the project, the following configurations are required:
- Install Python and the necessary libraries (Streamlit, Pandas, Plotly).
- Configure the development container using Docker and VS Code.
- Prepare the Instagram data in a CSV file.

## Output Examples
The project output is an interactive dashboard that displays the following sections:
- **General Performance**: General KPIs of posts (views, reach, likes, comments).
- **Metric Evolution**: A line chart that shows the evolution of metrics over time.
- **Scatter Plot**: A scatter plot that shows the relationship between interactions and views.
- **Longevity**: A scatter plot that shows the relationship between reach and posting time.
- **Detailed Performance**: A bar chart that shows the detailed performance by post.
- **Boxplot and Effectiveness**: A boxplot that shows the dispersion of views by month and the effectiveness by post type.

## Added Value and Technologies Used
The added value of this project is to provide an interactive tool to visualize and analyze the performance data of Instagram posts. The technologies used are:
- **Streamlit**: Allows creating interactive web applications quickly and easily.
- **Pandas**: Allows efficient and effective data analysis.
- **Plotly**: Allows interactive and customizable data visualization.

## Code Segmentation
The code is segmented into the following sections:
- **Data Loading**: The CSV file containing the Instagram data is loaded.
- **Data Processing**: The data is processed to convert it into a suitable format for analysis.
- **Dashboard Creation**: The interactive dashboard is created using Streamlit.
- **Data Visualization**: The data is visualized using Plotly.

```python
# Example code that shows the output structure
data = {
    "Views": [100, 200, 300],
    "Reach": [500, 600, 700],
    "Likes": [10, 20, 30],
    "Comments": [5, 10, 15]
}

df = pd.DataFrame(data)

# The output structure is displayed
print(df)
```

```markdown
# Output Structure
| Views | Reach | Likes | Comments |
| --- | --- | --- | --- |
| 100 | 500 | 10 | 5 |
| 200 | 600 | 20 | 10 |
| 300 | 700 | 30 | 15 |
```