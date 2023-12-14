-- lists all genres and displays the number of shows linked to each
    SELECT tv_genres.name as genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
      FROM tv_genres
RIGHT JOIN tv_show_genres
        ON tv_show_genres.genre_id = tv_genres.id
  GROUP BY genre_id
  ORDER BY number_of_shows DESC;