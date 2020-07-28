import copy

def complement(perm):
    n = len(perm)
    sortedElements = sorted(copy.deepcopy(perm))
    complement = [0] * n
    for i in range(n):
        j = sortedElements.index(perm[i])
        complement[i] = sortedElements[n - 1 - j]
    return complement
        
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

def convertPerm(perm):
    if len(perm) <= 1:
        return perm
    maxIndex, minIndex = maximalElements(perm)
    if minIndex < maxIndex:
        perm = complement(perm)
        minIndex = maxIndex
    return convertPerm(perm[0:minIndex]) + [perm[minIndex]] + convertPerm(perm[minIndex + 1:])



            
            
        
