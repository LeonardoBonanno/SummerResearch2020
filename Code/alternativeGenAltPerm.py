# File implements code to generate a uniformly random alternating permutation
# using a similar method to that described in Marchal
# this method is slightly diffenr in the updates and acceptances, but is about the same

# imports
import numpy as np
import random
import math

# constants
N = 30
TRIALS = 100

# conducts markovian update
def update(x):
    return (2 / math.pi) * math.asin(random.random() * math.cos(math.pi * x/2))

# helper function for calculating acceptance
def calculateAcceptanceProb(x_n, x_0):
    alpha = math.cos(math.pi * x_n/ 2) / math.cos(math.pi * x_0/ 2)
    return 1 / (alpha + 1 / alpha)

# sample tri-diagonal stochastic matrix superdiagonal
def generateX(n, acceptanceProb = None):
    X = [0] * n
    forward = True
    while True:
        X[0] = random.random()
        for i in range(1, n):
            X[i] = update(X[i-1])
        acceptProb = calculateAcceptanceProb(X[n-1], X[0])
        p = random.random()
        if acceptanceProb != None:
            acceptanceProb.append(2 * acceptProb)
        if p < 2 * acceptProb:
            forward = p < acceptProb
            break
    return X, forward

# bijection from stochastic matrix superdiagonal to sequence of alternating reals 
def generateY(X, forward, n):
    Y = [0] * n
    increment, start = (1, 0) if forward else (-1, n - 1)
    for i in range(n):
        if i % 2 == 0:
            Y[i]= X[start + increment * i]
        else:
            Y[i] = 1 - X[start + increment * i]
    return Y

# converts alternating sequence of reals to alternating permutation
def convertToPerm(Y, n):
    sigma_prime = list(np.argsort(Y))
    sigma = [0] * n
    for i in range(n):
        sigma[i] = sigma_prime.index(i) + 1
    return sigma

# generate uniformly random down-up alternating permutation
def generateUniformPerm(n, acceptanceProb = None):
    X, forward = generateX(n, acceptanceProb)
    Y = generateY(X, forward, n)
    return convertToPerm(Y, n)

# code to test this method
# select acceptance if you want to print the average acceptance probability
# select percentages to view the percentages for each permutation
def testMethod(trials, n, acceptance, percentages):                       
    perms = dict()
    acceptanceProb = [] if acceptance else None
    for i in range(trials):
        perm = tuple(generateUniformPerm(n, acceptanceProb))
        if perm in perms:
            perms[perm] += 1
        else:
            perms[perm] = 1
    if acceptance:
        print("Printing acceptance probabilities:")
        print(sum(acceptanceProb)/len(acceptanceProb))
        print("")
    if percentages:
        print("Printing percentages each permutation occurs:")
        for entry in perms:
            print(entry, "has frequency", perms[entry] * 100 / trials, "%")

def main():
    testMethod(trials, N, True, True)

if __name__ == "__main__":
    main()

        
    
    

    
