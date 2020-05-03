import pyrebase
config = {
    "apiKey": "AIzaSyDLZMgt8t6na99i3dYPIF4qK2XoFvisUWY",
    "authDomain": "eattendance-31dca.firebaseapp.com ",
    "databaseURL": "https://eattendance-31dca.firebaseio.com/",
    "projectId": "eattendance-31dca",
    "storageBucket": "eattendance-31dca.appspot.com",
    "serviceAccount": "eattendance-31dca-firebase-adminsdk-lmng9-dea083f54e.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
# user0 = auth.create_user_with_email_and_password('sadiannasir@gmail.com','123qwe123qwe')
user = auth.sign_in_with_email_and_password('sadiannasir@gmail.com', '123qwe123qwe') 
data = {
  'Countries': 'CAMEROON'
}


 # Pass the user's idToken to the push method
results = db.child("eAttendance").set(data, user['idToken'])
# result = db.child("eAttendance").get()

# print(result.val())