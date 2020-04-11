
import json
import random
from flask import Flask, jsonify, render_template, request
import src.rider as rdr


app = Flask(__name__)

names = ["James", "Patricia", "Robert",	"Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara",
         "Raj", "Ayush", "Himanshu", "Shreya", "Sumit", "Akash", "Deepak", "Harman", "Aanya", "Amayra", "Ananya"]

riders = []


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


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8002", debug=True)
