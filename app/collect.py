import urllib, urllib2, json
from random import randint

chosenSources = ["bbc-news",
                "bloomberg",
                "buzzfeed",
                "cnn",
                "national-geographic",
                "new-york-magazine",
                "the-economist",
                "the-huffington-post",
                "the-new-york-times",
                "the-wall-street-journal",
                "the-washington-post",
                "time"]

def retrieve():
    apiKey = "066301c377dd44cfbe7558f92871ff1e"
    source = chosenSources[randint(0,len(chosenSources)-1)]
    sortBy = "top"
    url = 'https://newsapi.org/v1/articles' + "?apiKey=" + apiKey + "&source=" + source + "&sortBy=" + sortBy
    response = urllib2.urlopen(url).read()

    articlesJSON = json.loads(response)
    articlesList = articlesJSON["articles"]
    article = articlesList[randint(0,len(articlesList)-1)]

    print articlesJSON["source"]

    return article
