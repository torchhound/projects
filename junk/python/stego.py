import random, os, nltk

def enSteg(key, file, message):
	image = open(file, 'r+')
	capsule = key + ' ' + message #add termination character
	location = random.randrange(os.path.getsize(file))
	token = nltk.word_tokenize(image) #reduce complexity by using seek() instead of nltk?
	token.insert(location, capsule) 
	image.write(token)
	image.close()
	
def deSteg(key, file):
	image = open(file, 'r')
	if key in image.read(): #not sure if this will work for large files
		print() #print until termination character
	image.close()

def main():
	userFunc = input("Choose mode, type encrypt or decrypt ")
	if userFunc == 'encrypt':
		userFile = input("Specify a file: ")
		userMessage = input("Specify a message: ")
		userKey = input("Specify a key: ")
		enSteg(userKey, userFile, userMessage)
	elif userFunc == 'decrypt':
		userKey = input("Specify a key: ")
		userFile = input("Specify a file: ")
		deSteg(userKey, userFile)
	else:
		print("Invalid response")
	
main()
