from flask import Flask
app = Flask(__name__)

print(__name__)


@app.route("/")  # Python Decorator - gives additional functionality to functions
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "bye"

if __name__ == "__main__":
    app.run()



