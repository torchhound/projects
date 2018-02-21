import urllib
import urllib2
import os
import re
from bs4 import BeautifulSoup
def image_scrape():
	url = raw_input("Type url for image scrape: ")
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)
	name = 0
	for tag in soup.find_all(re.compile("img")):
		path = os.path.normpath('C:\\Users\\Sorcerer\\Downloads')
		name += 1
		file_path = os.path.join(path, name)
		downloaded_image = file(file_path, 'wb')
		downloaded_image.write(chunk)
		downloaded_image.close()

image_scrape()
