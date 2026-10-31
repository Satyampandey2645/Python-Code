# --------------------------------------------------- String Slicing ---------------------------------------------------

fruit = "Mango"
mangoLen = len(fruit)

print("Mango is a", mangoLen, "letter word")  # Mango is a 5 letter word
print(fruit[0:4])  # Mang → includes index 0 to 3rd but excludes index 4
print(fruit[1:4])  # ang
print(fruit[:4])  # Mang  -> [:4] means [0:4], python automatically take it 0
print(fruit[:])  # Mango  -> [:] means [0:len(fruit)], Here length of string is 5
print(fruit[:5])  # Mango  
print(fruit[0:-3])  # Ma → [0:-3] means [0:len(fruit)-3] → [0:2]
print(fruit[0:len(fruit)-3])  # Ma 
print(fruit[:-3])  # Ma 
print(fruit[-1:-3])  # Empty output -> [5-1:5-3] => [4:2]. So, If start > end, result is an empty string
print(fruit[-3:-1])  # ng → [-3:-1] means [len-3 : len-1] → [2:4] 