import urllib.request
import bs4 as bs
import re
import os
import time
import datetime
from pathlib import Path

#Settings
tagsToSearch = ['Drift','Streeto','180sx','jzx100','jzx110','326power']
avgNotes = 100
CycleMode = True
hourInterval = 2


indexOfPopularPosts = []
listOfNotes = []
imgLinks = []
total = 0
now = datetime.datetime.now()
dateAndTimeString = now.strftime("%Y-%m-%d %H:%M")
imgLibrary = []
creditsList = []

while CycleMode is True:
    for tagSearch in range(len(tagsToSearch)):
        print('[' + dateAndTimeString + ']' + 'Crawling: ' +tagsToSearch[tagSearch])
        #searching the tags above
        urlToSearch =  urllib.request.urlopen('https://www.tumblr.com/search/' + tagsToSearch[tagSearch]).read()
        soup = bs.BeautifulSoup(urlToSearch, "html.parser")

        #find all posts that are images
        r = soup.find_all('article', class_="is_photo")

        #Building up list that contains the amount of popularity of each post
        for article in r:
              for tag in article.descendants:
                   if hasattr(tag, 'attrs') and 'data-count' in tag.attrs:
                       listOfNotes.append(int(tag.attrs['data-count']))
                   if hasattr(tag, 'attrs') and 'data-tumblelog' in tag.attrs:
                       creditsList.append(str(tag.attrs['data-tumblelog']))
        #print(creditsList)
        #print(listOfNotes)


        #Populating list of popular images in the same order as the amount of likes each photo has
        allImages = soup.find_all('img')
        for img in allImages:
            if hasattr(img, 'attrs') and 'src' in img.attrs:
                if (str(img.attrs['src'])[0:10] == ('https://68')):
                    imgLinks.append(str(img.attrs['src']))
        print(imgLinks)


        #Downloading Popular Content
        for i in range(len(listOfNotes)):
            if (listOfNotes[i] > avgNotes):
                DownloadLink = (str(imgLinks[i]))
                FullFileName = os.path.join('Photos', (tagsToSearch[tagSearch]+ '_'+str(total)+'.gif'))
                myPath = Path("Photos/" +tagsToSearch[tagSearch]+ '_'+str(total)+'.gif')

                if DownloadLink not in imgLibrary: #TODO: Find different method of checking if exists
                    urllib.request.urlretrieve(DownloadLink, FullFileName)
                    imgLibrary.append(DownloadLink)
                    total += 1
    time.sleep(hourInterval*3600)
