-- lists all genres and displays the number of shows linked to each.
    SELECT name, COUNT(genre_id) AS number_of_shows
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_show_genres.genre_id = tv_genres.id
  GROUP BY genre_id
  ORDER BY number_of_shows DESC;