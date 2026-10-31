import time

hour=int(time.strftime('%H'))
mint=int(time.strftime('%M'))

print(f"The current time is {hour}:{mint}")

if hour>=0 and hour<12 :
    print("Good morning");
elif hour>=12 and hour<17 : 
    print("Good afternoon");
elif hour>=17 and hour<19: 
    print("Good evening")
else:
    print("Good night")