import random
#class?
def rps():
	match = {
	1:"Rock",
	2:"Paper",
	3:"Scissors",
	"Rock":"Scissors",
	"Scissors":"Paper",
	"Paper":"Rock"
	}
	input = raw_input("Rock, Paper, or Scissors? r/p/s")
	input.lower()
	ai = random.randint(1,3)
	aic = ""
	pc = ""
	if ai == 1:
		aic = "Rock"
	elif ai == 2:
		aic = "Paper"
	elif ai == 3:
		aic = "Scissors"
	elif input == "r":
		pc = "Rock"
	elif input == "p":
		pc = "Paper"
	elif input == "s":
		pc = "Scissors"
	else:
		return False
	if aic == pc:
		print "Tie"
	elif 