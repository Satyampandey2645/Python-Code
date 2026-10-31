# ------------------------------------------------- List Comprehension -------------------------------------------------

lst1 = [i for i in range(4)]
print(lst1)  # [0, 1, 2, 3]

lst2 = [i*i for i in range(4)]
print(lst2)  # [0, 1, 4, 9]

lst2 = [i*i for i in range(10) if i % 2 == 0]
print(lst2)  # [0, 4, 16, 36, 64]

# ------------------------------ Names containing "o" ------------------------------

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]

names_with_o = [item for item in names if "o" in item]
print(names_with_o)  # ['Milo', 'Bruno', 'Rosa']

# ------------------------- Names with more than 4 letters -------------------------

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]

long_names = [item for item in names if len(item) > 4]
print(long_names)  # ['Sarah', 'Bruno', 'Anastasia']
