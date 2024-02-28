$(document).ready(function () {
  $.get({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (french) => {
      $('#hello').text(french.hello);
    }
  });
});
