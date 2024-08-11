#Steam_Analysis

## Objective

The aim is to perform a statistical analysis and a recommendations system based on data obtained from [Steam](https://store.steampowered.com/?l=spanish) platform.
It's a gaming platform in which users can buy games and play online, and make comments and recommendations about them.

## Basic information

It is based on the following information:
- [steam_games](/Raw_Data/steam_games.json.gz): game data on the Steam platform
- [user_items](/Raw_Data/users_items.json.gz): game data and hours played per user
- [user_reviews](/Unprocessed_Data/user_reviews.json.gz): users comments and recommendations

## Deployed functions

- PlayTimeGenre (_enter genre_): Returns the year with the most hours played for the selected genre.
- UserForGenre (_enter genre_): Returns the user who accumulates the most hours played for the given genre and a list of the total hours played per year.
- UsersRecommend (_enter year_): Returns the top 3 games most recommended by users for the given year.
- UsersNotRecommend (_enter year_): Returns the top 3 games least recommended by users for the given year. 
- sentiment_analysis (_enter year_): Returns a list with the number of user reviews records based on a sentiment analysis for the selected year.
- game_recommendation (_enter product id_): Returns a list with 5 recommended games similar to the entered product.

## Results

The results of the functions can be obtained from the following [**App**](https://analisis-steam.onrender.com/docs)

## Exploratory data analysis

Performing an analysis of the data classified by genre, it can be concluded that the two most played genres, and those that contribute the most revenue, are Action and Adventure. On the other hand, the genre that has the most amount of games is Indie. Steam should invest more in games in the first two categories.
![](/Datos_procesados/Imagenes/RevenuesbyGenre.png)
![](/Datos_procesados/Imagenes/PlayersbyGenre.png)
![](/Datos_procesados/Imagenes/GamesbyGenre.png)

There are also 2,823 games with a total turnover of less than $100. It may be advisable to evaluate whether these games should continue on the platform or not.

On the other hand, since 2014 the number of reviews has been decreasing. There should be more emphasis on generating more reviews (since their feedback helps improve the game proposal).

![](/Processed_Data/Images/ReviewsbyYear.png)

[**Instructions Video**](https://www.youtube.com/watch?v=i5LjFiq1ah4)


# Analisis Steam (versión en español)

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
- UserForGenre (_ingresar género_): Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
- UsersRecommend (_ingresar año_): Devuelve el top 3 de juegos más recomendados por usuarios para el año dado.
- UsersNotRecommend (_ingresar año_): Devuelve el top 3 de juegos menos recomendados por usuarios para el año dado. 
- sentiment_analysis (_ingresar año_): Devuelve una lista con la cantidad de registros de reseñas de usuarios según un análisis de sentimiento para el año ingresado.
- recomendacion_juego (_ingresar id de producto_): Devuelve una lista con 5 juegos recomendados similares al producto ingresado.

## Resultados

Los resultados de las funciones pueden obtenerse de la siguiente [**App**](https://analisis-steam.onrender.com/docs)

## Análisis exploratorio de datos

Realizando iun análisis de los datos clasificados por género, se concluye que los dos géneros más jugados, y que más facturación aportan son Action y Adventure. Por otro lado, el género que más juegos tiene es Indie. Steam debería invertir más en los juegos de las dos primeras categorías.
![](/Datos_procesados/Imagenes/RevenuesbyGenre.png)
![](/Datos_procesados/Imagenes/PlayersbyGenre.png)
![](/Datos_procesados/Imagenes/GamesbyGenre.png)

Existen también 2.823 juegos con una facturación total menor a 100 dólares. Quizás sea conveniente evaluar su permanencia.

Por otro lado, puede observarse que desde el año 2014 la cantidad de reviews viene bajando. Debería insitirse más en generar más reviews (pues su feedback ayuda a mejorar la propuesta de juegos).

![](/Datos_procesados/Imagenes/ReviewsbyYear.png)

[**Video Explicativo**](https://www.youtube.com/watch?v=i5LjFiq1ah4)