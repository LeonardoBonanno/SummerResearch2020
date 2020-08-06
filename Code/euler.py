import math
import time


def calculateFirstNEulerNumbers(n):
    x = [0] * (n + 1)
    x[0] = 1
    x[1] = 1
    for i in range(2, n + 1):
        calculateEulerNumber(i, x)
    return x

def calculateEulerNumber(i, x):
    E_n = 0
    for k in range(1, i, 2):
        E_n += math.comb(i - 1, k) * x[k] * x[i - 1 - k]
    x[i] = E_n

t0 = time.time()
calculateFirstNEulerNumbers(1000)
t1 = time.time()
print(t1 - t0)


