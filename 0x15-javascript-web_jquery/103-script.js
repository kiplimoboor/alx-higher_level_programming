$('document').ready(() => {
  function translate () {
    const lang = $('#language_code').val();
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      success: (translated) => {
        $('#hello').text(translated.hello);
      }
    });
  }
  $('#btn_translate').on('click', () => {
    translate();
  });
  $('#language_code').keypress((e) => {
    const key = e.which;
    if (key === 13) {
      translate();
    }
  });
});
