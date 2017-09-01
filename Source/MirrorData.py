import datetime
import json
import os
from urllib.request import urlopen

import pytz

from Source import ApiKeys as keys


def weather():
    url = 'http://api.wunderground.com/api/'+keys.WeatherKey()+'/geolookup/conditions/q/CA/San_Francisco.json'
    f = urlopen(url)
    json_string = f.read().decode('UTF-8')
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    stmt = "Current temperature in %s is: %s" % (location, temp_f)
    f.close()
    return stmt


def news():
    hlns = []
    u = 'https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey='+keys.NewsKey()
    c = urlopen(u)
    json_string = c.read().decode('UTF-8')
    parsed_json = json.loads(json_string)
    for H in range(0, 8, 1):
        hlns[H] = parsed_json['articles'][H]['title']
    return hlns


def stocks():
    url = 'https://www.quandl.com/api/v3/datasets/CHRIS/CME_ES1.json?rows=1&api_key='+keys.StockKey()
    c = urlopen(url)
    json_string = c.read().decode('UTF-8')
    json_parsed = json.loads(json_string)
    price = json_parsed['dataset']['data'][0][4]
    return "S&P500: $%s" % price


def times():
    dtfmt = '%A, %B %d, %Y'
    date = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime(dtfmt)
    fmt = '%I:%M:%S %p'
    tm = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime(fmt)
    return date + os.linesep + tm
    #print "Time in New York: %s" % datetime.datetime.now(pytz.timezone('America/New_York')).strftime(fmt)
    #print "Time in London: %s" % datetime.datetime.now(pytz.timezone('Europe/London')).strftime(fmt)
    #print "Time in Johannesburg: %s" % datetime.datetime.now(pytz.timezone('Africa/Johannesburg')).strftime(fmt)
    #print "Time in Dubai: %s" % datetime.datetime.now(pytz.timezone('Asia/Dubai')).strftime(fmt)
    #print "Time in Hong Kong: %s" % datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')).strftime(fmt)


weather()
stocks()
