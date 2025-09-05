# using 'is' and '=='
# == checks for equality of value
print(True == 1) #True
print('' == 1) #False
print([] == 1)  #False
print(10 == 10.0) #True
print([] == []) #True

# 'is' checks if location in memory is the same is yes then True False otherwise
print(True is 1) #False
print('' is 1) #False
print([] is 1)  #False
print(10 is 10.0) #False
print([] is []) #False