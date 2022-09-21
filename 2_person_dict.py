person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #keys can be a list like this
person["pets"] = {"dog": "Fido", "cat": "Sox"} #dictionaries can also be keys, so, this dictionary has keys as lists and dictionaries # you can put many objects as keys/indexes within a list/dictionary

print(person)

print(type(person['children'][1]))   #use the function type to learn what object your are dealiing with dictionaries -> index Lists -> keys

print(type(person['pets']['cat']))

for child in person['children']:
    print(child) 

for pet in person['pets']:
    print(person['pets'][pet]) #pay attention to the modified way of returning the keys 