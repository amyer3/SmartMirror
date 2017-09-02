import datetime
import json
import os
from urllib.request import urlopen
import pytz
import ApiKeys as keys


deg = u'\u00b0'


def weather():
    url = 'http://api.wunderground.com/api/'+keys.WeatherKey()+'/geolookup/conditions/q/CA/San_Francisco.json'
    f = urlopen(url)
    json_string = f.read().decode('UTF-8')
    parsed_json = json.loads(json_string)

    cond = parsed_json['current_observation']['weather']
    temp_f = parsed_json['current_observation']['temp_f']
    stmt = "%s, %s%s" % (cond, temp_f, deg)
    f.close()
    return stmt


def forecast():
    #tup[0][i] = hours
    #tup[1][i] = temp_fwds
    url3 = 'http://api.wunderground.com/api/' + keys.WeatherKey() + '/hourly/q/CA/San_Francisco.json'
    fcst = urlopen(url3)
    json_string_fcst = fcst.read().decode('UTF-8')
    fcst_json = json.loads(json_string_fcst)
    hour = []
    temp_fwd = []
    for T in range(0, 10):
        hour.insert(T, fcst_json['hourly_forecast'][T]['FCTTIME']['hour'])
        temp_fwd.insert(T, fcst_json['hourly_forecast'][T]['temp']['english'])
    fcst.close()
    tup = (hour, temp_fwd)
    return tup


def news():
    hlns = []
    u = 'https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey='+keys.NewsKey()
    c = urlopen(u)
    json_string = c.read().decode('UTF-8')
    parsed_json = json.loads(json_string)
    for H in range(0, 8):
        hlns.append(parsed_json['articles'][H]['title'])
    return hlns


def stocks():
    url = 'https://www.quandl.com/api/v3/datasets/CHRIS/CME_ES1.json?rows=1&api_key='+keys.StockKey()
    c = urlopen(url)
    json_string = c.read().decode('UTF-8')
    json_parsed = json.loads(json_string)
    price = json_parsed['dataset']['data'][0][4]
    return "S&P500: $%s" % price


def times():
    dtfmt = '%A' + os.linesep + '%B %d, %Y' + os.linesep + '%I:%M:%S %p'
    date = datetime.datetime.now(pytz.timezone('US/Pacific')).strftime(dtfmt)
    return date
    #print "Time in New York: %s" % datetime.datetime.now(pytz.timezone('America/New_York')).strftime(fmt)
    #print "Time in London: %s" % datetime.datetime.now(pytz.timezone('Europe/London')).strftime(fmt)
    #print "Time in Johannesburg: %s" % datetime.datetime.now(pytz.timezone('Africa/Johannesburg')).strftime(fmt)
    #print "Time in Dubai: %s" % datetime.datetime.now(pytz.timezone('Asia/Dubai')).strftime(fmt)
    #print "Time in Hong Kong: %s" % datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')).strftime(fmt)


def graph():
    dat = forecast()
    print(dat)

