# ----------------------------------------------------- Set Methods -----------------------------------------------------

# add()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)  # {'Madrid', 'Helsinki', 'Delhi', 'Tokyo', 'Berlin'}

# update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}

cities.update(cities2)
print(cities)  # {'Delhi', 'Seoul', 'Helsinki', 'Berlin', 'Warsaw', 'Madrid', 'Tokyo'}

# remove()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)  # {'Madrid', 'Berlin', 'Delhi'}

# cities.remove("Seoul")  # KeyError -> bcoz "Seoul" doesn't exist in cities it means remove throw error for unknown item
# so to neglect error for unknown item we can use discard() method

# discard()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Madrid")
print(cities)  # {'Delhi', 'Berlin', 'Tokyo'}

cities.discard("Seoul")  # No error 
print(cities)  # {'Delhi', 'Berlin', 'Tokyo'}

# pop()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()  
print(cities)  # {'Madrid', 'Tokyo', 'Berlin'}  -> anything can be popped out from end becoz sets are unordered
print(item)  # Delhi -> this output can be change whenever we run this code becoz sets are unordered

# del
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities -> uncomment this to see error, I have commented this bcoz it throws error due to which below codes can't executes
print(cities)  # Error -> We can't access it becoz the entire set "cities" is deleted

# if we don't want to delete entire set and just want to delete all items of the set we will use clear()

# clear()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)  # set()
