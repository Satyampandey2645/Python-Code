# ---------------------------------------- String formating using format() method ---------------------------------------

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Satyam"

print(letter.format(name, country))  # Hey my name is Satyam and I am from India
print(letter)  # Hey my name is {} and I am from {}

print(letter.format(country, name))  # Hey my name is India and I am from Satyam
# so, to resolve this issue below format is used


myInfo = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Satyam"

print(myInfo.format(country, name))  # Hey my name is Satyam and I am from India


txt = "For only {price:.2f}"
print(txt.format(price = 49.09999))  # For only 49.10  -> .2f shows 2 digits after decimal  

# ----------------------------------------------------- f-string -------------------------------------------------------

print(f"Hey my name is {name} and I am from {country}")  # Hey my name is Satyam and I am from India

price = 89.09999
txt = f"For only {price:.2f}"
print(txt)  # For only 89.10

print(f"{2*30}")  # 60
print(type(f"{2*30}"))  # <class 'str'>

# This f-string demonstrates how to print literal curly braces by escaping them with double braces {{ }} instead of substituting variables.
print(f"We use f-string like this: Hey my name is {{name}} and I am from {{country}}") 
# We use f-string like this: Hey my name is {name} and I am from {country} 