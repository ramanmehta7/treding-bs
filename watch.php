<?php include("header.php"); ?>
<!DOCTYPE html>
<html>
<head>
    <title> Watch Video </title>
</head>
<body>

<section class="top-section">
    <div class="container">
        <h1>Title</h1>
        <div class="row">
            <div class=col-md-6>
                <iframe width="560" height="315" src="https://www.youtube.com/embed/F4neLJQC1_E?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class=col-md-6>
                <!-- Hi! This is the really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really really big description of this great video which was once trending!! -->
                <button id="desc" class="ui blue button huge">Description</button>
                <br>
                <br>

                <div class="extra">
                    <div class="ui image label massive">
                    <img src="/images/avatar/small/joe.jpg">
                    Channel Name
                    </div>
                    <div class="ui label huge">Subcribers 12,546,542</div>
                </div>
            </div>
        </div>
        <br>
        <div class="ui label huge">Likes 100,518,453</div>
        <div class="ui label huge">Dislikes 21,563</div>
    </div>
</section>


<div class="ui modal">
  <i class="close icon"></i>
  <div class="header">
    Profile Picture
  </div>
  <div class="image content">
    <div class="ui medium image">
      <img src="/images/avatar/large/chris.jpg">
    </div>
    <div class="description">
      <div class="ui header">We've auto-chosen a profile image for you.</div>
      <p>We've grabbed the following image from the <a href="https://www.gravatar.com" target="_blank">gravatar</a> image associated with your registered e-mail address.</p>
      <p>Is it okay to use this photo?</p>
    </div>
  </div>
  <div class="actions">
    <div class="ui black deny button">
      Nope
    </div>
    <div class="ui positive right labeled icon button">
      Yep, that's me
      <i class="checkmark icon"></i>
    </div>
  </div>
</div>



<?php include("script.php"); ?>
<script src="js/watch.js"></script>
</body>
</html>