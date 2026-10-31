# Case 2: try…except Inside Function (Without finally)

def func():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred") 
        return 0   
    
    print("I'm always executed")  # Now this line in function won't get printed ever without finally block
        
x = func()
print(x)  


'''
Explanation:
    * Function returns from try or except
    * Code after return is never executed
    * That print() is unreachable

📌 This is the real problem
'''         