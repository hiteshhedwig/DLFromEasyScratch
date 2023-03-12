import math
from typing import Callable

# derviative of math.exp will not change
def exp_function(x):
    return math.exp(x)


def linear_function(x):
    return x

def chained_function(func1 : Callable, 
                     func2 : Callable,
                     input_):
    return func2(func1(input_))

if __name__ == '__main__':
    out = chained_function(linear_function, exp_function, 3)
    print(out)