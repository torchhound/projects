import requests
import json

districtStudents = requests.get('https://api.clever.com/v1.1/districts/4fd43cc56d11340000000005/students?count=true', headers={'Authorization':'Bearer DEMO_TOKEN'})
print("Status code: {}".format(districtStudents.status_code))
dSJson = json.loads(districtStudents.text)
print("Total number of students in the district: {}".format(dSJson["count"]))

districtSections = requests.get('https://api.clever.com/v1.1/districts/4fd43cc56d11340000000005/sections?count=true', headers={'Authorization':'Bearer DEMO_TOKEN'})
print("Status code: {}".format(districtSections.status_code))
dSecJson = json.loads(districtSections.text)
print("Total number of sections in the district: {}".format(dSecJson["count"]))

average = dSJson["count"] / dSecJson["count"]
print("The average number of students per section is: {}".format(average))
