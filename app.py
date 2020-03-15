from flask import Flask
from flask import render_template

app = Flask(__name__)

strs = "gh"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080", debug=True)
