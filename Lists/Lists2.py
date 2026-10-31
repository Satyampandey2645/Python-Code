# printing range of list items

marks = [4, 5, 6, "Harry", True]

print(marks)  # [4, 5, 6, 'Harry', True]
print(marks[:])  # [4, 5, 6, 'Harry', True] -> by default compile understand it as marks[0:len(marks)] => marks[0:5]
print(marks[1:])  # [5, 6, 'Harry', True] -> from 1st index(included) to last index
print(marks[1:4])  # [5, 6, 'Harry'] -> from 1st index(included) to 3r index (4th excluded)
print(marks[1:-1])  # [5, 6, 'Harry'] -> Same as marks[1:4] bcoz marks[1:len(marks)-1] => marks[1:5-1] => marks[1:4]

# -----------------------------------------------------------------------------------------------------------------------
# jumpIndex

var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(var[1::1])  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(var[1:11:1])  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(var[1:10:1])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(var[1:10:2])  # [2, 4, 6, 8, 10]
print(var[1:11:2])  # [2, 4, 6, 8, 10]
print(var[1:11:3])  # [2, 5, 8, 11] 
