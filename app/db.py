import pyrebase

config = {
  "apiKey": "AIzaSyDsoYLse6FrkbClDm-C0BoLg_m7U0yyBps",
  "authDomain": "easykey-160212.firebaseapp.com",
  "databaseURL": "https://easykey-160212.firebaseio.com",
  "storageBucket": "easykey-160212.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def create_user(username, email, password):
    db.child("users").child(username).set({
        "email" : email,
        "password" : password
    })

def remove_user(username):
    db.child("users").child(username).remove()


def create_provider(providername, email, password):
    db.child("providers").child(providername).set({
        "email" : email,
        "password" : password
    })

def remove_provider(providername):
    db.child("providers").child(providername).remove()


def get_requests(username):
    req = db.child("requests").child(username).get()
    return req.val() 


def create_request(provider, request_type, request_description, fields, success, failure, username):
    db.child("requests").child(username).push({
        "provider" : provider,
        "type" : request_type,
        "description" : request_description,
        "fields" : ",".join(fields),
        "success" : success,
        "failure" : failure,
        "status" : "none"
    })