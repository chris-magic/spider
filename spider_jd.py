# -*- coding: utf-8 -*-

import os
import re
import time

import requests
from bs4 import BeautifulSoup

image_path = 'image'

def analyze_jd(url, headers):
    #get the page
    resp = requests.get(url, headers=headers)
    html = resp.content
    #html = html.decode('gbk').encode('utf-8')
    soup = BeautifulSoup(html)

    #title
    try:
        title = soup.html.head.title.string.encode('utf-8')
        s1 = u"【行情 报价 价格 评测】-京东"
        s1 = s1.encode('utf-8')
        title = title.replace(s1,'')
        #print title

    #price
        url_id = url.split('/')[-1].split('.')[0]
        url_p = 'http://p.3.cn/prices/get?skuid=J_' + url_id
        resp_price = requests.get(url_p, headers=headers)
        price = resp_price.content.split(',')[1].split(':')[1]
        #print price

    #image
        links_try = soup.find(attrs={'class':"spec-items"})
        if links_try is not None:
            links = links_try.find_all('img')
        if links_try is None:
            links = soup.find(attrs={'class':"p-img"}).find_all('img')
        for i,link0 in enumerate(links):
            link_split = link0['src'].split("/n")
            links[i] = link_split[0] + "/n0" + link_split[1][1:]
            #print links[i]
        #print link

        #image_get = requests.get(url=link, headers=headers)
        #img_content = image_get.content

        #file_name = str(int(time.time()*1000))+'.jpg'
        #file_path = os.path.join(image_path,file_name)
        #image = open(file_path,'wb')
        #image.write(img_content)
        #image.close()
#    html = html.decode('gbk').encode('utf-8')
 #   soup = BeautifulSoup(html)
        return {'t':title, 'p':price, 'l':links}

    except:
        return {}






if __name__ == '__main__':
    analyze_jd()
