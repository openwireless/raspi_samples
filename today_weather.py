#! /usr/bin/env python3
 
import urllib.request, urllib.parse
import json, sys, os
 
def getWeather():
    jsonUrl = "http://weather.livedoor.com/forecast/webservice/json/v1?"
    city = "170010"	# 石川県金沢市
    url = jsonUrl + "city=" + city
    site = urllib.request.urlopen(url)
    jsonData = json.loads(site.read().decode("utf-8"))
    return jsonData
 
if __name__ == "__main__":
    data = getWeather()
    try:
        weather = data["location"]["city"] + "地方、明日の天気は" + data["forecasts"][1]["telop"] + "でしょう。"
        weather = weather.replace("曇", "曇り")
        tempMax = data["forecasts"][1]["temperature"]["max"]["celsius"]
        weather += "最高気温は、" + tempMax + "度。"
        tempMin = data["forecasts"][1]["temperature"]["min"]["celsius"]
        tempMin = tempMin.replace("-", "マイナス")
        weather += "最低気温は、" + tempMin + "度でしょう。"
    except TypeError:
        pass
    print(weather)
    cmd = "/home/pi/util/aquestalkpi/AquesTalkPi " + weather + " -s 90 | aplay -q"
    os.popen(cmd).readline().strip()

