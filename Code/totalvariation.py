from euler import calculateNthEulerZigzagNumber
import matplotlib.pyplot as plt
import math


cache = {} 
def cardinality(n, c):
    return cardinalityHelper(n, c, cache)
    
def cardinalityHelper(n, c, cache):
    if (n, c) in cache:
        return cache[(n, c)]
    if c == 0:  
        return 0
    if c == 1:
        return 1
    if 2 * c > n:
        return 0
    val = cardinality(n - 1, c) * c + cardinality(n - 1, c - 1) * (n - 2 * c + 1)
    cache[(n, c)] = val
    return val

def cardinalities(n):
    E_nm1 = calculateNthEulerZigzagNumber(n - 1)
    C = [0] * int(n /2)
    for c in range(1, int(n / 2) + 1):
        C[c - 1] = cardinality(n, c)
    return C

def proportions(n, tajima):
    E_nm1 = calculateNthEulerZigzagNumber(n - 1)
    C = [0] * int(n /2)
    for c in range(1, int(n / 2) + 1):
        if tajima:
            C[c - 1] = cardinality(n, c) * (math.pow(2, -c)) / E_nm1
        else:
            C[c - 1] = cardinality(n, c) / E_nm1
    total = 0
    for c in range(int(0.3 * n), int(0.4 * n)):
        total += C[c]
    print(total/sum(C))
    return C

def cherryProportions(N, tajima):
    p = proportions(N, tajima)
    C = [i for i in range(1, int(N / 2) + 1)]
    plt.plot(C, p)
    plt.title('Proportion of Trees by Cherry Count')
    plt.xlabel('Cherries')
    plt.ylabel('Proportion of Trees')
    plt.show()
   
    
def uniformExpectedCherries(n):
    E_nm1 = calculateNthEulerZigzagNumber(n - 1)
    Ec = 0
    for c in range(1, int(n / 2) + 1):
        Ec += cardinality(n, c) * c / E_nm1
    return Ec

def totalVariationTajimaUniform(n):
    E_nm1 = calculateNthEulerZigzagNumber(n - 1)
    total_variation = 0
    for c in range(1, int(n / 2) + 1):
        total_variation += abs(cardinality(n, c) * (math.pow(2, n - c - 1) / math.factorial(n - 1)) - cardinality(n, c) / E_nm1)
    total_variation /= 2
    return total_variation

def plotDistance(n):
    x = [i for i in range(2, n  + 1)]
    y = [totalVariationTajimaUniform(i) for i in range(2, n + 1)]
    plt.plot(x, y)
    plt.title('Total Variation Distance between Tajima and Uniform')
    plt.xlabel('n')
    plt.ylabel('Total Variation Distance')
    plt.show()

plotDistance(150)
        
        
