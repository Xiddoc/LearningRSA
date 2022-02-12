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

# Print plaintext
plaintext_message = "This is a message!"
print(f"Plaintext message: {plaintext_message}")

# Use public key to encrypt a message
encrypted_message = RSA.encrypt(plaintext_message, rsa.get_public_key())
print(f"Encrypted message: {encrypted_message}")

# Decrypt
print(f"Decrypted message: {rsa.decrypt(encrypted_message)}")
