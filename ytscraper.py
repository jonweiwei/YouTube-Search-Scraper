from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

def sortByViews(arr):
    print('hi')


def getData():
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/results?search_query=f1')
    time.sleep(2)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.findAll('a', id = 'video-title')
    urls = soup.findAll('a', id = 'video-title')
    #views = soup.findAll('span', class_ = 'style-scope ytd-video-meta-block')
    channels = soup.findAll('a', class_ = 'yt-simple-endpoint style-scope yt-formatted-string')
    durations = soup.findAll('span', id = 'text')

    views = []
    dates = []
    likes = []
    comments = []
    subs = []

    for i in range(len(titles)):
        driver.get('https://www.youtube.com{}'.format(urls[i].get('href')))
        driver.maximize_window()
        # time.sleep is used here to ensure the scrolling is effective
        time.sleep(1)
        # scroll down the page to load the comments
        driver.execute_script("window.scrollTo(0,600)")
        # time.sleep is used here to ensure that the page has loaded before the data is read
        # the value should be changed depending on the speed of the computer and the network as well
        time.sleep(2)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        views.append(soup.find('span', class_ = 'view-count style-scope ytd-video-view-count-renderer'))
        dates.append(soup.find('div', id = 'info-strings'))
        likes.append(soup.find('a', class_ = 'yt-simple-endpoint style-scope ytd-toggle-button-renderer'))
        comments.append(soup.find('yt-formatted-string', class_ = 'count-text style-scope ytd-comments-header-renderer'))
        subs.append(soup.find('yt-formatted-string', id = 'owner-sub-count'))

    arr = [[''] * 9 for i in range(len(titles))]
    j = 0
    for i in range(len(titles)):
        arr[i][0] = titles[i].text.replace('\n', '')
        arr[i][1] = channels[j].text
        arr[i][2] = views[i].text
        arr[i][3] = dates[i].text
        temp = durations[i].text.replace('\n', '')
        arr[i][4] = temp.replace(' ', '')
        arr[i][5] = likes[i].text
        if(isinstance(comments[i], type(None))):
            arr[i][6] = ''
        else:
            arr[i][6] = comments[i].text
        arr[i][7] = subs[i].text
        arr[i][8] = 'https://www.youtube.com{}'.format(urls[i].get('href'))
        j += 2
    
    for i in arr:
        print(i)

getData()
