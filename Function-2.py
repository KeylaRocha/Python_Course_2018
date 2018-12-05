## *args and **kwargs

# *args

def new_function(a,b,c):
    return a,b,c

print(new_function("Hello", 10, "Hi"))

def new_function(*args):
    return args

print(new_function("Hello", 10))


def cal_per(a,b):
    return sum((a,b)) * 0.4

print(cal_per(70,30))

def cal_per(*args):
    return sum((args)) * 0.4

cal_per(70,30,40)

def cal_per(*tom):
    return sum((tom)) * 0.4

print(cal_per(70,30,40))

# kwargs

def my_function(**asdf):
    print(asdf)
    if "flower" in asdf:
        print("We have {} for you !".format(asdf["flower"]))
    else:
        print("There is no flower for you !")
        
print(my_function(color = "Orange", flower = "Rose"))

## args and kwargs together

def my_function(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like to have {} {} ".format(args[0],kwargs["fruit"]))

print(my_function(1,2,3, color = "Green", fruit = "Apple"))

# *args

# **kwargs

## args and kwargs together