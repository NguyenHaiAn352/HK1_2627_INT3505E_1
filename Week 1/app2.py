from flask import Flask, jsonify, request
from uuid import uuid4
app = Flask(__name__)
students_array = []

@app.route("/student", methods=["POST"])
def student():
    body = request.get_json(silent=True) or {}
    name = body.get("name")
    gpa = body.get("gpa", 0.0)
    if not name:
        return jsonify({"Error":"A name is required!"})
    student = {
        "name": name,
        "id": str(uuid4),
        "gpa": gpa
    }
    students_array.append(student)
    return student, 201

if __name__ == "__main__":
    app.run(debug=True)