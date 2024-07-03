#immutability is actually a lie
#initially we know that a string and a dictionary to be unchanged once created can't be changed
word : str ='Khalil'
print("initial" , id(word))
word = word + 'Ibrahim'
print("final" , id(word))
print(word)
#so actually for strings it can overwitten by creating a new variable 
#a new variable with a new id 
point:tuple[float,float]= 3,6
print("initial" , id(point))
point += 7,
print("final" , id(point))
print(point)