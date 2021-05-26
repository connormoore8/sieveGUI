import numpy as np
import pandas as pd

def sieve(X, n):
    return np.setdiff1d(X,[n**2 + n*y for y in range(0,len(X)//n)])

if __name__ == '__main__':
    X = np.linspace(2,100,99, dtype=int)
    for x in X:
        X=sieve(X, x)
    print(X)




