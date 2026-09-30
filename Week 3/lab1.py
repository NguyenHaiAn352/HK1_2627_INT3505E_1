from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

# Post chưa được định nghĩa trước
@app.route('/posts', methods=['GET'])
def get_posts():
    user_id = request.args.get('user_id')
    query = Post.query
    if user_id:
        query = query.filter_by(user_id=user_id)
    posts = query.all()
    return jsonify([post.to_dict() for post in posts])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)