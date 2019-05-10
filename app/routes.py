from app import app, db
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/login-session", methods=["POST","DELETE"])
def login_session():
    if request.method == "POST":
        pass # perform login
    elif request.method == "DELETE":
        pass # user logout


@app.route("/user", methods=["POST", "DELETE"])
def user_handler():
    if request.method == "POST":
        pass # create user
    elif request.method == "DELETE":
        pass # delete user



@app.route("/provider", methods=["POST", "DELETE"])
def provider_handler():
    if request.method == "POST":
        content = request.get_json()
        db.create_provider(content["providername"],
                    content["email"], content["password"])
    elif request.method == "DELETE":
        content = request.get_json()
        db.remove_provider(content["providername"])
    return "DONE"

@app.route("/request", methods=["POST"])
def request_handler():
    if request.method == "POST":
        content = request.get_json()
        db.create_request(content["providername"],content["type"],content["description"], 
            content["fields"], content["success"],content["failure"], content["username"])
        return "REQUEST CREATED"

@app.route("/request-status/<username>/<id>")
def status_handler(username, id):
    status = db.get_request_status(username, id)
    return {
        "status" : status
    }