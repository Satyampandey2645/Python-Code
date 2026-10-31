# ----------------------------------- Implicit Typecasting (Implicit Type Conversion) -----------------------------------

a = 10      # int
b = 2.5     # float
c = a + b
print(c)  # 12.5
print(type(c))  # <class 'float'>

# -----------------------------------------------------------------------------------------------------------------------

x = 5
y = True
z = x + y  # (True is treated as 1)
print(z)  # 6
