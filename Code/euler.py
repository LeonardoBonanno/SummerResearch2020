import math
import time

n = 10


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
x = calculateFirstNEulerNumbers(n)
print(x)
y = [math.factorial(i) * 2 * math.pow(2/math.pi, i + 1) /x[i] for i in range(n + 1)]
print(y)
t1 = time.time()
print(t1 - t0)


