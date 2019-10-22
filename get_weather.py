# Get weather for Kanazawa 

import urllib.request, urllib.parse
import json

jsonUrl = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
city = '170010'
url = jsonUrl + 'city=' + city
site = urllib.request.urlopen(url)
jsonData = json.loads(site.read().decode('utf-8'))

print(jsonData)

