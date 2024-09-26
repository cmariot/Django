async function jquery_get_replace(url, id) {
  await $.get(url, function (data) {
    $(id).replaceWith(data);
  });
}
