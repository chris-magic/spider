# -*- coding: utf-8 -*-

import os
import re
import time

import requests
from bs4 import BeautifulSoup

url="http://item.taobao.com/item.htm?spm=a219r.lm869.0.0.NufoDi&id=13878246530&ns=1"
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip,deflate,sdch",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive"}

image_path = 'image'

def spider():
    html = get_info()
    price = analyze_info(html)
    print price
   # print title

def get_info():
    url = raw_input("please input the website:")
    resp = requests.get(url, headers=headers)
    html = resp.content
    #print html
    return html


def analyze_tao():
    html = get_info()
    html = html.decode('gbk').encode('utf-8')
    soup = BeautifulSoup(html)
    title = soup.html.head.title.string
    price = soup.find(attrs={'class':"tb-rmb-num"}).string
    print price
    link = soup.find(id="J_ImgBooth")
  #  print link
    link = link['data-src']
    print link

    image_get = requests.get(url=link, headers=headers)
    img_content = image_get.content

    file_name = str(int(time.time()))+'.jpg'
    file_path = os.path.join(image_path,file_name)
    image = open(file_path,'wb')
    image.write(img_content)
    image.close()




   # return link






if __name__ == '__main__':
    analyze_tao()
