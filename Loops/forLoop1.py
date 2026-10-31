# ----------------------------------------------- Iterating over a string -----------------------------------------------
print("Iterating over a string: ")

name = "Abhishek"

for i in name:
    print(i, end=", ")
    if (i == 'b'):
        print("This is something special")
       
# ------------------------------------------------ Iterating over a list ------------------------------------------------
print("\n\nIterating over a list: ")

colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors:
    print(color)
    for i in color:
        print(i)
             
        