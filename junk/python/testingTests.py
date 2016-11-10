import unittest

def testFunc(a, b):
	if a > b:
		return False
	else:
		return True

def isPrime(number):
	for x in range(number):
		if number % x == 0:
			return False
	return True

class allTestCases(unittest.TestCase):
	def testTestFunc(self):
		self.assertTrue(testFunc(5, 6))
	def testIsPreim(self):
		self.assertTrue(isPrime(5))
		self.assertTrue(isPrime(7))
		self.assertFalse(isPrime(9))

if __name__ == "__main__":
	unittest.main()
