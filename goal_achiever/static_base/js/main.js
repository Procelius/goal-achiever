$(document).ready(function() {
  $('.container.switch').on('click', function(e) {
    var $goalForm = $(this).find('div.accordion');
    if ($goalForm.css('height') == '0px') {
      $goalForm.css('height', 'auto');
    } else if (e.target.className == 'cancel') {
      $goalForm.css('height', '0');
    }
  });
});
