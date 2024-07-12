print("Welcome to kherleelu's game")
game=input('Do you want to play my game? ')

if game.lower() != 'yes':
    quit()
print("Alright let's play")
score=0
Question1=input('What is the slogan for Plateau State? ')

if Question1.lower()=='home of peace and tourism':
    print('correct')
    score+=1
else:
    print('incorrect')
Question2=input('What is the capital of borno State? ')

if Question2.lower()=='maiduguri':
    print('correct')
    score+=1
else:
    print('incorrect')

Question3=input('What is the capital of nigeria? ')

if Question3.lower()=='abuja':
    print('correct')
    score+=1
else:
    print('incorrect')  

Question4=input('When did nigeria get her independence? ')

if Question4.lower()=='1960':
    print('correct')
    score+=1
else:
    print('incorrect')   
    
Question5=input('What is the capital of Saudi Arabia? ')

if Question5.lower()=='riyadh':
    print('correct')
    score+=1
else:
    print('incorrect')         

print(f'you got {score} question correct!')
print(f'you got {score/5 *100} %')
