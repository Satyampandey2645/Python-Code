a = 1;
b = True;
c = "Satyam"
d = None
e = 1.1;
f = complex(2, -3);

print(f);  # (2-3j)

print("The type of a is ", type(a));  # The type of a is  <class 'int'>
print("The type of b is ", type(b));  # The type of b is  <class 'bool'>
print("The type of c is ", type(c));  # The type of c is  <class 'str'>
print("The type of d is ", type(d));  # The type of d is  <class 'NoneType'>
print("The type of e is ", type(e));  # The type of e is  <class 'float'>
print("The type of f is ", type(f));  # The type of f is  <class 'complex'>

# ---------------------------------------------------- list -----------------------------------------------------

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]] 
print(list1)  # [8, 2.3, [-4, 5], ['apple', 'banana']]

# ---------------------------------------------------- tuple ----------------------------------------------------

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))  
print(tuple1);  # (('parrot', 'sparrow'), ('Lion', 'Tiger'))

# ----------------------------------------------------- dict ----------------------------------------------------

dict1 = {"name":"Satyam", "age": 21, "canVote": True}
print(dict1);  # {'name': 'Satyam', 'age': 21, 'canVote': True}