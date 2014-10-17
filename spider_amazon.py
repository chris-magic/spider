# -*- coding: utf-8 -*-

import os
import re
import time

import requests
from bs4 import BeautifulSoup

image_path = 'image'


def analyze_amazon(url, headers):
    #get the page
    resp = requests.get(url, headers=headers)
    html = resp.content
    soup = BeautifulSoup(html)
    price = None
    links = []


    try:
        title1 = soup.head.title
        print title1

        price_try = soup.find(attrs={'class':"priceLarge"})
        if price_try is None:
            price = soup.find(id="priceblock_ourprice").string.encode('utf-8')

        if price_try is not None:
            price = soup.find(attrs={'class':"priceLarge"}).string.encode('utf-8')

        if title1 is None:
            title = soup.find(id="btAsinTitle").string.encode('utf-8')

            links = soup.find_all(attrs={'class':"kib-ma-container"})
            for i,link in enumerate(links):
                links[i] = link.img['src']
                print links[i]

        if title1 is not None:
            title = title1.string.encode('utf-8')
            s1 = u"【摘要 书评 试读】图书"
            s1 = s1.encode('utf-8')
            title = title.replace(s1,'')
            #image
            links = soup.find(id="thumb-strip").find_all('img')
            for i,link in enumerate(links):
                links[i] = link['src'].split('_SL75')[0] + "_SL500_PIsitb-sticker-arrow-big,TopRight,35,-73_OU28_.jpg"
            #print link
        return {'t':title, 'p':price, 'l':links}

    except:
        return {}


if __name__ == '__main__':
    analyze_amazon()
