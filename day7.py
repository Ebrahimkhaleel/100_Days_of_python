import numpy as np
np.random.seed(123)

outcomes=[]
for x in range(10):
    dice=np.random.randint(0,2)
    if dice == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
print(outcomes)
##2
tails=[0]
for x in range(10):
    dice=np.random.randint(0,2)
    tails.append(tails[x] + dice)
print(tails)    


    
                