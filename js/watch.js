$(document).ready(function () {

    function getVideoDetailsData() {
        let link = window.location.href;
        var parameter = new URL(link);
        var url = parameter.searchParams.get("url");
        let uri = window.location.protocol + "//" + window.location.hostname + ":3000/details/" + encodeURIComponent(url);
        $.ajax({
            url: uri,
            type: 'GET',
            "success": function (data) {
                populateIndividualVideo(data);
            },
            "error": function (XMLHttpRequest) {
                console.log(XMLHttpRequest.status);
            },
        });
    }
    getVideoDetailsData();
    
    function populateIndividualVideo(data) {
        let title = data["details"][0]["title"];
        let description = data["details"][0]["description"];
        let likes = data["details"][0]["likes"] + " likes";
        let dislikes = data["details"][0]["dislikes"] + " dislikes";
        let subscribers = data["details"][0]["subscribers"];
        let views = data["details"][0]["views"];
        let channel_name = data["details"][0]["channel_name"]
        let channel_thumbnail = data["details"][0]["channel_thumbnail"];

        $('#title').text(title);
        $('#video_desc').text(description);
        $('#likes_count').text(likes);
        $('#dislikes_count').text(dislikes);
        $('#views').text(views);
        $('#channel_name').text(channel_name);
        $('#Subs_count').text(subscribers);
        $('#channel_thumbnail').attr('src', channel_thumbnail);
        
        let yt_url = data["details"][0]["url"] + "?autoplay=1";
        yt_url = yt_url.replace("watch?v=", "embed/");
        $('#YT-Player').attr('src', yt_url);
    }

    $('#desc').click(function() {
        $('.ui.modal').modal('show');
    });
});