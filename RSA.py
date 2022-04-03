"""
RSA class.
"""
from json import loads, dumps
from typing import Tuple

from MathUtils import MathUtils


# noinspection PyUnusedFunction
class RSA:
    """
	RSA class.
	For a new public and private key, make a new instance.
	"""

    __public_key: Tuple[int, int]
    __private_key: int

    def __init__(self, bit_count: int = 1024) -> None:
        # Get 2 large prime numbers, p and q
        p: int = MathUtils.get_random_prime(bits=bit_count)
        q: int = MathUtils.get_random_prime(bits=bit_count)
        # Calculate n = p * q
        n: int = p * q
        # Get totient function of n, which looks like: λ(n)
        # All of the math is explained on the linked Wikipedia
        # page, but the takeaway is: λ(n) = lcm(p − 1, q − 1)
        n_totient: int = MathUtils.lcm(p - 1, q - 1)
        # Get value for e (not to be mistaken for Euler's irrational number, which is equal to 2.718...)
        e: int = 65537  # FIXME: THIS ONLY WORKS IF n_totient is larger than 65537
        # Calculate d as the modular multiplicative inverse of e modulo λ(n)
        d: int = pow(e, -1, n_totient)

        # Let's assign the keys to the class variables
        self.__public_key = (e, n)  # (Public Exponent, Modulus)
        self.__private_key = d  # Private Exponent

        # Delete unnecessary variables from memory
        del p, q, n_totient

    @classmethod
    def encrypt(cls, message: str, public_key: Tuple[int, int]) -> int:
        """
		Wrapper function for encrypt_from_bytes.
		"""
        return cls.encrypt_from_bytes(message.encode('utf-8'), public_key)

    @classmethod
    def encrypt_from_bytes(cls, message: bytes, public_key: Tuple[int, int]) -> int:
        """
		Encrypt a bytes object using an RSA public key.

		:param message: The string to encrypt.
		:param public_key: The public key to encrypt with.
		:return: The integer representation of the encrypted string.
		"""
        # Convert message to an integer
        # message ^ public_exponent ( % public_modulo )
        return pow(cls.__bytes_to_int(message), public_key[0], public_key[1])

    def decrypt(self, encrypted_message: int) -> str:
        """
		Wrapper for decrypt_to_bytes.
		"""
        return self.decrypt_to_bytes(encrypted_message).decode('utf-8')

    def decrypt_to_bytes(self, encrypted_message: int) -> bytes:
        """
		Decrypt an RSA encrypted string.

		:param encrypted_message: The message to decrypt.
		:return: The cleartext string.
		"""
        # message ^ private_exponent ( % public_modulo )
        # Then convert the message to a string
        return self.__int_to_bytes(pow(encrypted_message, self.__private_key, self.__public_key[1]))

    def get_public_key(self) -> Tuple[int, int]:
        """
		:return: This instance's public key.
		"""
        return self.__public_key

    def get_serialized_pub_key(self) -> bytes:
        """
		Serialize the public key to a bytes object.
        """
        # Put values in dict
        # Then serialize to JSON
        return dumps({
	        "e": self.__public_key[0],
	        "m": self.__public_key[1]
        }).encode("utf-8")

    @staticmethod
    def __bytes_to_int(data: bytes) -> int:
        """
		:return: Bytes to Integer
		"""
        return int(data.hex(), 16)

    @staticmethod
    def __int_to_bytes(data: int) -> bytes:
        """
		:return: Integer to Bytes
		"""
        return bytes.fromhex(hex(data)[2:])

    @staticmethod
    def deserialize_pub_key(data: bytes) -> Tuple[int, int]:
        """
		Takes a byte object and deserializes it to a public key.

        :param data: The serialized public key.
        :return: The public key.
        """
        # Parse JSON
        pub_dict = loads(data.decode("utf-8"))
        # Pull out values
        return pub_dict["e"], pub_dict["m"]
