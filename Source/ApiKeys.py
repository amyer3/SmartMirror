from lxml import etree

def keyFinder(key):
    e = etree.parse('keys.xml').find(key).text
    return e
