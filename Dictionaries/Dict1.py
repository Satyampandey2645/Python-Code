dic = {
    344 : "Harry",
    56  : "Satyam",
    678 : "Shivam",
    567 : "Aditya"
}

print(dic)  # {344: 'Harry', 56: 'Satyam', 678: 'Shivam', 567: 'Aditya'}
print(dic[344])  # Harry
print(dic[567])  # Aditya

print(dic.get(56))  # Satyam
print(dic.get(678))  # Shivam


info = {
    'name' : "Karan",
    'age'  : 19,
    'eligible' : True
}

print(info)  # {'name': 'Karan', 'age': 19, 'eligible': True}
print(info["name"])  # Karan
print(info.get("eligible"))  # True

print(info.get("address"))  # None -> this will give none when item is not in the dictionary 'info'
print(info["address"])  # KeyError -> this will throw KeyError becoz item is not in the dictionary 'info

