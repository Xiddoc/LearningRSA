"""
Random class.
"""
from random import randint
from math import gcd

from sympy import isprime


class MathUtils:
	"""
	Static class for random numbers
	and other number operations.
	"""

	@classmethod
	def get_random_prime(cls, bits: int) -> int:
		"""
		:return: Returns a random prime number.
		"""
		# Until we find a valid random prime
		while True:
			# Get a random number with that amount of bits
			# [2 ^ (bits - 1)   :to:    2 ^ bits - 1]
			# For example, for 3 bits:
			# [0b100            :to:    0b111]
			random_number: int = randint(2 ** (bits - 1), 2 ** bits - 1)
			# If it is prime
			if cls.is_prime(random_number):
				# Return it
				return random_number

	@classmethod
	def is_prime(cls, number: int) -> bool:
		"""
		Check if a number is prime.

		:param number: The value to check
		:return: Boolean value; Is the value a prime number?
		"""
		# Implement later using Rabin-Miller
		return isprime(number)

	@staticmethod
	def lcm(a, b):
		"""
		Math.lcm implementation (since not available in 3.8).
		:return:
		"""
		return abs(a*b) // gcd(a, b)