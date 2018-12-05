## Project 6 : Tracing IP address

import requests

res = requests.get("https://ipinfo.io")

data = res.json()

print(res.text)
print(data)

print(type(res.text))
print(type(data))

city = data["city"]
city

location = data["loc"].split(",")
location
lattitude = location[0]
lattitude
longitude = location[1]
longitude
region = data["region"]
country = data["country"]


print("Lattitude is : ", lattitude)
print("Longitude is : ", longitude)
print("City is ", city)
print("Region is ", region)
print("Country is : ", country)