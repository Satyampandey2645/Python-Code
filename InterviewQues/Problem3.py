name = "python"

if name == "java" or "html":  # This condition will always be true
    print("Login Successful")  # Login Successful -> 
else:
    print("Authentication Failed")  
    
# Correct way      
if name == "java" or name == "html":
    print("Login Successful")
else:
    print("Authentication Failed")  # Authentication Failed
    
# Cleaner and recommended way  (using in):
if name in ("java", "html"):
    print("Login Successful")
else:
    print("Authentication Failed")  # Authentication Failed

    