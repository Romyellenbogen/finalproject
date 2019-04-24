from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv

html = urlopen('https://ich.unesco.org/en/lists')
bsObj = BeautifulSoup(html, "html.parser")

f = open('links.txt', 'w')

table = bsObj.find("table", {"id": "list"})
links = table.find_all('a', {"class":"link"})
for link in links:
    if 'href' in link.attrs:
        f.write(link.attrs['href'] + '\n')

f.close()
