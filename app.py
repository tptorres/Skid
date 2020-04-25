import json
from collections import OrderedDict
from flask import Flask, jsonify, request
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# Helper functions for routes


def get_employees():
    with open('employees.json', 'r') as f:
        data = json.load(f)
        return data


def get_employee(eid):
    with open('employees.json', 'r') as f:
        data = json.load(f)
        res = [emp for emp in data if emp["EID"] == int(eid)]
        return res[0]

# @info Gets all of the employees
# @access Public
@app.route('/api/v1/employees', methods=['GET'])
def get_all_employees():
    return jsonify(get_employees())

# @info Grabs one employee's information
# @access Public
@app.route('/api/v1/employees/<EID>')
def get_single_employee(EID):
    return jsonify(get_employee(EID))


# @info Gets all employees from a specific department
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
