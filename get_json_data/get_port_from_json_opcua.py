import json

with open('opcua_fields.json') as file:
   data = json.load(file)

valore_porta = data["opcua"][0]["port"]
print(valore_porta)


