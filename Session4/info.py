# person = ["Đức",96,175,"Sơn La", False,"dev"]

person = {
    "name": "Đức", 
    "yob":96, 
    "home":"Sơn La",
    "bmi":{
        "weight":70,
        "height":175
    }
}

#READ
name = person["yob"]
print(name)
print("1. __________________________")
for key in person:
    print(key)

print("2. __________________________")
for key in person:
    print(key, person[key])
#READ

print("3. __________________________")
weight = person["bmi"]["weight"]
print(weight)

print("4. __________________________")
person["hair"] = "short"   # CREATE
person["bmi"]["weight"] = 75 #UPDATE
print(person)

print("5. __________________________")
del person["bmi"] #DELETE
print(person)

#CHECK KEY IN DICT
print("6. __________________________")
print('relationship' in person)
print('name' in person)
#CHECK KEY IN DICT
