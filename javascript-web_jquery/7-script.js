// Script fetches the character name from the URL given
// The name must be displayed in the HTML tag DIV#character

let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, txtstatus) {
  $('div#character').text(data.name);
});
