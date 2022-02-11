"""
Random class.
"""
from random import randint


class Random:
	"""
	Static class for random numbers
	and other number operations.
	"""

	@classmethod
	def get_random_prime(cls, bits: int) -> int:
		"""
		:return: Returns a random prime number.
		"""
		# Get a random number with that amount of bits
		# [2 ^ (bits - 1)   :to:    2 ^ bits - 1]
		# For example, for 3 bits:
		# [0b100            :to:    0b111]
		random_number: int = randint(2 ** (bits - 1), 2 ** bits - 1)
		# If it is prime, return it
		# Otherwise, test a new random number (recursion)
		return random_number if cls.is_prime(random_number) else cls.get_random_prime(bits=bits)

	@classmethod
	def is_prime(cls, number) -> bool:
		"""
		Check if a number is prime.

		:param number: The value to check
		:return: Boolean value; Is the value a prime number?
		"""