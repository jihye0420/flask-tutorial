from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, Sungshinasdfasdfasdf!"

@app.route("/hello")
def hello_world2():
    return "Hello, Sungshin2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
