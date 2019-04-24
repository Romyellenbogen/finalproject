from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv

html = urlopen('http://whc.unesco.org/en/list/')
bsObj = BeautifulSoup(html, "html.parser")

f = open('heritagePages.txt', 'w')

links = bsObj.find("div", {"id" : "acc"})
sites = links.find_all("div", {"class": "list_site"})
for site in sites:
    uls = site.find("ul")
    lis = uls.find_all("li")
    for li in lis:
        pages = li.find("a")
        for page in pages:
            link = pages.attrs['href']
            f.write(link + '\n')
        #f.write(pages)
#for site in sites:
    #url = site.find_all("a")
    #f.write(url + '\n')


f.close()
