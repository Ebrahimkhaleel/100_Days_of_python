#splitting list into same equal pieces
from typing import List, Generator
import random

def batched(iterable: List[float], n: int) -> Generator[List[float], None, None]:
    """Batch data into lists of length n. The last batch may be shorter."""
    for i in range(0, len(iterable), n):
        yield iterable[i:i + n]

# Your list
my_list=[2, 5, 6, 7, 4, 2, 6, 7, 4, 5, 6, 7, 8, 1, 0]
my1_list: List[float] = random.sample(my_list,len(my_list))

# Create batches
batch = batched(my1_list, n=2)

# Print batches
print(list(batch))
