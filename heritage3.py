from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import codecs
import time
import csv

file = open('heritage6.csv', 'w', newline="", encoding="utf-8")
c = csv.writer(file)
c.writerow(['Site name','Country Name', 'Description', 'Coordinates', 'Region', 'Inscription date', 'Criteria'])

with open('heritagePages.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

info = []

def heritageLoop(link):
    url = ('http://whc.unesco.org' + link)
    html = requests.get(url)
    bsObj = BeautifulSoup(html.text, "html.parser")
    name = bsObj.find("h1")
    # create new empty dictionary to hold this location
    world_her_loc = {}

    # <div class="alternate">
    box = bsObj.find( "div", {"class":"alternate"} )
    # print(box)
    divs = box.find_all('div')
    countries = []
    no_colon = []
    has_colon = []
    for div in divs:
        # any div that contains an img will be a country, so -
        # grab all those and process them at the end
        if div.find('img'):
            countries.append(div)
        elif not ':' in div.get_text().strip(' \n\r\t'):
            no_colon.append(div)
        else:
            has_colon.append(div)

    # deal with countries
    countries_clean = []
    for country in countries:
        countries_clean.append(country.get_text().strip(' \n\r\t'))
    # print(countries_clean)
    if len(countries_clean) == 1:
        joincountry = countries_clean[0]
    else:
        country = countries_clean
        joincountry = ', '.join(country)
    # print(country)
    world_her_loc['country'] = joincountry
    #print(len(country))
    #if len(country) == 1:
        #joincountry = country
    #else:
        #joincountry = ', '.join(country)
        #print(joincountry)


    # deal with no_colon items
    # print(no_colon)

    if len(no_colon) == 1:
        latlong = no_colon[0].get_text().strip(' \n\r\t')
        region = "N/A"
        # print(latlong)
        world_her_loc['latlong'] = latlong
    elif len(no_colon) == 2:
        region = no_colon[0].get_text().strip(' \n\r\t')
        latlong = no_colon[1].get_text().strip(' \n\r\t')
        # print(region)
        # print(latlong)
        world_her_loc['latlong'] = latlong
        world_her_loc['region'] = region
    elif len(no_colon) == 0:
        latlong = 'N/A'
        region = "N/A"
    else:
        print('Alert: ' + link + ' has more than 2 no_colon items!')

    # deal with has_colon items
    # print(has_colon)
    for item in has_colon:
        ilist = item.get_text().split(':')
        # Date of Inscription
        if 'Inscription' in ilist[0]:
            inscrip_date = ilist[1].strip(' \n\r\t')
            world_her_loc['inscrip_date'] = inscrip_date
        # Criteria: (x)
        elif 'Criteria' in ilist[0]:
            criteria = ilist[1].strip(' \n\r\t')
            world_her_loc['criteria'] = criteria
        # Property : 360,000 ha
        elif 'Property' in ilist[0]:
            property_val = ilist[1].strip(' \n\r\t')
            world_her_loc['property_val'] = property_val
        # Ref: 937
        elif 'Ref' in ilist[0]:
            ref_val = ilist[1].strip(' \n\r\t')
            world_her_loc['ref_val'] = ref_val
        else:
            print('Alert: ' + link + ' has an unknown has_colon item!')

    # loop over dict and print each item
    for k, v in world_her_loc.items():
        if not type(v) == list:
            print(k + ": " + v)
        else:
            print(k + ": ")
            for item in v:
                print(item)

    desPath = bsObj.find("div", {"id": "contentdes_en"})
    des = desPath.find("p")

    info = [name, joincountry, des, latlong, region, inscrip_date, criteria]
    row = []
    for item in info:
        try:
            row.append(item.get_text())
        except:
            row.append(item)
    time.sleep(2)
    c.writerow(row)

for urls in content:
    hl = heritageLoop(urls)

#test = heritageLoop('/en/list/211')

f.close()
file.close()
