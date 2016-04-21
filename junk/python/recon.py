import requests
from subprocess import call

def googleDork():
	#null

def subDomainSearch():
	#null

def githubBreach():
	#null

def validURL(url):
	req = requests.bet(url)
	if requests.status_code == 200:
		print("valid URL")
	else:
		print requests.status_code

def dnsInfo(url):
	try:
		call("whois %s" %url)
		call("dig %s ANY" %url)
	except TypeError:
		call("whois %d" %url)
		call("dig %d ANY" %url)

def scanIPRange(start, end):
	call("nmap {start}-{end}".format(start, end))

def main():
	userArgs = input("Choose url, dns, or ip: ")
	if userArgs == "url": 
		userURL = input("Input URL to check: ")
		validURL(userURL)
	else if userArgs == "dns":
		userDNS = input("Input URL or IP: ")
		dnsInfo(userDNS)
	else if userArgs == "ip":
		userIPS = input(Input the complete starting IP address: ")
		userIPE = input("Input the final quad of the IP address: ")
		scanIPRange(userIPS, userIPE)
	else:
		return False
