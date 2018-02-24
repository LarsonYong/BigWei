# coding=utf-8
import os
from bs4 import BeautifulSoup
import urllib2
import urllib

def CrawlerEach(url, urldir):
    req=urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib2.urlopen(req)

    html = con.read().decode('utf-8')
    items = BeautifulSoup(html, "lxml").find('body').find('div', id='main-content').find('div',attrs={"class":"container-fluid"}).find('div',attrs={"class":"row-fluid"}).find(name='section', attrs={"class":"span8 archive-list"}).find('div', attrs={"class":"widget-box"}).find('div', attrs={"class":"widget-content"}).find('ul').findAll(name='li')
    for item in items:
        target = item.find(name='h2').find(name='a')
        if target:
            urldir[target.text] = target.get('href')
    return urldir



def Crawler():
    urldir = {}
    i = 0
    url = 'http://www.daweijita.com/video_lesson/easy_tc/page/1'
    print ("=====================正在爬取第" + str(i + 1) + "页=========")
    urldir = CrawlerEach(url, urldir)
    print urldir

def CrawlerEach1(url):
    req=urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib2.urlopen(req)

    html = con.read().decode('utf-8')
    items = BeautifulSoup(html, "lxml")
    return items


def Crawler1():
    urldir = {}
    i = 0
    url = 'http://www.daweijita.com/video_lesson/easy_tc/page/1'
    print ("=====================正在爬取第" + str(i + 1) + "页=========")
    urldir = CrawlerEach(url, urldir)
    print urldir

if __name__ == "__main__":
    # Crawler()
    urldir ={}
    picdir = {}
    # url = 'http://www.daweijita.com/video_lesson/easy_tc/page/1'
    # req=urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    # con = urllib2.urlopen(req)
    #
    # html = con.read().decode('utf-8')
    # items = BeautifulSoup(html, "lxml").find('body').find('div', id='main-content').find('div',attrs={"class":"container-fluid"}).findAll('div',attrs={"class":"row-fluid"})
    # for item in items:
    #     if item.find('section'):
    #         lis = item.find(name='section', attrs={"class":"span8 archive-list"}).find('div', attrs={"class":"widget-box"}).find('div', attrs={"class":"widget-content"}).find('ul').findAll(name='li')
    #         for li in lis:
    #             target = li.find(name='h2')
    #             title = target.text
    #             url =  target.find(name='a').get('href')
    #             urldir[title] = url
    #
    # for title, url in urldir.iteritems():
    #     req=urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    #     con = urllib2.urlopen(req)
    #     html = con.read().decode('utf-8')
    #     items = BeautifulSoup(html, "lxml").find('body').find('div', id='main-content').find('div',attrs={"class":"container-fluid"}).findAll('div',attrs={"class":"row-fluid"})
    #     for item in items:
    #         if item.find('div', attrs={"class":"span8"}):
    #             print title
    #             ps = item.find('div', attrs={"class":"span8"}).find('div', attrs={"class":"widget-box"}).find('article',attrs={"class":"widget-content single-post"}
    #             ).find('div', attrs={"class":"entry"}).findAll('p')
    #             picUrl = []
    #             i = 0
    #             for p in ps:
    #                 i += 1
    #                 if p.find('a', attrs={"class":"highslide-image"}):
    #                     target = p.find('a', attrs={"class":"highslide-image"}).get('href')
    #                     picUrl.append(target)
    #             target_1 = picUrl[-1]
    #             target_1 = target_1[:-5] + '1' + target_1[-4:]
    #             print target_1
    #             picUrl.append(target_1)
    #             print picUrl
    #             a = 0
    #             while a < len(picUrl):
    #                 if '/' in title:
    #                     title = title.replace('/', '')
    #                 name = title + '_' + str(a + 1)
    #                 if not os.path.exists(title):
    #                     os.mkdir(title)
    #                     local_path = os.path.join(os.getcwd(),title)
    #                 else:
    #                     local_path = os.path.join(os.getcwd(),title)
    #                 print local_path
    #                 fullname = os.path.join(local_path, name)
    #                 urllib.urlretrieve(picUrl[a],fullname)
    #                 a += 1
    # for key,value in urldir.iteritems():
    #     print "==============================="
    #     print "Title: " + key
    #     print value

    url = 'http://www.daweijita.com/43342.html'
    title = 'airuchaoshui'
    req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib2.urlopen(req)
    html = con.read().decode('utf-8')
    items = BeautifulSoup(html, "lxml").find('body').find('div', id='main-content').find('div',attrs={"class":"container-fluid"}).findAll('div',attrs={"class":"row-fluid"})
    for item in items:
        if item.find('div', attrs={"class":"span8"}):
            print title
            ps = item.find('div', attrs={"class":"span8"}).find('div', attrs={"class":"widget-box"}).find('article',attrs={"class":"widget-content single-post"}
                ).find('div', attrs={"class":"entry"}).findAll('p')
            picUrl = []
            i = 0
            for p in ps:
                i += 1
                if p.find('a', attrs={"class":"highslide-image"}):
                    target = p.find('a', attrs={"class":"highslide-image"}).get('href')
                    picUrl.append(target)
            target_1 = picUrl[-1]
            target_1 = target_1[:-5] + '1' + target_1[-4:]
            print target_1
            picUrl.append(target_1)
            print picUrl
            a = 0
            while a < len(picUrl):
                if '/' in title:
                    title = title.replace('/', '')
                name = title + '_' + str(a + 1)
                if not os.path.exists(title):
                    os.mkdir(title)
                    local_path = os.path.join(os.getcwd(),title)
                else:
                    local_path = os.path.join(os.getcwd(),title)
                print local_path
                fullname = os.path.join(local_path, name)
                try:
                    urllib.urlretrieve(picUrl[a],fullname)
                except:
                    print "Error: " + fullname
                    break
                a += 1