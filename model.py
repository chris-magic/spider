# -*- coding: utf-8 -*-

from extension import db

#db = SQLAlchemy()


class item_img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemid = db.Column(db.Integer, db.ForeignKey('item.id'))
    imgsrc = db.Column(db.Text)
    item = db.relationship('item', backref=db.backref('item_img', lazy='dynamic'))

    def __init__(self, imgsrc, item):
        #self.itemid = itemid
        self.imgsrc = imgsrc
        self.item = item


class item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    price = db.Column(db.String(120))
    #imgsrc = db.Column(db.Text)

    def __init__(self, title, price):
        self.title = title
        self.price = price
        #self.imgsrc = imgsrc
