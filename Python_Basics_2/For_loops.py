# For loops

for item in 'Zero to Mastery':
    print(item)

# works with sets {} or tuples ()
for item in [1,2,3,4,5]:
    print(item)

print("hi")

for item in (1,2,3,4,5):
    for x in ["a", "b" , "c"]:
        print(item , x)


# iterable
user = {
    "name": "Golem",
    "age": 5006,
    "can_swim" : False
}

for item in user:
    print(item)

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)