# ----------------------------------------------------- Set Methods -----------------------------------------------------

# isdisjoint()
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities1.isdisjoint(cities2))  # False

cities3 = {"Moscow", "Denver", "Berlin", "Delhi"}
cities4 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities3.isdisjoint(cities4))  # True

# issuperset()
cities5 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities6 = {"Seoul", "Kabul"}

print(cities5.issuperset(cities6))  # False

cities7 = {"Seoul", "Madrid", "Kabul"}
print(cities5.issuperset(cities7))  # False

print(cities6.issuperset(cities7))  # False
print(cities7.issuperset(cities6))  # True

# issubset()
cities8 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities9 = {"Delhi", "Madrid"}

print(cities9.issubset(cities8))  # True
print(cities8.issubset(cities9))  # False
