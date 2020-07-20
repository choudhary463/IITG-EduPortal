import pyrebase
config = {
    "apiKey": "AIzaSyAEue4ktaLv-1wqKQgtgkfWJ1Oj6NNW-8U",
    "authDomain": "e-learning-ccbd8.firebaseapp.com",
    "databaseURL": "https://e-learning-ccbd8.firebaseio.com",
    "projectId": "e-learning-ccbd8",
    "storageBucket": "e-learning-ccbd8.appspot.com",
    "messagingSenderId": "1053587965345",
    "appId": "1:1053587965345:web:b97bb311c911183b0d77e0",
    "measurementId": "G-K1YGG2H5VQ"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def currentUser(request):
    try:
        idtoken = request.session['uid'] 
        info = authe.get_account_info(idtoken)
        users = info['users']
        user = users[0]
        localid = user['localId']
        user1 = database.child("users").child(localid).get().val()
        return user1
    except:
        return None
        

def user_authenticated(request):
    if(currentUser(request) is None):
        return False
    else:
        return True