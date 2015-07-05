import random

class creature(object):
	def __init__(self, name,):
        self.name = name
	def qualities(image, stats):
		self.image = []
		self.stats = {}

class tamagotchi(creature):
	def __init__(self, soiled, egg):
		self.soiled = soiled
		self.egg = egg
		
def game():
	print ("Care for your egg to hatch it into a pet!")
	game_status = True
	name = raw_input("Please name your pet: ")
	while game_status = True:
		pet = tamagotchi(%s, name) #fix classes and inheritance
		#"O", 'hp':'5', 'level':'1', 'xp':'1', 'hunger':'5', 'intelligence':'5', 'strength':'5', 'happiness':'5', 'boredom':'5'
		for x in 3:
			input = raw_input("MENU \n 1.Stats \n 2.Feed \n 3.Play \n 4.Clean Up 5.Evolve")
			if input == 1:
				print (self.image)
			elif input == 2:
				if self.egg = True:
					print ("You can't feed an egg.")
					break
				else:
					break
				2 #increase hunger
				#implement different types of food
			elif input == 3:
				3 #randomly increases, decreases, or does nothing to a stat
			elif input == 4:
				if self.soiled == True:
					print "All Clean!"
				else:
					print "Nothing to see here..."
			elif input == 5:
				5 #checks xp if ready changes self.image
			else:
				print "Try Again"
		for x in 2:
			psr = random.randint(1,6)
			if psr >= 2:
				#decrease hunger
			elif psr >= 4:
				break
			elif psr <= 6:
				self.soiled = True
			else:
				break
		if pet.stats.items() == 0: #find a better way to check for death
			game_status = False
		if game_status = False:
			print "Game Over"
			break

def main():
	game()

if __name__ == "__main__":
    main()
