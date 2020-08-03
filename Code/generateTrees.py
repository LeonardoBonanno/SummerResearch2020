#code to generate uniformly random Ranked Unlabeled Tree and print it out as an ordered matching

import time
from generationAltPerm import *
from permsToTrees import *

n = 8
N = 20

def generateUniformTree(n):
    return complement(convertPerm(generatePerm(n)))

def mySort(tuple):
    return tuple[2]

def generateUniformTrees(n, samples):
    return [generateUniformTree(n) for _ in range(samples)]

def maximalElement(perm):
    maxVal = 0
    maxIndex = 0
    for i in range(len(perm)):
        if perm[i] > maxVal:
            maxVal = perm[i]
            maxIndex = i
    return maxIndex, maxVal

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRight(self, rightTree):
        self.right = rightTree

    def setLeft(self, leftTree):
        self.left = leftTree

    def calculateCherriesHelper(self, cherries):
        leftEmpty = self.left is None
        rightEmpty = self.right is None
        if leftEmpty and rightEmpty:
            cherries[0] += 1
        if not leftEmpty:
            self.left.calculateCherriesHelper(cherries)
        if not rightEmpty:
            self.right.calculateCherriesHelper(cherries)

    def calculateCherries(self):
        cherries = [0]
        self.calculateCherriesHelper(cherries)
        return cherries[0]
        

    def traverse(self, representation):
        info = [0,0]
        if self.left is not None:
            info[0] = self.left.data
            self.left.traverse(representation)
        if self.right is not None:
            info[1] = self.right.data
            self.right.traverse(representation)
        info = sorted(info)
        info.append(self.data)
        info = tuple(info)
        representation.append(info)
        
    def __str__(self):
        representation = []
        self.traverse(representation)
        representation.sort(key = mySort)
        treeAsString = ""
        for i in range(len(representation)):
            treeAsString += str((representation[i][0], representation[i][1])) + "^{" + str(representation[i][2]) + "}" + "\n"
        return treeAsString


def buildTree(perm):
    n = len(perm)
    if n == 1:
        return Tree(perm[0])
    maxIndex, maxVal = maximalElement(perm)
    newTree = Tree(maxVal)
    if maxIndex != 0:
        newTree.setRight(buildTree(perm[:maxIndex]))
    if maxIndex != n - 1:
        newTree.setLeft(buildTree(perm[maxIndex + 1:]))
    return newTree


start = time.time()
randomPerm = generateUniformTree(10000)
randomTrees = buildTree(randomPerm)
end = time.time()
print(end - start)




    
    
        




    

    


        
        
