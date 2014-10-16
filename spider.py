# -*- coding: utf-8 -*-

import re

from spider_taobao import analyze_tao
from spider_jd import analyze_jd
from spider_tmail import analyze_tmail
from spider_amazon import analyze_amazon
from spider_kno import analyze_kno


headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip,deflate,sdch",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive"}

def spider(url):
    iteminfo = {}
    if (re.search(u"taobao", url) is not None) and (re.search(u"tmall", url) is None):
        iteminfo = analyze_tao(url, headers)
    #jingdong
    if re.search(u"jd", url) is not None:
        iteminfo = analyze_jd(url, headers)
    #tmail
    if re.search(u"tmall", url) is not None:
        iteminfo = analyze_tmail(url, headers)
    #amazon
    if re.search(u"amazon", url) is not None:
        iteminfo = analyze_amazon(url, headers)
    #knewone
    if re.search(u"knewone", url) is not None:
        iteminfo = analyze_kno(url, headers)

    return iteminfo
