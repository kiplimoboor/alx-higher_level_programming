$('document').ready(() => {
  const myList = $('.my_list');
  $('#add_item').on('click', () => {
    myList.append('<li>Item</li>');
  });
  $('#remove_item').on('click', () => {
    myList.children('li:last').remove();
  });
  $('#clear_list').on('click', () => {
    myList.empty();
  });
});
