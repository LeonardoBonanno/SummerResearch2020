# code to generate uniformly random Ranked Unlabeled Tree and print out its ordered matching representation

# imports
import time
from generationAltPerm import *
from permsToTrees import *

# constants
N = 30

# generate uniformly random tree perm in order easiest to print
def generateUniformTreePerm(n):
    return complement(convertToTreePerm(generateUniformPerm(n)))

# helper sorting function
def mySort(tuple):
    return tuple[2]

# tree class to help print out
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
    
    # recursively traverses tree   
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

    def getTree(self):
        representation = []
        self.traverse(representation)
        representation.sort(key = mySort)
        return representation
        
    def __str__(self):
        representation = []
        self.traverse(representation)
        representation.sort(key = mySort)
        treeAsString = ""
        for i in range(len(representation)):
            treeAsString += str((representation[i][0], representation[i][1])) + "^{" + str(representation[i][2]) + "}" + "\n"
        return treeAsString

# build a tree from a proper tree permutation, you can print right and left subtrees as well
def buildTree(treePerm):
    n = len(treePerm)
    if n == 1:
        return Tree(treePerm[0])
    maxIndex, maxVal = maximalElement(treePerm)
    newTree = Tree(maxVal)
    if maxIndex != 0:
        newTree.setRight(buildTree(treePerm[:maxIndex]))
    if maxIndex != n - 1:
        newTree.setLeft(buildTree(treePerm[maxIndex + 1:]))
    return newTree

# generate uniform random tree with N + 1 leaves and print the ordered matching representation
def main():
    start = time.time()
    randomPerm = generateUniformTreePerm(N)
    randomTree = buildTree(randomPerm)
    print(randomTree)
    print("Printing random tree:")
    end = time.time()
    print("Computation time:", end - start)

if __name__ == "__main__":
    main()





    
    
        




    

    


        
        
