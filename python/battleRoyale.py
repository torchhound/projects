#rpg battle royale simulator

import random 
from numpy import *

class Hero(): #include position data with each hero object?
	id = '' 
	dex = '' #dexterity
	str = '' #strength
	con = '' #constitution
	int = '' #intelligence
	wis = '' #wisdom
	char = '' #charisma
	
	def __init__(self, id, dex, str, con, int, wis, char):
		self.id = id
		self.dex = dex
		self.str = str
		self.con = con
		self.int = int
		self.wis = wis
		self.char = char
		
	def deBuff(self, skill, new):
		self.skill = new
		
	def getSkill(self, skill):
		return self.skill
	
def createMap(xSize, ySize): #terrain mod?
	map = np.zeros(xSize, ySize)

def mapEdit(map, xCor, yCor):
	
	
def createHeroes(number, xSize, ySize): #variety mod? or specific classes mod?
	heroLocationX = {}
	heroLocationX = {}
	for x in number:
		nameInc = "hero" + x
		hero = Hero(nameInc, random.randrange(0,20), random.randrange(0,20), random.randrange(0,20), random.randrange(0,20), random.randrange(0,20), random.randrange(0,20))
		heroLocationX[nameInc] = random.randrange(xSize)
		heroLocationY[nameInc] = random.randrange(ySize)

def battle(turns, map, heroes): #unnecessary parameters? or maybe more params?
	#either move or fight, battles decided based on stats, chance to fight based on wisdom and charisma
	#print or return hero and their stats

def main():
	print("Welcome to Battle Royale Sim!")
	argHeroes = input("How many heroes?")
	argTurns = input("How many turns?")
	argMapX = input("Size of map X axis?")
	argMapY = input("Size of map Y axis?")
	battle(argTurns, createMap(argMapX, argMapY), createHeroes(argHeroes))

if __name__ == '__main__':
	main()