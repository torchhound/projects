import requests
from sqlalchemy import *
from bs4 import BeautifulSoup

db = create_engine("sqlite:///webArchiveGame.db")

#define db

url = "https://archive.org/search.php?query=mediatype:software&sort=-publicdate"
rq = request.get(url)
soup = BeautifulSoup(rq)
for x in soup.find("div" {"class" : "C234"}):
	if x == "game":
		#write to db
