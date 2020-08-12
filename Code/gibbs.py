# File: gibbs sampling on tridiagonal stochastic matrices to alternating permutations

# imports
import numpy as np
import random
import math
from generationAltPerm import generateY, convertToPerm

# constants
samples = 1000000
N = 6

# markovian update for gibs sampling
def update(X, n):
    i = random.sample(range(n), 1)[0]
    first = (i == 0)
    last = (i == n - 1)
    p = random.random()
    allow = (first) or (X[i - 1] + p < 1)
    if allow and (last or (X[i + 1] + p < 1)):
        X[i] = p

# generate a length n stochastic matrix
def generateStochastic(n, steps):
    X = [0] * n
    for _ in range(steps):
        update(X, n)
    return X

# convert stochastic matrix to alternating sequence of reals  
def convertToAlternating(X, forward, n):
    Y = [0] * n
    for i in range(n):
        if i % 2 == 0:
            Y[i]= X[i]
        else:
            Y[i] = 1 - X[i]
    return Y

# convert sequence of reals to alternating permutation
def sequenceToPerm(C, n):
    Y = generateY(C, True, n)
    return convertToPerm(list(np.argsort(Y)), n)

# gibbs sampling of real sequences (tridiagonal stochastic matrices), using the method described in Diaconis
def gibbsSampling(samples, n):                       
    perms = dict()
    C = generateStochastic(n, int(10 * n * math.log(n)))
    perm = tuple(sequenceToPerm(C, n))
    perms[perm] = 1
    for _ in range(samples):
        update(C, n)
        perm = tuple(sequenceToPerm(C,n))
        if perm in perms:
            perms[perm] += 1
        else:
            perms[perm] = 1
    for entry in perms:
        print(entry, perms[entry] * 100 / (samples + 1), " %")

def main():
    gibbsSampling(samples, N)

main()
        




        
    
    

    
