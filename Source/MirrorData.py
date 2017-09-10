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


def stocks():
    url = 'https://www.quandl.com/api/v3/datasets/CHRIS/CME_ES1.json?rows=1&api_key='+keys.keyFinder('stocks')
    c = urlopen(url)
    json_parsed = json.loads(c.read().decode('UTF-8'))
    price = json_parsed['dataset']['data'][0][4]
    return "S&P500: $%s" % price


def times():
    dtfmt = '%A' + os.linesep + '%B %d, %Y' + os.linesep + '%I:%M:%S %p'
    date = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime(dtfmt)
    return date


def strFormatter():
    tup = weather()
    colBreak = ": "
    hyphBreak = " - "
    barBreak = " | "
    arr = []
    for i in range(1, 5):
        out = tup[3][i] + colBreak + tup[2][i] + hyphBreak + tup[0][i] + barBreak + tup[1][i]
        arr.insert(i, out)
    return arr
    #print(arr[0])


def svgSelector():
    inpt = weather()
    cond = inpt[2][0]
    if 'overcast' or 'cloudy' in cond:
        return 'icons/mostly-cloudy.svg'
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
