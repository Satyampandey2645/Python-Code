# ---------------------- Without enumerate ----------------------

marks = [12, 56, 32, 98, 12, 45, 1, 4]

index = 0;
for mark in marks:
    print(mark)
    if (index == 3):
        print("Satyam, Awesome!");
    index += 1;   
    
# ---------------------- With enumerate ----------------------             
print("\nEnumerate function: ")

marks = [12, 56, 32, 98, 12, 45, 1, 4]

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Satyam, Awesome!"); 
        
# -----------------------------------------------------------------------------------------------------------------------
print("\nEnumerate function: ")

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)    