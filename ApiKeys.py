from lxml import etree


def NewsKey():
    e = etree.parse('keys.xml').find('news').text
    return e


def StockKey():
    e = etree.parse('keys.xml').find('stocks').text
    return e


def WeatherKey():
    e = etree.parse('keys.xml').find('weather').text
    return e

NewsKey()
StockKey()
WeatherKey()
