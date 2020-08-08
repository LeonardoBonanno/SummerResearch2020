import numpy as np
import random
import math

def generateStochastic(n, steps):
    X = [0] * n
    for _ in range(steps):
        update(X, n)
    return X

def update(X, n):
    i = random.sample(range(n), 1)[0]
    first = (i == 0)
    last = (i == n - 1)
    p = random.random()
    allow = (first) or (X[i - 1] + p < 1)
    if allow and (last or (X[i + 1] + p < 1)):
        X[i] = p
    
def convertToAlternating(X, n):
    Y = [0] * n
    for i in range(n):
        if i % 2 == 0:
            Y[i]= X[i]
        else:
            Y[i] = 1 - X[i]
    return Y

def convertPerm(sigma_prime, n):
    sigma = [0] * n
    for i in range(n):
        sigma[i] = sigma_prime.index(i) + 1
    return sigma

def sequenceToPerm(C, n):
    Y = convertToAlternating(C, n)
    return convertPerm(list(np.argsort(Y)), n)

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
    print(len(perms))
    for entry in perms.keys():
        print(entry, perms[entry] * 100 / samples, " %")

samples = 1000000
n = 6
gibbsSampling(samples, n)



        
    
    

    
