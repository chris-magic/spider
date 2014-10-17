# -*- coding: utf-8 -*-

import os
import re
import time

import requests
from bs4 import BeautifulSoup

image_path = 'image'

def analyze_kno(url, headers):
    #get the page
    resp = requests.get(url, headers=headers)
    html = resp.content
 #   html = html.decode('gbk').encode('utf-8')
    soup = BeautifulSoup(html)

    try:
        #title
        title = url.split('/')[-1]
        #price
        price = soup.find(id="price").string.encode('utf-8')
        #image
        links = soup.find(attrs={'class':"carousel-inner"}).find_all('img')
        #print link
        for i,link in enumerate(links):
            links[i] = link['src']

        return {'t':title, 'p':price, 'l':links}

    except:
        return {}


if __name__ == '__main__':
    analyze_kno()
