import random

number_=input('Enter a number')
if number_.isdigit():
    number_=int(number_)
    if number_ <=0:
        print("enter a number greater than zero")
        quit()
else:
    print('enter a number next time')
    quit()
number=random.randint(0,number_)
guesses=0

while True:
    guesses += 1
    guess=input('enter your guess')
    if guess.isdigit():
        guess=int(guess)
        if number_ <=0:
            print("enter a number greater than zero")
            quit()
    else:
        print('enter a number next time')
        continue
    if number == guess:
        print('you got it right')
        break
    elif number > guess:
        print('guess greater than number')
    elif number < guess:
        print('guess less than number')
    else:
        print('guess was below the number')
            #prints the number of guesses made
    print(f"the number of guesses are: {guesses}")   
