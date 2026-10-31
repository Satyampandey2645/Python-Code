info = {
    'name' : "Karan",
    'age'  : 19,
    'eligible' : True
}

# access keys and values of dictionary

print(info.keys())  # dict_keys(['name', 'age', 'eligible'])
print(info.values())  # dict_values(['Karan', 19, True])

for key in info.keys():
    print(key)          # name age eligible (in the next line to each other)
    
for value in info.values():
    print(value)        # Karan 19 True (in the next line to each other)
    
for key in info.keys():
    print(info[key])    # Karan 19 True (in the next line to each other)
    
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}") 
# Output:
    # The value corresponding to the key name is Karan
    # The value corresponding to the key age is 19
    # The value corresponding to the key eligible is True
    
    
