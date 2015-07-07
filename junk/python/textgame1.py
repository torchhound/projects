import random, os #numpy for arrays? pygame for graphics?

class entity(object):
	def __init__(self, image):
		self.image = image #array?

class player(entity):
	def __init__(self, stats):
		self.stats = stats #array?
	
class enemy(entity):
	def __init__(self, stats):
		self.stats = stats #array?

def help():
	print "Available commands: grab, forward, up, down, left, right, backward, examine, map"
	
def map():
	matrix = [[0 for x in range(5)] for x in range(5)] 
	
def character():
	name = str(raw_input("Who are you?: "))

def game():	
	print "Welcome",name,"." #need to make this a global variable, maybe stored in an external file?
	print "You are standing on a bluff overlooking a city."
	print "Into the city, back into the forest, or into an interesting cave?"
	action = str(raw_input("Where do you go?: "))
	if action == "city":
		print "You make your way into the city."
	elif action == "forest":
		print "You fall back into the trees."
	elif action == "cave":
		print "You enter the mouth of the cave."
	else:
		print "That city looks mighty inviting!"
	map()
		
def main():
	game = True
	while game == True:
		print "Super Text Game Menu! \n Create Character \n Begin \n Help \n Exit \n"
		player_input = raw_input("Enter a command: ")
		if player_input = "Help":
			help()
		elif player_input = "Create Character":
			character()
		elif player_input = "Begin":
			game()
		elif player_input = "Exit":
			os.exit()
		else:
			null
			
if __name__ == "__main__":
    main()