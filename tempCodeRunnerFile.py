from itertools import batched

my_list : list[float]=[2,5,6,7,4,2,6,7,4,5,6,7,8,1,0]
batch: batched =batched(my_list,n=3)
print(batch)