# Multiple Objects
print("13", "03", "2004")  # 13 03 2004

# sep=""
print("13", "03", "2004", sep="-")  # 13-03-2004
print("13", "03", "2004", sep="=>")  # 13=>03=>2004

# end=""
print("13", "03", "2004", end=":")  # 
print()

# file
with open("PrintPara/output.txt", "w") as f:  # this creates output.txt file and Hello is written in this file
    print("Hello", file=f)  
    
# flush
print("Loading...", end="", flush=True)
print()
print("Done")

print("Wait...", flush=False)
print("Hi")

# ---------------------------------------------------------------------------------------------------------------
import time

print("Sssssssshhhhhhhh...", flush=False)
time.sleep(5)
print("Hello")

print("Hmmmmm...", flush=True)
time.sleep(5)
print("Hello")
    