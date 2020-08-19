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

def proportions(n):
    E_nm1 = calculateNthEulerZigzagNumber(n - 1)
    C = [0] * int(n /2)
    for c in range(1, int(n / 2) + 1):
        C[c - 1] = cardinality(n, c) * (math.pow(2, -c)) / E_nm1
    return C
N = 120
p = proportions(N)
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

#plotDistance(170)
        
        
