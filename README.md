# Analisis_Steam

## Objetivo

Se busca realizar un análisis estadístico y de recomendaciones a partir de datos obtenidos de la plataforma [Steam](https://store.steampowered.com/?l=spanish).
La misma es una plataforma de juegos en la cual los usuarios pueden adquirir juegos y jugar en línea, además de poder realizar comentarios y recomendaciones de los mismos.

## Información base

Se parte de la siguiente información:
- [steam_games](/Datos_sin_procesar/steam_games.json.gz): datos de juegos en la plataforma de Steam
- [user_items](/Datos_sin_procesar/users_items.json.gz): datos de juegos y horas jugadas por usuario
- [user_reviews](/Datos_sin_procesar/user_reviews.json.gz): comentarios y recomendaciones de los usuarios

## Funciones desarrolladas

- PlayTimeGenre (_ingresar género_): Devuelve el año con mas horas jugadas para el género ingresado.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
- UserForGenre (_ingresar género_): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
- UsersRecommend (_ingresar año_): Devuelve el top 3 de juegos más recomendados por usuarios para el año dado.
- UsersNotRecommend (_ingresar año_): Devuelve el top 3 de juegos menos recomendados por usuarios para el año dado. 
- sentiment_analysis (_ingresar año_): Devuelve una lista con la cantidad de registros de reseñas de usuarios según un análisis de sentimiento para el año ingresado.
- recomendacion_juego (_ingresar id de producto_): Devuelve una lista con 5 juegos recomendados similares al producto ingresado.

## Resultados

Los resultados de las funciones pueden obtenerse de la siguiente [**App**](https://analisis-steam.onrender.com/docs)
