## File Handling Basics

# Read file from a default folder
my_file = open("Booleans.py")
my_file.read()
my_file.read()
my_file.seek(0)
my_file.read()
my_file.seek(0)

my_file.readlines()
my_file.seek(0)

# Store file data into a variable
new_file = my_file.read()
print(new_file)

# Find the current directory
#print(pwd)

# Read a file from anywhere in th computer
#my_file = open("C:\\Users\\vijay\\Desktop\\Python 3\\The Avengers.txt")
#my_file.read()
#my_file.seek(0)
#my_file.readlines()

# Path format for MAC/Linux
my_file = open("/home/demonho/vsCode/Python-Course-2018/Booleans.py")

# Close the file
my_file.close()
## File Handling Basics

# 1) Read file from a default folder
# 2) Store file data into a variable
# 3) Find the current directory
# 4) Read a file from anywhere in th computer
# 5) Close the file