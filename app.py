# -*- coding: utf-8 -*-

from flask import Flask

from web import web
from extension import db



SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/spiderdb'
app = Flask(__name__)
app.config.from_object(__name__)

db.init_app(app)

app.register_blueprint(web)


if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
