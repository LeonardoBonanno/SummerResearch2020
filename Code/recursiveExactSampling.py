from euler import calculateEulerZigzagNumbers
import math
import numpy as np
import random

rng = np.random.default_rng()

def recursiveExactSampling(n):
    sigma = [0] * n
    numbers = [i for i in range(1, n + 1)]
    return samplingHelper(numbers, True)

def samplingHelper(numbers, forward):
    n = len(numbers)
    if n == 0:
        return []
    if n == 1:
        return [numbers[0]]
    k = getK(n, forward)
    if forward:
        lowerNumbers = sorted(random.sample(numbers[0:n-1], k - 1)) if k > 1 else []
        upperNumbers = sorted(list(set(numbers[0:n - 1]).difference(set(lowerNumbers))))
        return samplingHelper(lowerNumbers, forward) + [numbers[n-1]] + samplingHelper(upperNumbers, not forward)
    else:
        lowerNumbers = sorted(random.sample(numbers[1:], k - 1)) if k > 1 else []
        upperNumbers = sorted(list(set(numbers[1:]).difference(set(lowerNumbers))))
        return samplingHelper(lowerNumbers, forward) + [numbers[0]] + samplingHelper(upperNumbers, not forward)
        

def getK(n, forward):
    E = calculateEulerZigzagNumbers(n)
    values = list(range(1, n + 1, 2))
    p = [math.comb(n - 1, k - 1) * E[k - 1] * E[n - k] / E[n] for k in values]
    k = values[list(rng.multinomial(1, p)).index(1)]
    return k

def testMethod(n):
    dic = dict()
    steps = 100000
    for _ in range(steps):
        perm = tuple(recursiveExactSampling(n))
        if perm in dic:
            dic[perm] += 1
        else:
            dic[perm] = 1
    for entry in dic:
        print(entry, ":", dic[entry])

testMethod(4)

    
            
    
