def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print("The Geometric Mean of", a, "and", b, "is", mean)
    
calculateGmean(3, 2)  # 1.2
calculateGmean(9, 8)  # 4.235294117647059

# -----------------------------------------------------------------------------------------------------------------------

def isGreater(a, b):
    if (a>b):
        print("First number is greater")
    elif (a==b):
        print("Both number are equal")
    else:
        print("Second number is greater")  
        
isGreater(8, 9)  # Second number is greater             
isGreater(10, 8)  # First number is greater            
isGreater(6, 6)  # Both number are equal   
          
# -----------------------------------------------------------------------------------------------------------------------

def islesser(a, b):
    pass

islesser(10, 8)