tup1 = (1, 5, 6)
print(type(tup1))  # <class 'tuple'>
print(tup1)  # (1, 5, 6)

tup2 = (1)  # for single element it will give type int. So, to make this tuple we need to give comma after that element (tup3) 
print(type(tup2))  # <class 'int'>
print(tup2)  # 1

tup3 = (1,)  # Now this is tuple of single element
print(type(tup3))  # <class 'tuple'>
print(tup3)  # (1,)

tup4 = (1, 2, 76, 342, 32, "green", True)
print(type(tup4))  # <class 'tuple'>
print(tup4)  # (1, 2, 76, 342, 32, 'green', True)
print(len(tup4))  # 7

# positive indexing
print(tup4[0])  # 1
print(tup4[1])  # 2
print(tup4[5])  # green
print(tup4[6])  # True

# negative indexing
print(tup4[-1])  # True  -> similar to tup4[len(tup4)-1] => tup4[7-1] => tup4[6]
print(tup4[-2])  # green
print(tup4[-4])  # 342
print(tup4[-7])  # 1

if 342 in tup4:
    print("Yes, 342 is present")  # Yes, 342 is present
else:
    print("No, 342 is absent")
    
if 3421 in tup4:
    print("Yes, 3421 is present")
else:
    print("No, 3421 is absent")  # No, 3421 is absent
    
# Range of Index
tup5 = (1, 2, 76, 342, 32, "green", True)
print(tup5[1:4])  # (2, 76, 342) -> 1st index(included) to 4th index(excluded) 
print(tup5[0:])  # (1, 2, 76, 342, 32, 'green', True) -> Similar to tup5[0:len(tup5)] => tup5[0:7]
print(tup5[:3])  # (1, 2, 76) -> Similar to tup5[0:3] -> 0th index(included) to 3rd index(excluded)
print(tup5[:])  # (1, 2, 76, 342, 32, 'green', True) -> Similar to tup5[0:len(tup5)] => tup5[0:7]





