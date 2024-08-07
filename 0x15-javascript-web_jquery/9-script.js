#!/usr/bin/node
$(document).ready(function () {
    $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr",
        function (data, helloStatus, jqXHR) {
            $('DIV#hello').append(data['hello']);
        }
    );
});
