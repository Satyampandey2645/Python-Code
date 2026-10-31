# Case 3: Using finally Block (Correct Way ✅)

def func():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred") 
        return 0   
    finally:
        print("I'm always executed") 
        
x = func()
print(x)    


'''
Explanation:
    * finally runs before returning
    * Runs whether:
        -> index is valid
        -> index is invalid
        -> exception occurs
    * Ensures cleanup / final statements always execute
'''       