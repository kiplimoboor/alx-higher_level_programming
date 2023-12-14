-- list genres for a show
   SELECT name
     FROM tv_genres
LEFT JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows
       ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_show_genres.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')