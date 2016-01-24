# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:14:26 2016

@author: prcobol
"""

import urllib
import json

def buildURL(key,source, target,text):
    return "https://www.googleapis.com/language/translate/v2?q=" + text + "&source=" + source + "&target=" + target + "&key=" + key

def getJSON(key,source, target,text):
    url = buildURL(key,source,target,text)
    response = urllib.urlopen(url)
    data = json.load(response)
    return data
    
def getTranslation(source,target,text):
    data = getJSON("AIzaSyBIJxVeb8GOebSNEEC_pjOUKEKaYhPVvus",source,target,text)
    translation = data['data']['translations'][0]['translatedText']
    return translation


#print getTranslation("fr","en","je suis un bon person")
    