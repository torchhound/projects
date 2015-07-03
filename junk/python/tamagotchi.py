import random

class creature(object):
	def __init__(self, name, image, stats):
        self.name = name
		self.image = []
		self.stats = {}

class tamagotchi(creature):
		def __init__(self, soiled):
			self.soiled = soiled
		
def game():
	game_status = True
	name = raw_input("Please name you pet: ")
	while game_status = True:
		pet = tamagotchi(%s, "x", 'hp:5', 'level:1', 'xp:1', 'hunger:5', 'intelligence:5', 'strength:5', name)
		for x in 3:
			input = raw_input("MENU \n 1.Stats \n 2.Feed \n 3.Play \n 4.Clean Up 5.Evolve")
			if input == 1:
				print (self.image)
			elif input == 2:
				2 #increase hunger
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
		if pet.stats.items() == 0: #find a better way to check for death
			game_status = False
		if game_status = False:
			print "Game Over"
			break

def main():
	game()

if __name__ == "__main__":
    main()