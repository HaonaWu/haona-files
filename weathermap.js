var map;
var moodys = ol.proj.fromLonLat([-74.012,40.713428])
var homeView = new ol.View({
  center: moodys,
  zoom: 6
});

function movesToCountry() {
  var countryName = document.getElementById("country name").value;
  console.log(document);
  console.log(document.getElementById("country name"));
  console.log(document.getElementById("country name").value);

  if (countryName === "") {
    panHome();
    return;
  }

}

function panHome() {
  homeView.animate({

    center: moodys,
    duration: 2000
    });
}

function init() {
  map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        LoadTilesWhileAnimating: true,
        view: homeView,
      });
}

window.onload = init;
