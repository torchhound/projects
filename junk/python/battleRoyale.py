#rpg battle royale simulator

import random
from numpy import *

class hero():
	__name = ''
	__dex = ''
	__str = ''
	__con = ''
	__int = ''
	__wis = ''
	__char = ''
	
	def __init__(self, name, dex, str, con, int, wis, char):
		self.__name = name
		self.__dex = dex
		self.__str = str
		self.__con = con
		self.__int = int
		self.__wis = wis
		self.__char = char
	
def createMap(xSize, ySize): #terrain mod?
	map = np.zeros(xSize, ySize)

def createHeroes(number): #variety mod? or specific classes mod?
	for x in number:
		#return heroes in a data structure or just as objects? 

def battle(turns, map, heroes): #unnecessary parameters? or maybe more params?

def main():
	print("Welcome to Battle Royale Sim!")
	argHeroes = input("How many heroes?")
	argTurns = input("How many turns?")
	argMapX = input("Size of map X axis?")
	argMapY = input("Size of map Y axis?")
	battle(argTurns, createMap(argMapX, argMapY), createHeroes(argHeroes))

if __name__ == '__main__':
	main()