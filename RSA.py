"""
RSA class.
"""

import math

class RSA:
	"""
	RSA class.
	For a new public and private key, make a new instance.
	"""

	__public_key: int
	__private_key: int

	def get_public_key(self) -> int:
		"""
		:return: This instance's public key.
		"""
		return self.__public_key

	def get_private_key(self) -> int:
		"""
		:return: This instance's private key.
		"""
		return self.__private_key

	def __string_to_int(self, data: str) -> int:
		"""
		:return: String to Integer
		"""
		return int.from_bytes(data.encode(), byteorder='big')

	def __int_to_string(self, data: int) -> str:
		"""
		:return: Integer to String
		"""
		return data.to_bytes(math.ceil(data.bit_length() / 8), byteorder='big').decode()
