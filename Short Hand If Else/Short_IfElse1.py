a = 330
b = 3303
print("A") if a > b else print("=") if a == b else print("B")  # B

print(9) if a < b else ""  # 9
print(10) if a > b else ""  # Nothing will get printed because here else statement will execute and it has nothing to print

c = 9 if a > b else 0
print(c)  # 0 -> becoz a is less than b so else will execute

# ----------------------------------------------------------------------------------------------------------------------- 

x = 330000
y = 3303

z = 9 if x > y else 0
print(z)  # 9

# -----------------------------------------------------------------------------------------------------------------------

marks = 60

status = "Pass" if marks >= 40 else "Fail"
print(status)  # Pass
 