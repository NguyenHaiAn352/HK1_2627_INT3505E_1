from flask import Flask, jsonify, request
app = Flask(__name__)
# Check if the server is still alive
@app.route("/connect", methods=["GET"])
def connect():
    return jsonify({"status":"ok"}), 200
# Return to the client what the client sent - echoing
@app.route("/echo", methods=["POST"])
# Single quote the data, escape double quote to treat them as characters within the data
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({"What were sent": data}), 200
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)