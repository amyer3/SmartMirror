import datetime
import json
import os
from urllib.request import urlopen
import pytz
import ApiKeys as keys


def weather():
    DEG = '\u00b0'
    url = 'http://api.wunderground.com/api/'+keys.keyFinder('weather')+'/forecast10day/q/CA/San_Francisco.json'
    f = urlopen(url)
    parsed_json = json.loads(f.read().decode('UTF-8'))
    f.close()
    high = []
    lo = []
    cond = []
    for W in range(0, 3):
        high.insert(W, parsed_json['forecast']['simpleforecast']['forecastday'][W]['high']['fahrenheit'])
        lo.insert(W, parsed_json['forecast']['simpleforecast']['forecastday'][W]['low']['fahrenheit'])
        cond.insert(W, parsed_json['forecast']['simpleforecast']['forecastday'][W]['conditions'])
    data = (high, lo, cond)
    return data


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
