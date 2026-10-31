marks = [4, 5, 6, "Harry", True]

print(marks)  # [4, 5, 6]
print(type(marks))  # <class 'list'>
print(len(marks))  # 5

# positive indexing
print(marks[0])  # 4
print(marks[1])  # 5
print(marks[2])  # 6
print(marks[3])  # Harry
print(marks[4])  # True

# negative indexing
print(marks[-3])  # 6  -> same as marks[len(marks)-3] => marks[5-3] => marks[2] => 6

# check whether an item is present in the list or not
if 7 in marks:
    print("Yes")
else: 
    print("No")  # No
    
if "Harry" in marks:
    print("Yes")  # Yes
else: 
    print("No") 
    
# if we check "6" as string present in the list
if "6" in marks:
    print("Yes")
else: 
    print("No")  # No
           