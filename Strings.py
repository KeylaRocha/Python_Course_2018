## String's ##

# 1) concatenation of the string's

greeting = "Hello"
name = "Mark"
print(greeting + name)
print(greeting + " " + name)

# 2) input function

greeting = "Hello"
name = input("What is your sweet name ? ")

print(greeting + " " + name)

# 3) Spliting of the strings
split_string = "Hello everyone, Welcome to the world of Python !!!"
print(split_string)

split_string = "Hello everyone, \nWelcome to the world of Python !!!"
print(split_string)

tab_string = "1\t2\t3\t4"
print(tab_string)

# 4) Indexing

color = "Orange"
len(color)
print(color[3])
print(color[0])
print(color[-1])
print(color[-2])

print(color[0:3]) # upper bound excluded
print(color[0:4])

print(color[-4:-1]) # Upper bound excluded

print(color[:3])
print(color[2:])

# 5) String formating

age = str(27) 
print("I am " + age + " Year's old")

age = 27 
print("I am " + str(age) + " Year's old")

print("The colors are {} {} {} ".format("Red", "Green", "Blue"))

print("The colors are {0} {1} {2} ".format("Red", "Green", "Blue"))

print("The colors are {0} {0} {0} ".format("Red", "Green", "Blue"))

print("The colors are {2} {2} {2} ".format("Red", "Green", "Blue"))

print("The colors are {r} {g} {b} ".format(r="Red", g="Green", b="Blue"))

print("The colors are {r} {r} {r} ".format(r="Red", g="Green", b="Blue"))

pie = 3.14
print(pie)

print("The value of pie is {} ".format(pie))

# 1) concatenation of the string
# 2) input function
# 3) Spliting of the strings
# 4) Indexing
# 5) String formating

















































