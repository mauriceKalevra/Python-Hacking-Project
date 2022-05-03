// Slideshow starts after all images are loaded.
$(window).on("load", function () {
  // List all images that shall be used as background images.
  var background_images = [
    "pic1.jpg",
    "pic2.jpg",
    "pic4.jpg"
  ]

  // Add path "img/background-images/" to every image name to store the path.
  var path_to_background_images = "img/background-images/";
  var nrOfBackgroundImages = background_images.length
  var imgList = new Array()

  for (var i = 0; i < nrOfBackgroundImages; i++) {
    var tmp = background_images[i];
    background_images[i] = path_to_background_images + tmp;
    imgList[i] = new Image();
    imgList[i].src = background_images[i];
  }

  // Every X miliseconds change the background image.
  var X = 4000
  backgroundImageIdx = 0;
  window.setInterval(function () {
    $(".jumbotron").css("background-image", "url(" + imgList[backgroundImageIdx].src + ")");
    backgroundImageIdx++;
    if (backgroundImageIdx >= nrOfBackgroundImages) {
      backgroundImageIdx = 0;
    }
  }, X);
});
