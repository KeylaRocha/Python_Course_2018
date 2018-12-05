## Map, Filter and  Lambda Expressions

# Map function

def cal_square(n):
    return n*n

Print(cal_square(4))

my_num = [1,2,3,4,5]

map(cal_square, my_num)

print(list(map(cal_square, my_num)))

for items in map(cal_square, my_num):
    print(items)
    
def len_char(c):
    return len(c)

my_char = ["Apple", "Banana", "Mushroom"]

print(list(map(len_char, my_char)))

for items in map(len_char, my_char):
    print(items)
    
    
    
    
    
    
## Filter function

def even_num(n):
    return n % 2 == 0

my_num = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(even_num, my_num)))

for items in filter(even_num, my_num):
    print(items)
    
## Lambda Expressions

# Stem 1
    
def cal_square(n):
    return n*n
print(cal_square(3))

# Step 2

def cal_square(n):return n*n
print(cal_square(4))

# Step 3
    
cal_square = lambda n:n*n
print(cal_square(5))
my_list = [1,2,3,4,5]

list(map(cal_square, my_list))

list(map(lambda n:n*n, my_list))

# Step 1

def even_num(n):
    return n % 2 == 0

# Step 2
def even_num(n):return n % 2 == 0

# Step 3

even_num = lambda n:n % 2 == 0

my_list = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda n:n % 2 == 0, my_list)))

# map function
# filter function
# lambda expression
# lambda expression with map and filter function