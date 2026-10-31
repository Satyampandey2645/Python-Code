def VarLenArgu(*number):
    sum = 0
    for i in number:
        sum += i
        
    return sum/len(number )  
    
c = VarLenArgu(1, 2, 3, 4)  
print(c)  # 2.5

# -----------------------------------------------------------------------------------------------------------------------

# if we use multiple return statment in our function then first return value will be return finally
def average(a, b):
    return 7
    return (a+b)/2;

ans = average(2, 4)  # Here function will return 7 to ans
print(ans)