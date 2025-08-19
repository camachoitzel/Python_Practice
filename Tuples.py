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

# assign things to tuples
x = my_tuple[1] #returns 2
y = my_tuple[2] #returns 3

# assigning values like a list
x,y,z, *other = (1,2,3,4,5)

print(x) #prints 1
print(y) #prints 2
print(other) #prints [4,5]

# tuple methods
my_tuple1 = (1,2,3,4,5,5)

# count(): returns the number of occurences of the passed element
print(my_tuple1.count(5)) # returns 2 b/c there are 2 5's

# index(): returns the index of the passed element
print(my_tuple1.index(5)) # returns 4

# len(): gets length of tuple
print(len(my_tuple1)) # returns 6