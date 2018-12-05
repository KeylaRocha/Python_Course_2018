## Tuple's ##

# Define a Tuple

prime_numbers = (2,3,5,7,11)
print(type(prime_numbers))

perfect_squares = [1,4,9,16,25,36]
print(type(perfect_squares))

print(len(prime_numbers))
print(len(perfect_squares))

my_tuple = ("Hieee", 100, 12.47)
print(my_tuple)
print(type(my_tuple))

# Indexing in Tuple's
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[0:2])
print(my_tuple[-1])

print(my_tuple.count(100))


# Difference between the List and Tuple

l = ["a", "b", "c", "d", "e"]
t= ("a", "b", "c", "d", "e")
print(type(l))
print(type(t))

l[0] = "New Element"
print(l)
t[0] = "New Element"
print(t)


# Define a Tuple
# Indexing in Tuple's
# Difference between the List and Tuple