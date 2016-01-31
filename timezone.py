import urllib
import json
import re

def buildURL(key, location):
	return "http://api.worldweatheronline.com/free/v2/tz.ashx?key=" + key + "&q=" + location + "&format=JSON"

def getJSON(location):
	url = buildURL("3fc66d9c63d9061a23478337e2538", location)
	response = urllib.urlopen(url)
	data = json.load(response)
	return data

def lintResponse(location):
	city = re.sub(r"[ \t\n\r\f\v]", "+", location)
	return city

def getTime(location):
	location = lintResponse(location)
	data = getJSON(location)
	time = data["data"]["time_zone"][0]["localtime"]
	return time

print getTime("New York")