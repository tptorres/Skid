import json
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    return "Hello " + name


@app.route('/api/v1/employees')
def api_all():
    with open("test.json", "r") as f:
        data = json.load(f)
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)  # similar to nodemon, allows automatic server restart
