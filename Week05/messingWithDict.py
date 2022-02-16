# messingWithDict.py
#
# Messing around with the dict variable
#
# Author: Elaine Tynan

car = {
    "make": "Bugatti",
    "model": "Veyron",
    "year": 2022,
    "owner": "Elaine"
}

car2 = {
    "make": "Bugatti",
    "model": "Veyron",
    "year": 2022,
    "owner": {
        "name":"Elaine",
        "driver-number":1234
    }
}

print(car2["owner"])
print(car2["owner"]["driver-number"])

print("~~~~~~~~~~~~~")
print(car2["owner"].get("driver-number"))
print(car2["owner"].get("driver number"))

print("~~~~~~~~~~~~~")
print("~~ KEYS ~~")
for key in car:
    print(key)

print("~~~~~~~~~~~~~")
print("~~ KEY-VALUES ~~")
for x, y in car2.items():
    print("Key: ",x," Value: ",y)
