from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
    newArr = sorted(arr, key = lambda date: datetime.strptime(date[3].replace(',', ''), '%d %b %Y'), reverse = True)
    return newArr

def sortByOldest(arr) -> list:
    newArr = sorted(arr, key = lambda date: datetime.strptime(date[3].replace(',', ''), '%d %b %Y'))
    return newArr

def sortByLongest(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[4].replace(':', '')), reverse = True)
    return newArr

def sortByShortest(arr) -> list:
    newArr = sorted(arr, key = lambda x: int(x[4].replace(':', '')))
    return newArr

def getNum(num) -> int:
    if ',' in num:
        num = num.replace(',' '')
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

def getComments(num) -> int:
    return int(num.replace(',', ''))

def sortByComments(arr) -> list:
    newArr = sorted(arr, key = lambda x: getComments(x[6].split()[0]), reverse = True)
    return newArr

def sortByCommentsReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: getComments(x[6].split()[0]))
    return newArr

def sortBySubs(arr) -> list:
    newArr = sorted(arr, key = lambda x: getNum(x[7].split()[0]), reverse = True)
    return newArr

def sortBySubsReverse(arr) -> list:
    newArr = sorted(arr, key = lambda x: getNum(x[7].split()[0]))
    return newArr

def getData(search) -> list:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.youtube.com/results?search_query={}'.format(search))
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

    for i in range(len(titles)):
        driver.get('https://www.youtube.com{}'.format(urls[i].get('href')))
        # time.sleep is used here to make sure the page loads the required data
        time.sleep(1)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        views.append(soup.find('span', class_ = 'view-count style-scope ytd-video-view-count-renderer'))
        dates.append(soup.find('div', id = 'info-strings'))
        likes.append(soup.find('a', class_ = 'yt-simple-endpoint style-scope ytd-toggle-button-renderer'))
        #comments.append(soup.find('yt-formatted-string', class_ = 'count-text style-scope ytd-comments-header-renderer'))
        subs.append(soup.find('yt-formatted-string', id = 'owner-sub-count'))
        driver.execute_script("return scrollBy(0, 1000);")
        comments.append(WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//h2[@id='count']/yt-formatted-string"))).text)

    arr = [[''] * 9 for i in range(len(titles)]
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
            arr[i][6] = '0 Comments'
        else:
            arr[i][6] = comments[i]
        if(subs[i].text == ''):
            arr[i][7] = '0 subscribers'
        else:
            arr[i][7] = subs[i].text
        arr[i][8] = 'https://www.youtube.com{}'.format(urls[i].get('href'))
        j += 2
    
    driver.quit()
    
    return arr
