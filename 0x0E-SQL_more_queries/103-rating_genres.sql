-- Rate Genres
   SELECT name,
          sum(rate) as rating
     FROM tv_genres
LEFT JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows
       ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_show_ratings
       ON tv_shows.id = tv_show_ratings.show_id
 GROUP BY name
 ORDER BY rating DESC;