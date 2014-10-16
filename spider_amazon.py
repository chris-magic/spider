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
    #title = None
    #title

    title1 = soup.head.title
    print title1

    #electric
    if title1 is None:
        title = soup.find(id="btAsinTitle").string.encode('utf-8')
        try:
            price = soup.find(attrs={'class':"priceLarge"}).string.encode('utf-8')
            print price
        except:
            return {}
        links = soup.find_all(attrs={'class':"kib-ma-container"})
        for i,link in enumerate(links):
            links[i] = link.img['src']
            print links[i]

    #traditional book
    if title1 is not None:
        title = title1.string.encode('utf-8')
        s1 = u"【摘要 书评 试读】图书"
        s1 = s1.encode('utf-8')
        title = title.replace(s1,'')
        #print title

        try:
            price = soup.find(attrs={'class':"priceLarge"}).string.encode('utf-8')
            print price
        except:
            return {}

    #image

        links = soup.find(id="thumb-strip").find_all('img')
        for i,link in enumerate(links):
            links[i] = link['src'].split('_SL75')[0] + "_SL500_PIsitb-sticker-arrow-big,TopRight,35,-73_OU28_.jpg"
        #print link

        #image_get = requests.get(url=link, headers=headers)
        #img_content = image_get.content

        #file_name = str(int(time.time()*1000))+'.jpg'
        #file_path = os.path.join(image_path,file_name)
        #image = open(file_path,'wb')
        #image.write(img_content)
        #image.close()
   # return link
    return {'t':title, 'p':price, 'l':links}






if __name__ == '__main__':
    analyze_amazon()
