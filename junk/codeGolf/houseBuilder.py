#written for http://codegolf.stackexchange.com/questions/79033/automatic-house-builder
import numpy as np
def k(h,w,d):
	u=np.array([]) #mgrid?
	u.shape=(h,w,d)