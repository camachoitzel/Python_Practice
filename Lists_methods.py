# List Methods

basket = [1,2,3,4,5]

# # adding
# new_list = basket.append(100)
# print(basket)
# print(new_list)

# # will allow the new list to be printed
# basket.append(100)
# new_list = basket
# print(basket)
# print(new_list)

# # insert method takes in the item you insert and the index of where you want to insert
# basket.ainsert(4, 100)
# new_list = basket
# print(basket)
# print(new_list)

# # extrend method adds multiple items at once to list one after another
# new_list = basket.extend([100, 101])
# print(basket)
# print(new_list)

# # removing
# basket.pop()
# # removes item at specific index
# basket.pop(0)
# print(basket)

# # remove method: removes that specific value from list
# basket.remove(4)
# print(basket)

# # clear method: clears out a list aka empties it
# new_list = basket.clear()
# print(basket)

# index method: returns index of the value you passed as a param
# print(basket.index(2))

# new_basket = ["a","b", "c" ,"d","e"]
# print(new_basket.index("d", 0, 2)) #not in list
# print(new_basket.index("d", 0, 3))# not in list
# print(new_basket.index("d", 0, 4)) #in list

# # 'in' keyword for lists: checks if that value is in list
# print("x" in new_basket)
# print("i" in "hi my name is Ian")

# # count: counts how many of that item are in the list and returns the count
# print(new_basket.count("d"))

# sort: sorts list in place
# another_basket = ["a","x", "b", "c" ,"d", "e", "d"]
# another_basket.sort()
# print(another_basket)

# # sorted: creates new list but does not modify original
# print(sorted(another_basket))
# print(another_basket)
# # essentially does the following
# new_basket = another_basket[:] #use list slicing to copy list or use another_basket.copy()
# new_basket.sort()
# print(new_basket)
# print(another_basket)

# # reverse: switches indexes into opposite sides in place but does NOT sort
# another_basket.reverse()
# print(another_basket)

# # generating a list
# print(list(range(1,100))) #generate a list from 1-99
# print(list(range(100))) #generate a list from 0-99
# print(list(range(101))) #generate a list from 0-100

# .join(): creates new item does not change the original need to assign it to new var
# sentence = " "
# new_sentence = sentence.join(["hi", "my" , "name", "is", "JOJO"])
# # OR instead in 1 line
# new_sentence = ' '.join(["hi", "my" , "name", "is", "JOJO"])
# print(new_sentence)

# list unpacking

a,b,c, *other , d = [1,2,3,4,5,6,7,8,9]

print(a)
print(b)
print(c)
print(other)
print(d)