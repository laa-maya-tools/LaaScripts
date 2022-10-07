# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
#
# cred = credentials.Certificate("Src/_Credentials/laascripts_firebase_key.json")
# firebase_admin.initialize_app(cred)
#
# db = firestore.client()
#
# db.collection('users').add({'login': 'login', 'password': 'password'})

from firebase import firebase
fb = firebase.FirebaseApplication("https://laascripts-default-rtdb.europe-west1.firebasedatabase.app/", None)

users = {
    'login': 'miguel.garde@helloanima.com',
    'password': 'miguel.garde'
}
#
# result = fb.post('/users', users)
read = fb.get('/users', '')
print(read)

# read = fb.put('/tutorial/datos/-NDj5D4MCtlAsKy1zdH4', 'login', 'login_new')
# print(read)
