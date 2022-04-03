"""
Example usage of RSA class.
"""

from RSA import RSA

# Make instance of RSA class (this generates private / public key pair)
rsa = RSA()

# Print out private key (secret!!!)
print(f"\n\nPrivate key: {rsa.get_private_key()}")

# Print public key
print(f"\n\nPublic key: {rsa.get_public_key()}")

# Print plaintext
plaintext_message = 'RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data ' \
                    'transmission. It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron ' \
                    'Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977. An ' \
                    'equivalent system was developed secretly in 1973 at GCHQ (the British signals intelligence ' \
                    'agency) by the English mathematician Clifford Cocks. That system was declassified in 1997.'

print(f"\n\nPlaintext message: {plaintext_message}")

# Use public key to encrypt a message
encrypted_message = RSA.encrypt(plaintext_message, rsa.get_public_key())
print(f"\n\nEncrypted message: {encrypted_message}")

# Decrypt
print(f"\n\nDecrypted message: {rsa.decrypt(encrypted_message)}")
