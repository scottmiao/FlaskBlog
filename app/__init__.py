from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate

import os
# Get the current working directory to place sched.db during development.
# In production, use absolute paths or a database management system.
PWD = os.path.abspath(os.curdir)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/app.db'.format(PWD)
app.config.from_object('config')

db = SQLAlchemy()
db.app = app
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

from app import models
from app import views
