function jquery_get_replace(url, id) {
  $.get(url, function (data) {
    $(id).replaceWith(data);
  });
}
