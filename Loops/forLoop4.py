for i in range(5):
    print(i)
else:
    print("Sorry no i")  
# 0 1 2 3 4 Sorry no i -> (in the next line of each other)  
# Here else statement is printed means loop is ended (not break) 

# -----------------------------------------------------------------------------------------------------------------------

for i in []:
    print(i)
else:
    print("Sorry no i in list")  # Sorry no i in list 
    
# -----------------------------------------------------------------------------------------------------------------------
        
for i in [1, 2, 3]:
    print(i)
else:
    print("Sorry no more i left in list")  # Sorry no i in list    
# 1 2 3 Sorry no more i left in list -> (in the next line of each other)  

# -----------------------------------------------------------------------------------------------------------------------

for i in range(6):
    print(i)
    if i == 4:
        break
else: 
    print("Sorry Sorry") 
# 0 1 2 3 4  
# Here else statement is not printed it means loop is break        