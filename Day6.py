# Custom decorators for functions
from typing import Callable
from functools import wraps
from time import perf_counter, sleep

def get_time(func: Callable) -> Callable:
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper __doc__"""
        start_time: float = perf_counter()
        result = func(*args, **kwargs)
        end_time: float = perf_counter()
        print(f"'{func.__name__}()' took {end_time - start_time:.3f} seconds")
        return result
    
    return wrapper

@get_time
def multiply(a, b):
    """Multiply __doc__"""
    print(f'Calculating: {a} * {b}')
    sleep(2)
    print(f'{a} * {b} = {a * b}')
    return a * b

multiply(2,7)    
# print(multiply.__name__)
# print(multiply.__doc__)
