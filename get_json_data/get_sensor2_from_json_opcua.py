import json

with open('opcua_fields.json') as file:
   data = json.load(file)


valore_var2 = data["opcua"][0]["objects"][0]["variables"][1]
print(valore_var2)

