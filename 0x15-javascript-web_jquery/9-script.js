// Script fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello fetched from HTML tag DIV#hello

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data, stat) {
  $(DIV#hello).text(data.hello);
});
