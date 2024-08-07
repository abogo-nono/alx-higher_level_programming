#!/usr/bin/node

$(document).ready(function () {
    $(document).ready(function () {
        $('DIV#update_header').click(function (e) {
            e.preventDefault();
            $('header').text('New Header!!!');
        });
    });
});

