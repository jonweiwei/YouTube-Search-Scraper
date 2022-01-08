from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

def sortByAZ(arr) -> list:
    newArr = sorted(arr, key = lambda x: x[0])
    return newArr

def sortByAZReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: x[0], reverse = True)
    return newArr

def sortByChannelAZ(arr) -> list:
    newArr = sorted(arr, key = lambda x: x[1])
    return newArr

def sortByChannelAZReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: x[1], reverse = True)
    return newArr

def sortByViews(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[2].split()[0].replace(',', '')), reverse = True)
    return newArr

def sortByViewsReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[2].split()[0].replace(',', '')))
    return newArr

def sortByNewest(arr) -> list:
    newArr = sorted(arr, key = lambda date: datetime.strptime(date[3].replace(',', ''), '%b %d %Y'), reverse = True)
    return newArr

def sortByOldest(arr) -> list:
    newArr = sorted(arr, key = lambda date: datetime.strptime(date[3].replace(',', ''), '%b %d %Y'))
    return newArr

def sortByLongest(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[4].replace(':', '')), reverse = True)
    return newArr

def sortByShortest(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[4].replace(':', '')))
    return newArr

def getNum(num) -> int:
    if 'K' in num:
        newNum = int(float(num.replace('K', ''))*1000)
    elif 'M' in num:
        newNum = int(float(num.replace('M', ''))*1000000)
    elif 'B' in num:
        newNum = int(float(num.replace('B', ''))*1000000000)
    else:
        newNum = int(num)
    return newNum

def sortByLikes(arr) -> list:
    newArr = sorted(arr, key = lambda x: getNum(x[5]), reverse = True)
    return newArr

def sortByLikesReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: getNum(x[5]))
    return newArr

def sortByComments(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[6].split()[0]), reverse = True)
    return newArr

def sortByCommentsReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[6].split()[0]))
    return newArr

def sortBySubs(arr) -> list:
    newArr = sorted(arr, key = lambda x: getNum(x[7].split()[0]), reverse = True)
    return newArr

def sortBySubsReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: getNum(x[7].split()[0]))
    return newArr

def getData() -> list:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.youtube.com/results?search_query=f1')
    time.sleep(2)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.findAll('a', id = 'video-title')
    urls = soup.findAll('a', id = 'video-title')
    channels = soup.findAll('a', class_ = 'yt-simple-endpoint style-scope yt-formatted-string')
    durations = soup.findAll('span', id = 'text')

    views = []
    dates = []
    likes = []
    comments = []
    subs = []

    for i in range(3):
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

    arr = [[''] * 9 for i in range(3)]
    j = 0
    for i in range(3):
        arr[i][0] = titles[i].text.replace('\n', '')
        arr[i][1] = channels[j].text
        arr[i][2] = views[i].text
        arr[i][3] = dates[i].text
        temp = durations[i].text.replace('\n', '')
        arr[i][4] = temp.replace(' ', '')
        arr[i][5] = likes[i].text
        if(isinstance(comments[i], type(None))):
            arr[i][6] = '0 Comments'
        else:
            arr[i][6] = comments[i].text
        if(subs[i].text == ''):
            arr[i][7] = '0 subscribers'
        else:
            arr[i][7] = subs[i].text
        arr[i][8] = 'https://www.youtube.com{}'.format(urls[i].get('href'))
        j += 2
    
    driver.quit()
    
    return arr

array = getData()
array = sortBySubsReverse(array)
for i in range(3):
    print(array[i])
