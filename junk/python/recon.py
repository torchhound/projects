import requests, json
from subprocess import call
from github import Github

def googleDork(domain):
	site = "site:%s" %domain
	dorks = []
	for x in dorks:
		query = site + " " + x
		rq = requests.get('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + query)
		jsonContent = rq.content
		jsonObject = json.loads(jsonContent)
		for index,result in enumerate(jsonObject['responseData']['results']):
			print (str(index+1) + ") " + result['titleNoFormatting'])
			print (result['url'])
			
def subDomainSearch(url):
	call("dig %s soa" %url) #dig SOA url
	#call("dig @ns.SOA.com %s axfr" %url)
	call("host -t %s" %url)

def githubBreach(): #user, password
	#gh = Github(user, password)
	while True:
		userGuess = input("Input an organization or user or a guess: ")
		try:
			print(github.MainClass.Github.get_organization(userGuess))
			try:
				print( github.Organization.userGuess.get_repos()
			except:
				continue
		except:
			continue

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
	call("nmap {start}-{end}".format(start, end)) #format function vs percent

def main():
	userArgs = input("Choose url, dns, github, or ip: ")
	if userArgs == "url": 
		userURL = input("Input URL to check: ")
		validURL(userURL)
		subDomain(userURL)
	else if userArgs == "dns":
		userDNS = input("Input URL or IP: ")
		dnsInfo(userDNS)
	else if userArgs == "ip":
		userIPS = input("Input the complete starting IP address: ")
		userIPE = input("Input the final quad of the IP address: ")
		scanIPRange(userIPS, userIPE)
	else if userArgs == "github":
		userGithubU = input("Input github username: ")
		userGithubP = input("Input github password: ")
		githubBreach(userGithubU, userGithubP)
	else:
		return False
