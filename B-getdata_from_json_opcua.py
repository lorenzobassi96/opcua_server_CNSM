import json

#f = open('ciao.json', "r")
#data = json.loads(f.read())

#for i in data['opcua']:
#     print(i)
#f.close

with open('opcua_fields.json') as file:
   data = json.load(file)
   #data["opcua"]["port"]
   data["opcua"][0]["ip"]
print(data)

print("---------------")
valore_ip = data["opcua"][0]["ip"]
print("ip: "+valore_ip)


print("---------------")
valore_porta = data["opcua"][0]["port"]
print("porta: "+valore_porta)


print("---------------")
valore_uri = data["opcua"][0]["uri"]
print("uri: "+valore_uri)


print("---------------")
valore_object_name = data["opcua"][1]["objects"][0]["object_name"]
print("object_name: "+valore_object_name)


print("---------------")
valore_var1 = data["opcua"][1]["objects"][0]["variables"][0]
print("var1: "+valore_var1)


print("---------------")
valore_var2 = data["opcua"][1]["objects"][0]["variables"][1]
print("var2: "+valore_var2)


