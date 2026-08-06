import json

person = {'name': 'jhon', 'age': 28, 'city': 'nyc','haschildran': False}


personJson = json.dumps(person, indent=4, sort_keys=True)
#print(personJson)

#with open('personJson','w') as file:
#    json.dump(person,file,indent = 4)
    
with open('personJson.json','r') as file:
    person = json.load(file)
    print(person)