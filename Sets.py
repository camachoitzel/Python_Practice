# Set data sets
my_set = {1,2,3,4,5}
print(my_set) #returns {1,2,3,4,5}

# sets are unique, with no duplicates

my_set2 = {1,2,3,4,5,5}
print(my_set2) # returns {1,2,3,4,5} not including duplicates


my_set2.add(100)
my_set2.add(2)
print(my_set2) #returns {1,2,3,4,5,100} does not add 2 b/c its already in the set

#return a list w/o any duplicate items
my_list = [1,2,3,4,5,5]
# convert list to set so it removes duplicates
print(set(my_list))

print(my_set2[0]) #sets do NOT support indexing

# to check if an items is in a set
print(1 in my_set2) #looking for 1 in my_set2

# len() works on sets too
print(len(my_set2)) #only counts the non duplicate values in this case it would be 5 rather than 6

# convert a set into a list
print(list(my_set2)) #retusn set as a list

# copying a set

new_set = my_set2.copy() #new_set is a new set with the same data as my_set2

my_set2.clear() #clears my_set2

print(new_set) # returns {1,2,3,4,5}
print(my_set2) #returns empty set()