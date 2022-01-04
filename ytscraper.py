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
    #for channel in channels:
        #print(channel)
    #print(url.get('href'))
    

main()