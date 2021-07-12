<?php include("header.php"); ?>
<!DOCTYPE html>
<html>
<head>
    <title> Home </title>
</head>
<body>

<section class="top-section">
    <div class="container">
        <h1>Trending Videos</h1>
        <!-- <button class="ui right floated black button">Black</button> -->
        <button id="scrape_btn" class="ui right floated green button">Scrape</button>
        <div id="videos_here"> </div>
    </div>
</section>
<?php include("script.php"); ?>
<script src="js/index.js"></script>
</body>
</html>