from euler import calculateNthEulerZigzagNumber
import matplotlib.pyplot as plt
import math


def cardinality(n, c):
    if c == 0:
        return 0
    if c == 1:
        return 1
    if 2 * c > n:
        return 0
    return cardinality(n - 1, c) * c + cardinality(n - 1, c - 1) * (n - 2 * c + 1)

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
    
plotDistance(25)
        
        
