from bs4 import BeautifulSoup
import requests

tagsToSearch = ['drift', 'hoonigan', 'drifting', 'drifted']

for i in tagsToSearch
    urlToSearch = 'https://www.tumblr.com' + tagsToSearch
    tumblrRequest = requests.get(urlToSearch)

    soup = BeautifulSoup(tumblrRequest.content)

