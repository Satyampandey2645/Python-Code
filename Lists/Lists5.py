# ---------------------------------------------------- Lists Methods ----------------------------------------------------

l = [11, 9, 8, 2, 4, 6]

m = l  # not recommended becoz any operation on m will also change l. So, to not change l we can use copy() method
m[0] = 0
print(m)  # [0, 9, 8, 2, 4, 6]
print(l)  # [0, 9, 8, 2, 4, 6]

# copy()
lst1 = [11, 9, 8, 2, 4, 6]
n = lst1.copy()
n[0] = 0
print(n)  # [0, 9, 8, 2, 4, 6]
print(lst1)  # [11, 9, 8, 2, 4, 6] -> no effect happened on original list lst1

# insert()
lst2 = [11, 9, 8, 2, 4, 6]
lst2.insert(1, 899)
print(lst2)  # [11, 899, 9, 8, 2, 4, 6]

# extend()
lst3 = [11, 9, 8, 2, 4, 6]
lst4 = [900, 1000, 1100]

lst3.extend(lst4)  
print(lst3)  # [11, 9, 8, 2, 4, 6, 900, 1000, 1100]

# by extend() method lst3 will change and if we don't want to change any variable and want to concatenate two variable then
lst5 =  [11, 9, 8, 2, 4, 6]
lst6 = [900, 1000, 1100]

k = lst5 + lst6
print(k)  # [11, 9, 8, 2, 4, 6, 900, 1000, 1100]