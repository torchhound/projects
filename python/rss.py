import feedparser
import argparser

def argParser():
	parser = argparse.ArgumentParser(description = "Retrieve RSS feeds")

	parser.add_argument("-l", "--list", action = "store", type = string, help = rssList.__doc__)

	parser.add_argument("-u", "--url", action = "store", type = string, help = rssURL.__doc__)

	parser.add_argument("-s", "--save", default = False, help = "Saves your request to output.txt")

	return args = parser.parse_args()

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
	args = argParser()
	if args.url == True and args.save == True:
		rssURL(args.url)
	elif args.url == True:
		rssURL(args.url)
	elif args.list == True:
		rssList(args.list)

if __name__ == '__main__':
	main()
