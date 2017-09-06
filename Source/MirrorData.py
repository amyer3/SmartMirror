import datetime
import json
import os
from urllib.request import urlopen
import pytz
import ApiKeys as keys
import matplotlib.pyplot as plt
from matplotlib import pylab as pl


def weather():
    url = 'http://api.wunderground.com/api/'+keys.keyFinder('weather')+'/forecast10day/q/CA/San_Francisco.json'
    f = urlopen(url)
    parsed_json = json.loads(f.read().decode('UTF-8'))
    f.close()
    day = []
    wthr = []
    for W in range(0, 3):
        day.insert(W, parsed_json['forecast']['txt_forecast']['forecastday'][W]['title'])
        wthr.insert(W, parsed_json['forecast']['txt_forecast']['forecastday'][W]['fcttext'])
    #today = "%s:%s%s" % (day, os.linesep, wthr)
    upcoming = (day, wthr)
    return upcoming


def forecast():
    # tup[1][i] = hours
    # tup[2][i] = temp_fwds
    # tup[3][i] = condition pulled as 'wx'
    url3 = 'http://api.wunderground.com/api/' + keys.keyFinder('weather') + '/hourly10day/q/CA/San_Francisco.json'
    fcst = urlopen(url3)
    fcst_json = json.loads(fcst.read().decode('UTF-8'))
    count = []
    hour = []
    temp_fwd = []
    cond = []
    hmil = []
    for T in range(0, 30):
        count.insert(T, T)
        hour.insert(T, fcst_json['hourly_forecast'][T]['FCTTIME']['civil'])  # 'civil' for str hour
        temp_fwd.insert(T, fcst_json['hourly_forecast'][T]['temp']['english'])
        cond.insert(T, fcst_json['hourly_forecast'][T]['wx'])
        hmil.insert(T, int(fcst_json['hourly_forecast'][T]['FCTTIME']['hour_padded']))
    fcst.close()
    tup = (count, hour, temp_fwd, cond, hmil)
    return tup
    #print(24 - tup[4][0])  # for data validation


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
    # print "Time in New York: %s" % datetime.datetime.now(pytz.timezone('America/New_York')).strftime(fmt)
    # print "Time in London: %s" % datetime.datetime.now(pytz.timezone('Europe/London')).strftime(fmt)
    # print "Time in Johannesburg: %s" % datetime.datetime.now(pytz.timezone('Africa/Johannesburg')).strftime(fmt)
    # print "Time in Dubai: %s" % datetime.datetime.now(pytz.timezone('Asia/Dubai')).strftime(fmt)
    # print "Time in Hong Kong: %s" % datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')).strftime(fmt)


weather()
