#NUMBER GUESSING GAME
#importing the random module
import random
#collecting user input
number_range=input("guess the number: ") 
#an if statement to ensure we have a digit from our input
if number_range.isdigit():
    #coverting our input to integer 
    number_range=int(number_range)
    if number_range <=0:
        print("enter a number greater than zero")
        #quiting the program as the number we have is less than or equal to zero
        quit()
else:
    print("print a number next time")
    #quiting as the input is not a digit 
    quit()
x=random.randint(0,number_range)
guesses=0

while True:
    guesses +=1
    guess=input('enter your guess: ')
    if guess.isdigit():
    #coverting our input to integer 
        guess=int(guess)
        if guess <=0:
            print("enter a number greater than zero")
            #quiting the program as the number we have is less than or equal to zero
            quit()
    else:
        print("print a number next time")
        #quiting as the input is not a digit 
        #the continue statement to go back to the loop again
        continue
    
    if guess==x:
        print('you got it right')
        break
        #if not gotten right its either the guess is less than or greater than
    elif guess> x:
        print('guess greater than number')
    else:
        print('guess was below the number')
            #prints the number of guesses made
    print(f"the number of guesses are: {guesses}")
    