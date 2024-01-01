# Flask is the server that will run my API

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Nunya Business",
        "email": "nunyabusiness@example.com"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

'''
I can access my API endpoint at http://127.0.0.1:5000/get-user/123 (replace 123 with any user ID).
Furthermore, to test the 'extra' parameter, I can use the URL like: 
http://127.0.0.1:5000/get-user/123?extra=some_data.
'''


if __name__ == "__main__":
    app.run(debug=True)
