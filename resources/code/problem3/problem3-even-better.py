from math import sqrt

N = 600851475143

def sieve_for_primes_to(n):
    pass

def findLargestNumber(N):
    max = 1
    a = sieve_for_primes_to(int(sqrt(N)))
    print(len(a))
    for i in a:
      if N % i == 0:
        max = i
    return max