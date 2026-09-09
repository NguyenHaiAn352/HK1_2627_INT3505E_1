from flask import Flask
app = Flask(__name__)
@app.route("/")
# When someone visits the root of the site, run index(); can define multiple routes.
def index():
    return {"message": "Hello, API!"}
# This is written so that when the file is executed directly from the terminal, a new server under http://127.0.0.1:5000/ is created
# If the app is ran as a module (__name__ = app), this block won't be executed, but Flask will still be able to see
# all routes and configurations attached to the app.
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)