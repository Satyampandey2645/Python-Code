# ----------------------------------- Explicit Typecasting (Explicit Type Conversion) -----------------------------------

a = "1"
b = "2"

print(a+b)  # 12
print(int(a)+int(b))  # 3

# -----------------------------------------------------------------------------------------------------------------------

x = "Satyam"
y = "Pandey"

print(x+y)  # SatyamPandey
# print(int(x)+int(y))  # This will throw an error

# -----------------------------------------------------------------------------------------------------------------------

string = "15"
number = 7

string_number = int(string)  # throws an error if the string is not a valid integer
sum = number + string_number
print("The sum of both the number is", sum)  # The sum of both the number is 22