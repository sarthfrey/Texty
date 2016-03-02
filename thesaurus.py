import urllib
from xml.dom import minidom
import re

def addWords(words):
	returning = ""
	if len(words) > 3:
		for i in xrange(0, 3):
			returning = returning + str(words[i]) + " "
	else:
		for word in words:
			returning = returning + str(word) + " "
	return returning


def buildURL(key, word):
	return "http://www.dictionaryapi.com/api/v1/references/thesaurus/xml/" + word + "?key=" + key

def getXML(word):
	url = buildURL("c694a881-e36a-4d4f-affd-d3372411d874", word)
	response = urllib.urlopen(url).read()
	data = minidom.parseString(response)
	return data

def getSynonyms(word):
	
	data = getXML(word)
	itemlist = data.getElementsByTagName('syn')
	if len(itemlist) == 0:
		return "No synonyms found."
	to_return = ""
	for i in itemlist:
		words = i.childNodes[0].nodeValue.split(', ')
		to_return = to_return + addWords(words) + "\n\n"
	return to_return

#print getSynonyms("mate")