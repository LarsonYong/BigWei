# coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import urllib
import os

def CrawlerURL(url, urldir):
    req=urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib2.urlopen(req)

    html = con.read().decode('utf-8')
    items = BeautifulSoup(html, "lxml").find('body').find('div', id='main-content').find('div',attrs={"class":"container-fluid"}).findAll('div',attrs={"class":"row-fluid"})
    for item in items:
        if item.find('section'):
            lis = item.find(name='section', attrs={"class":"span8 archive-list"}).find('div', attrs={"class":"widget-box"}).find('div', attrs={"class":"widget-content"}).find('ul').findAll(name='li')
            for li in lis:
                target = li.find(name='h2')
                title = target.text
                url =  target.find(name='a').get('href')
                urldir[title] = url
    return urldir

def CrawlerPic(urldir):
    picUrl = []
    for title, url in urldir.iteritems( ):
        req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        html = con.read( ).decode('utf-8')
        items = BeautifulSoup(html, "lxml").find('body').find('div', id='main-content').find('div', attrs={
            "class": "container-fluid"}).findAll('div', attrs={"class": "row-fluid"})
        for item in items:
            if item.find('div', attrs={"class": "span8"}):
                print title
                ps = item.find('div', attrs={"class": "span8"}).find('div', attrs={"class": "widget-box"}).find(
                    'article', attrs={"class": "widget-content single-post"}
                    ).find('div', attrs={"class": "entry"}).findAll('p')

                i = 0
                for p in ps:
                    i += 1
                    if p.find('a', attrs={"class": "highslide-image"}):
                        target = p.find('a', attrs={"class": "highslide-image"}).get('href')
                        picUrl.append(target)
                if picUrl[-1]:
                    target_1 = picUrl[-1]
                    target_1 = target_1[:-5] + '1' + target_1[-4:]
                    print target_1
                    picUrl.append(target_1)
                    picUrl = SavePic(title,picUrl)

def SavePic(title, picUrl):
    a = 0
    while a < len(picUrl):
        if '/' in title:
            title = title.replace('/', '')
        name = title + '_' + str(a + 1)
        if not os.path.exists(title):
            os.mkdir(title)
            local_path = os.path.join(os.getcwd( ), title)
        else:
            local_path = os.path.join(os.getcwd( ), title)
        fullname = os.path.join(local_path, name)
        print fullname
        try:
            urllib.urlretrieve(picUrl[a], fullname)
        except:
            print "@@@@@@@@@@@@@@@@@@@@@@"
            print "Error: " + fullname
            break
        a += 1
    picUrl = []
    return picUrl


def Crawler():
    urldir = {}
    for i in range(2,4):
        url = 'http://www.daweijita.com/video_lesson/easy_tc/page/' + str(i + 1)
        print ("=====================正在爬取第" + str(i + 1) + "页=========")
        urldir = CrawlerURL(url, urldir)
        picUrl = CrawlerPic(urldir)
    urldir2 = {}
    url2 = 'http://www.daweijita.com/video_lesson/regular_tc'
    print ("=====================正在爬取第" + 'regulra' + "页=========")
    urldir2 = CrawlerURL(url2, urldir2)
    picUrl2 = CrawlerPic(urldir2)

    urldir3 = {}
    url3 = 'http://www.daweijita.com/video_lesson/hardened_tc'
    print ("=====================正在爬取第" + 'regulra' + "页=========")
    urldir3 = CrawlerURL(url3, urldir3)
    picUrl3 = CrawlerPic(urldir3)


if __name__ == "__main__":
    Crawler()
