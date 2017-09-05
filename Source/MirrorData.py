import datetime
import json
import os
from urllib.request import urlopen
import pytz
import ApiKeys as keys
import matplotlib.pyplot as plt


DEG = u'\u00b0'  # degree symbol. \final\



def weather():
    url = 'http://api.wunderground.com/api/'+keys.WeatherKey()+'/geolookup/conditions/q/CA/San_Francisco.json'
    f = urlopen(url)
    json_string = f.read().decode('UTF-8')
    parsed_json = json.loads(json_string)

    cond = parsed_json['current_observation']['weather']
    temp_f = parsed_json['current_observation']['temp_f']
    stmt = "%s, %s%s" % (cond, temp_f, DEG)
    f.close()
    return stmt


def forecast():
    # tup[1][i] = hours
    # tup[2][i] = temp_fwds
    # tup[3][i] = condition pulled as 'wx'
    url3 = 'http://api.wunderground.com/api/' + keys.WeatherKey() + '/hourly10day/q/CA/San_Francisco.json'
    fcst = urlopen(url3)
    json_string_fcst = fcst.read().decode('UTF-8')
    fcst_json = json.loads(json_string_fcst)
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
    # print "Time in New York: %s" % datetime.datetime.now(pytz.timezone('America/New_York')).strftime(fmt)
    # print "Time in London: %s" % datetime.datetime.now(pytz.timezone('Europe/London')).strftime(fmt)
    # print "Time in Johannesburg: %s" % datetime.datetime.now(pytz.timezone('Africa/Johannesburg')).strftime(fmt)
    # print "Time in Dubai: %s" % datetime.datetime.now(pytz.timezone('Asia/Dubai')).strftime(fmt)
    # print "Time in Hong Kong: %s" % datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')).strftime(fmt)


def graph():
    tup = forecast()
    x = tup[0]
    y = tup[2]
    fig, ax = plt.subplots()
    ax.plot(x, y, color='white')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(axis='y', color='white')
    ax.tick_params(axis='x', color='black')
    ax.set_xticks(tup[0])
    plt.setp(ax.get_yticklabels(), color='white')
    ax.set_xticklabels(tup[1], rotation=90, color="white")
    ax.set_facecolor('black')
    fig.set_facecolor('black')
    targ = tup[0][0] + (24 - tup[4][0])  # finds midnight
    ax.axvline(targ, color='white')
    plt.setp(ax.get_xticklabels()[::2], visible=False)
    plt.show()

graph()


