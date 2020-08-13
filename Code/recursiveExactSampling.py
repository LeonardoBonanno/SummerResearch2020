from euler import calculateEulerZigzagNumbers
import math
import numpy as np
import random

rng = np.random.default_rng()

def recursiveExactSampling(n):
    sigma = [0] * n
    numbers = [i for i in range(1, n + 1)]
    samplingHelper(n, sigma, numbers, 0, True)
    return sigma

def samplingHelper(n, sigma, numbers, start, forward):
    if n == 1:
        sigma[start] = numbers[0]
        return
    if n == 0:
        return
    k = getK(n)
    sigma[start + k - 1] = numbers[n - 1]
    lowerNumbers = sorted(random.sample(numbers[0:n-1], k - 1)) if k > 1 else []
    upperNumbers = sorted(list(set(numbers[:n - 1]).difference(set(lowerNumbers))))
    if forward:
        upperNumbers.reverse()
    else:
        lowerNumbers.reverse()
    if forward:
        samplingHelper(k - 1, sigma, lowerNumbers, start, True)
        samplingHelper(n - k, sigma, upperNumbers, start + k, False)
    else:
        samplingHelper(k - 1, sigma, lowerNumbers, start, False)
        samplingHelper(n - k, sigma, upperNumbers, start + k, True)   

def getK(n):
    E = calculateEulerZigzagNumbers(n)
    p = [0.5 * math.comb(n - 1, k - 1) * E[k - 1] * E[n - k] / E[n] for k in range(1, n + 1)]
    k = list(rng.multinomial(1, p)).index(1) + 1
    print(k)
    return k

print(recursiveExactSampling(10))
    
            
    
