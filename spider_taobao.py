# -*- coding: utf-8 -*-

import os
import re
import time

import requests
from bs4 import BeautifulSoup


image_path = 'image'


def analyze_tao(url, headers):
    #get the page
    resp = requests.get(url, headers=headers)
    html = resp.content
    html = html.decode('gbk').encode('utf-8')
    soup = BeautifulSoup(html)

    #title
    try:
        title = soup.find('title').string.encode('utf-8')
        s1 = u"-淘宝"
        s1 = s1.encode('utf-8')
        title = title.replace(s1,'')
        #print title

        price = soup.find(attrs={'class':"tb-rmb-num"}).string.encode('utf-8')

        #image
        url_p = "http://detailskip.taobao.com/json/mjsDetailNew.htm?user_id=1072417851"
        resp1 = requests.get(url_p, headers=headers)
        f = open('page.html', 'w')
        html1 = resp1.content
        links = soup.find(id="J_UlThumb").find_all('img')
        for i,link in enumerate(links):
            links[i] = link['data-src'].split('_50')[0]

        return {'t':title, 'p':price, 'l':links}

    except:
        return {}


if __name__ == '__main__':
    analyze_tao()
