import json
from urllib.request import urlopen

from depreciated import ApiKeys


def weather():
    url = 'http://api.wunderground.com/api/' + ApiKeys.keyFinder('weather') + '/forecast10day/q/CA/San_Francisco.json'
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
    return high, lo, cond, day, svgSelector(cond[0])


def svgSelector(cond):
    if 'overcast' or 'cloudy' in cond:
        return 'ArtAssets/icons/overcast.svg'
    elif 'rain' or 'showers' or 'drizzle' in cond:
        return 'ArtAssets/icons/rain.svg'
    elif 'snow' or 'ice' or 'hail' in cond:
        return 'ArtAssets/icons/snow.svg'
    elif 'thunder' in cond:
        return 'ArtAssets/icons/thunder.svg'
    elif 'fog' in cond:
        return 'ArtAssets/icons/fog.svg'
    else:
        return 'ArtAssets/icons/sun.svg'
