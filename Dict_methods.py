# Dictionary methods

user = {

    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
# prints True b/c it does exist
print('basket' in user)

# only checks the keys using method .keys
# this would be False
print('size' in user.keys())
# this would be True
print('age' in user.keys())

# use .values to iterate over the values only
print('hello' in user.values())

# use .items to return the whole dict in tuples
print(user.items())

# use .clear to create an empty dict
user.clear()
print(user) #will be an empty dict

# use .copy to copy one dict to another
user2 = user.copy()
print(user)
print(user2)

# removes key from dict
print(user.pop("age")) # will return 20

# will print the dict without age b/c it was popped
print(user)

# removes last key: value from dict
# useful to destructively iterate over a dict
print(user.popitem())

# updates key value
print(user.update({"age": 55})) #changes age val to 55

print(user.update({"ages" : 55})) #adds ages key: value to dict 