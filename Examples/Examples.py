class Fraction:
	def __init__(self, top, bottom):
		self.numerator = top
		self.denominator = bottom

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator)

	def __add__(self, other):
		n = self.numerator * other.denominator + \
			self.denominator * other .numerator
		d = self.denominator * other.denominator
		c = gcd(n, d)
		return Fraction(n // c, d // c)

	def __eq__(self, other):
		n = self.denominator * other.numerator
		m = self.numerator * other.denominator
		return n == m

def gcd(m, n):
	while m % n != 0:
		oldm = m
		oldn = n
		m = oldn
		n = oldm % oldn
	return n
