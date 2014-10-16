# -*- coding: utf-8 -*-

import re

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import Blueprint

from spider import spider

from model import item, item_img
from extension import db


web = Blueprint('web', __name__)


@web.route('/store', methods=['POST'])
def item_store():
    title = request.form.get("title").encode('utf-8')

    price = request.form.get("price")

    links = request.form.get("links")[1:-2]

    links = links.split(', ')
    #print links
    item0 = item(title, price)
    db.session.add(item0)
    for i,link in enumerate(links):
        links[i] = links[i].replace("u'","")
        links[i] = links[i].replace("'","")
        #print link
        item_img0 = item_img(links[i], item0)
        db.session.add(item_img0)
    db.session.commit()

    #print links
    return "Successfully saved! Check it on your database"


@web.route('/')
def input():
    return render_template("input_url.html")


@web.route('/', methods=['POST'])
def get_info():
    url = request.form.get('url')

    if re.search(u"http", url) is None:
        url = "http://" + url

    error = None
    #spider(url)
    iteminfo = spider(url)

    if iteminfo == {}:
        error = "invalid item"
        return render_template("show_info.html", error=error)
    if iteminfo != {}:
        title = iteminfo['t'].decode('utf-8')
        price = iteminfo['p'].decode('utf-8')
        links = iteminfo['l']
    #return iteminfo[1]
        return render_template("show_info.html", title=title, price=price, links=links )
