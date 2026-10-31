# ----------------------------- Here is the proof that this enumerate function returns tuple ----------------------------

fruits = ["apple", "banana", "mango"]

for v in enumerate(fruits):
    print(v)  
print(type(v))  # <class 'tuple'>

# --------------------- Loop over a list and print the index (starting at 1) and value of each element ------------------

print("\nLoop over a list and print the index (starting at 1) and value of each element")

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)  
  
# -------------------------------------------------- Printing serial numbers --------------------------------------------

print("\nPrinting serial numbers")

fruits = ['apple', 'banana', 'mango']

for index, fruit in enumerate(fruits):
    print(f"{index + 1}: {fruit}")

