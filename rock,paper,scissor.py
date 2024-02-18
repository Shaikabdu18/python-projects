import random
user=0
computer=0
how=int(input("how many times you want to play:"))
option=["rock","paper","scissor"]
while how>0:
    user_pick=input("Type rock/paper/scissor or q to quit:").lower()
    if user_pick=='q':
       break
    if user_pick not in option:
        print("give correct option")
        continue
    how-=1
    computer_pick=random.randint(0,2)
    c=option[computer_pick]
    print("computerpick:",c)
    if user_pick == "rock" and c=="scissor":
        print("You win")
        user+=1
    elif user_pick == c:
        print("it's a tie")
    elif user_pick == "paper" and c=="rock":
        print("You win")
        user+=1
    elif user_pick == "scissor" and c=="paper":
        print("You win")
        user+=1
    else:
        print("computer win")
        computer+=1
print("Finally You win",user,"times\ncomputer wins",computer,"times")
    
