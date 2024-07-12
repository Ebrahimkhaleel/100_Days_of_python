#CHOOSE YOUR ADVENTURE
print("welcome to choose an adventure to survive")
name=input('Enter your name: ')
print('Welcome ', name)

a1=input("You just moved and encounterd a block, do you want to go left or right? ").lower()
if a1=='left':
    l1=input("you moved left and you are in river, enter swim to swim across or walk to walk across. ")
    if l1=='swim':
        print('you were klled by a crocodile')
    elif l1=='walk':
        print()
    else:
        print('response not valid')
elif a1=='right':
    r1=input("you moved right and you are in middle of the road, enter cross to cross the road  or go back to not to cross. ")
    if r1=='cross':
        print('you were klled by a crocodile')
    elif r1=='go back':
        print()
    else:
        print('response not valid')