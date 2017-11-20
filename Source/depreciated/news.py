import json
from urllib.request import urlopen

from depreciated import ApiKeys


def news():
    hlns = []
    u = 'https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=' + ApiKeys.keyFinder('news')
    c = urlopen(u)
    parsed_json = json.loads(c.read().decode('UTF-8'))
    for H in range(0, 8):
        hlns.append(parsed_json['articles'][H]['title'])
    return hlns


#return "$('#newsJQ').text(articles[i]"