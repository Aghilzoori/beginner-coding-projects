friends = {
    "Ali" : ["Tehran", 15],
    "Aghil" : ["Tehran", 14],
    "mmd" : ["Tehran", 15]
}
def greet_friend(name, age, city):
    return f"Hello {name}! You are {age} years old and live in {city}"
for key in friends:
    print(greet_friend(key, friends[key][1], friends[key][0]))