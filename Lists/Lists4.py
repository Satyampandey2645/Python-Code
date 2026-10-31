# ---------------------------------------------------- Lists Methods ----------------------------------------------------

# append() 
l = [11, 9, 8, 2, 4, 6]
print(l)  # [11, 9, 8, 2, 4, 6]
a = l.append(7)
print(a)  # None
print(l)  # [11, 9, 8, 2, 4, 6, 7]

# sort() 
b = l.sort()
print(b)  # None
print(l)  # [2, 4, 6, 7, 8, 9, 11]

# sort() with reverse=True parameter for sorting in descending order
c = l.sort(reverse=True)
print(c)  # None
print(l)  # [11, 9, 8, 7, 6, 4, 2]

# reverse()
lst1 = [42, 32, 7, 1, 4, 3]
d = lst1.reverse()
print(d)  # None
print(lst1)  # [3, 4, 1, 7, 32, 42]

# index()
lst2 = [42, 32, 7, 1, 4, 3]
print(lst2.index(7))  # 2
print(lst2.index(32))  # 1

# count()
lst3 = [4,2,5,3,6,1,2,1,2,8,9,7]
print(lst3.count(2))  # 3
print(lst3.count(1))  # 2

