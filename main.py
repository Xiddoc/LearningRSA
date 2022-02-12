"""
Entry script.
"""

# Let's make a new instance of the RSA class
from RSA import RSA

rsa = RSA()

# Print out private key (secret!!!)
print(f"Private key: {rsa.get_private_key()}")

# Print public key
print(f"Public key: {rsa.get_public_key()}")

# Use public key to encrypt a message
encrypted_message = RSA.encrypt("testing", rsa.get_public_key())
print(f"Encrypted message: {encrypted_message}")

# Decrypt
print(f"Decrypted message: {rsa.decrypt(encrypted_message)}")
