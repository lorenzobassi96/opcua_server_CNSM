import json


with open('opcua_fields.json') as file:
   data = json.load(file)
   #data["opcua"]["port"]
   data["opcua"][0]["ip"]

valore_var1 = data["opcua"][1]["objects"][0]["variables"][0]
print(valore_var1)


