from flask import Flask
import random
app = Flask(__name__)


@app.route("/")  # Python Decorator - gives additional functionality to functions
def main_page():
    return '<h1>Guess a number between 0 to 9</h1>' \
            '<img scr="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


random_num = random.randint(0, 9)

@app.route("/<int:number>")
def guess(number):
    if random_num > number:
        return '<h1 color="red">It is too low....TRY AGAIN.</h1>'
    if random_num < number:
        return '<h1 color="blue">It is too high....FLY DOWN</h1>'
    if random_num == number:
        return '<h1 color="green">YOU GOT IT CORRECT!!</h1>'

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)