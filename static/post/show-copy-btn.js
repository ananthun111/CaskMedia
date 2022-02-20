var $ = django.jQuery;

$(document).ready(function() {
    var myButton = '<button>Copy</button>';
    $(myButton).insertAfter($('#id_title'));
});