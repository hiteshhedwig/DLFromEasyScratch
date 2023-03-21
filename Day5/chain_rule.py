import numpy as np
# from Day3 import derivative as derv
from typing import Callable


def derv(func : Callable,
          input_ : np.ndarray,
          delta: float = 0.001) -> np.ndarray:
    
    return (func(input_ + delta) - func(input_ - delta))/ (2*delta)


def sigmoid(x):
    return 1/(1+np.exp(-x))

def square(x):
    return x * x


def chain_deriv_2(chain,
                  input_range):
    
    f1 =  chain[0]
    f2 =  chain[1]


    f1_of_x = f1(input_range)

    # derivative of f1
    df1dx =  derv(f1, input_range)

    # derivative of f2(f1)
    df2du = derv(f2 , f1_of_x)

    # multiply both  
    return df1dx * df2du

def main():
    chain_1 = [sigmoid, square]

    out = chain_deriv_2(chain_1, 4)
    print(out)

if __name__ == '__main__':
    main()
