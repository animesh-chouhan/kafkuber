mapboxgl.accessToken = ""; // add the mapbox token here

var map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/dark-v10",
    center: [77.5946, 12.9716], // starting position [lng, lat]
    zoom: 12 //starting zoom
});

map.on("load", function() {
    var marker = new mapboxgl.Marker({ draggable: true }).setLngLat([77.59, 12.97]).addTo(map);

    function onDragEnd() {
        var lngLat = marker.getLngLat();
        coordinates.style.display = "block";
        coordinates.innerHTML = "Longitude: " + lngLat.lng + "<br />Latitude: " + lngLat.lat;
    }

    marker.on("dragend", onDragEnd);
});
