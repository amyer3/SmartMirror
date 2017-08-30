import datetime
import json
import time
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
    u = 'https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey='+keys.NewsKey()
    c = urlopen(u)
    json_string = c.read().decode('UTF-8')
    parsed_json = json.loads(json_string)
    print("Top Headlines: ")
    for H in range(0, 8, 1):
        apexp = "AP Explains "
        analysis = "Analysis: "
        tttk = "10 Things to Know "
        nextheadline = parsed_json['articles'][H]['title']
        if nextheadline.__contains__(apexp or analysis or tttk):
            H+1
        else:
            print(nextheadline)
            time.sleep(5)


def stocks():
    url = 'https://www.quandl.com/api/v3/datasets/CHRIS/CME_ES1.json?rows=1&api_key='+keys.StockKey()
    c = urlopen(url)
    json_string = c.read().decode('UTF-8')
    json_parsed = json.loads(json_string)
    price = json_parsed['dataset']['data'][0][4]
    return "S&P500: $%s" % price


def times():
    while True:
        fmt = '%I:%M:%S %p'
        return "Time in California: %s" % datetime.datetime.now(pytz.timezone('US/Pacific')).strftime(fmt)
        #print "Time in New York: %s" % datetime.datetime.now(pytz.timezone('America/New_York')).strftime(fmt)
        #print "Time in London: %s" % datetime.datetime.now(pytz.timezone('Europe/London')).strftime(fmt)
        #print "Time in Johannesburg: %s" % datetime.datetime.now(pytz.timezone('Africa/Johannesburg')).strftime(fmt)
        #print "Time in Dubai: %s" % datetime.datetime.now(pytz.timezone('Asia/Dubai')).strftime(fmt)
        #print "Time in Hong Kong: %s" % datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')).strftime(fmt)
        time.sleep(.5)


weather()
stocks()
