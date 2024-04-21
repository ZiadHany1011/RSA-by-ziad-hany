import time                              # Importing the time module for time-related functions
import random                            # Importing the random module for generating random numbers
import math                              # Importing the math module for mathematical operations

def is_prime(num):                       # Define a function to check if a number is prime
    if num < 2:                          # Check if the number is less than 2
        return False                     # Return False since numbers less than 2 are not prime
    for i in range(2, int(num**0.5) + 1):# Iterate through numbers from 2 to the square root of 'num'
        if num % i == 0:                 # If 'num' is divisible by 'i'
            return False                 # Return False since 'num' is not prime
    return True                          # If no divisor found, return True indicating 'num' is prime

def gcd_extended(a, b):                  # Define a function to perform extended Euclidean algorithm
    x0, x1, y0, y1 = 1, 0, 0, 1           # Initialize variables for the extended GCD algorithm
    while b:                             # Loop until 'b' becomes zero
        q, a, b = a // b, b, a % b       # Compute quotient and remainder
        x0, x1 = x1, x0 - q * x1         # Update x values
        y0, y1 = y1, y0 - q * y1         # Update y values
    return a, x0, y0                     # Return GCD and coefficients