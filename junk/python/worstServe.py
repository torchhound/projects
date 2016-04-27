from subprocess import call

def telnet():


def chat(port):


def webServe(page):
	call("nc -l -p 80 -q 1 < %s" %page) #might need a keep alive
	
def main():
	print("Serves an html page on port 80, only works on Linux")
	userPage = input("Path to page to serve: ")
	webServe(userPage)
	
if __name__ == '__main__':
	main()