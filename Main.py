import urllib.request
import bs4 as bs
import re

#Input tags to analyze and scrape
tagsToSearch = 'drift'
noOfNotes = []
counter = 0
avgNotes = 100
indexOfSavedPost = []
j = 0
listOfNotes = []

#searching the tags above
urlToSearch =  urllib.request.urlopen('https://www.tumblr.com/search/' + tagsToSearch).read()
soup = bs.BeautifulSoup(urlToSearch, "html.parser")

#find all posts that are images
r = soup.find_all('article', class_="is_photo")

#david's code. I want it to grab just the value of data-count. It prints what I sent you.
for article in r:
      for tag in article.descendants:
           if hasattr(tag, 'attrs') and 'data-count' in tag.attrs:
               listOfNotes.append(int(tag.attrs['data-count']))


#Seperating popular content from content we don't want
for j in noOfNotes:
    if (noOfNotes[j] > avgNotes):
        indexOfSavedPost.append(j)
        print (j,noOfNotes[j])