## Scope of the Variables in Python

# 1) Local variable

def greeting():
    name = "Scarlett"
    print("Hello " + name)
    
greeting()

# 2) Enclosing functional local variable

name = "Robert"

def greeting():
    name = "Chris"
    def hello():
        print("Hi "+ name)
    hello()
    
greeting()

# 3) Global variable

name = "Robert"

def greeting():
    def hello():
        print("Hi "+ name)
    hello()
    
greeting()

# Use of the Keyword "Global"

x = 200

def my_function():
    global x
    x = 100
    print("The value of x is {} ".format(x))
    
print(x)
my_function()
print(x)

# 1) Local variable

# 2) Enclosing functional local variable

# 3) Global variable

# 4) Use of the Keyword "Global"