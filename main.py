"""
Entry script.
"""

# Let's make a new instance of the RSA class
from RSA import RSA

rsa = RSA()

# Print out private key (secret!!!)
print(rsa.get_private_key())

# Print public key
print(rsa.get_public_key())

