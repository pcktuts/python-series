# Partial functions
from functools import partial

def multiply(x , y):
    return x * y 

part1 = partial(multiply, 10)
print(part1(20))
print(multiply(10, 20))
