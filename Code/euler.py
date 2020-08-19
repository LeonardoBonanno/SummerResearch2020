# file contains code to calculate Euler-Zigzag Numbers and their asymptotic approximations

import math
import time

# constants
N = 50
round_factor = 10

# returns list with first n Euler-Zigzag Numbers (E_0 - E_n)
def calculateEulerZigzagNumbers(n):
    E = [0] * (n + 1)
    E[0] = 1
    E[1] = 1
    for i in range(2, n + 1):
        calculateEulerZigzagNumber(i, E)
    return E

def calculateNthEulerZigzagNumber(n):
    return calculateEulerZigzagNumbers(n)[n]

# helper function to calculate a single euler-zigzag number
def calculateEulerZigzagNumber(i, E):
    E_i= 0
    for k in range(1, i, 2):
        E_i += math.comb(i - 1, k) * E[k] * E[i - 1 - k]
    E[i] = E_i

# returns list first n Euler-Zigzag numbers asymptotic approximations
# note, to prevent overflow errors, keep n < 150
def calculateEulerZigzagApprox(n):
    return [round(math.factorial(i) * 2 * math.pow(2/math.pi, i + 1), round_factor) for i in range(n + 1)]

# calculate n-th Euler-Zigzag number with Entringer Numbers
def calculateEulerZigzagEntringer(n):
    E = dict()
    E[(0, 0)] = 1
    for k in range(1, n + 1):
        E[(k, 0)] = 0
    return calculateEntringerNumber(n, n, E)

# calculate E(n, k) recursively using memoization
def calculateEntringerNumber(n, k, E):
    if (n, k) in E:
        return E[(n, k)]
    E_nk = calculateEntringerNumber(n, k - 1, E) + calculateEntringerNumber(n - 1, n - k, E)
    E[(n, k)] = E_nk
    return E_nk

    
# print first N Euler-Zigzag Numbers, Asymptotic Expansion, and Ratio
def main():
    start = time.time()
    E = calculateEulerZigzagNumbers(N)
    end = time.time()
    E_prime = calculateEulerZigzagApprox(N)
    ratios = [round(E[i] / E_prime[i], round_factor) for i in range(N + 1)]
    print("Printing first %d Euler-Zigzag Numbers:\n" % N)
    for i in range(N + 1):
        print("E_%d =" % i, E[i], "~", E_prime[i], "| Ratio:", ratios[i])
    print("\nComputation Time:", end - start)

if __name__ == "__main__":
    main()

