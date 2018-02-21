import random
import os
import Image
def import_img(file_name):
	try:
		img = Image.open(file_name)
		break
	except IOError:
		print "Please input a valid image file name."
		return False
def glitch(passes):
	
	