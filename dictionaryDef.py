import urllib
from xml.dom import minidom
import re

def buildResponse(node_list):
	return_string = ""
	for i in node_list:
		return_string = return_string + i + "\n"
	return return_string.strip()

def buildURL(key, word):
	return "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/" + word + "?key=" + key

def getXML(word):
	url = buildURL("1a276aec-1aa8-42d4-9575-d29c2d4fb105", word)
	response = urllib.urlopen(url).read()
	data = minidom.parseString(str(response))
	return data

def getDefinition(word):
	data = getXML(word)
	itemlist = data.getElementsByTagName('def')
	node_list = []
	for i in itemlist:
		dts = i.getElementsByTagName('dt')
		node_list.append(str(dts[0].childNodes[0].nodeValue))
	if len(node_list) < 3:
		return buildResponse(node_list)
	else:
		return buildResponse(node_list[:3])
