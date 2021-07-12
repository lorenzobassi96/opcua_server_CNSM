import json


with open('opcua_fields.json') as file:
   data = json.load(file)


#valore_var1 = data["opcua"][1]["objects"][0]["variables"][0]
#print(valore_var1)

dimensione_lista = len(data["opcua"][1]["objects"][0]["variables"])
print(dimensione_lista)
