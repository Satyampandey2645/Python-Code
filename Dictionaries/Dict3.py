info = {
    'name' : "Karan",
    'age'  : 19,
    'eligible' : True
}

print(info.items())  # dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}") 
# Output:    
    # The value corresponding to the key name is Karan
    # The value corresponding to the key age is 19
    # The value corresponding to the key eligible is True    
 
# We can create empty dictionary like this:
dic = {}
print(type(dic))  # <class 'dict'>