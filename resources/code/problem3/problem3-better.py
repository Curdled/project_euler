from math import sqrt,ceil
import timeit

def isPrime(N):
  for i in xrange(2,int(ceil(sqrt(N)))):
    if N % i == 0:
      return False
  return True

def findLargestNumber(N):
    max = 1
    for i in xrange(2,int(ceil(sqrt(N)))):
      if N % i == 0 and isPrime(i):
        max = i
    return max
