import json
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/api/v1')
def hello():
    return "<h1>Welcome to the Skid API</h1>"


@app.route('/api/v1/test')
# @info Gets a random number of employees
# @access Public
@app.route('/api/v1/employees', methods=['GET'])
def get_all_employees():
    data = get_employees()
    return jsonify(data)


def get_employees():
    with open('employees.json', 'r') as f:
        data = json.load(f)
        return data

# @info Gets a random number of employees from a specific department
# @access Public
@app.route("/api/v1/employees/department", methods=['GET'])
def get_department_employees():
    if 'name' in request.args:
        department = request.args['name']
    else:
        return "Error: No department was specified"

    res = []
    data = get_employees()

    for employee in data:
        if employee['department'] == department:
            res.append(employee)

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)  # similar to nodemon, allows automatic server restart
