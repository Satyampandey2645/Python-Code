# ------------------------------------------------- Manipulating Tuples -------------------------------------------------

countries = ("Spain", "Italy", "India", "England", "Germany")

temp = list(countries)

temp.append("Russia")     # Add item
temp.pop(3)               # Remove item at index 3
temp[2] = "Finland"       # Modify item

countries = tuple(temp)
print(countries)  # ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')


# ------------------------------------------------- Concatenating Tuples ------------------------------------------------

countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
countries2 = ("Vietnam", "India", "China")

southEastAsia = countries1 + countries2
print(southEastAsia)  # ('Pakistan', 'Afghanistan', 'Bangladesh', 'Sri Lanka', 'Vietnam', 'India', 'China')

# --------------------------------------------------- Tuples Methods ---------------------------------------------------

# len()
t1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res1 = len(t1)
print("Length of tuple t1:", res1)  # 10 

# count()
t2 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res2 = t2.count(3)
print("Count of 3:", res2)  # Count of 3: 4
print(t2.count(32))  # 0 -> becoz 32 is not in tuple t2

# index()
t3 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res3 = t3.index(3)
print("First occurrence of 3 is:", res3)  # First occurrence of 3 is: 3

t4 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res4 = t4.index(3, 4, 8)  # -> it will find the index of first occurence of 3 from index 4(included) to 7 ( 8 excluded)
print(res4)  # 5 
print(t4.index(32))  # ValueError


