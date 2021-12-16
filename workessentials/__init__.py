from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, UserMixin, login_required, logout_user, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

Bootstrap(app)
db = SQLAlchemy(app)

from workessentials import routes