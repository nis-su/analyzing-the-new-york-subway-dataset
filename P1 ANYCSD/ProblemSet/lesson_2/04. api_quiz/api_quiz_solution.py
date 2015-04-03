import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    d = json.loads(data)
    topartist = d['topartists']['artist'][0]['name']
    return topartist


if __name__ == '__main__':
	# url should be the url to the last.fm api call which
	# will return find the top artists in Spain
    url ='http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=535105e2d8513b0e1455065d98b24886&format=json'
    print api_get_request(url) 

