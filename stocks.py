# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 00:52:05 2016

@author: prcobol
"""

import urllib
import json

def buildURL(ticker):
    return "https://www.quandl.com/api/v3/datasets/WIKI/" + ticker + ".json"

def getJSON(ticker):
    url = buildURL(ticker)
    response = urllib.urlopen(url)
    data = json.load(response)
    return data

def getQuote(ticker):
    data = getJSON(ticker)
    return data['dataset']['data'][0][4]
    

#print getQuote("FB")