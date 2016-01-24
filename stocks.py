# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 01:32:40 2016

@author: prcobol
"""

import urllib
import json

def getJSON(url):
    fhand = urllib.urlopen(url)
    line = [line for line in fhand]
    print line
<<<<<<< HEAD
    data = json.loads(line[0])
    return data

print getJSON("http://dev.markitondemand.com/MODApis/Api/v2/AAPL")
=======
    data = json.loads(line)
    return data

print getJSON("https://www.quandl.com/api/v3/datasets/SEC/AAPL_SALESREVENUENET_Q.json&api_key=PyTmLZ-bT44EashsCs6P")
>>>>>>> 89508c263927188f544c455e2910062be3090d0c
