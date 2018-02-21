import random
def main():
	coin = random.random()
	if coin >= 0.50:
		print "Heads!"
	else:
		print "Tails!"
main()