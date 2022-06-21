from numpy import sqrt,floor
from random import randint

#basic single-number evaluation methods

def basicPrime(number):
    '''Most primitive algorithm to find prime numbers.'''
    if number < 2:
        return False
    elif number == 2:
        return True
    for index in range(3,number+1):
        if index == number:
            return True
        if number % index == 0:
            return False
        
def basicOnlyOdd(number):
    '''Improves upon the basic algorithm by evaluating only odd numbers- since any even number is divisible by 2 and thus not prime.'''
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for index in range(3,number+1):
        if index == number:
            return True
        if number % index == 0:
            return False
        
#not a definite test- True implies the number is probably prime, not necessarily prime
def fermatPrimality(num,k):
    #num must be >3
    #k: number of times to test for primality
    for i in range(1,k+1):
        rand = randint(2,num-2)
        if ((rand**(num-1)) % num != 1):
            return False
    return True
    


#historically famous algorithms

#sieve methods return all prime number less than input num

def sieveEratosthenes(num):
    # o n log log n
    #algo marks 1 as a prime number
    results = [True]*(num+1)
    for i in range(2, int(sqrt(num))):
        if results[i]:
            j = i**2
            while j <= num:
                results[j] = False
                j += i
    
    return [m for m, bool_val in enumerate(results) if bool_val]


def sieveSundaram(num):
    #o n log n
    #does not include 2 as a prime number
    k = floor((num-1)/2)
    results = [True]*int(k+1)
    
    for i in range(1,int(sqrt(k))):
        j = i
        while ((i+j+2*i*j)<=k):
            results[(i+j+2*i*j)] = False
            j += 1
            
    primes = []
    for i in range(1,int(k+1)):
        if results[i]:
            primes.append(2*i +1)
    return primes