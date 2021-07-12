<?php include("header.php"); ?>
<!DOCTYPE html>
<html>
<head>
    <title> Watch Video </title>
</head>
<body>

<section class="top-section">
    <div class="container">
        <h1 id="title"></h1>
        <div class="row">
            <div class=col-md-6>
                <iframe id="YT-Player" width="560" height="315" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class=col-md-6>
                <button id="desc" class="ui blue button huge">Description</button>
                <br>
                <br>

                <div class="extra">
                    <div class="ui image label massive">
                    <img id="channel_thumbnail" src="">
                    <span id="channel_name"></span>
                    </div>
                    <div id="Subs_count" class="ui label huge"></div>
                </div>
            </div>
        </div>
        <br>
        <div id="likes_count" class="ui label huge"></div>
        <div id="dislikes_count" class="ui label huge"></div>
        <div id="views" class="ui label huge"></div>
    </div>
</section>


<div class="ui modal">
  <i class="close icon"></i>
  <div class="header">
    <h1 style="margin-top: 3%;"><i class="hand point right icon"></i>&nbsp;Video Description</h1>
  </div>
  
  <div class="container">
        <p id="video_desc" style="font-size: 1.4em;"></p>
    </div>
</div>



<?php include("script.php"); ?>
<script src="js/index.js"></script>
<script src="js/watch.js"></script>
</body>
</html>