$('document').ready(() => {
  $('#btn_translate').on('click', () => {
    const lang = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      success: (translated) => {
        $('#hello').text(translated.hello);
      }
    });
  });
});
