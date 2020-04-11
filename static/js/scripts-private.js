mapboxgl.accessToken = "pk.eyJ1IjoiYW5pbWVzaHNpbmdoIiwiYSI6ImNrN3FlY3hxaDAyeXgzZ3FwczNlNzhqNGoifQ.PlxnBSZe9KlvABtyshEMtw";

const drivers = [];
const riders = [];

class Driver {
    constructor(lat, lng) {
        this.driver_id = "d" + (drivers.length + 1001).toString();
        this.lat = lat;
        this.lng = lng;
        this.assigned = false;
        this.assigned_to = null;
    }
}

class Rider {
    constructor(lat, lng) {
        this.rider_id = "r" + (riders.length + 2001).toString();
        this.lat = lat;
        this.lng = lng;
        this.assigned = false;
        this.assigned_to = null;
    }
}

// Add card template
function addCard(topic, content, section, id) {
    let div = document.createElement("div");
    div.className = "card";
    div.id = id;
    div.innerHTML = "<h3>" + topic + "</h3>" + "<p>" + content + "</p>";
    document.getElementsByClassName(section)[0].append(div);
}

// Map instance
var map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: [77.5946, 12.9716], // starting position [lng, lat]
    zoom: 12 //starting zoom
});

map.on("load", function() {
    // Spawn Driver
    $(".spawn-driver").click(function() {
        var marker = new mapboxgl.Marker({ draggable: true }).setLngLat(map.getCenter()).addTo(map);

        function onDragEnd() {
            lngLat = marker.getLngLat();
            coordinates.style.display = "block";
            coordinates.innerHTML = "Longitude: " + lngLat.lng + "<br />Latitude: " + lngLat.lat;

            // Marker for each driver
            var el = document.createElement("div");
            el.className = "driver-icon";
            new mapboxgl.Marker(el).setLngLat(lngLat).addTo(map);

            var driver = new Driver(lngLat.lat, lngLat.lng);
            drivers.push(driver);

            var posting = $.ajax({
                url: "spawndriver",
                type: "POST",
                data: JSON.stringify(driver),
                dataType: "json",
                contentType: "application/json; charset=utf-8"
            });

            // Update info on the screen
            posting.done(function(recv_data) {
                if (recv_data["error"] == null) {
                    // Add card for each driver
                    addCard(recv_data["driver_name"], JSON.stringify(recv_data), "drivers", recv_data["driver_id"]);
                } else {
                    alert(recv_data["error"]);
                }
            });
            marker.remove();
        }

        marker.on("dragend", onDragEnd);
    });

    // Spawn Rider
    $(".spawn-rider").click(function() {
        var marker = new mapboxgl.Marker({ draggable: true }).setLngLat(map.getCenter()).addTo(map);

        function onDragEnd() {
            lngLat = marker.getLngLat();
            coordinates.style.display = "block";
            coordinates.innerHTML = "Longitude: " + lngLat.lng + "<br />Latitude: " + lngLat.lat;

            // Marker for each rider
            var el = document.createElement("div");
            el.className = "rider-icon";
            new mapboxgl.Marker(el).setLngLat(lngLat).addTo(map);

            var rider = new Rider(lngLat.lat, lngLat.lng);
            riders.push(rider);

            var posting = $.ajax({
                url: "spawnrider",
                type: "POST",
                data: JSON.stringify(rider),
                dataType: "json",
                contentType: "application/json; charset=utf-8"
            });

            posting.done(function(recv_data) {
                if (recv_data["error"] == null) {
                    // Add card for each driver
                    addCard(recv_data["rider_name"], JSON.stringify(recv_data), "riders", recv_data["rider_id"]);
                } else {
                    alert(recv_data["error"]);
                }
            });
            marker.remove();
        }

        marker.on("dragend", onDragEnd);
    });

    setInterval(function() {
        $.get("matchmaker", function(data) {
            alert(data);
        });
    }, 10000);

    // Docs: https://github.com/mapbox/mapbox-gl-directions/blob/master/API.md
    var directions = new MapboxDirections({
        accessToken: mapboxgl.accessToken,
        unit: "metric",
        profile: "mapbox/driving",
        interactive: false,
        flyTo: false,
        controls: { inputs: true, instructions: false, profileSwitcher: false }
    });

    directions.setOrigin([77.55039, 12.964825]);
    directions.setDestination([77.647557, 12.9455864]);
    map.addControl(directions, "top-right");
});
