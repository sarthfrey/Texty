# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:14:26 2016

@author: prcobol
"""

import requests
import json

def buildURL(key,target,text):
    return "https://www.googleapis.com/language/translate/v2?q=" + text + "&target=" + target + "&key=" + key

def getJSON(key,target,text):
    url = buildURL(key,target,text)
    data = requests.get(url).json()
    return data
    
def getTranslation(target,text):
    data = getJSON("AIzaSyBIJxVeb8GOebSNEEC_pjOUKEKaYhPVvus",target,text)
    print data
    translation = data['data']['translations'][0]['translatedText']
    return translation

print getTranslation("fr","pennapps is awesome")
    