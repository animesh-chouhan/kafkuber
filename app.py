
import json
import random
import src.rider as rdr
import src.driver as drvr
from geopy.distance import geodesic
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

names = ["James", "Patricia", "Robert",	"Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
         "Raj", "Ayush", "Himanshu", "Shreya", "Sumit", "Akash", "Deepak", "Harman", "Aanya", "Amayra", "Ananya"]

drivers = []
riders = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/spawndriver", methods=["POST"])
def spawn_driver():
    if request.is_json:
        data = request.get_json()
        if data["driver_id"] not in [driver.driver_id for driver in drivers]:
            driver = drvr.Driver(data["driver_id"], random.choice(names),
                                 data["assigned"], data["assigned_to"], data["lat"], data["lng"])
            drivers.append(driver)
            return driver.__repr__()

        else:
            return json.dumps({"error": "This driver id is taken. Please reload the server."})


@app.route("/spawnrider", methods=["POST"])
def spawn_rider():
    if request.is_json:
        data = request.get_json()
        if data["rider_id"] not in [rider.rider_id for rider in riders]:
            rider = rdr.Rider(data["rider_id"], random.choice(names),
                              data["assigned"], data["assigned_to"], data["lat"], data["lng"])
            riders.append(rider)
            return rider.__repr__()
        else:
            return json.dumps({"error": "This rider id is taken."})


@app.route("/matchmaker", methods=["GET"])
def match_maker():
    for driver in drivers:
        if driver.driver_assigned == False:
            min_dist = float("inf")
            min_rider_id = None
            for rider in riders:
                if rider.rider_assigned == False:
                    dist = geodesic((driver.driver_latitude, driver.driver_longitude),
                                    (rider.rider_latitude, rider.rider_longitude)).miles
                    if dist < min_dist:
                        min_dist = dist
                        min_rider_id = rider.rider_id

            if min_rider_id != None:
                driver.driver_assigned = True
                driver.driver_assigned_to = min_rider_id

    return json.dumps([driver.__repr__() for driver in drivers])


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8000", debug=True)
