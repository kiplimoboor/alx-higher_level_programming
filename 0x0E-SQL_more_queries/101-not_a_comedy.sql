-- Not Comedy
SELECT title
FROM tv_shows
WHERE title NOT IN
    (
        SELECT title 
        FROM tv_genres 
        LEFT JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
        RIGHT JOIN tv_shows
        ON tv_shows.id = tv_show_genres.show_id
        WHERE NAME = 'Comedy'
    )
ORDER BY title;