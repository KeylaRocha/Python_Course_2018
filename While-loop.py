# While loop

i = 0

while i < 5:
    print(i)
    i = i + 1
    
i = 0

while i < 5:
    print(i)
    i = i + 1
else:
    print("i is not less than 5")
    
i = 10

while i < 5:
    print(i)
    i = i + 1
else:
    print("i is not less than 5")
    
# Pass, Break and Contineu
    
l = [1,2,3,4,5]

for items in l:
    # Comment
    pass
print("I will work after !!!")

my_string = "Hello World"

for letters in my_string:
    if letters == "r":
        break
    print(letters)
    
my_string = "Hello World"

for letters in my_string:
    if letters == "e":
        continue
    print(letters)
    
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i = i + 1