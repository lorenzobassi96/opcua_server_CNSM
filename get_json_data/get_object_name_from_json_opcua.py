import json

with open('opcua_fields.json') as file:
   data = json.load(file)
   #data["opcua"]["port"]
   data["opcua"][0]["ip"]


valore_object_name = data["opcua"][1]["objects"][0]["object_name"]
print(valore_object_name)


