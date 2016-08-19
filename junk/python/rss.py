import feedparser
import argparser
import json

def argParser():
	parser = argparse.ArgumentParser(description = "Retrieve RSS feeds")

	parser.add_argument("-l", "--list", action = "store", type = string, help = rssList.__doc__)

	parser.add_argument("-u", "--url", action = "store", type = string, help = rssURL.__doc__)

	parser.add_argument("-s", "--save", default = False, help = "Saves your request to output.txt")

	return args = parser.parse_args()

def userInput(url, list): #pointless with type = and action =?
	'''Gets user input.'''
	if url == True:
		userI = input("Please input URL: ")
		return userI
	elif list == True:
		userI = input("Please input the full path to the list: ")
		return userI

def rssURL(url, save):
	'''Retrieves an RSS feed from the specified URL.'''
	if save == True:
		try:
			out = feedparser.parse(url)
			file.open("output.txt", "w+")
			print(out)
			print("Output successfully saved to output.txt")
		except Exception as e:
			print(e)
	else:
		try:
			feedparser.parse(url)
		except Exception as e:
			print(e)

def rssList(file):
	'''Gets all RSS feeds from a file.'''
	uFile = file.open(file, "r")
	for x in uFile:
		rssURL(x)

def main():
	argParser()

if __name__ == '__main__':
	main()
