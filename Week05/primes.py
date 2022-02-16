# primes.py
#
# Generate prime numbers
#
# Author: Andrew Beatty


primes = []
upTo = 10001

for candidate in range(2,upTo):
    #print(candidate)
    isPrime = True
    
    for divisor in primes:
        # If divisible by an int it is not a prime
        if(candidate % divisor == 0):
            isPrime = False
            # So there is no reason to keep checking
            break

    if isPrime: 
        primes.append(candidate)

print(primes)