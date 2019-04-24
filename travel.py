from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from codecs import BOM_UTF8
import time
import csv

file = open('travel.csv', 'w', newline="", encoding="utf-8-sig")
c = csv.writer(file)
c.writerow(['Name', 'Precaution', 'Passport Validity', 'Passport pages', 'Tourist visa', 'Vaccionations', 'Currency entry', 'Currency Exit'])

with open('countries.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

travelInfo = []

def travelloop(link):
    driver = webdriver.Chrome('C:/Users/romyj/Documents/UF/Senior/webapps/python/scraping/chromedriver')
    driver.get('https://travel.state.gov' + link + '.html');
    html = driver.page_source
    bsObj = BeautifulSoup(html, "html.parser")
    name = bsObj.find("div", {"class": "tsg-rwd-csi-contry-name"}).get_text().strip()
    advisoryPath = bsObj.find("div", {"id": "tsg-rwd-advisories"})
    advisorySplit = advisoryPath.find("h3", {"class" : "tsg-rwd-eab-title-frame"}).get_text().split(' - ')
    advisory = advisorySplit[1]
    try:
        dataList = bsObj.find_all("div", {"class": "tsg-rwd-qf-box"})
        title = bsObj.find_all("div", {"class": "tsg-rwd-qf-box-title"})
        answerPath = bsObj.find_all("div", {"class": "tsg-rwd-qf-box-data"})
        passportPath = answerPath[0]
        passport = passportPath.find("p")
        passportPages = answerPath[1]
        pages = passportPages.find("p")
        visaPath = answerPath[2]
        visa = visaPath.find("p")
        vaxPath = answerPath[3]
        vax = vaxPath.find("p")
        entryPath = answerPath[4]
        entry = entryPath.find("p")
        exitPath = answerPath[5]
        exit = exitPath.find("p")
    except:
        passport = "N/A"
        pages = "N/A"
        visa = "N/A"
        vax = "N/A"
        entry = "N/A"
        exit = "N/A"



    info = [name, advisory, passport, pages, visa, vax, entry, exit]
    row = []
    for item in info:
        try:
            row.append(item.get_text().strip())
        except:
            row.append(item)
    c.writerow(row)
    driver.quit()

for urls in content:
    tl = travelloop(urls)

#tl = travelloop('/content/travel/en/international-travel/International-Travel-Country-Information-Pages/FrenchWestIndies.html.html?wcmmode=disabled')

f.close()
file.close()
