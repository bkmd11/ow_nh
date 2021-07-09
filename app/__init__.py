from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from config import Config


db = SQLAlchemy()
# migrate = Migrate()
# login.login_view = 'auth.login'

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
bootstrap = Bootstrap(app)



from app import routes, models
