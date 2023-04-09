'''
=== prime number validator ===
- checks to see if integer is a prime number

Problem from IENG 331 - HW1
'''

import random

def main():
    '''
    main function
    '''
    numInt = 5
    max = 100

    # generate a specified number of random integers from 1-max
    for i in range(numInt):
        num = random.randint(1,max)
        # print output
        print(f'Is {num} a prime number? {isPrime(num)}')

def isPrime(num): 
    '''
    determines if number is prime by using trial division
    returns boolean value on if number is prime
    O(n)
    '''
    for i in range(2,num):
        # if number has an even divisor, return true
        if (num % i) == 0:
            return False
    
    # otherwise return false
    return True

if __name__ == "__main__":
    main()