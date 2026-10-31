def average(a=9, b=1):  # default arguments
    print("The average is:", (a+b)/2)
    
average()  # The average is: 5.0    
average(1, 5)  # The average is: 3.0     
average(7)  # The average is: 4.0 -> Here 7 will be assigned to a and b's default value(1) will be taken automatically
average(b=3)  # The average is: 6.0 -> Here b's value is 3 and a's default value(9) will be taken automatically

# Keyword arguments
average(b = 8, a = 7)  # The average is: 7.5  

# -----------------------------------------------------------------------------------------------------------------------

def name(fname, mname="Jhon", lname="whatson"): 
    print("Hello,", fname, mname, lname)

name("Amy")  # Hello, Amy Jhon whatson
name("Ankit", "Kumar", "Mishra")  # Hello, Ankit Kumar Mishra

# -----------------------------------------------------------------------------------------------------------------------

def averageOfThreeNum(a, b, c=1):  
    print("The average is:", (a+b+c)/3)
    
averageOfThreeNum(5, 6)  # The average is: 4.0 -> Here a & b are required arguments

# -----------------------------------------------------------------------------------------------------------------------

# Variable length Arguments
def VarLenArgu(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum += i
    print("The average is:", sum/len(number ))    
    
VarLenArgu(1, 2, 3, 4)   
# <class 'tuple'>
# The average is: 2.5 