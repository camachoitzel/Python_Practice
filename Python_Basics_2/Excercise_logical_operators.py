# Logical Operator excercise

is_magician = True
is_expert = True

# check if magician and expert: "you are a master magician"
if is_magician and is_expert:
    print("You are a master magician!")
# check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("At least you're getting there")
# if you're not a magician: "you need magic powers!"
elif not is_magician:
    print("You need magic powers!")