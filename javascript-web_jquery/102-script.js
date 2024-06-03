// Script fetches and prints how to say “Hello” depending on the language

let url = 'https://www.fourtonfish.com/hellosalut/?lang=';
$('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').text();
    $.get(url,  + lang, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
   });
