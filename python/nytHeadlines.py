import requests
from bs4 import BeautifulSoup as BS

f = open("nytHeadlines.txt", "w")
url = "http://www.newyorktimes.com/"
r = requests.get(url)
rHtml = r.text
soup = BS(rHtml)

for row in soup.find_all("h2", attrs = {"class" : "story-heading"}):
    f.write(row.text + "\n")
    print(row.text)
print("Finished!")
