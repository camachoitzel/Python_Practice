# Set Methods

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# # .difference()
# print(my_set.difference(your_set)) #prints {1,2,3} b/c those are the diff btwn my_set and your_set
#  print(my_set) #prints {1,2,3,4,5} b/c my_set was not modified

# # .discard()
# print(my_set.discard(5)) #returns None
# print(my_set) #prints {1,2,3,4} so 5 was removed from my_set

# .differemce_update()
print(my_set.difference_update(your_set)) #returns None b/c only modifies set
print(my_set) #prints {1,2,3} b/c my_set was modified


# .intersection()
print(my_set.intersection(your_set)) #prints {4,5} b/c those are the common nums in both sets

# .isdisjoint()
print(my_set.isdisjoint(your_set)) #returns False b/c they do have elements in common, would return True if nothing in common

# .issubset()

# .issuperset()

# .union()
