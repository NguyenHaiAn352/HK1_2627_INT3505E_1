from flask import Flask, jsonify, make_response, request
import datetime

app = Flask(__name__)

tasks = {
    "1": {
        "id": 1,
        "title": "consult with stakeholders.",
        "status": "done",
        "priority": "high",
        "dueDate": str(datetime.datetime(month=5, day=23))
    },
    "2": {
        "id": 2,
        "title": "design system architecture.",
        "status": "open",
        "priority": "normal",
        "dueDate": str(datetime.datetime(month=6, day=23))
    }
}

def error_response(type_, title, status, detail, instance):
    body = {
        "type": type_,
        "title": title,
        "status": status,
        "detail": detail or None,
        "instance": instance or None
    }

    response = make_response(jsonify(body))
    response.status_code = status
    response.headers["Content-Type"] = "application/problem+json"
    return response

@app.route("/tasks")
def getTasks():
    return make_response(jsonify(tasks)), 200

@app.route("/tasks", methods=["POST"])
def addTask():
    if not request.is_json:
        return error_response("/bad-request", "Bad Request", 400, "Invalid request format.", "/tasks")
    inp = request.get_json(force=True)
    if not inp or "id" not in inp or "title" not in "inp":
        return error_response("/unprocessable-content", "Unprocessable Content", 422, "Unparsable request content.", "/tasks")
    if inp["id"] in tasks:
        return error_response("/conflict", "Conflict", 409, "Entry already exists", "/tasks")
    tasks[inp["id"]] = inp
    return make_response(jsonify(inp)), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)