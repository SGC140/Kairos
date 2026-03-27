import pandas as pd
import os



datos_raw = pd.read_csv("Jan-01-2026_Mar-26-2026_1888590108521750.csv")
datos = pd.DataFrame(datos_raw)
headers = datos.columns


headers_necesarios = ['Nombre de la cuenta', 'Descripción', 
                      'Hora de publicación', 'Enlace permanente','Tipo de publicación', 'Visualizaciones', 
                      'Alcance', 'Me gusta', 'Veces que se compartió','Seguimientos', 'Comentarios', 'Veces que se guardó']

analyitics_kairos = datos[headers_necesarios]

analyitics_kairos = analyitics_kairos.rename(columns={'Identificador de la publicación': 'ID Publicación', 
                                                      'Identificador de la cuenta': 'ID Cuenta', 
                                                      'Hora de publicación': 'Fecha Post'})


analyitics_kairos['Fecha Post'] = pd.to_datetime(analyitics_kairos['Fecha Post'], errors='coerce')
analyitics_kairos['Fecha'] = analyitics_kairos['Fecha Post'].dt.date
analyitics_kairos['Hora Post'] = analyitics_kairos['Fecha Post'].dt.time
analyitics_kairos.drop(columns=['Fecha Post'], inplace=True)
analyitics_kairos['Seguimientos'] = analyitics_kairos['Seguimientos'].fillna(0)
analyitics_kairos['Descripción'] = (analyitics_kairos['Descripción'].str.split('\n').str[0])


print(analyitics_kairos.head())

df = analyitics_kairos.to_csv("Insight Kairós.csv")





