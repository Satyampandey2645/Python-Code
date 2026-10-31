# ------------------------------- symmetric_difference() & symmetric_difference_update() -------------------------------

# symmetric_difference()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.symmetric_difference(cities2) 
print(cities3)  # {'Delhi', 'Kabul', 'Berlin', 'Seoul'}

print(cities)  # {'Madrid', 'Berlin', 'Tokyo', 'Delhi'}
print(cities2)  # {'Seoul', 'Kabul', 'Tokyo', 'Madrid'}

# symmetric_difference_update()
cities.symmetric_difference_update(cities2)
print(cities)  # {'Delhi', 'Kabul', 'Seoul', 'Berlin'}
print(cities2)  # {'Seoul', 'Madrid', 'Tokyo', 'Kabul'}