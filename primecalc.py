bigListOPrimes = []

# Set up a range of numbers to find out if they are prime
for testPrime in range(2,100001):


# This needs to start at 1 for every loop in the while loop
  divisorVar = 1

# We can't test an undeclared var, so we declare it here
  divideRemainder = 0.5


  while divideRemainder != 0:         # is the remainder 0? if not keep running the test
      divisorVar = divisorVar + 1     # increment the divisor from 2 to testPrime
      divideRemainder = testPrime % divisorVar  # divide the testPrime by the divisor and store the remainder

# The while loop exited because the remainder was 0.
# does the divisor equal the test number?
  if divisorVar == testPrime:
      bigListOPrimes.append(testPrime)

primeCount = len(bigListOPrimes)
print(f'I have {primeCount} primes')
print(f'My biggest prime is: {bigListOPrimes[-1]}')