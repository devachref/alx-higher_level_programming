//Script fetches and lists the title for all movies by using given URL
//All movie titles must be list in the HTML tag UL#list_movies

let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';$.get(url, function (data) {
  let films = data.results;
  for (let film of films) {
    $('ul#list_movies').append(`<li>{film.title}</li>`);
    }
  });
