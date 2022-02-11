"""
RSA class.
"""


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
