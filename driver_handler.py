
import json
import random
from flask import Flask, jsonify, render_template, request
import src.driver as drvr


app = Flask(__name__)

names = ["James", "Patricia", "Robert",	"Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
         "Raj", "Ayush", "Himanshu", "Shreya", "Sumit", "Akash", "Deepak", "Harman", "Aanya", "Amayra", "Ananya"]

drivers = []


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


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8001", debug=True)
