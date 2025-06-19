# initilaizing strings
username = 'supercoder'
password = 'supersecret'

# writing a long string = use '''
long_string = '''
WOW 
0 0
---
'''

print(long_string)

first_name = 'Iris'
last_name = 'Thorne'

full_name = first_name + ' ' + last_name

print(full_name)

# string concatenation
print('hello' + 'Andrei')

# formatted strings
name = 'Johnny'
age = 55

print(f'hi {name}. You are {age} years old')

print('hi {}. You are {} years old'.format(name, age))

print('hi {new_name}. You are {age} years old'.format(new_name = 'Sally', age = 100))