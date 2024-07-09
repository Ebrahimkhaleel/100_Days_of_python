#removing duplicates in a list
m_list: list[int]=[1,1,5,2,2,3,4,6,6,4,7,6,8,7,9,7,8,9]

# 1.a sets data type doesnt hold duplicate values but doesnt maintain the order
# interested in arranging them in ascending order
# 2.a dictionary doesnt hold duplicate keys keeping the orders intact

one=set(m_list)
two=dict.fromkeys(m_list)
print(one)
print(two)

print(list(one))
print(list(two))