# Lists Practice

# li = [1,2,3,4,5]

# li2 = ['a', 'b', 'c']

# li3 = [1,2,'a',True]

# amazon_cart = ['notebooks', 'sunglasses']
# # access items in list
# print(amazon_cart[0])
# print(amazon_cart[1])

# # List slicing

amazon_cart1 = [
    'notebooks', 
    'sunglasses',
    'toys',
    'grapes'
    ]

print(amazon_cart1[0:2])

print(amazon_cart1[0::2])

amazon_cart1[0] = "laptop"
print(amazon_cart1)

print(amazon_cart1[0:3])
print(amazon_cart1)

new_cart = amazon_cart1[0:3]
print(new_cart)

new_cart[0] = "gum"
print(new_cart)
print(amazon_cart1)

new_cart = amazon_cart1
print(new_cart)
print(amazon_cart1)

# copies the amazon_cart but does not change the original
new_cart = amazon_cart1[:]
print(new_cart)
print(amazon_cart1)