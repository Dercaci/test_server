from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def say_hello():
    return jsonify({'msg': 'Hello'})


if __name__ == "__main__":
    app.run(debug=True)