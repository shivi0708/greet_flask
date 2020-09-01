from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!!"

# new route added

@app.route("/david")
def david():
    return "HEllo David!!"

# a route for any name

@app.route("/<string:name>")
def hello(name):
    name=name.capitalize()
    return f"Hello there, {name}"
