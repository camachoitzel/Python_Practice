# Tuple
# immutable list
my_tuple =(1,2,3,4,5)

# tuple is immutable so this would give you an error
my_tuple[1] = 'z'

# is valid prints the 2nd elem in tuple: returns '2'
print(my_tuple[1])

# check if 5 is in the tuple: returns True
print(5 in my_tuple)


# faster than lists
# good for geographic locations that don't move


user = { 
    "basket" : [1,2,3],
    "greet" : "hello",
    "age" : 20
}

# returns key and value in a tuple
print(user.items())

user = { 
    (1,2) : [1,2,3],
    "greet" : "hello",
    "age" : 20
}

# prints [1,2,3]
print(user[(1,2)])

# tuples can be sliced
new_tuple = my_tuple[1:2]