#code for markov chain on alternating permutations, with and without tajima coalescent adjustments

from generationAltPerm import *
from permsToTrees import *
from generateTrees import *
import copy
import random

N = 50
n = 8

def tajimaAlternatingMCMC(startingPerm, samples):
    n = len(startingPerm)
    currentPerm = startingPerm
    sampDic = {}
    for _ in range(samples):
        print(buildTree(complement(convertPerm(currentPerm))))
        if tuple(currentPerm) in sampDic:
            sampDic[tuple(currentPerm)] += 1
        else:
            sampDic[tuple(currentPerm)] = 1
        while True:
            [i, j] = sorted(random.sample(range(n), 2))
            if abs(i - j) > 1:
                break
        isFirst = i == 0
        isLast = j == n - 1
        sigma_i = currentPerm[i]
        sigma_j = currentPerm[j]
        sigma_ip1 = currentPerm[i + 1]
        sigma_jm1 = currentPerm[j - 1]
        firstDecreasing = sigma_i > sigma_ip1
        secondDecreasing = sigma_jm1 < sigma_j 
        if not isFirst:
            if (currentPerm[i - 1] < sigma_j) != firstDecreasing:
                continue
        if not isLast:
            if (sigma_i > currentPerm[j + 1]) != secondDecreasing:
                continue
        if (sigma_j > sigma_ip1) != firstDecreasing:
            continue
        if (sigma_jm1 < sigma_i) != secondDecreasing:
            continue
        otherPerm = copy.deepcopy(currentPerm)
        otherPerm[i] = currentPerm[j]
        otherPerm[j] = currentPerm[i]
        p = random.random()
        if p < min(1, 2 ** (calculateCherries(currentPerm) - calculateCherries(otherPerm))):
            currentPerm = otherPerm
    print(sampDic)


def uniformAlternatingMCMC(startingPerm, samples):
    n = len(startingPerm)
    currentPerm = startingPerm
    sampDic = {}
    for _ in range(samples):
        print(buildTree(complement(convertPerm(currentPerm))))
        if tuple(currentPerm) in sampDic:
            sampDic[tuple(currentPerm)] += 1
        else:
            sampDic[tuple(currentPerm)] = 1
        while True:
            [i, j] = sorted(random.sample(range(n), 2))
            if abs(i - j) > 1:
                break
        isFirst = i == 0
        isLast = j == n - 1
        sigma_i = currentPerm[i]
        sigma_j = currentPerm[j]
        sigma_ip1 = currentPerm[i + 1]
        sigma_jm1 = currentPerm[j - 1]
        firstDecreasing = sigma_i > sigma_ip1
        secondDecreasing = sigma_jm1 < sigma_j 
        if not isFirst:
            if (currentPerm[i - 1] < sigma_j) != firstDecreasing:
                continue
        if not isLast:
            if (sigma_i > currentPerm[j + 1]) != secondDecreasing:
                continue
        if (sigma_j > sigma_ip1) != firstDecreasing:
            continue
        if (sigma_jm1 < sigma_i) != secondDecreasing:
            continue
        temp = currentPerm[i]
        currentPerm[i] = currentPerm[j]
        currentPerm[j] = temp
    print(sampDic)

uniformAlternatingMCMC(generatePerm(n), N)

    



            
            
                
        
    
    
        
