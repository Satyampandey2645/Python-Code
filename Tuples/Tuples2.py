# Creating Tuples
tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")

print(tuple1)  # (1, 2, 2, 3, 5, 4, 6)
print(tuple2)  # ('Red', 'Green', 'Blue')

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)  # ('Abhijeet', 18, 'FYBScIT', 9.8)

# positive indexing
country = ("Spain", "Italy", "India")

print(country[0])  # Spain
print(country[1])  # Italy
print(country[2])  # India

# Negative Indexing
country = ("Spain", "Italy", "India", "England", "Germany")

print(country[-1])  # Germany -> Last element
print(country[-3])  # India
print(country[-4])  # Italy

# Check if an Item Exists in a Tuple
country = ("Spain", "Italy", "India", "England", "Germany")

if "Germany" in country:
    print("Germany is present.")  # Germany is present.
else:
    print("Germany is absent.")
    
    
country = ("Spain", "Italy", "India", "England", "Germany")

if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")  # Russia is absent.
    
# Printing elements within a range
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")

print(animals[3:7])  # ('mouse', 'pig', 'horse', 'donkey') 
print(animals[-7:-2])  # ('bat', 'mouse', 'pig', 'horse', 'donkey')

# Printing elements from a given index till the end
print(animals[4:])  # ('pig', 'horse', 'donkey', 'goat', 'cow')
print(animals[-4:])  # ('horse', 'donkey', 'goat', 'cow')

# Printing elements from start till a given index
print(animals[:6])  # ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
print(animals[:-3])  # ('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')

# Printing alternate elements
print(animals[::2])  # ('cat', 'bat', 'pig', 'donkey', 'cow')
print(animals[-8:-1:2])  # ('dog', 'mouse', 'horse', 'goat')

# Printing every 3rd element within a range
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])  # ('dog', 'pig', 'goat')


    
    


