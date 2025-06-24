# input('jayjay')
# input('secret')

# print('{username}, password {******} is {password_length} long')

username = input("Enter your username: ")
password = input("Enter your password: ")

hidden_password = '*' * len(password)
password_len = len(password)

print(f'{username}, your password {hidden_password} is {password_len} letters long')