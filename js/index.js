$(document).ready(function getVideosList(){

    let uri = window.location.protocol + "//" + window.location.hostname + ":3000/listvideos";
    $.ajax({
        url: uri,
        type: 'GET',
        async: false,
        "success": function (data) {
            populateVideoList(data);
        },
        "error": function (XMLHttpRequest) {
            console.log(XMLHttpRequest.status);
        },
    });
});

function populateVideoList(data) {
    for (let i = 0; i < data["videos"].length;i++) {
        let video_url = "'"+ data["videos"][i]["url"] + "'";

        $('#videos_here').append('<div class="ui divided items">' + 
        '<div class="item">' + 
            '<div class="image">' + 
            '<img src="' + 
            'https://i.ytimg.com/vi/T54LOlTFDD0/maxresdefault.jpg' + 
            '">' +
            '</div>' + 
            '<div class="content">' + 
            '<div class="header">' + 
                data["videos"][i]["title"] + 
            '</div>' +
            '<div class="meta">' +
                '<span class="cinema">' + 
                    data["videos"][i]["views"] + 
                '</span>' +
            '</div>' +
            '<div class="subscription">' +
                '<p>' + 
                    data["videos"][i]["subscribers"] + 
                '</p>' +
            '</div>' +
            '<div class="extra">' +
                '<div class="ui label">' + 
                    data["videos"][i]["likes"] + 
                '</div>' +
                '<div class="ui label">' + 
                    data["videos"][i]["dislikes"] + 
                '</div>' +
                '<div class="ui right floated primary button">' +
                '<a onclick="getVideoDetails(' + video_url + ')">' +
                        'Watch Video' +
                        '<i class="right chevron icon"></i>' + 
                    '</a>' +
                '</div>' +
            '</div>' +
            '<div class="ui label">' +
            '<img class="ui right spaced avatar image" ' + 
                'src="' + 
                    data["videos"][i]["channel_thumbnail"] +
                '">' +
                    data["videos"][i]["channel_name"] +
            '</div>' +
            '</div>' +
        '</div>')
    }
}

function getVideoDetails(video_url) {
    window.location.href = "watch.php?url=" + encodeURIComponent(video_url);
}

$('#scrape_btn').click(function() {
    $('#scrape_btn').addClass('loading');

    let uri = window.location.protocol + "//" + window.location.hostname + ":3000/runScript";
    $.ajax({
        url: uri,
        type: 'GET',
        async: false,
        "success": function (data) {
            console.log(data);
            $('#scrape_btn').removeClass('loading');
        },
        "error": function (XMLHttpRequest) {
            console.log(XMLHttpRequest.status);
            $('#scrape_btn').removeClass('loading');
        },
    });
});