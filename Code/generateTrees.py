from generationAltPerm import *
from permsToTrees import *

N = 1000

def generateUniformTree(n):
    return complement(convertPerm(generatePerm(n)))

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
    om = [0] * N
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

    def traverse(self):
        pair = [0,0]
        if self.left is not None:
            pair[0] = self.left.data
            self.left.traverse()
        if self.right is not None:
            pair[1] = self.right.data
            self.right.traverse()
        pair = tuple(sorted(pair))
        Tree.om[self.data - 1] = pair

    def calculateCherries(self):
        counter = 0
        for i in range(N):
            if Tree.om[i] == (0,0):
                counter += 1
        return counter
        
    def __str__(self):
        treeAsString = ""
        for i in range(N):
            treeAsString += str(Tree.om[i]) + "^{" + str(i + 1) + "}" + "\n"
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

randomTreePerm = generateUniformTree(N)
randomTree = buildTree(randomTreePerm)
randomTree.traverse()
print(randomTree)
print(randomTree.calculateCherries())




    
    
        




    

    


        
        
