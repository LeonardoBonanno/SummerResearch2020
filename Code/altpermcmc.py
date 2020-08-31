# code for markov chain on alternating permutations, with and without tajima coalescent adjustments

# imports
from generationAltPerm import *
from permsToTrees import *
from generateTrees import *
import copy
import random

# constants
N = 5000
samples = 100

# helper function for generating two numbers that differ by more than one
def generateIJ(n):
    while True:
            [i, j] = sorted(random.sample(range(n), 2))
            if abs(i - j) > 1:
                break
    return i, j

# swaps two elements if tajima allows for it
def updateIJ(currentPerm, i, j, tajima):
    if tajima:
        otherPerm = copy.deepcopy(currentPerm)
        sigma_i = currentPerm[j]
        sigma_j = currentPerm[i]
        otherPerm[i] = currentPerm[j]
        otherPerm[j] = currentPerm[i]
        p = random.random()
        if p < min(1, 2 ** (calculateCherries(currentPerm) - calculateCherries(otherPerm))):
            currentPerm[i] = sigma_i
            currentPerm[j] = sigma_j
    else:
        temp = currentPerm[i]
        currentPerm[i] = currentPerm[j]
        currentPerm[j] = temp

# helper function, whether swapping of two elements is allowed
def canUpdate(currentPerm, n, i, j):
    isFirst = (i == 0)
    isLast = (j == n - 1)
    sigma_i = currentPerm[i]
    sigma_j = currentPerm[j]
    sigma_ip1 = currentPerm[i + 1]
    sigma_jm1 = currentPerm[j - 1]
    firstDecreasing = (sigma_i > sigma_ip1)
    secondDecreasing = (sigma_jm1 < sigma_j) 
    if not isFirst:
        if (currentPerm[i - 1] < sigma_j) != firstDecreasing:
            return False
    if not isLast:
        if (sigma_i > currentPerm[j + 1]) != secondDecreasing:
            return False
    if (sigma_j > sigma_ip1) != firstDecreasing:
        return False
    if (sigma_jm1 < sigma_i) != secondDecreasing:
        return False
    return True

# implements MCMC markovian update 
def update(currentPerm, n, tajima):
    i, j = generateIJ(n) 
    if canUpdate(currentPerm, n, i, j):
        updateIJ(currentPerm, i, j, tajima)

def difference(first, second, n):
    total = 0
    for i in range(n):
        if first[i] != second[i]:
            total += 1
    return total
    
# alternating permutation MCMC with element swapping
# tajima for whether want to metropolize the chain to converge to tajima
# printTrees for whether want to print trees as we go
def alternatingPermMCMC(startingPerm, samples, tajima, printTrees):
    n = len(startingPerm)
    currentPerm = startingPerm
    sampDic = {}
    total = 0
    currentRep = [(0,0,0)] * n
    for _ in range(samples):
        c = calculateCherries(currentPerm)
        if printTrees:
            tree = buildTree(complement(convertToTreePerm(currentPerm)))
            newRep = tree.getTree()
            total += difference(newRep, currentRep, n)
            currentRep = newRep
            #print(tree)
        if tuple(currentPerm) in sampDic:
            sampDic[tuple(currentPerm)] += 1
        else:
            sampDic[tuple(currentPerm)] = 1
        update(currentPerm, n, tajima)
    print((total - n)/samples)
    #for entry in sampDic:
        #print(entry, "has frequency", sampDic[entry] * 100 / samples, "%")

def main():
    alternatingPermMCMC(generateUniformPerm(N), samples, False, True)

main()

    



            
            
                
        
    
    
        
