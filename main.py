from fastapi import FastAPI
import pandas as pd

#creacion de API
app=FastAPI()

#Lectura de datos y listas de validaciones
df_genres=pd.read_csv('Datos_procesados/genres_analysis.csv')
genres=df_genres['Genre'].to_list()
df_recommended_gamesxgames=pd.read_csv('Datos_procesados/df_recommended_gamesxgames.csv')
product_ids=df_recommended_gamesxgames['item_id'].to_list()

#Endpoints de la API
#@profile

@app.get("/PlayTimeGenre/{genero}")
def PlayTimeGenre( genero : str ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(genero)!= str) or (genero not in genres): 
        return str("No se encuentra el género indicado. \nEste es un listado de los géneros con los que contamos: \n" + ', '.join(genres))
    else:
        Anio= df_genres[df_genres['Genre']==genero]['RYMaxHours'].item()
        return('{"Año de lanzamiento con más horas jugadas para Género X" : '+str(Anio)+'}')


@app.get("/usergenre/{genero}")
def UserForGenre( genero : str ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(genero)!= str) or (genero not in genres): 
        return ("No se encuentra el género indicado. \nEste es un listado de los géneros con los que contamos: \n" + ', '.join(genres))
    else:
        jugador= df_genres[df_genres['Genre']==genero]['PlayerMH'].item()
        detalleanio= df_genres[df_genres['Genre']==genero]['Years Played by player'].item()
        return('{"Usuario con más horas jugadas para Género X" : '+str(jugador)+', \n"Horas jugadas":'+str(detalleanio))
    

@app.get("/Recomendación_juego/{product_id}")
def recomendacion_juego( product_id : int ):
     # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(product_id)!= int) or (product_id not in product_ids): 
        return ("No se encuentra el id de juego indicado. Pruebe con otro valor")
    else:
        juego=df_recommended_gamesxgames[df_recommended_gamesxgames['item_id']==product_id]['item_title'].item()
        reco1=df_recommended_gamesxgames[df_recommended_gamesxgames['item_id']==product_id]['recommended_game_1'].item()
        reco2=df_recommended_gamesxgames[df_recommended_gamesxgames['item_id']==product_id]['recommended_game_2'].item()
        reco3=df_recommended_gamesxgames[df_recommended_gamesxgames['item_id']==product_id]['recommended_game_3'].item()
        reco4=df_recommended_gamesxgames[df_recommended_gamesxgames['item_id']==product_id]['recommended_game_4'].item()
        reco5=df_recommended_gamesxgames[df_recommended_gamesxgames['item_id']==product_id]['recommended_game_5'].item()
        return ('Para el juego elegido '+ juego +' se recomiendan los siguientes juegos : '+ reco1 + ', ' + reco2 + ', ' + reco3  + ', ' + reco4  + ', ' + reco5)

