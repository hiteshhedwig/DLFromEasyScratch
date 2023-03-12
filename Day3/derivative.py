import numpy as np
from typing import Callable
import math

# derviative of math.exp will not change
def expFunction(x):
    return math.exp(x)

def constantFunction(x):
    return 3

def linearFunction(x):
    return x

def deriv(func : Callable,
          input_ : np.ndarray,
          delta: float = 0.001) -> np.ndarray:
    
    return (func(input_ + delta) - func(input_ - delta))/ (2*delta)

if __name__ == '__main__':
    exp_out = deriv(expFunction, 2)
    print("exponential function derivative when e^x :", 
          exp_out)
    
    const_out = deriv(constantFunction,2)
    print("constant function derivative    when y = 2, irrespective of x :", 
          const_out)
    
    linear_out = deriv(linearFunction,2)
    print("linear function derivative      when y = x  :", 
          linear_out)