from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

file = open('factbook.csv', 'w', newline="", encoding="utf-8")
c = csv.writer(file)
c.writerow(['Country name', 'Country code', 'Region', 'Climate', 'Population', 'Languages', 'Other languages', 'Major urban areas'])

with open('factbookNames.txt') as fName:
    nameContent = fName.readlines()

nameContent = [y.strip() for y in nameContent]

with open('factbookPages.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

info = []

def factbookLoop(link):
    #driver = webdriver.Chrome('C:/Users/romyj/Documents/UF/Senior/webapps/python/scraping/chromedriver')
    #driver.get('https://www.cia.gov/library/publications/the-world-factbook/geos/' + link + '.html');
    #html = driver.page_source
    html = urlopen('https://www.cia.gov/library/publications/the-world-factbook/geos/' + link + '.html')
    bsObj = BeautifulSoup(html, "html.parser")
    namepath = bsObj.find("div", {"id": "geos_title"})
    name = namepath.find("span", {"class": "region_name1 countryName"})
    regionPath = bsObj.find("div", {"id": "field-map-references"})
    region = regionPath.find("div", {"class": "category_data subfield text"})
    climate = bsObj.find("div", {"id": "field-climate"})
    population = bsObj.find("div", {"id": "field-population"})
    try:
        pop = population.find("span", {"class": "subfield-number"})
    except:
        pop = "N/A"
    languagePath = bsObj.find("div", {"id": "field-languages"})
    try:
        mainLang = languagePath.find("div", {"class": "category_data subfield text"})
        langNote = languagePath.find("div", {"class": "category_data note"})
    except:
        mainLang = "N/A"
        langNote = "N/A"
    try:
        urban = bsObj.find("div", {"id": "field-major-urban-areas-population"}).text.split("(2018)")
        urban = urban[0].strip(' \n')
    except:
        urban = "N/A"
    try:
        flagPath = bsObj.find("div", {"class": "modalFlagBox"})
        flagimgpath = flagPath.find("img")
        flagimg = flagimgpath.get("src").split("../")
        flag = flagimg[1]
        fullflag = "https://www.cia.gov/library/publications/the-world-factbook/" + flag
    except:
        fullflag = "N/A"

    info = [name, link, region, climate, pop, mainLang, langNote, urban, fullflag]
    row = []
    for item in info:
        try:
            row.append(item.get_text().strip())
        except:
            row.append(item)
    time.sleep(2)
    c.writerow(row)
    #driver.quit()



for urls in content:
    fl = factbookLoop(urls)

#test = factbookLoop('af')

f.close()
fName.close()
file.close()
