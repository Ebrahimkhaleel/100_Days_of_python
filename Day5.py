#itemgetter library
# The itemgetter function from operator library allows you to retrieve specific elements 
# from an iterable object (like a list, tuple, or dictionary) in a concise way.

from operator import itemgetter

fruits=['apple','melon','banana','pineapple','guava',"cherry", "orange"]
#accessing list items using index
first_mid_last=itemgetter(0,len(fruits)//2,-1)(fruits)
print(first_mid_last)

# Access dictionary values using keys
person = {"name": "Alice", "age": 30}
name_age = itemgetter("name",'age')(person)
print(name_age)

# accessing items in a tuple and set
tuople=(1,23,4,4,7,8)
seet={'hi',2,6,'load',7,'car'}

new=itemgetter(1,-1)(seet)
new1=itemgetter(1,-1)(tuople)
print(new)
print(new1)

