from bs4 import BeautifulSoup
import requests
import os
def image_scrape():
	url = raw_input("Type url for image scrape: ")
	x = requests.get(url, stream=True)
	soup = BeautifulSoup(x)
	#name = 0
	#IMG_DIR = os.path.join(os.path.dirname(__file__), 'name')
	img = soup.find_all('img')
	for img in img:
		#name += 1
		f = open(img)
		f.write(x.content)
		f.close()
 
image_scrape()
