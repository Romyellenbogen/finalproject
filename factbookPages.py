from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv

html = urlopen('https://www.cia.gov/library/publications/the-world-factbook/docs/profileguide.html')
bsObj = BeautifulSoup(html, "html.parser")

f = open('factbookPages.txt', 'w')
fName = open('factbookNames.txt', 'w')

links = bsObj.find("div", {"id" : "cntrySelect"})
countries = links.find_all("option")
for country in countries:
    if 'data-place-code' in country.attrs:
        f.write(country.attrs['data-place-code'] + '\n')
        fName.write(country.text.strip() + '\n')

f.close()
fName.close()
