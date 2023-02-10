# Dictionary :key -Value pairs, unordered, Mutable

mydict ={"name":"Max","age":28,"city":"New York"}
print(mydict)

mydict2 = dict(name="marry",age =27,city ="Boston")
print(mydict2)

value = mydict["name"]
print(value)

mydict["email"] = "max.@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print((mydict["name"]))
    
try:
    print(mydict["name"])
except:
    print("Error")
    
for key in mydict:
    print(key)
    
for key,value in mydict.items():
    print(key,value)
    
mydict_cpy = mydict

mydict_cpy["email"] = "raja123@.com"
print(mydict_cpy)
print(mydict)

mydict2 = dict(name="marry",age =27,city ="Boston")
mydict ={"name":"Max","age":28,"city":"New York"}

mydict.update(mydict2)
print(mydict)