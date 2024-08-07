#!/usr/bin/node
$(document).ready(function () {
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json",
        function (data, titlesStatus, jqXHR) {
            data['results'].forEach(movie => {
                $('UL#list_movies').append(`<li>${movie['title']}</li>`);
            });
        }
    );
});
