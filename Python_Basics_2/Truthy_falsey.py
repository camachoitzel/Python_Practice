# Truthy and Falsey

is_old = 'hello'
is_licenced = 5

print(bool('hello')) #prints True
print(bool(5)) #prints True

print(bool('')) #prints False
print(bool(0)) #prints False

if is_old and is_licenced: #b/c both true this line runs
    print("You are old enough to drive, and you have a licence!")
else:
    print("You are not of age!")

password = '123'
username = 'johnny'


if password and username:
    print('Thank you for inputting a username and password')

else:
    print('No username or no password entered please try again')