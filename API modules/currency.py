# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 23:29:34 2016

@author: prcobol
"""

import urllib
import json

def getJSON(url):
    fhand = urllib.urlopen(url)
    line = [line for line in fhand]
    data = json.loads(line[0])
    return data
    
def getExchangeRate(country_code):
    data = getJSON("http://api.fixer.io/latest")
    print data
    if country_code not in data['rates']:
        return -1
    rate = data['rates'][country_code]
    return rate
   
#MAIN
def getConversionRate(base_country, new_country):
    if not (getExchangeRate(base_country) + 1 or getExchangeRate(new_country) + 1):
        return -1
    ratio = getExchangeRate(new_country) / getExchangeRate(base_country)
    return ratio

#Returns -1 if input is invalid
#This case returns the # CAD dollars per USD
#print getConversionRate('USD','CNY')