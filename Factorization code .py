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

n_value = int(input("Enter the modulus (n) of the public key: "))  # Input modulus n
e_value = int(input("Enter the public exponent (e): "))             # Input public exponent e

start_time = time.perf_counter()         # Record the starting time for performance measurement

p_value, q_value = factorise_modulus(n_value)  # Factorize modulus into prime factors
phi_n_value = (q_value - 1) * (p_value - 1)     # Calculate Euler's totient function φ(n)
gcd_value, x_value, y_value = extended_gcd(e_value, phi_n_value)  # Compute extended GCD of e and φ(n)
d_value = modular_inverse(e_value, phi_n_value)  # Compute modular inverse of e

print("Prime factors (p, q):", p_value, q_value)   # Print prime factors p and q
print("Private exponent (d):", d_value)            # Print private exponent d
end_time = time.perf_counter()                      # Record the ending time for performance measurement

time_taken = (end_time - start_time) * 1000         # Calculate exact time taken in milliseconds
print(f"Time taken: {time_taken:.10f} milliseconds")  # Print the time taken 