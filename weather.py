# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 00:36:59 2016

@author: prcobol
"""

import urllib
import json

def buildURL(city, key):
    city = city.replace(" ","+")
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key
    return url

def getJSON(city):
    url = buildURL(city,"44db6a862fba0b067b1930da0d769e98")
    fhand = urllib.urlopen(url)
    line = [line for line in fhand]
    data = json.loads(line[0])
    return data
    
def getWeather(units, city):
    data = getJSON(city)
    city = data['name']
    celsius = data['main']['temp'] - 273.15
    fahrenheit = celsius * 1.8 + 32
    description = data['weather'][0]['description']
    if(units == "fahrenheit"):
        return "Temperature is " + str(fahrenheit) + " F in " + city + ". " + description + "."
    output = "Temperature is " + str(celsius) + " C in " + city + ". " + description + "."
    return output
    
#print getWeather("Waterloo")
