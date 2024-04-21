import math                               # Importing the math module for mathematical operations
import time                               # Importing the time module for time-related functions

def extended_gcd(a, b):
    """Extended Euclidean Algorithm for finding modular inverse."""
    x0, x1, y0, y1 = 1, 0, 0, 1           # Initialize variables for extended GCD algorithm
    while b:                              # Continue loop until b becomes zero
        q, a, b = a // b, b, a % b        # Compute quotient and remainder
        x0, x1 = x1, x0 - q * x1          # Update x values
        y0, y1 = y1, y0 - q * y1          # Update y values
    return a, x0, y0                      # Return gcd and coefficients

def modular_inverse(e, n): 
    """Calculate the modular inverse of e modulo n."""
    gcd, x0, y0 = extended_gcd(e, n)      # Compute extended GCD of e and n
    if gcd != 1:                          # If gcd is not 1, modular inverse does not exist
        raise ValueError('Modular inverse does not exist')
    return x0 % n                         # Return the modular inverse of e

def factorise_modulus(n):
    """Factorize modulus into its prime factors."""
    for i in range(2, int(math.sqrt(n)) + 1):  # Iterate from 2 to square root of n
        if n % i == 0:                    # If n is divisible by i
            return i, n // i              # Return the factors i and n//i