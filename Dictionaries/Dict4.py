# ------------------------------------------------- Dictionary Methods --------------------------------------------------

# update()
ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
ep2 = {222 : 67, 566 : 90}

ep1.update(ep2)
ep1:update
print(ep1)  # {122: 45, 123: 89, 567: 69, 670: 69, 222: 67, 566: 90}


info = {'name' : "Karan", 'age'  : 19, 'eligible' : True}

info.update({"age" : 20})
info.update({"DOB" : 2001})  
print(info)  # {'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}

# clear()
ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}

ep1.clear()
print(ep1)  # {} -> empty dictionary

# pop()
ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}

ep1.pop(122)
print(ep1)  # {123: 89, 567: 69, 670: 69}

# popitem()
ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}

poplast = ep1.popitem()  # it will automatically remove last key-pair from ep1 and return tuple of popped item as diff item
print(ep1)  # {122: 45, 123: 89, 567: 69}
print(poplast)  # (670, 69)
print(type(poplast))  # <class 'tuple'>

# del
ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
# del ep1 -> uncomment this to see error, I have commented this bcoz it throws error due to which below codes can't executes
print(ep1)  # error


ep1 = {122 : 45, 123 : 89, 567 : 69, 670 : 69}
del ep1[567]  # this will delete only key-value of key '567'f
print(ep1)  # {122: 45, 123: 89, 670: 69}
