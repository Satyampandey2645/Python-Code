# --------------------------------------- intersection() & intersection_update() ---------------------------------------

# intersection()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.intersection(cities2)
print(cities3)  # {'Tokyo', 'Madrid'}

print(cities)  # {'Tokyo', 'Madrid', 'Berlin', 'Delhi'}
print(cities2)  # {'Tokyo', 'Madrid', 'Kabul', 'Seoul'}

# intersection_update()
cities.intersection_update(cities2)

print(cities)  # {'Tokyo', 'Madrid'}
print(cities2)  # {'Tokyo', 'Madrid', 'Kabul', 'Seoul'}