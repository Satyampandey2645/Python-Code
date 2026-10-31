# ------------------------------------------------- union() & update() -------------------------------------------------

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# union()
print(s1.union(s2))  # {1, 2, 3, 5, 6, 7}  -> this opertion won't affect s1 and s2
print(s1, s2)  # {1, 2, 5, 6} {3, 6, 7}

# update()
s1.update(s2)  # it means add all elements of s2 in s1 and update s1 -> this opertion will change s1

print(s1, s2)  # {1, 2, 3, 5, 6, 7} {3, 6, 7}

# union()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.union(cities2)
print(cities3)  # {'Madrid', 'Seoul', 'Delhi', 'Berlin', 'Kabul', 'Tokyo'}

print(cities)  # {'Delhi', 'Madrid', 'Tokyo', 'Berlin'}
print(cities2)  # {'Seoul', 'Kabul', 'Madrid', 'Tokyo'}

# update()
cities.update(cities2)

print(cities)  # {'Madrid', 'Delhi', 'Tokyo', 'Berlin', 'Kabul', 'Seoul'}
print(cities2)  # {'Kabul', 'Tokyo', 'Seoul', 'Madrid'}
