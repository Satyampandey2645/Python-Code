# -------------------------------------------- Using enumerate() with Tuple ---------------------------------------------

print("With Tuple")

colors = ('red', 'green', 'blue')

for index, color in enumerate(colors):
    print(index, color)

# -------------------------------------------- Using enumerate() with String ---------------------------------------------

print("\nWith String")

s = "hello"

for index, ch in enumerate(s):
    print(index, ch)
