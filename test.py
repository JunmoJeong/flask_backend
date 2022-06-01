from flask import Flask
app = Flask(__name__)


@app.route("/hello")
def abc():
    return "<h1>Hello World!</h1>"
