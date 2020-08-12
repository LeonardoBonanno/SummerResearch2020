# code to convert random alternating permutation to its tree permutation using the bijection from Donaghey

# imports
import copy

# generates complement of a permutation defined in Donaghey
def complement(perm):
    n = len(perm)
    sortedElements = sorted(copy.deepcopy(perm))
    complement = [0] * n
    for i in range(n):
        j = sortedElements.index(perm[i])
        complement[i] = sortedElements[n - 1 - j]
    return complement

# returns index of max and minimal elements of a permutation   
def maximalElements(perm):
    minVal = float("inf")
    maxVal = 0
    minIndex = 0
    maxIndex = 0
    for i in range(len(perm)):
        if perm[i] < minVal:
            minVal = perm[i]
            minIndex = i
        if perm[i] > maxVal:
            maxVal = perm[i]
            maxIndex = i
    return maxIndex, minIndex

# converts regular permutation to its tree permutation form recursively
def convertToTreePerm(perm):
    if len(perm) <= 1:
        return perm
    maxIndex, minIndex = maximalElements(perm)
    if minIndex < maxIndex:
        perm = complement(perm)
        minIndex = maxIndex
    return convertToTreePerm(perm[0:minIndex]) + [perm[minIndex]] + convertToTreePerm(perm[minIndex + 1:])

# returns index and value of minimal element in a permutation
def minimalElement(perm):
    minVal = float("inf")
    minIndex = 0
    for i in range(len(perm)):
        if perm[i] < minVal:
            minVal = perm[i]
            minIndex = i
    return minIndex, minVal

# returns index and value of maximal element in a permutation
def maximalElement(perm):
    maxVal = 0
    maxIndex = 0
    for i in range(len(perm)):
        if perm[i] > maxVal:
            maxVal = perm[i]
            maxIndex = i
    return maxIndex, maxVal

# calculate the number of cherries in a regular permutation
def calculateCherries(perm):
    convertedPerm = convertToTreePerm(perm)
    cherries = [0]
    calculateCherriesHelper(convertedPerm, cherries)
    return cherries[0]

# helper function to calculate number of cherries in a permutation
def calculateCherriesHelper(perm, cherries):
    n = len(perm)
    if n == 1:
        cherries[0] += 1
    minIndex, minVal = minimalElement(perm)
    if minIndex != 0:
        calculateCherriesHelper(perm[:minIndex], cherries)
    if minIndex != n - 1:
        calculateCherriesHelper(perm[minIndex + 1:], cherries)




            
        
