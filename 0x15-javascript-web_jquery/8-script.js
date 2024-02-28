const listMovies = $('#list_movies');

$.get({
  url: 'https://swapi-api.alx-tools.com/api/films/?',
  success: function (response) {
    const movies = response.results;
    $.each(movies, (_i, movie) => {
      listMovies.append(`<li>${movie.title}</li>`);
    });
  }
}
);
