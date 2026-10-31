s = {2, 4, 2, 6}
print(s)  # {2, 4, 6}
print(type(s))  # <class 'set'>

info = {"Carla", 19, False, 5.9, 19}
print(info)  # {False, 19, 5.9, 'Carla'}  -> Output will be in any order bcoz set doesn't maintain order
print(type(info))  # <class 'set'>

# ------------------------------------------------- empty set creation -------------------------------------------------

st = {}
print(type(st))  # <class 'dict'>   -> So, st = {} will give dictionary

# to make empty sets we need to make it by this
st = set()
print(type(st))  # <class 'set'>

# ------------------------------------------------- Accessing set items -------------------------------------------------

info = {"Carla", 19, False, 5.9}

# print(info[0]) -> This will throw an error, we can't access set's item using this method bcoz set doesn't maintain order

for item in info:
    print(item)
    