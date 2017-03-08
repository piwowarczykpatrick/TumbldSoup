import urllib.request
import bs4 as bs
import re
import os
import time
import datetime

#Input tags to analyze and scrape
tagsToSearch = ['Drift','Streeto','180sx','jzx100','jzx110','326power']
avgNotes = 100
indexOfPopularPosts = []
listOfNotes = []
imgLinks = []
total = 0
CycleMode = True
hourInterval = 2
now = datetime.datetime.now()
dateAndTimeString = now.strftime("%Y-%m-%d %H:%M")

while CycleMode is True:
    for tagSearch in range(len(tagsToSearch)):
        print('[' + dateAndTimeString + ']' + 'Crawling: ' +tagsToSearch[tagSearch])
        #searching the tags above
        urlToSearch =  urllib.request.urlopen('https://www.tumblr.com/search/' + tagsToSearch[tagSearch]).read()
        soup = bs.BeautifulSoup(urlToSearch, "html.parser")

        #find all posts that are images
        r = soup.find_all('article', class_="is_photo")

        #david's code. I want it to grab just the value of data-count. It prints what I sent you.
        for article in r:
              for tag in article.descendants:
                   if hasattr(tag, 'attrs') and 'data-count' in tag.attrs:
                       listOfNotes.append(int(tag.attrs['data-count']))
        #print(listOfNotes)


        #Seperating popular content from content we don't want
        for j in range(len(listOfNotes)):
            if (listOfNotes[j] > avgNotes):
                indexOfPopularPosts.append(j)
                #print (j,listOfNotes[j])


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
                urllib.request.urlretrieve(DownloadLink, FullFileName)
                total += 1
    time.sleep(hourInterval*3600)
