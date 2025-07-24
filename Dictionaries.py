# Dictionary

# dictionary = {

#     'a' : 1,
#     'b' : 2,
#     'x' : 3
# }

# # prints 2
# print(dictionary['b'])

# # throws error
# print(dictionary['c'])

# valid inputs for a dicitonary
# dictionary = {

#     'a' : [1,2,3],
#     'b' : 'hello',
#     'x' : True
# }

# #prints the list in 'a'
# print(dictionary['a'])

# # prints item at index 1 of list in 'a' = 2
# print(dictionary['a'][1])

# my_list = [
#     {
#     'a' : [1,2,3],
#     'b' : 'hello',
#     'x' : True
#     },
#     {
#     'a' : [4,5,6],
#     'b' : 'hello',
#     'x' : True
#     }
# ]

# prints first item in list gets the list in 'a' and gets the item at index 2 = 3
# print(my_list[0]['a'][2])

# valid keys for dict
# dictionary = {

#     123 : [1,2,3],
#     True : 'hello',
#     [100] : True #not valid b/c has to be unmutable 
# }
# # prints list
# print(dictionary[123])

# # prints 'hello'
# print(dictionary[True])

# # throws error
# print(dictionary[100])

# using same key values
dictionary = {

    '123' : [1,2,3],
    '123' : 'hello' #overwrites the previous '123' key
}

# prints 'hello' b/c list [1,2,3] was overwritten
print(dictionary['123'])

# checking if a dictionary has a certain key
user = {

    'basket' : [1,2,3],
    'greet' : 'hello'
}

# prints None
print(user.get('age'))

# add a default value if none exists in dict
print(user.get('age', 55))

# when 'age' exists
user = {

    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

# prints 20 b/c the age attribute exists
print(user.get('age', 55))

# diff way of writing a dict using a function
user2 = dict( name ='JohnJohn')

# prints out the dict user2
print(user2)