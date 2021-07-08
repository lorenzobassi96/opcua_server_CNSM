import json

with open('opcua_fields.json') as file:
   data = json.load(file)
   #data["opcua"]["port"]
   data["opcua"][0]["ip"]

valore_uri = data["opcua"][0]["uri"]
print(valore_uri)


