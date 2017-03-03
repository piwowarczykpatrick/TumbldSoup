import urllib.request
import bs4 as bs
import re

#Input tags to analyze and scrape
tagsToSearch = 'drift'
photoPostSubtring = "is_photo post_tumblelog_"

#for tag in tagsToSearch:
urlToSearch =  urllib.request.urlopen('https://www.tumblr.com/search/' + tagsToSearch).read()
soup = bs.BeautifulSoup(urlToSearch, "lxml")

for i in soup.find_all('article', {'class' : re.compile('is_photo post_tumblelog_*')}):
#for i in soup.select('article[class*=is_photo post_]'):
    posts = soup

print(posts)