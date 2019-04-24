from urllib.request import urlopen
from bs4 import BeautifulSoup
import codecs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time
import csv

file = open('cultureencoded.csv', 'w', newline="", encoding="utf-8")
c = csv.writer(file)
c.writerow(['Practice', 'Country', 'Summary', 'Image', 'Audio'])

with open('links.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

info = []


def cultureloop(link):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('C:/Users/romyj/Documents/UF/Senior/webapps/python/scraping/chromedriver')
    driver.get(link);
    html = driver.page_source
    #html = urlopen(link)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1", {"class": "page-title"})
    country = bsObj.find("p", {"class": "link element-country"})

    textPath = bsObj.find("div", {"class": "element-item"})
    text = textPath.find("p", {"class": "wiki-text"})
    #strippedP = ""
    #for p in text:
        #strippedP += p.get_text()

    try:
        audioPath = bsObj.find("div", {"id": "ElementAudio"})
        audio = audioPath.find("audio")
        a = audio.get('src')
    except:
        a="N/A"

    try:
        picPath = bsObj.find("dt", {"class": "slideshow-box script_progress photo"})
        pic = picPath.find("img", {"class": "slideshow-img script_hide"})
        src = pic.get('src')
    except:
        src = "N/A"
    time.sleep(2)
    driver.quit()

    #categories = bsObj.find_all("p", {"class": "text-2"})
    #category = categories.find_all("a", {"class": "link"})
    #for cat in category:
        #if 'href' in category.attrs:
            #cat = category.get_text()
            #print(cat)

    info = [title, country, text, src, a]
    row = []
    for item in info:
        try:
            row.append(item.get_text())
        except:
            row.append(item)
    s = random.randint(1, 5)
    time.sleep(s)
    c.writerow(row)

for urls in content:
    cp = cultureloop(urls)

#test = cultureloop('https://ich.unesco.org/en/RL/slava-celebration-of-family-saint-patrons-day-01010')

f.close()
file.close()
