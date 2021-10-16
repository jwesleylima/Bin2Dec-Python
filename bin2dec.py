"""Module written on 08/22/2021 by JWesleyLima.
Visit my profile: https://github.com/jwesleylima."""


def bin2dec(*, binary_digits: str) -> int:
	"""Converts binary digits into decimal numbers.

	- Keyword Parameters:
		binary_digits: Binary digits as a string.

	- Return:
		int: Decimal number
	
	- Usage Example:
		some_decimal = bin2dec(binary_digits='0101')
	"""
	binary_digits = binary_digits.replace(' ', '')
	VALID_BINARY_DIGITS = ('0', '1')

	if not isinstance(binary_digits, str):
		raise TypeError('Binary digits must be of type \'str\'')
	elif len(binary_digits) == 0:
		raise ValueError('An empty string was entered')
	elif not str(binary_digits).isnumeric() or not \
	all(d in VALID_BINARY_DIGITS for d in binary_digits):
		raise ValueError(f'Only binary digits (0 and 1) are allowed: "{binary_digits}" entered')

	# Convert
	decimal_number = 0
	for i, digit in enumerate(binary_digits[::-1]):
		decimal_number += (int(digit) * 2 ** i)
	return decimal_number
