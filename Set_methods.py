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
#shorthand for intersection
print(my_set & your_set)

# .isdisjoint()
print(my_set.isdisjoint(your_set)) #returns False b/c they do have elements in common, would return True if nothing in common

# .issubset()
#if my_set = {4,5}
my_set.issubset(your_set) #returns True b/c all of my_set is in your_set

# .issuperset()
#if my_set = {4,5}
print(my_set.issuperset(your_set)) #returns false b/c my_set does not encompass all of your_set
print(your_set.issuperset(my_set)) #returns True b/c your_set encompasses all of my_set

# .union()
# union unites sets together w/o duplicates and returns a new set diff from the 2 it combined
print(my_set.union(your_set)) #prints {1,2,3,4,5,6,7,8,9,10}
#shorthand for union
print(my_set | your_set)
