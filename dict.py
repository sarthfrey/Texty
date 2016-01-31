# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 00:36:59 2016

@author: prcobol
"""

import requests
import json

def buildURL(city, key):
    city = city.replace(" ","+")
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key
    return url

def getJSON(city):
    url = buildURL(city,"dict.1.1.20160127T060653Z.092f108b217dc586.e637541b0afc7ce53e1f725f077230286eac412f")
    fhand = urllib.urlopen(url)