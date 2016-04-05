N = 600851475143
max = 1

def isPrime(N):
  for i in xrange(2,N-1):
    if N % i == 0:
      return False
  return True

for i in xrange(2,N-1):
  if N % i == 0 and isPrime(i):
    print(max)
    max = i
