from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

posts = []

@app.route('/users/<int:user_id>/posts', methods=['GET'])
def get_posts(user_id):
    # Filter posts by user_id
    user_posts = [post for post in posts if post["user_id"] == user_id]
    return jsonify(user_posts)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)