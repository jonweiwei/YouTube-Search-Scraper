from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def main():
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/results?search_query=f1')
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.findAll('a', id = 'video-title')
    urls = soup.findAll('a', id = 'video-title')
    views = soup.findAll('span', class_ = 'style-scope ytd-video-meta-block')
    channels = soup.findAll('a', class_ = 'yt-simple-endpoint style-scope yt-formatted-string')
    durations = soup.findAll('span', class_ = 'style-scope ytd-thumbnail-overlay-time-status-renderer')

    arr = [[''] * 8 for i in range(len(titles))]
    j = 0
    k = 1
    for i in range(len(titles)):
        arr[i][0] = titles[i].text
        arr[i][1] = channels[j].text
        arr[i][2] = views[j].text
        arr[i][3] = views[k].text
        j += 2
        k += 2
    
    for i in arr:
        print(i)

    print(len(titles))

    #for i in durations:
        #print(i.text)
    #for i in views:
        #print(i.text)
    #print(url.get('href'))
    

main()
