# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:02:19 2016

@author: prcobol
"""

import urllib
import json

def getJSON(url):
    fhand = urllib.urlopen(url)
    line = [line for line in fhand]
    print line
    data = json.loads(line[0])
    return data
    
print getJSON("http://api.espn.com/v1/sports/baseball/mlb/events")