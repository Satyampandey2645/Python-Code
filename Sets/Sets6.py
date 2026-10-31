# ----------------------------------------- difference() & difference_update() -----------------------------------------

# difference()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}

cities3 = cities.difference(cities2)
print(cities3)  # {'Madrid', 'Tokyo', 'Berlin'}

print(cities)  # {'Tokyo', 'Madrid', 'Berlin', 'Delhi'}
print(cities2)  # {'Seoul', 'Delhi', 'Kabul'}

# difference_update()
cities.difference_update(cities2)
print(cities)  # {'Madrid', 'Tokyo', 'Berlin'}
print(cities2)  # {'Kabul', 'Delhi', 'Seoul'}