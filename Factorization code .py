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
