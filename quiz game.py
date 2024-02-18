print("hii Welcome to the quiz game")
score=0
a=input("Shall we start the game:").lower()
if a =="yes":
    print("Let's go")
else:
    quit()
a=input("973 runs scored cricketer in IPL:").lower()
if a=="virat":
    print("Correct")
    score+=1
else:
    print("Incorrect")
a=input("264 scored batsman:").lower()
if a=="rohit":
    print("Correct")
    score+=1
else:
    print("Incorrect")
a=input("175 scored cricketer:").lower()
if a=="gayle":
    print("Correct")
    score+=1
else:
    print("Incorrect")
a=input("most winning captain:").lower()
if a=="dhoni":
    print("Correct")
    score+=1
else:
    print("Incorrect")
print("Your score is",score,"out of 4")



