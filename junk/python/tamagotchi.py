import random

class creature(object):
	def __init__(self, name, image, stats):
        self.name = name
		self.image = []
		self.stats = {}

class tamagotchi(creature):
		
def game():
	game_status = True
	name = raw_input("Please name you pet: ")
	while game_status = True:
		pet = tamagotchi(%s, "x", 'hp:5', 'xp:1', 'hunger:5', 'intelligence:5', 'strength:5', name)
		if pet.stats.items() == 0:
			game_status = False
		if game_status = False:
			break

def main():
	game()

if __name__ == "__main__":
    main()