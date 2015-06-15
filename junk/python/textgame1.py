#import pygame
def help():
	help = "Available commands: grab, forward, up, down, left, right, backward, examine"
	if action == "help":
		print help
	else:
		return null
def map():
	pass
#character creation?
name = str(raw_input("Who are you?: "))
print "Welcome",name,"."
print "You are standing on a bluff overlooking a city."
action = str(raw_input("Where do you go?: "))
if action == city:
	print "You make your way into the city"
else:
	print "That city looks mighty inviting!"

