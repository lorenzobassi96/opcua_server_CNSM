import json

with open('opcua_fields.json') as file:
   data = json.load(file)

valore_object_name = data["opcua"][0]["objects"][0]["object_name"]
print(valore_object_name)


