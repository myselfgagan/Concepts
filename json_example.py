import json

# person = {"name":"John", "age":30, "city":"New York", "hasChildren":False, "title":["engineer", "programmer"]}

# personJSON = json.dumps(person, indent=4, sort_keys=True)   # converting to JSON object
# print(personJSON)

# with open("person.py", "w") as file:     # creating JSON file
#     json.dump(person, file, indent=4)
    
# with open("person.json", "r") as file:   # converting JSON file to python
#     person = json.load(file)
#     print(person)
    
# person = json.loads(personJSON)        # converting JSON to python
# print(person)



# Encode custom object
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
user = User("Gagan", 26)

def encode_user(o):
    if isinstance(o, User):
        return{"name":o.name, "age": o.age, o.__class__.__name__:True}
    else:
        raise TypeError("Object of type User is not JSON serializable")
    
userJSON = json.dumps(user, default=encode_user)
print(userJSON)



# we can also do this to encode

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age":o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    
userJSON = UserEncoder.encode(user)
print(userJSON)



# decoding back to python

def decode_user(dct):
    if user.__name__ in dct:
        return User(name=dct["name"], age=["age"])
    return dct
    
user = json.loads(userJSON, object_hook=decode_user)
print(user)