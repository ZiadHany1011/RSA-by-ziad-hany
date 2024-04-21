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

def generate_prime(bits_length):         # Define a function to generate a prime number of specified bit length
    while True:                          # Continue generating until a prime number is found
        prime = random.getrandbits(bits_length)  # Generate a random number of specified bit length
        if is_prime(prime):              # Check if the generated number is prime
            return prime                 # Return the prime number

def factorise_modulus(n):               # Define a function to factorize modulus into prime factors
    for i in range(2, int(math.sqrt(n)) + 1): # Iterate through numbers from 2 to square root of 'n'
        if n % i == 0:                  # If 'n' is divisible by 'i'
            return i, n // i            # Return 'i' and 'n // i' as factors of 'n'

def encode_msg(msg):                     # Define a function to encode a message into a list of ASCII values
    return [ord(ch) for ch in msg]       # Return a list of ASCII values of characters in the message

def decode_msg(encoded_msg):             # Define a function to decode a list of ASCII values into a string
    return "".join(chr(ch) for ch in encoded_msg)  # Convert ASCII values back to characters and join them into a string

def encrypt_msg(msg, pub_e, pub_n):      # Define a function to encrypt a message using RSA encryption
    encoded_msg = encode_msg(msg)        # Encode the message into a list of ASCII values
    return [pow(ch, pub_e, pub_n) for ch in encoded_msg]  # Encrypt each ASCII value using public exponent and modulus

def decrypt_msg(ciphertext, priv_d, pub_n): # Define a function to decrypt a message using RSA decryption
    return [pow(ch, priv_d, pub_n) for ch in ciphertext] # Decrypt each ciphertext value using private exponent and modulus

def brute_force_decrypt(e, n, encrypted_msg): # Define a function to brute-force decrypt an encrypted message
    start_time = time.perf_counter()      # Record the start time for performance measurement
    factors = factorise_modulus(n)        # Factorize the modulus into prime factors
    if len(factors) != 2:                 # If the number of factors is not 2
        print("Public key n requires two prime factors.")  # Print an error message
        return None                        # Return None indicating decryption failure
    p, q = factors                        # Get the prime factors
    phi = (p - 1) * (q - 1)               # Calculate Euler's totient function (phi)
    d = 1                                  # Initialize private exponent
    while True:                           # Infinite loop until decryption is successful
        if (e * d) % phi == 1:            # If the modular equation holds true
            end_time = time.perf_counter() # Record the end time for performance measurement
            decrypted_msg = ''            # Initialize decrypted message
            for char in encrypted_msg.split(','):  # Iterate through each ciphertext character
                decrypted_char = pow(int(char), d, n)  # Decrypt the character
                decrypted_msg += chr(decrypted_char)   # Convert decrypted character to ASCII and append
            print("Decrypted message:", decrypted_msg) # Print decrypted message
            print("Private key exponent (d):", d)     # Print private key exponent
            print("\nBrute Force Time: {:.6f} milliseconds".format((end_time - start_time) * 1000)) # Print decryption time
            return decrypted_msg         # Return decrypted message
        d += 1                            # Increment private exponent for next iteration