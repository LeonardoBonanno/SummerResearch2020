# generate uniformly random alternating permutation

import numpy as np
import random
import math

N = 30
TRIALS = 1

def update(u, x):
    return (2 / math.pi) * math.asin(u * math.sin(math.pi * (1 - x)/2))

def calculateAlpha(x_n, x_0):
    return math.cos(math.pi * x_n/ 2) / math.cos(math.pi * x_0/ 2)

def generateX(n, acceptance):
    X = [0] * n
    first = True
    while True:
        U = [random.random() for i in range(n)]
        X[0] = U[0]
        for i in range(1, n):
            X[i] = update(U[i], X[i-1])
        alpha = calculateAlpha(X[n-1], X[0])
        p = random.random()
        acceptProb = 1 / (alpha + 1 / alpha)
        acceptance.append(2 * acceptProb)
        if p < 2 * acceptProb:
            first = p < acceptProb
            break
    return X, first

def generateY(first, X, n):
    Y = [0] * n
    increment, start = (1, 0) if first else (-1, n - 1)
    for i in range(n):
        if i % 2 == 0:
            Y[i]= X[start + increment * i]
        else:
            Y[i] = 1 - X[start + increment * i]
    return Y

def convertPerm(sigma_prime, n):
    sigma = [0] * n
    for i in range(n):
        sigma[i] = sigma_prime.index(i) + 1
    return sigma
    
def generatePerm(n, acceptance):
    X, first = generateX(n, acceptance)
    Y = generateY(first, X, n)
    return convertPerm(list(np.argsort(Y)), n)

def testMethod(trials, n):                       
    perms = dict()
    acceptance = []
    for i in range(trials):
        perm = tuple(generatePerm(n, acceptance))
        if perm in perms:
            perms[perm] += 1
        else:
            perms[perm] = 1
    print(len(perms))
    print(sum(acceptance)/len(acceptance))
    #for entry in perms.keys():
        #print(entry, perms[entry] * 100 / trials, " %")

testMethod(10000, 100)

        
    
    

    

        
        
    
