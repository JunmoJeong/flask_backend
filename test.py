from flask import Flask
app = Flask(__name__)


@app.route("/hello")
def abc():
    return "<h1>Hello World!</h1>"


host_addr = "127.0.0.1"
port_num = "8080"

if __name__ == "__main__":
    app.run(host=host_addr, port=port_num, debug=True)
