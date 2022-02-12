"""
RSA class.
"""
from math import lcm, ceil
from typing import Tuple

from Random import Random


class RSA:
	"""
	RSA class.
	For a new public and private key, make a new instance.
	"""

	__public_key: Tuple[int, int]
	__private_key: int

	def __init__(self, bit_count: int = 1024) -> None:
		# Get 2 large prime numbers, p and q
		p: int = Random.get_random_prime(bits=bit_count)
		q: int = Random.get_random_prime(bits=bit_count)
		# Calculate n = p * q
		n: int = p * q
		# Get totient function of n, which looks like: λ(n)
		# All of the math is explained on the linked Wikipedia
		# page, but the takeaway is: λ(n) = lcm(p − 1, q − 1)
		# FIXME: THIS ONLY WORKS ON Python 3.9
		n_totient: int = lcm(p - 1, q - 1)
		# Get value for e (not to be mistaken for Euler's irrational number, which is equal to 2.718...)
		e: int = 65537  # FIXME: THIS ONLY WORKS IF n_totient is larger than 65537
		# Calulate d as the modular multiplicative inverse of e modulo λ(n)
		d: int = pow(e, -1, n_totient)

		# Let's assign the keys to the class variables
		self.__public_key = (e, n)  # (Public Exponent, Modulus)
		self.__private_key = d  # Private Exponent

		# Delete unnecessary variables from memory
		del p, q, n_totient

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
