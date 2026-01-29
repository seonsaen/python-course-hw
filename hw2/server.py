from flask import Flask, jsonify, request
from dotenv import dotenv_values
from controllers import operation

app = Flask(__name__)


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config and config["PORT"]:
        return int(config["PORT"])
    return 5000


@app.route("/")
def server_info():
    return "My server"


@app.route("/author")
def author():
    author_info = {
        "name": "Aytal",
        "course": 2,
        "age": 19,
    }
    return jsonify(author_info)


@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    result = operation(a, b)

    return jsonify({'sum': result})


if __name__ == "__main__":
    app.run(debug=True, port=get_port())