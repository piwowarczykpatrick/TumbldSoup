import urllib.request
import bs4 as bs
import re
import os
import time
import datetime
from pathlib import Path

#Settings
tagsToSearch = ['240sx']
avgNotes = 100
CycleMode = True
hourInterval = 2
run = False


indexOfPopularPosts = []
listOfNotes = []
imgLinks = []
total = 0
now = datetime.datetime.now()
dateAndTimeString = now.strftime("%Y-%m-%d %H:%M")
imgLibrary = []
creditsList = []
def runScript():
    print('SETTINGS')
    print('Average Notes: ', avgNotes)
    print('Cycle Mode: ', CycleMode)
    print('Hour Interval:', hourInterval)

    for tagSearch in range(len(tagsToSearch)):
        total = 0 #Reset filename count for each tag
        print('[' + dateAndTimeString + ']' + 'Crawling: ' +tagsToSearch[tagSearch])
        #searching the tags above
        urlToSearch =  urllib.request.urlopen('https://www.tumblr.com/search/' + tagsToSearch[tagSearch]).read()
        soup = bs.BeautifulSoup(urlToSearch, "html.parser")

        #find all posts that are images
        r = soup.find_all('article', class_="is_photo")

        #Building up list of authors

        for article in r:
            breakdown = (article.a)
            dict = breakdown.attrs
            if (dict.get('title') is not None):
                creditsList.append(dict.get('title'))
            else:
                creditsList.append('None')


            # Building up list that contains the amount of popularity of each post

            for tag in article.descendants:
                if hasattr(tag, 'attrs') and 'data-count' in tag.attrs:
                    listOfNotes.append(int(tag.attrs['data-count']))
                    #creditsList.append(tag.attrs['data-tumblelog'])
                if hasattr(tag, 'attrs') and 'post-info-tumblelog' in tag.attrs:
                    creditsList.append(str(tag.attrs['name']))
                    print(creditsList)
                    print('hi')

        print(creditsList)
        #print(listOfNotes)


        #Populating list of popular images in the same order as the amount of likes each photo has
        allImages = soup.find_all('img')
        for img in allImages:
            if hasattr(img, 'attrs') and 'src' in img.attrs:
                print('hello')
                print(img)
                if (str(img.attrs['src'])[0:10] == ('https://66')):
                    imgLinks.append(str(img.attrs['src']))
        print(imgLinks)


        #Downloading Popular Content
        for i in range(len(listOfNotes)):
            if (listOfNotes[i] > avgNotes):
                print(imgLinks)
                DownloadLink = (str(imgLinks[i]))
                FullFileName = os.path.join('/Users/patrickpiwowarczyk/Documents/Dropbox/Depaul/School/DamnDrifters', (tagsToSearch[tagSearch]+ '_'+str(total)+ '_Author: @' + creditsList[i]+'.gif'))
                myPath = Path("Photos/" +tagsToSearch[tagSearch]+ '_'+str(total)+'.gif')

                if DownloadLink not in imgLibrary:
                    urllib.request.urlretrieve(DownloadLink, FullFileName)
                    imgLibrary.append(DownloadLink)
                    total += 1
    time.sleep(hourInterval * 3600)

if CycleMode and run:
    runScript()
