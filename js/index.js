$(document).ready(function () {
    for (let i = 0; i < 50;i++) {
        $('#videos_here').append('<div class="ui divided items">' + 
        '<div class="item">' + 
            '<div class="image">' + 
            '<img src="/images/wireframe/image.png">' +
            '</div>' + 
            '<div class="content">' + 
            '<div class="header">Title 1</div>' +
            '<div class="meta">' +
                '<span class="cinema">Views 1</span>' +
            '</div>' +
            '<div class="description">' +
                '<p>Description 1</p>' +
            '</div>' +
            '<div class="extra">' +
                '<div class="ui label">Likes 1</div>' +
                '<div class="ui label">Dislikes 1</div>' +
                '<div class="ui right floated primary button">' +
                'Watch Video' +
                '<i class="right chevron icon"></i>' +
                '</div>' +
            '</div>' +
            '<div class="ui label">' +
            '<img class="ui right spaced avatar image" src="/images/avatar/small/elliot.jpg">' +
            'Channel Name' +
            '</div>' +
            '</div>' +
        '</div>')
    }
});