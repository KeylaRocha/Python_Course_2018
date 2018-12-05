## List's ##

my_list = ["Hello", 100, 23.47]
print(my_list)

second_list = ["one", "two", "three"]
print(second_list)

print(my_list, second_list)

# 1) concatenation

new_list = my_list + second_list
print(new_list)

# 2) Define empty list
empty_list = []
print(empty_list)

# 3) Indexing in list

students = ["Robert", "Chris", "Katarina", "Scarlett"]
print(students)

print(students[0])
print(students[2])
print(students[-1])
print(students[0:2])

# 4) Editing the list's

# Replace values
students[0] = "Sam"
print(students)

# Add values
students.append("Paul")
print(students)

# Remove values
students.remove("Scarlett")
print(students)

list1 = ["one", "two", "three", "four", "five"]
print(list1)
list1.pop()

list1.pop(0)
print(list1)

# 5) Add list into list
color = ["Red", "Green", "Blue", "Violet"]
print(color)
age = [21, 23, 25, 27]
print(age)

color.extend(age)
print(color)


# 6) Python in-build functions with the list's
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
print(numbers)

print(sorted(numbers))

print(len(numbers))
print(max(numbers))
print(min(numbers))

# 1) concatenation
# 2) Define empty list
# 3) Indexing in list
# 4) Editing the list's
# 5) Add list into list
# 6) Python in-build functions with the list's