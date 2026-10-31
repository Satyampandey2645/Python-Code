# ---------------------------------------------------- Lists Methods ----------------------------------------------------

# sort()
colors = ["violet", "indigo", "blue", "green"]
colors.sort()
print(colors)  # ['blue', 'green', 'indigo', 'violet']

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)  # [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]

# sort(reverse=True)
colors.sort(reverse=True)
num.sort(reverse=True)

print(colors)  # ['violet', 'indigo', 'green', 'blue']
print(num)  # [9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]

# reverse()
colors = ["violet", "indigo", "blue", "green"]
colors.reverse()
print(colors)  # ['green', 'blue', 'indigo', 'violet']

# index()
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.index("green"))  # 1

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))  # 3

# count()
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.count("green"))  # 2

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))  # 3

# copy()
colors = ["violet", "green", "indigo", "blue"]
newlist = colors.copy()

print(colors)  # ['violet', 'green', 'indigo', 'blue']
print(newlist)  # ['violet', 'green', 'indigo', 'blue']

# append()
colors = ["violet", "indigo", "blue"]
colors.append("green")
print(colors)  # ['violet', 'indigo', 'blue', 'green']

# insert()
colors = ["violet", "indigo", "blue"]
colors.insert(1, "green")
print(colors)  # ['violet', 'green', 'indigo', 'blue']

# extend()
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]

colors.extend(rainbow)
print(colors)  # ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# List concatenation
colors1 = ["violet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]

print(colors1 + colors2)  # ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# remover()
colors = ["red", "green", "blue", "green"]
colors.remove("green")
print(colors)  # ['red', 'blue', 'green']

# pop
num = [10, 20, 30, 40]
num.pop()  # Without index
print(num)  # [10, 20, 30]

num = [10, 20, 30, 40]
num.pop(1)  # With index
print(num)  # [10, 30, 40]

# clear()
colors = ["red", "green", "blue"]
colors.clear()
print(colors)  # []

# del
colors = ["red", "green", "blue"]
del colors[1]  # delete element by index
print(colors)  # ['red', 'blue']

del colors  # delete entire list
# print(colors)  # error bcoz list of 'colors' are deleted











