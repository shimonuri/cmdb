from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    print("main")
    return "Welcome!"


@app.route("/how are you")
def hello():
    print("hello")
    return "I am good, how about you?"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
