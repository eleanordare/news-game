import urllib, urllib2

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

def call_API():
    url = 'https://newsapi.org/v1/sources?apiKey=066301c377dd44cfbe7558f92871ff1e'
    response = urllib2.urlopen(url).read()
    return response
