"""
RSA class.
"""
from math import ceil
from typing import Tuple
import json

from MathUtils import MathUtils


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
		# FIXME: THIS ONLY WORKS ON Python 3.9
		n_totient: int = MathUtils.lcm(p - 1, q - 1)
		# Get value for e (not to be mistaken for Euler's irrational number, which is equal to 2.718...)
		e: int = 65537  # FIXME: THIS ONLY WORKS IF n_totient is larger than 65537
		# Calulate d as the modular multiplicative inverse of e modulo λ(n)
		d: int = pow(e, -1, n_totient)

		# Let's assign the keys to the class variables
		self.__public_key = (e, n)  # (Public Exponent, Modulus)
		self.__private_key = d  # Private Exponent

		# Delete unnecessary variables from memory
		del p, q, n_totient

	@classmethod
	def encrypt(cls, message: str, public_key: Tuple[int, int]) -> int:
		"""
		Encrypt a string using an RSA public key.

		:param message: The string to encrypt.
		:param public_key: The public key to encrypt with.
		:return: The integer representation of the encrypted string.
		"""
		# Convert message to an integer
		# message ^ public_exponent ( % public_modulo )
		return pow(cls.__string_to_int(message), public_key[0], public_key[1])

	def decrypt(self, encrypted_message: int) -> str:
		"""
		Decrypt an RSA encrypted string.

		:param encrypted_message: The message to decrypt.
		:return: The cleartext string.
		"""
		# message ^ private_exponent ( % public_modulo )
		# Then convert the message to a string
		return self.__int_to_string(pow(encrypted_message, self.__private_key, self.__public_key[1]))

	def get_public_key(self) -> Tuple[int, int]:
		"""
		:return: This instance's public key.
		"""
		return self.__public_key

	def get_private_key(self) -> int:
		"""
		:return: This instance's private key.
		"""
		return self.__private_key

	@staticmethod
	def __string_to_int(data: str) -> int:
		"""
		:return: String to Integer
		"""
		return int.from_bytes(data.encode(), byteorder='big')

	@staticmethod
	def __int_to_string(data: int) -> str:
		"""
		:return: Integer to String
		"""
		return data.to_bytes(ceil(data.bit_length() / 8), byteorder='big').decode()

	@staticmethod
	def serialize_pub_key(key: Tuple[int, int]) -> bytes:
		return json.dumps({"e": key[0], "m": key[1]}).encode("utf-8")

	@staticmethod
	def deserialize_pub_key(data: bytes) -> Tuple[int, int]:
		pub_dict = json.loads(data.decode("utf-8"))
		return pub_dict["e"], pub_dict["m"]
