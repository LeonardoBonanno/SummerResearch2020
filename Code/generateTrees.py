from generationAltPerm import *
from permsToTrees import *

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
        if self.left is not None:
            print(self.data, "-> ", self.left.data)
            self.left.traverse()
        else:
            print(self.data, "->", "LEAF")
        if self.right is not None:
            print(self.data, "-> ", self.right.data)
            self.right.traverse()
        else:
            print(self.data, "->", "LEAF")
    

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


randomTreePerm = generateUniformTree(10)
print(randomTreePerm)
randomTree = buildTree(randomTreePerm)
randomTree.traverse()


    
    
        




    

    


        
        
