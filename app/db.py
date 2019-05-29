import pyrebase

config = {
  "apiKey": "AIzaSyAc9SAym94EeJbciccRESpgNm4WISzl-GM",
  "authDomain": "easykey-53a02.firebaseapp.com",
  "databaseURL": "https://easykey-53a02.firebaseio.com",
  "storageBucket": "easykey-53a02.appspot.com"
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

def get_user(username):
    return db.child("users").child(username).get().val()

def create_provider(providername, email, password):
    db.child("providers").child(providername).set({
        "email" : email,
        "password" : password,
    })

def get_provider_key(providername):
    return db.child("providers").child(providername).child("password").get().val()


def remove_provider(providername):
    db.child("providers").child(providername).remove()


def get_requests(username):
    req = db.child("requests").child(username).get()
    return req.val() 

def get_request_status(username, id):
    req = db.child("requests").child(username).child(id).child("status").get()
    return req.val()

def get_request_fields(username, id):
    req = db.child("requests").child(username).child(id).child("fields").get()
    return req.val()

def create_request(provider, request_type, request_description, fields, success, failure, username):
    a = db.child("requests").child(username).push({
        "provider" : provider,
        "type" : request_type,
        "description" : request_description,
        "fields" : fields,
        "success" : success,
        "failure" : failure,
        "status" : "none"
    })
    return a["name"]

if __name__=="__main__":
    create_request("provider", "request_type", "request_description", "fields", "success", "failure", "abhinav")
    
