import random
print("Welcome to Number Guessing game:) ")
a=int(input("Enter a maximum number:"))
rn=random.randint(0,a)
if a<=0:
    print("give number more than zero")
    quit()
guess=0
while True:
    guess+=1
    b=int(input("Enter number to guess:"))
    if b<=0:
        print("give number more than zero")
        quit()
    elif b==rn:
        print("you got it:)")
        break
    elif b>rn:
        print("you entered more than a number")
    else:
        print("You eneterd less than anumber")
print("you guessed correctly with this",guess,"attempt")
        
    
