selfish = 'me me me'
          #01234567
 
# prints char in 7th index
print(selfish[7])

print(selfish)

# [start: stop]

selfish2 = '01234567'
print(selfish2[0:2])
# output = 01

print(selfish2[0:7])
# output = 0123456

print(selfish2[0:8])
# output = 01234567

# [start: stop: stepover]
print(selfish2[0:8:2])
# output = 0246 b/c steps over by 2

print(selfish2[1:])
# output = 1234567

print(selfish2[:5])
# output = 01234

print(selfish2[::1])
# output = 01234567

# starting at the end

print(selfish2[-1])
# output = 7

print(selfish2[::-1])
# output = 76543210

print(selfish2[::-2])
# output = 7531