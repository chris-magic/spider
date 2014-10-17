# -*- coding: utf-8 -*-

import os
import re
import time

import requests
from bs4 import BeautifulSoup


image_path = 'image'


def analyze_tmail(url, headers):
    #get the page
    resp = requests.get(url, headers=headers)
    html = resp.content
    html = html.decode('gbk').encode('utf-8')
    soup = BeautifulSoup(html)

    try:
        #title
        title = soup.html.head.title.string.encode('utf-8')
        s1 = u"-tmall.com天猫"
        s1 = s1.encode('utf-8')
        title = title.replace(s1,'')
        print title
        #price
        price = soup.find(attrs={'class':"originPrice"}).string.encode('utf-8')
        #image
        links = soup.find(id="J_UlThumb").find_all('img')
        #print link
        for i,link in enumerate(links):
            links[i] = link['src'].split('_60')[0]
        return {'t':title, 'p':price, 'l':links}

    except:
        return {}


if __name__ == '__main__':
    analyze_tmail()
