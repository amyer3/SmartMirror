import datetime
import json
import os
from urllib.request import urlopen
import pytz
import ApiKeys as keys


def weather():
    url = 'http://api.wunderground.com/api/'+keys.keyFinder('weather')+'/forecast10day/q/CA/San_Francisco.json'
    f = urlopen(url)
    parsed_json = json.loads(f.read().decode('UTF-8'))
    f.close()
    high = []
    lo = []
    cond = []
    day = []
    for W in range(0, 5):
        day.insert(W, parsed_json['forecast']['simpleforecast']['forecastday'][W]['date']['weekday_short'])
        high.insert(W, parsed_json['forecast']['simpleforecast']['forecastday'][W]['high']['fahrenheit'])
        lo.insert(W, parsed_json['forecast']['simpleforecast']['forecastday'][W]['low']['fahrenheit'])
        cond.insert(W, parsed_json['forecast']['simpleforecast']['forecastday'][W]['conditions'])
    data = (high, lo, cond, day)
    return data
    #print(data[3][0])


def news():
    hlns = []
    u = 'https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey='+keys.keyFinder('news')
    c = urlopen(u)
    parsed_json = json.loads(c.read().decode('UTF-8'))
    for H in range(0, 8):
        hlns.append(parsed_json['articles'][H]['title'])
    return hlns


def times():
    dtfmt = '%A' + os.linesep + '%B %d, %Y' + os.linesep + '%I:%M:%S %p'
    date = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime(dtfmt)
    return date


def svgSelector():
    inpt = weather()
    cond = inpt[2][0]
    if 'overcast' or 'cloudy' in cond:
        return 'icons/overcast.svg'
    elif 'rain' or 'showers' or 'drizzle' in cond:
        return 'icons/rain.svg'
    elif 'snow' or 'ice' or 'hail' in cond:
        return 'icons/snow.svg'
    elif 'thunder' in cond:
        return 'icons/thunder.svg'
    elif 'fog' in cond:
        return 'icons/fog.svg'
    else:
        return 'icons/sun.svg'
