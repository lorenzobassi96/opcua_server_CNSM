import json


with open('opcua_fields.json') as file:
   data = json.load(file)


dimensione_lista = len(data["opcua"][0]["objects"][0]["variables"])


i=0
while (i<dimensione_lista):
     valore_var = data["opcua"][0]["objects"][0]["variables"][i]
     print(valore_var)
     i=i+1
