from fastapi import FastAPI
import pandas as pd

#creacion de API
app=FastAPI()

#Lectura de datos
df_genres=pd.read_csv('Datos_procesados/genres_analysis.csv')
genres=df_genres['Genre'].to_list()

#Endpoints de la API
#@profile

@app.get("/PlayTimeGenre/{genero}")
def PlayTimeGenre( genero : str ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(genero)!= str) or (genero not in genres): print("No se encuentra el género indicado. \nEste es un listado de los géneros con los que contamos: \n" + ', '.join(genres))
    else:
        Anio= df_genres[df_genres['Genre']==genero]['RYMaxHours'].item()
        print('{"Año de lanzamiento con más horas jugadas para Género X" : '+str(Anio)+'}')


@app.get("/usergenre/{genero}")
def UserForGenre( genero : str ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(genero)!= str) or (genero not in genres): print("No se encuentra el género indicado. \nEste es un listado de los géneros con los que contamos: \n" + ', '.join(genres))
    else:
        jugador= df_genres[df_genres['Genre']==genero]['PlayerMH'].item()
        detalleanio= df_genres[df_genres['Genre']==genero]['Years Played by player'].item()
        print('{"Usuario con más horas jugadas para Género X" : '+str(jugador)+', \n"Horas jugadas":'+str(detalleanio))