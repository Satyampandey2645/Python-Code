i = 0
while(i < 7):
    print(i)
    i = i + 1
else:
    print("sorry sorry")  
# 0 1 2 3 4 5 6 sorry sorry (in the next line of each other)   
# Here else statement is printed means loop is ended (not break) 

# -----------------------------------------------------------------------------------------------------------------------
  
i = 0
while(i < 7):
    print(i)
    i = i + 1
    if i == 4:
        break
else:
    print("sorry sorry")  
# 0 1 2 3     
# Here else statement is not printed it means loop is break 