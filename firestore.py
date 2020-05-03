import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import storage
from firebase_admin.firestore import client





# Use the application default credentials
cred = credentials.Certificate("eattendance-31dca-firebase-adminsdk-lmng9-dea083f54e.json")
App = firebase_admin.initialize_app(cred, {
  'projectId': "eattendance-31dca",
})


db = firestore.client(App)
# uni_ref = db.collection('Countries').document('Country').collection('Universities').document('University')
# contry_ref = db.collection('Countries').document('Nigeria').collection('Universities').document('Federal University Gusau')
# contry_ref.set({'state':'Zamfara State'}, merge=True)
# contry_ref = db.collection('Countries').document('Nigeria').collection('Universities').document('Usmanu Danfodio University Sokoto')
# contry_ref.set({'state':'Sokoto State'}, merge=True)

# class City(object):
#     def __init__(self, name, state, country, capital=False, population=0,
#                  regions=[]):
#         self.name = name
#         self.state = state
#         self.country = country
#         self.capital = capital
#         self.population = population
#         self.regions = regions

#     @staticmethod
#     def from_dict(source):
#       pass
    
#     def to_dict(self):
#       return {'name':self.name, "state":self.state, 'country':self.country, 'capital':self.capital , 'population':self.population, 'region':self.regions}

#     def __repr__(self):
#         return(
#             u'City(name={}, country={}, population={}, capital={}, regions={})'
#             .format(self.name, self.country, self.population, self.capital,
#                     self.regions))

# cities_ref = db.collection(u'cities')

# cities_ref.document(u'BJ').set(
#     City(u'Beijing', None, u'China', True, 21500000, [u'hebei']).to_dict())
# cities_ref.document(u'SF').set(
#     City(u'San Francisco', u'CA', u'USA', False, 860000,
#          [u'west_coast', u'norcal']).to_dict())
# cities_ref.document(u'LA').set(
#     City(u'Los Angeles', u'CA', u'USA', False, 3900000,
#          [u'west_coast', u'socal']).to_dict())
# cities_ref.document(u'DC').set(
#     City(u'Washington D.C.', None, u'USA', True, 680000,
#          [u'east_coast']).to_dict())
# cities_ref.document(u'TOK').set(
#     City(u'Tokyo', None, u'Japan', True, 9000000,
#          [u'kanto', u'honshu']).to_dict())

docs = db.collection(u'cities').stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))


"""
App
credentials
datetime
delete_app
get_app
initialize_app
json
os
threading
"""