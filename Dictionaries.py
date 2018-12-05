## Dictionaries ##

# 1)  Define a Dictionary

my_dict = {"key1":"value1", "key2":"value2"}
print(my_dict)
print(my_dict["key1"])

fruits = {"Apple":3, "Banana":1.75, "Cherry":2}
print(fruits)
print(fruits["Apple"])

# 2) Dictionaries with all data type's

new_dict = {"k1":147, "k2": [15, 25, 35], "k3":{"Apple":3}}
print(new_dict)
print(new_dict["k2"])
print(new_dict["k2"][1])
print(new_dict["k3"])
print(new_dict["k3"]["Apple"])

d = {"students": ["a", "b", "c","d"]}
print(d)
print(d["students"][1])
print(d["students"][1].upper())
print(d["students"][1].lower())

# 3) Add values

d = {"k1":100, "k2": 200}
(d)
d["k3"] = 300
print(d)

# 4) Replace values
d["k1"] = "New One"
print(d)

# 5) Keys, Values and Item's 
print(d.keys())
print(d.values())
print(d.items())

# 1) Define a Dictionary
# 2) Dictionaries with all data type's
# 3) Add values
# 4) Replace values
# 5) Keys, Values and Item's retrieval