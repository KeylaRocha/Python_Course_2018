## Commonly used Built-in functions in Python

# 1) Range function

for num in range(10):
    print(num)
    
for num in range(3,10):
    print(num)
    
for num in range(0,11,2):
    print(num)

my_list = [1,2,3,4,5,6,7,8,9,10]
print(range(10))
print(list(range(10)))
print(list(range(1,11)))


## 2) Enumerate
# it gives back us an index count and object itself

word = "Batman"

for items in word:
    print(items)
    
for items in enumerate(word):
    print(items)

# It gives the output as tuples 
# And we know the tuple unpacking from for loop
    
for a,b in enumerate(word):
    print(a,b)

for a,b in enumerate(word):
    print(a)
    print(b)
    print("\n")


## 3) zip

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = ["a","b","d"]
zip(list1, list2)

for items in zip(list1, list2):
    print(items)

for a,b in zip(list1, list2):
    print(a,b)
    
for items in zip(list1, list2, list3):
    print(items)

for a,b,c in zip(list1, list2, list3):
    print(b)

# it will zip the items acc to shortest list 
# and ignore else

## 4) in
    
"a" in [1,2,3]
"a" in [1,2,3, "a"]
"s" in "school"
"s" in "School"

"k1" in {"k1":100, "k2":200, "k3":300}

d = {"k1":100, "k2":200, "k3":300}
print(100 in d.keys())
print(100 in d.values())


## List comprehensions in python

my_string = "Spartans"

for letters in my_string:
    print(letters)

my_list = []
for letters in my_string:
    my_list.append(letters)
print(my_list)

my_list = [letters for letters in my_string]
print(my_list)

list1 = [asdf for asdf in range(10)]
print(list1)