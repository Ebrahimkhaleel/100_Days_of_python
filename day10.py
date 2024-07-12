#ROCK PAPER SCISSORS
import random 
user_wins=0
computer_wins=0
options=["rock","paper", "scissors"]
while True:
    user_input=input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number= random.randint(0,2)
    #0 : represents rock, 1: represents paper, 2:represents scissors
    c_picks=options[random_number]
    print("computer picked", c_picks)
    if c_picks == "rock" and user_input=="scissors":
        print("you won")
        user_wins+=1
    elif c_picks == "paper" and user_input=="rock":
        print("you won")
        user_wins+=1  
        
    elif c_picks == "scissors" and user_input=="paper":
        print("you won")
        user_wins+=1
    elif c_picks == "scissors" and user_input=="scissors":
        print("A draw")
    elif c_picks == "paper" and user_input=="paper":
        print("A draw") 
    elif c_picks == "rock" and user_input=="rock":
        print("A draw")    
       
    else:
        print("computer won")
        computer_wins+=1 
        
print(f"the computer won {computer_wins} times and you won {user_wins} times.")        
print('Goodbye')

