import ntplib
from time import ctime

def ntpQuery():
	client = ntplib.NTPClient()
	response = client.request("time-c.nist.gov")
	print ctime(response.tx_time)
