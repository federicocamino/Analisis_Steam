from fastapi import FastAPI
import pandas as pd

#creacion de API
app=FastAPI()

#Lectura de datos y listas de validaciones
df_genres=pd.read_csv('Datos_procesados/genres_analysis.csv')
genres=df_genres['Genre'].to_list()
df_recommended_gamesxgames=pd.read_csv('Datos_procesados/df_recommended_gamesxgames.csv')
product_ids=df_recommended_gamesxgames['item_id'].to_list()
df_year_recommendations=pd.read_csv('Datos_procesados/year_recommendations.csv')
anios=sorted(df_year_recommendations['year'].to_list())
df_releaseyear_sentiment=pd.read_csv('Datos_procesados/releaseyear_sentiment.csv')
anioslanzamiento=sorted(df_releaseyear_sentiment['release_year'].to_list())


#Endpoints de la API
#@profile

@app.get("/PlayTimeGenre/{genero}")
def PlayTimeGenre( genero : str ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(genero)!= str) or (genero not in genres): 
        return str("No se encuentra el género indicado. Este es un listado de los géneros con los que contamos: " + ', '.join(genres))
    else:
        Anio= df_genres[df_genres['Genre']==genero]['RYMaxHours'].item()
        return('{"Año de lanzamiento con más horas jugadas para Género X" : '+str(Anio)+'}')


@app.get("/usergenre/{genero}")
def UserForGenre( genero : str ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(genero)!= str) or (genero not in genres): 
        return ("No se encuentra el género indicado. Este es un listado de los géneros con los que contamos: " + ', '.join(genres))
    else:
        jugador= df_genres[df_genres['Genre']==genero]['PlayerMH'].item()
        detalleanio= df_genres[df_genres['Genre']==genero]['Years Played by player'].item()
        return('{"Usuario con más horas jugadas para Género X" : '+str(jugador)+', "Horas jugadas":'+str(detalleanio))


@app.get("/UsersRecommend/{año}")
def UsersRecommend( anio : int ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(anio)!= int) or (anio not in anios): 
        return ("No se encuentra el año indicado. Este es un listado de los años para los cuales tenemos información: " + str(anios))
    else:
        reco1 = df_year_recommendations[df_year_recommendations['year']==anio]['recommend_title_1'].item()
        reco2 = df_year_recommendations[df_year_recommendations['year']==anio]['recommend_title_2'].item()
        reco3 = df_year_recommendations[df_year_recommendations['year']==anio]['recommend_title_3'].item()
        return('Recomendaciones del año '+str(anio)+': '+str(reco1)+', '+str(reco2)+', '+str(reco3))


@app.get("/UsersNotRecommend/{año}")
def UsersNotRecommend( anio : int ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(anio)!= int) or (anio not in anios): 
        return ("No se encuentra el año indicado. Este es un listado de los años para los cuales tenemos información: " + str(anios))
    else:
        notreco1 = df_year_recommendations[df_year_recommendations['year']==anio]['not_recommend_title_1'].item()
        notreco2 = df_year_recommendations[df_year_recommendations['year']==anio]['not_recommend_title_2'].item()
        notreco3 = df_year_recommendations[df_year_recommendations['year']==anio]['not_recommend_title_3'].item()
        return('Juegos menos recomendados del año '+str(anio)+': '+str(notreco1)+', '+str(notreco2)+', '+str(notreco3))

@app.get("/sentiment_analysis/{año}")
def sentiment_analysis( anio : int ):
    # mensaje si se ingresa un tipo incorrecto o bien no se escribe bien el género. Devuelve el listado de géneros.
    if (type(anio)!= int) or (anio not in anioslanzamiento): 
        return ("No se encuentra el año indicado. Este es un listado de los años para los cuales tenemos información: " + str(anioslanzamiento))
    else:
        Negativo = df_releaseyear_sentiment[df_releaseyear_sentiment['release_year']==anio]['Negative'].item()
        Neutral = df_releaseyear_sentiment[df_releaseyear_sentiment['release_year']==anio]['Neutral'].item()
        Positivo = df_releaseyear_sentiment[df_releaseyear_sentiment['release_year']==anio]['Positive'].item()
        return('{Negative = '+str(Negativo) + ', Neutral = ' + str(Neutral) + ', Positive = ' + str(Positivo))

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